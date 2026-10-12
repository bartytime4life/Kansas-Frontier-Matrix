<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-flora-rare-plant-record
title: Rare Plant Record Contract — Flora
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners: OWNER_TBD — Flora steward · Rare-plant steward · Sensitivity reviewer · Restricted-data steward · Contract steward · Source steward · Schema steward · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: restricted; semantic-contract; flora; rare-plant; sensitive-location; default-deny; exact-geometry-restricted; source-role-aware; evidence-bound; release-gated
tags: [kfm, contracts, flora, rare-plant-record, rare-plants, protected-plants, sensitive-location, exact-geometry, geoprivacy, redaction, evidence, source-role, policy, release, correction, rollback]
related:
  - ./README.md
  - ./plant_taxon.md
  - ./flora_taxon_crosswalk.md
  - ./domain_observation.md
  - ./domain_feature_identity.md
  - ./specimen_record.md
  - ./flora_occurrence.md
  - ./occurrence_public.md
  - ./occurrence_restricted.md
  - ./phenology_observation.md
  - ./vegetation_community.md
  - ./invasive_plant_record.md
  - ./range_polygon.md
  - ./habitat_association.md
  - ./botanical_survey.md
  - ./restoration_planting.md
  - ./redaction_receipt.md
  - ./domain_validation_report.md
  - ../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../docs/domains/flora/OBJECT_FAMILIES.md
  - ../../../docs/domains/flora/SENSITIVITY_POSTURE.md
  - ../../../schemas/contracts/v1/domains/flora/rare_plant_record.schema.json
  - ../../../fixtures/domains/flora/rare_plant_record/
  - ../../../tests/domains/flora/
  - ../../../policy/domains/flora/
  - ../../../policy/sensitivity/flora/
  - ../../../data/registry/sources/flora/
  - ../../../release/manifests/
notes:
  - "Expanded from a thin scaffold into a Flora rare-plant semantic contract."
  - "The paired schema is a PROPOSED scaffold with no declared fields and additionalProperties=true; field-level machine enforcement remains NEEDS VERIFICATION."
  - "RarePlantRecord is a high-sensitivity occurrence/status surface; public exact geometry is default-deny and must not feed data/published directly."
  - "The canonical path register names KNHI / NatureServe Explorer Pro provenance for this object family; source rights, live endpoints, terms, and activation remain NEEDS VERIFICATION through source registry and policy review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Rare Plant Record — Flora

> Semantic contract for Flora `RarePlantRecord`: the high-sensitivity record for rare, protected, tracked, steward-controlled, culturally sensitive, or otherwise policy-significant plant occurrences, statuses, evidence, locations, review states, public-safe derivatives, correction, and rollback.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: domains/flora" src="https://img.shields.io/badge/family-domains%2Fflora-2ea44f">
  <img alt="Type: semantic contract" src="https://img.shields.io/badge/type-semantic__contract-blue">
  <img alt="Schema: proposed scaffold" src="https://img.shields.io/badge/schema-PROPOSED__scaffold-lightgrey">
  <img alt="Boundary: exact public geometry denied by default" src="https://img.shields.io/badge/boundary-exact__public__geometry__default--deny-critical">
</p>

`contracts/domains/flora/rare_plant_record.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Rare plant classes](#rare-plant-classes) · [Source-role rules](#source-role-rules) · [Sensitivity and access](#sensitivity-and-access) · [Public derivative relationship](#public-derivative-relationship) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/flora/rare_plant_record.md`  
> **Schema path:** `schemas/contracts/v1/domains/flora/rare_plant_record.schema.json`  
> **Truth posture:** the target contract path exists as a scaffold, the paired schema path exists as a PROPOSED scaffold, and the Flora canonical path register identifies `RarePlantRecord` as default-deny for public exact geometry with KNHI / NatureServe Explorer Pro provenance. Field-level schema shape, fixtures, validators, source registry terms, access-control runtime, policy runtime, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `RarePlantRecord` is a protected, policy-significant object. It must not publish exact rare-plant geometry, must not become a public source for `data/published/`, and must not bypass `OccurrenceRestricted`, `OccurrencePublic`, `RedactionReceipt`, sensitivity policy, review records, release manifests, correction notices, or rollback targets.

---

## Meaning

`RarePlantRecord` is the Flora semantic object for rare, protected, tracked, state-listed, globally ranked, steward-controlled, culturally sensitive, or otherwise sensitive plant records. It can carry occurrence support, taxon status, conservation status, source-native tracking fields, internal exact geometry, public-safe derivatives, review state, evidence support, restriction reasons, and correction lineage.

It answers:

- Which plant taxon or source taxon label is rare, protected, tracked, or sensitive in the record context?
- Which occurrence, specimen, survey, source status, rank, list, or steward review supports the record?
- What exact or restricted geometry exists, and why is it restricted?
- What public-safe representation, if any, may be released without exposing sensitive location or timing information?
- Which source role, rights, sensitivity state, review state, release state, correction state, and rollback target govern use?
- Which public API/UI/map/AI answers must abstain, deny, generalize, delay, aggregate, or cite a public-safe derivative instead?

A rare plant record can support conservation stewardship and controlled evidence resolution. It does not authorize public exposure merely because evidence quality is high.

---

## Repo fit

The Flora lane follows the responsibility-root pattern: contracts define semantic meaning, schemas define machine shape, policy gates admissibility/release, fixtures/tests prove behavior, and data/release roots carry lifecycle and publication state.

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Rare plant meaning | `contracts/domains/flora/rare_plant_record.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/flora/rare_plant_record.schema.json` | Linked only; currently scaffolded |
| Taxon identity | `plant_taxon.md`, `flora_taxon_crosswalk.md` | Plant identity, source-label, rank/list crosswalk support |
| Occurrence support | `flora_occurrence.md`, `occurrence_restricted.md` | Exact/internal occurrence support; not public by default |
| Public derivative | `occurrence_public.md` | Generalized/county/grid/suppressed public representation, if approved |
| Voucher and survey support | `specimen_record.md`, `botanical_survey.md`, `domain_observation.md` | Evidence, determination, method, and observation context |
| Sensitivity and transforms | `redaction_receipt.md`, `docs/domains/flora/SENSITIVITY_POSTURE.md` | Protective transform posture and audit trail |
| Context users | `range_polygon.md`, `habitat_association.md`, `phenology_observation.md`, `vegetation_community.md` | Adjacent claims that can amplify exposure risk |
| Validation report | `domain_validation_report.md` | Validates record, policy, transform, fixture, and release readiness |
| Source registry | `data/registry/sources/flora/` | Source identity, role, rights, cadence, attribution, access limits |
| Policy and sensitivity | `policy/domains/flora/`, `policy/sensitivity/flora/` | Deny/abstain/allow and access/release decisions |
| Published layers | `data/published/layers/flora/`, `release/` | Public-safe derivatives only after governed release |

---

## Schema posture

The paired schema currently exists as a **PROPOSED scaffold**.

| Schema fact | Current posture |
|---|---|
| Schema file path | `schemas/contracts/v1/domains/flora/rare_plant_record.schema.json` |
| Schema title | `Rare Plant Record` |
| Declared properties | none yet |
| Required fields | none declared |
| Additional properties | `true` |
| Schema status | `PROPOSED` |
| Source document | `docs/domains/flora/CANONICAL_PATHS.md` |
| Contract document | `contracts/domains/flora/rare_plant_record.md` |

Because the schema is empty and permissive, this contract defines **semantic expectations** for future schema fields, fixtures, validators, sensitivity policy checks, access control, source registry links, public derivative generation, correction flows, and rollback handling. It does not claim current machine enforcement.

---

## Assertions

A reviewed `RarePlantRecord` should semantically assert:

1. **Record identity** — deterministic identity for the rare plant record or candidate record.
2. **Taxon support** — PlantTaxon, source-native taxon name/ID, crosswalk state, status/list/rank context, and caveats.
3. **Rare/sensitive status** — rare, protected, tracked, listed, ranked, steward-controlled, culturally sensitive, source-restricted, candidate, or unresolved posture.
4. **Occurrence support** — occurrence, specimen, survey, observation, habitat, range, or source status support at the correct source role and scale.
5. **Location support** — exact, restricted, generalized, county, grid, range, suppressed, or public-safe geometry references.
6. **Restriction reason** — rare-plant, protected species, exact-location risk, habitat exposure, collection/harvest risk, private-land inference, cultural sensitivity, source rights, or review-pending reason.
7. **Source and role** — SourceDescriptor, source role, source record ID, source authority limits, rights, cadence, provenance, and attribution.
8. **Evidence support** — internal and public-safe EvidenceRef/EvidenceBundle projections sufficient for cite-or-abstain behavior.
9. **Access/release state** — internal access, public derivative, redaction receipt, review, policy decision, release manifest, and rollback target.
10. **Correction posture** — taxon correction, status update, geometry correction, source withdrawal, restriction update, supersession, and rollback lineage.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Publishing exact rare-plant geometry | Exact public geometry is default-deny and can expose vulnerable plants. |
| Treating high-quality evidence as release approval | Source quality does not override sensitivity risk. |
| Treating status/list row as occurrence proof | Regulatory or list status does not prove an occurrence at a place. |
| Using rare records directly in `data/published/` | Public outputs require transformed/released derivatives, not restricted records. |
| Leaking exact locations through evidence citations | Public EvidenceBundle projection must not reveal restricted content. |
| Joining rare records with habitat/range to expose search areas | Cross-layer joins require policy review and may require suppression/generalization. |
| Treating cultural plant knowledge as public taxonomy | Rights-holder and community governance must be respected. |
| Removing correction/rollback lineage for sensitive records | Auditability and reversibility are part of protection. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical rare plant record identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `flora` for this contract. |
| `record_class` | `rare_occurrence`, `protected_occurrence`, `tracked_taxon_status`, `element_occurrence`, `sensitive_specimen`, `rare_habitat_association`, `rare_range_context`, `public_derivative_source`, `candidate_record`, or `synthetic`. |
| `taxon_ref` | PlantTaxon or reviewed taxon candidate. |
| `taxon_crosswalk_ref` | Crosswalk support for source names, IDs, ranks, lists, and statuses. |
| `source_taxon_name` | Source-native taxon name retained for audit. |
| `rare_status` | Rare/protected/tracked/listed/ranked/source-sensitive status, as source-supported. |
| `status_authority_ref` | Source or authority behind status/rank/list posture. |
| `status_effective_time` | Time the status is valid or sourced. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, and authority limits. |
| `source_role` | Canonical source role: `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, or `synthetic`. |
| `source_record_ref` | Source-native occurrence/status/element/specimen/survey record. |
| `domain_observation_ref` | Observation-envelope reference, when applicable. |
| `flora_occurrence_ref` | Occurrence support reference. |
| `occurrence_restricted_ref` | Restricted exact occurrence counterpart, when applicable. |
| `occurrence_public_ref` | Public-safe derivative, if approved and released. |
| `specimen_record_ref` | Voucher/specimen support, when applicable. |
| `botanical_survey_ref` | Survey method/effort context, when applicable. |
| `range_polygon_ref` | Range/context support, when applicable. |
| `habitat_association_ref` | Habitat/context support, when applicable and safe. |
| `exact_geometry_ref` | Exact or restricted geometry reference; never public by default. |
| `public_geometry_ref` | Generalized, grid, county, suppressed, delayed, or public-safe geometry reference. |
| `geometry_precision` | Exact, high precision, source precision, generalized, grid, county, suppressed, withheld, or unknown. |
| `restriction_reasons` | Rare-plant, protected-status, exact-location, collection-risk, habitat-sensitive, private-land, cultural, source-restricted, or review-pending reasons. |
| `access_state` | Denied by default, steward-only, source-steward, sensitivity-reviewer, internal-validation, release-review, public-derivative-only, or blocked. |
| `evidence_refs_internal` | Internal evidence refs, access-controlled. |
| `evidence_refs_public_projection` | Public-safe evidence/citation projection, if one exists. |
| `redaction_receipt_ref` | Required when public representation is generalized, suppressed, delayed, binned, or otherwise transformed. |
| `policy_decision_ref` | Sensitivity/release/access decision. |
| `validation_report_ref` | Validation report for this record or derivative candidate. |
| `review_record_ref` | Source, taxon, sensitivity, steward, or release review. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage for public derivative only. |
| `observed_time` | Time of occurrence/evidence event, when known. |
| `valid_time` | Time span this record supports. |
| `source_time` | Time asserted by source. |
| `retrieval_time` | Time KFM retrieved source material. |
| `review_time` | Time restriction/review state was assigned. |
| `stale_state` | Current, historical, stale, superseded, withdrawn, or unknown. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `correction_refs` | CorrectionNotice, source withdrawal, status update, geometry correction, supersession, and rollback lineage. |
| `quality_flags` | Taxon-conflict, status-conflict, geometry-conflict, rights-unknown, sensitivity-unknown, stale-record, source-role-conflict, exact-public-risk, or incomplete-evidence flags. |

---

## Rare plant classes

| Class | Meaning | Default posture |
|---|---|---|
| `rare_occurrence` | Occurrence of a rare/tracked/protected plant. | Exact location restricted; public derivative required. |
| `protected_occurrence` | Occurrence tied to legal or regulatory protection. | Restrict exact geometry; preserve status source and date. |
| `tracked_taxon_status` | Taxon listed/tracked/ranked without occurrence proof. | Status context only; not occurrence proof. |
| `element_occurrence` | Source-native conservation element occurrence style record. | Restricted/steward access unless transformed. |
| `sensitive_specimen` | Specimen/voucher with sensitive locality. | Restrict locality and citation projection. |
| `rare_habitat_association` | Habitat clue tied to rare/protected taxon. | Fail closed unless generalized/reviewed. |
| `rare_range_context` | Range/distribution support for rare/protected taxon. | Generalize/suppress where inference risk is material. |
| `public_derivative_source` | Internal support used to produce public-safe output. | Requires redaction receipt and release manifest. |
| `candidate_record` | Unreviewed rare/sensitive import or possible match. | WORK/QUARANTINE; no public authoritative use. |
| `synthetic` | Generated/reconstructed/hypothetical rare-plant claim. | Reality-boundary disclosure; never observed fact. |

---

## Source-role rules

| Source pattern | Canonical `source_role` | RarePlantRecord posture |
|---|---|---|
| Steward-reviewed occurrence, specimen-backed rare record, validated survey detection | `observed` | Can support restricted occurrence when evidence, taxon, time, geometry, rights, and sensitivity resolve. |
| Rare/protected list, recovery plan, status/rank table, agency restriction | `regulatory` | Supports status/restriction context; not occurrence proof by itself. |
| Habitat/range/species distribution model for rare plant | `modeled` | Must remain modeled; exact public inference usually denied. |
| Atlas/county/grid/literature rare-plant summary | `aggregate` | Aggregate support only; public exact claims denied. |
| Management/stewardship program table or administrative site list | `administrative` | Internal management context, not biological truth by itself. |
| Unreviewed import, watcher result, unresolved candidate match | `candidate` | Hold in WORK/QUARANTINE until reviewed. |
| AI-generated rare-plant note or reconstructed sensitive location | `synthetic` | Must not be treated as occurrence; deny public authority. |

---

## Sensitivity and access

`RarePlantRecord` starts closed. Opening it to even a generalized public representation is a deliberate reviewed transition.

Rules:

- Exact rare/protected plant locations are withheld from public surfaces by default.
- Public exposure should use the safest accurate representation: generalized, aggregated, delayed, suppressed, or label-only where appropriate.
- Source quality is not a license to expose exact sensitive geometry.
- Every public-safe transform should leave a receipt that records what changed and why.
- When exposure risk, rights, review, source role, or evidence support is unresolved, the outcome should be `ABSTAIN`, `DENY`, or restricted review—not public publication.
- Culturally significant plant information is governed with appropriate rights-holders and communities; KFM must not unilaterally normalize it into public labels or exact locations.
- Public API/UI/map/AI surfaces must not read `RarePlantRecord` or restricted exact geometry directly.

---

## Public derivative relationship

A rare plant record may inform public output only through a governed derivative path:

```text
RarePlantRecord / OccurrenceRestricted
  -> sensitivity policy + source-rights review
  -> redaction, generalization, aggregation, delay, suppression, or withholding reason
  -> RedactionReceipt
  -> OccurrencePublic / RangePolygon / public-safe summary candidate
  -> DomainValidationReport
  -> ReleaseManifest / PromotionDecision
  -> published public layer/API/UI payload
```

The derivative must preserve support scale, source role, uncertainty, time, caveats, release state, correction state, and rollback target without exposing exact sensitive detail.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native rare plant rows, exact coordinates, element records, status/rank records, specimen labels, steward notes, and source-restricted fields remain source-bound. |
| WORK / QUARANTINE | Candidate records are normalized, taxon-crosswalked, source-role checked, rights checked, sensitivity-screened, deduplicated, and evidence-linked. Unresolved/risky records remain quarantined. |
| PROCESSED | Reviewed rare records receive deterministic identity, taxon support, restriction reasons, exact/restricted geometry refs, evidence links, source-role posture, access state, temporal support, and correction posture. |
| CATALOG / TRIPLET | Rare-plant claims may be cataloged or projected only inside governed boundaries with source role, time, evidence, sensitivity, and public-safe caveats preserved. |
| RELEASE CANDIDATE | A public derivative may be proposed only with policy decision, review record, redaction/withholding reason, validation report, release manifest, and rollback target. |
| PUBLISHED | This object is not the published artifact. Only approved public-safe derivatives or summaries may be published. |
| CORRECTION | Taxon change, status update, geometry correction, source withdrawal, sensitivity upgrade, rights change, or redaction failure triggers correction and possible rollback/suppression. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/flora/rare_plant_record.schema.json` beyond the empty scaffold.
- [ ] Add valid fixtures for exact restricted rare occurrence, protected status row, element occurrence, sensitive specimen, generalized public derivative source, suppressed public output, candidate rare record, and source-withdrawn rare record.
- [ ] Add invalid fixtures for exact public rare-plant geometry, missing restriction reason, missing source role, status-list row treated as occurrence proof, missing policy decision, missing redaction receipt for public derivative, missing release manifest, missing rollback target, and public evidence leaking restricted content.
- [ ] Add validator checks for deterministic identity, taxon crosswalk, rare/status authority, source role, restriction reasons, access state, exact/public geometry separation, evidence refs, rights state, sensitivity state, redaction receipt linkage, release linkage, and correction lineage.
- [ ] Add policy/access-control tests proving normal public clients cannot read rare plant exact records.
- [ ] Add policy tests for DENY / ABSTAIN / ERROR outcomes.
- [ ] Add no-network fixtures so CI can validate this contract without live source access.
- [ ] Add non-regression tests for source withdrawal, taxon correction, status update, geometry leak, sensitivity upgrade, redaction bug, and rollback of released derivatives.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Internal evidence resolves and requester has approved purpose/role | `ANSWER` / internal restricted use allowed |
| Evidence missing, source role ambiguous, rights/sensitivity unresolved, public-safe transform incomplete | `ABSTAIN` |
| Public exact geometry attempt, sensitive exposure, rights denial, policy denial, restricted evidence leak | `DENY` |
| Schema/validator/runtime/access-control failure | `ERROR` |

---

## Evidence basis

This contract is grounded in these evidence classes:

| Evidence class | Use |
|---|---|
| Current repo scaffold | Confirms the existing contract path and scaffold status before replacement. |
| Schema metadata | Confirms the paired schema path, title, empty properties, permissive additional properties, PROPOSED status, source doc, and contract doc link. |
| Directory Rules | Confirms `contracts/` owns object meaning, `schemas/` owns machine shape, and domain-specific files live as segments inside responsibility roots. |
| Flora canonical path register | Confirms `RarePlantRecord` is the Flora object-family contract for default-deny public exact geometry and KNHI / NatureServe Explorer Pro provenance. |
| Flora object-family register | Confirms `RarePlantRecord` is an expected Flora object family and that field-level shape remains outside the register. |
| Flora sensitivity posture | Confirms rare/protected/culturally sensitive plant information is protected by default, exact public locations are withheld by default, safe generalized representations are preferred, and transforms require receipts. |
| KFM lifecycle law | Confirms RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED, with publication as a governed transition. |
| KFM public-client rule | Confirms public clients should use governed APIs/released artifacts, not internal/restricted stores or direct model outputs. |

---

## Rollback

Rare-plant rollback is required when a released or review-authorized record weakens protection, leaks sensitive detail, misstates status, misstates source role, violates rights, loses evidence support, or cannot support correction.

Rollback triggers include:

- exact or inferable rare/protected plant location leak;
- habitat/range/phenology join exposes search area or collection window;
- private-land, steward, cultural, or source-restricted detail exposed;
- public derivative generated without valid policy decision or redaction receipt;
- rare record used directly in public layer/API/UI;
- source withdrawal or changed source terms;
- taxon correction, rank/list/status correction, or crosswalk supersession;
- geometry correction, duplicate merge/split, or sensitivity upgrade;
- public evidence projection leaks restricted source rows or reviewer notes;
- release manifest points to restricted source instead of public derivative;
- rollback target missing or invalid.

Rollback artifacts should include affected RarePlantRecord IDs, OccurrenceRestricted IDs, OccurrencePublic derivative IDs, taxon/crosswalk IDs, source records, release IDs, layer IDs, evidence refs, policy decisions, access/review logs where applicable, redaction receipts, correction notices, rollback cards, replacement derivatives, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which source families are approved for rare plant records, and what are their rights/access limits? | NEEDS VERIFICATION | Source registry, source steward review, and policy tests. |
| What exact mapping should KFM use for ranks/statuses/lists from KNHI, NatureServe-style sources, and state/federal lists? | NEEDS VERIFICATION | Taxonomy/status schema fixtures and source profiles. |
| Which generalized public geometry forms are acceptable for each sensitivity case? | NEEDS VERIFICATION | Sensitivity policy and redaction fixtures. |
| What public evidence projection is safe for rare plant records? | NEEDS VERIFICATION | EvidenceBundle projection rules and test fixtures. |
| How should culturally significant plant records be governed with rights-holders and communities? | NEEDS VERIFICATION | Policy, governance, and sovereignty/CARE review. |
| What retention/deletion/suppression rules apply after source withdrawal or rights change? | NEEDS VERIFICATION | Source terms, legal/policy review, and correction workflow. |

---

## Related contracts

- `plant_taxon.md` and `flora_taxon_crosswalk.md` — taxon identity, source names, ranks, statuses, and list mapping support.
- `domain_observation.md` — source observation envelope.
- `flora_occurrence.md` — occurrence-class support.
- `occurrence_restricted.md` — exact/restricted occurrence counterpart.
- `occurrence_public.md` — public-safe occurrence derivative.
- `specimen_record.md` — voucher/specimen support that may include sensitive locality.
- `botanical_survey.md` — survey method, effort, and completeness context.
- `range_polygon.md`, `habitat_association.md`, and `phenology_observation.md` — adjacent surfaces that can amplify sensitive inference and must preserve caveats.
- `redaction_receipt.md` — public-safe transformation proof.
- `domain_validation_report.md` — validation reports for rare records, fixtures, policy, sensitivity, and releases.

---

## Maintainer checklist

- [ ] Confirm this contract against `docs/domains/flora/CANONICAL_PATHS.md`, `docs/domains/flora/OBJECT_FAMILIES.md`, and `docs/domains/flora/SENSITIVITY_POSTURE.md`.
- [ ] Expand the schema in a separate schema PR.
- [ ] Add fixtures and validator coverage before any rare plant records are used for public derivative generation.
- [ ] Add source profiles for approved rare plant/status/rank sources before activation.
- [ ] Add policy/access-control tests for exact geometry, steward-only records, private-land context, source-restricted rows, culturally sensitive records, candidate rows, and public access denial.
- [ ] Confirm public API/UI/map/AI surfaces consume released public-safe derivatives only and never read rare exact records directly.
- [ ] Confirm every public derivative generated from a rare plant record has release manifest, redaction receipt when transformed, correction path, and rollback target.
- [ ] Record any contract/schema/path/source/sensitivity conflict in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
