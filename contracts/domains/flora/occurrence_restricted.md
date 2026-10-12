<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-flora-occurrence-restricted
title: Restricted Occurrence Contract — Flora
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners: OWNER_TBD — Flora steward · Occurrence steward · Restricted-data steward · Contract steward · Source steward · Schema steward · Sensitivity reviewer · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: restricted; semantic-contract; flora; restricted-occurrence; exact-geometry; steward-only; evidence-bound; source-role-aware; sensitivity-aware; no-public-publication-authority
tags: [kfm, contracts, flora, occurrence-restricted, restricted-occurrence, exact-geometry, rare-plant, steward-only, geoprivacy, evidence, source-role, sensitivity, policy, redaction, release, correction, rollback]
related:
  - ./README.md
  - ./domain_observation.md
  - ./domain_feature_identity.md
  - ./flora_occurrence.md
  - ./occurrence_public.md
  - ./rare_plant_record.md
  - ./specimen_record.md
  - ./plant_taxon.md
  - ./flora_taxon_crosswalk.md
  - ./phenology_observation.md
  - ./vegetation_community.md
  - ./invasive_plant_record.md
  - ./range_polygon.md
  - ./habitat_association.md
  - ./botanical_survey.md
  - ./redaction_receipt.md
  - ./domain_validation_report.md
  - ../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../docs/domains/flora/OBJECT_FAMILIES.md
  - ../../../docs/domains/flora/SENSITIVITY_POSTURE.md
  - ../../../schemas/contracts/v1/domains/flora/occurrence_restricted.schema.json
  - ../../../fixtures/domains/flora/occurrence_restricted/
  - ../../../tests/domains/flora/
  - ../../../policy/domains/flora/
  - ../../../policy/sensitivity/flora/
  - ../../../data/registry/sources/flora/
  - ../../../release/manifests/
notes:
  - "Expanded from a thin scaffold into a Flora restricted occurrence semantic contract."
  - "The paired schema is a PROPOSED scaffold with no declared fields and additionalProperties=true; field-level machine enforcement remains NEEDS VERIFICATION."
  - "OccurrenceRestricted is an internal exact-geometry or high-sensitivity occurrence surface; it is never the source for data/published and never a normal public-client path."
  - "Public exposure requires a separate OccurrencePublic derivative, policy decision, review record, redaction receipt when transformed, release manifest, correction path, and rollback target."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Occurrence Restricted — Flora

> Semantic contract for Flora `OccurrenceRestricted`: the internal, access-controlled occurrence surface for exact geometry, steward-only evidence, sensitive source detail, private-land context, rare-plant records, and other Flora occurrence support that must not be exposed through normal public paths.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: domains/flora" src="https://img.shields.io/badge/family-domains%2Fflora-2ea44f">
  <img alt="Type: semantic contract" src="https://img.shields.io/badge/type-semantic__contract-blue">
  <img alt="Schema: proposed scaffold" src="https://img.shields.io/badge/schema-PROPOSED__scaffold-lightgrey">
  <img alt="Boundary: restricted not public source" src="https://img.shields.io/badge/boundary-restricted__not__public__source-critical">
</p>

`contracts/domains/flora/occurrence_restricted.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Restricted classes](#restricted-classes) · [Source-role rules](#source-role-rules) · [Sensitivity and access](#sensitivity-and-access) · [Public derivative relationship](#public-derivative-relationship) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/flora/occurrence_restricted.md`  
> **Schema path:** `schemas/contracts/v1/domains/flora/occurrence_restricted.schema.json`  
> **Truth posture:** the target contract path exists as a scaffold, the paired schema path exists as a PROPOSED scaffold, and the Flora canonical path register identifies `OccurrenceRestricted` as the internal exact-geometry occurrence object with steward-only access that is never the source for `data/published/`. Field-level schema shape, fixtures, validators, access-control runtime, source registry terms, policy runtime, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `OccurrenceRestricted` is a protected internal surface. It must not be read by normal public clients, must not be treated as a published artifact, and must not be used as a shortcut around `OccurrencePublic`, `RedactionReceipt`, policy review, release manifests, correction notices, or rollback targets.

---

## Meaning

`OccurrenceRestricted` is the Flora semantic object for an occurrence-class record that contains exact, high-precision, access-controlled, steward-only, rights-limited, private, culturally sensitive, rare-plant, source-restricted, or otherwise non-public Flora occurrence support.

It answers:

- Which exact or restricted occurrence evidence exists?
- Which source, source role, taxon, geometry, time, and uncertainty support the restricted record?
- Why is the record restricted, and what access state applies?
- Which public-safe derivative, if any, may be produced without exposing restricted detail?
- Which review, policy, source-rights, redaction, release, correction, and rollback controls govern downstream use?
- Which fields must stay out of public API/UI/map payloads and AI answers?

A restricted occurrence can support internal review, evidence resolution, redaction, conservation stewardship, quality checks, and controlled derivative generation. It is not a public-facing object and is not a release artifact.

---

## Repo fit

The Flora lane follows the responsibility-root pattern: contracts define semantic meaning, schemas define machine shape, policy gates admissibility/release, fixtures/tests prove behavior, and data/release roots carry lifecycle and publication state.

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Restricted meaning | `contracts/domains/flora/occurrence_restricted.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/flora/occurrence_restricted.schema.json` | Linked only; currently scaffolded |
| Umbrella occurrence meaning | `contracts/domains/flora/flora_occurrence.md` | Upstream occurrence-class meaning; not replaced |
| Public derivative counterpart | `contracts/domains/flora/occurrence_public.md` | Public-safe derivative; must be separately released |
| Rare/protected source | `contracts/domains/flora/rare_plant_record.md` | Sensitive upstream specialization; often requires restricted handling |
| Voucher/source support | `specimen_record.md`, `domain_observation.md`, `botanical_survey.md` | Evidence and observation context |
| Taxon support | `plant_taxon.md`, `flora_taxon_crosswalk.md` | Taxon identity and label support |
| Redaction proof | `contracts/domains/flora/redaction_receipt.md` | Required for transformed public outputs |
| Validation report | `contracts/domains/flora/domain_validation_report.md` | Validates restricted record and derivative readiness |
| Policy and sensitivity | `policy/domains/flora/`, `policy/sensitivity/flora/` | Access/release and fail-closed decisions |
| Source registry | `data/registry/sources/flora/` | Rights, cadence, attribution, and authority limits |
| Published layers | `data/published/layers/flora/`, `release/` | Must consume only approved public derivatives, not this object |

---

## Schema posture

The paired schema currently exists as a **PROPOSED scaffold**.

| Schema fact | Current posture |
|---|---|
| Schema file path | `schemas/contracts/v1/domains/flora/occurrence_restricted.schema.json` |
| Schema title | `Occurrence Restricted` |
| Declared properties | none yet |
| Required fields | none declared |
| Additional properties | `true` |
| Schema status | `PROPOSED` |
| Source document | `docs/domains/flora/CANONICAL_PATHS.md` |
| Contract document | `contracts/domains/flora/occurrence_restricted.md` |

Because the schema is empty and permissive, this contract defines **semantic expectations** for future schema fields, fixtures, validators, access-control checks, sensitivity policy, source registry links, derivative generation, release gating, correction flows, and rollback handling. It does not claim current machine enforcement.

---

## Assertions

A reviewed `OccurrenceRestricted` should semantically assert:

1. **Restricted identity** — deterministic internal identity distinct from public derivative identity.
2. **Occurrence support** — the source occurrence, specimen, survey, rare-plant, invasive, phenology, or other Flora record support.
3. **Exact or restricted geometry** — precise point, polygon, route, plot, parcel-adjacent, site, grid, or steward-controlled location support.
4. **Restriction reason** — rare-plant, steward-only, source-restricted, private-land, culturally sensitive, vulnerable habitat, rights-limited, review-pending, or security-sensitive posture.
5. **Source and role** — SourceDescriptor, source role, source record ID, source authority limits, source terms, cadence, and attribution.
6. **Taxon support** — taxon identity, taxon crosswalk, source-native label, and candidate/review state.
7. **Temporal support** — observed, valid, source, retrieval, review, release-candidate, stale-state, and correction times where material.
8. **Evidence support** — EvidenceRef/EvidenceBundle links, including internal evidence refs that may not be public-safe.
9. **Access posture** — allowed user/role/service boundary, stewardship gate, audit requirement, and deny-by-default behavior.
10. **Governance state** — validation, policy, review, derivative generation, redaction, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Public clients reading restricted records | Public clients use governed released derivatives only. |
| Treating restricted exact geometry as published truth | This object is internal evidence support, not a release artifact. |
| Using restricted records directly in `data/published/` | Canonical path register states restricted occurrences are never the source for `data/published/`. |
| Omitting restriction reason | Access, policy, and redaction cannot be evaluated without explicit restriction posture. |
| Creating public maps from exact rare-plant points | Exact rare-plant or sensitive locations fail closed. |
| Leaking restricted evidence through citations or AI answers | Evidence projection must be public-safe or abstain/deny. |
| Treating access approval as release approval | Internal access can support review, not public publication. |
| Suppressing correction history | Restricted records still require correction, supersession, audit, and rollback lineage. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical restricted occurrence identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `flora` for this contract. |
| `restricted_record_class` | `exact_point`, `exact_polygon`, `plot`, `transect`, `parcel_sensitive`, `steward_only`, `rare_plant_exact`, `source_restricted`, `review_pending`, or `internal_derivation_source`. |
| `upstream_occurrence_ref` | FloraOccurrence or occurrence-family ref. |
| `rare_plant_record_ref` | Rare/protected record, when applicable. |
| `specimen_record_ref` | Voucher/specimen support, when applicable. |
| `domain_observation_ref` | Upstream observation-envelope reference, when applicable. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, and authority limits. |
| `source_role` | Canonical source role: `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, or `synthetic`. |
| `source_record_ref` | Source-native occurrence/specimen/survey/event ID. |
| `taxon_ref` | PlantTaxon or reviewed taxon candidate. |
| `taxon_crosswalk_ref` | Taxon crosswalk support. |
| `geometry_ref` | Exact or restricted geometry reference. |
| `geometry_type` | Point, polygon, plot, route, transect, grid, parcel-adjacent, source geometry, or withheld. |
| `geometry_precision` | Exact, high precision, source precision, uncertain, derived, generalized-internally, or unknown. |
| `location_uncertainty` | Numeric, categorical, or source-native uncertainty. |
| `restriction_reasons` | Rare-plant, steward-only, private-land, cultural, source-restricted, rights-limited, safety, review-pending, or policy-blocked reasons. |
| `access_state` | Denied by default, steward-only, source-steward, sensitivity-reviewer, internal-validation, release-review, admin-breakglass, or expired. |
| `access_policy_ref` | Policy/access-control rule governing internal use. |
| `audit_requirement` | Required audit receipt, access log, reviewer note, or purpose limitation. |
| `public_derivative_ref` | OccurrencePublic derivative, when one exists. |
| `redaction_receipt_ref` | Required if a public derivative was generated from this restricted support. |
| `observed_time` | Time the occurrence event occurred, when known. |
| `valid_time` | Time span this restricted record supports. |
| `source_time` | Time asserted by source. |
| `retrieval_time` | Time KFM retrieved the source material. |
| `review_time` | Time restriction/review state was assigned. |
| `evidence_refs_internal` | Internal evidence refs, access-controlled. |
| `evidence_refs_public_projection` | Public-safe evidence projection, if one exists. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `sensitivity_state` | Sensitive ecological, rare-plant, steward, private-land, cultural, source-restricted, or unknown posture. |
| `validation_report_ref` | Validation report for this restricted record or derivative candidate. |
| `policy_decision_ref` | Policy result governing access, transformation, or release. |
| `review_record_ref` | Steward/source/sensitivity/release review record. |
| `release_candidate_ref` | Release candidate that consumes a transformed derivative, if applicable. |
| `correction_refs` | CorrectionNotice, supersession, withdrawal, stale-state, and rollback lineage. |
| `quality_flags` | Duplicate, stale, taxon-conflict, geometry-conflict, access-conflict, rights-unknown, sensitivity-unknown, source-role-conflict, or incomplete-evidence flags. |

---

## Restricted classes

| Class | Meaning | Default posture |
|---|---|---|
| `exact_point` | Exact or high-precision point geometry. | Internal only; public derivative required. |
| `exact_polygon` | Exact polygon or site boundary. | Internal only unless transformed and released. |
| `plot` | Survey plot or vegetation plot with sensitive coordinates. | Internal/steward access. |
| `transect` | Survey route/transect with sensitive location detail. | Internal/steward access. |
| `parcel_sensitive` | Location could expose private-land or landowner context. | Fail closed unless policy allows transformed output. |
| `steward_only` | Source or steward restricts record access. | Deny by default outside approved roles. |
| `rare_plant_exact` | Exact rare/protected plant occurrence. | Deny public exact geometry. |
| `source_restricted` | Source terms restrict redistribution or disclosure. | Follow source registry and policy decision. |
| `review_pending` | Record needs source/taxon/sensitivity review. | WORK/QUARANTINE; not public. |
| `internal_derivation_source` | Internal support used to generate public derivative. | May feed redacted derivative only through governed release process. |

---

## Source-role rules

| Source pattern | Canonical `source_role` | Restricted posture |
|---|---|---|
| Steward-reviewed field observation, specimen-backed point, survey detection | `observed` | Can support restricted occurrence when evidence, taxon, geometry, time, and rights resolve. |
| Rare/protected status, recovery plan, agency restriction | `regulatory` | Can justify restriction; not occurrence proof by itself. |
| Suitability model or inferred sensitive location | `modeled` | Must remain modeled; exact exposure generally denied. |
| Atlas/portal/grid summary with restricted internal cells | `aggregate` | Restricted only when support scale or source terms require it; no exact claims. |
| Management/project/site table | `administrative` | Supports internal context; not biological occurrence truth by itself. |
| Unreviewed import or unresolved community-science row | `candidate` | WORK/QUARANTINE until reviewed. |
| AI-generated or reconstructed sensitive location | `synthetic` | Must not be treated as real occurrence; reality-boundary disclosure required. |

Source role must remain visible to internal reviewers and must not be silently upgraded during derivative generation.

---

## Sensitivity and access

`OccurrenceRestricted` is deny-by-default. Access is a governed exception for a defined purpose, not a public path.

Rules:

- Exact rare-plant locations, steward-controlled records, private-land context, culturally sensitive plant knowledge, and source-restricted details must fail closed.
- Internal access must be purpose-limited, role-limited, auditable, and reviewable.
- Public clients, map layers, normal UI surfaces, AI answers, and released artifacts must not consume this object directly.
- Evidence projections must avoid leaking exact coordinates, source-private notes, reviewer notes, or restricted source rows.
- Break-glass/admin shortcuts, if ever implemented, must be constrained, documented, audited, and prevented from becoming the normal public path.
- Candidate, rights-unknown, sensitivity-unknown, or evidence-incomplete records must remain in WORK/QUARANTINE or restricted review, not public release.

---

## Public derivative relationship

A restricted occurrence can inform a public representation only through a governed derivative path:

```text
OccurrenceRestricted
  -> sensitivity/policy/review
  -> RedactionReceipt or withholding reason
  -> OccurrencePublic release candidate
  -> validation report
  -> ReleaseManifest / PromotionDecision
  -> published public layer/API/UI payload
```

The public derivative must preserve support scale, source role, uncertainty, time, caveats, release state, correction state, and rollback target without exposing restricted exact detail.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source exact coordinates, restricted source rows, specimen details, survey routes, steward notes, and sensitive geometry remain source-bound. |
| WORK / QUARANTINE | Candidate restricted records are normalized, taxon-crosswalked, source-role checked, rights checked, sensitivity-screened, deduplicated, and evidence-linked. Unresolved/risky records remain quarantined. |
| PROCESSED | Reviewed restricted records receive deterministic identity, exact/restricted geometry refs, evidence links, source-role posture, access state, sensitivity state, temporal support, and correction posture. |
| CATALOG / TRIPLET | Restricted triples may exist only inside governed/internal access boundaries with source role, time, evidence, and sensitivity preserved. |
| RELEASE CANDIDATE | A public derivative may be proposed only with redaction/withholding reason, policy decision, review state, validation report, and rollback target. |
| PUBLISHED | This object is never the published artifact. Only `OccurrencePublic` or another approved public-safe derivative may be published. |
| CORRECTION | Taxon change, geometry correction, source withdrawal, rights change, sensitivity update, access-policy issue, or redaction failure triggers correction and possible rollback/suppression. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/flora/occurrence_restricted.schema.json` beyond the empty scaffold.
- [ ] Add valid fixtures for exact rare-plant point, steward-only occurrence, source-restricted occurrence, private-land sensitive occurrence, review-pending occurrence, and restricted-to-public derivative candidate.
- [ ] Add invalid fixtures for missing restriction reason, missing source role, missing access state, missing policy ref, public path reading restricted record, exact rare-plant geometry in published payload, missing redaction receipt for derivative, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, source role, exact/restricted geometry ref, restriction reasons, access state, evidence refs, rights state, sensitivity state, redaction receipt linkage, public derivative linkage, release linkage, and correction lineage.
- [ ] Add policy tests for DENY / ABSTAIN / ERROR outcomes.
- [ ] Add access-control tests proving normal public clients cannot read restricted occurrence payloads.
- [ ] Add no-network fixtures so CI can validate this contract without live source access.
- [ ] Add non-regression tests for source withdrawal, geometry leak, taxonomy correction, sensitivity upgrade, access-policy regression, and redaction-method bug.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Internal evidence resolves and requester has approved purpose/role | `ANSWER` / internal restricted use allowed |
| Evidence missing, source role ambiguous, rights/sensitivity unresolved, purpose unsupported | `ABSTAIN` |
| Public access attempt, sensitive exposure, rights denial, policy denial, restricted evidence leak | `DENY` |
| Schema/validator/runtime/access-control failure | `ERROR` |

---

## Evidence basis

This contract is grounded in these evidence classes:

| Evidence class | Use |
|---|---|
| Current repo scaffold | Confirms the existing contract path and scaffold status before replacement. |
| Schema metadata | Confirms the paired schema path, title, empty properties, permissive additional properties, PROPOSED status, source doc, and contract doc link. |
| Directory Rules | Confirms `contracts/` owns object meaning, `schemas/` owns machine shape, and domain-specific files live as segments inside responsibility roots. |
| Flora canonical path register | Confirms `OccurrenceRestricted` is the internal exact-geometry occurrence object, has steward-only access, and is never the source for `data/published/`. |
| Flora object-family register | Confirms Flora object-family scope and states that field-level shape remains outside the register. |
| KFM lifecycle law | Confirms RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED, with publication as a governed transition. |
| KFM public-client rule | Confirms public clients should use governed APIs/released artifacts, not internal stores or direct model outputs. |

---

## Rollback

Restricted occurrence rollback is required when an internal record causes or could cause sensitive exposure, wrong derivative generation, wrong public label, incorrect review state, access-control regression, or publication of unsupported claims.

Rollback triggers include:

- exact or inferable rare-plant location leak;
- private-land, steward, cultural, or source-restricted detail exposed;
- public derivative generated without valid redaction receipt;
- restricted record used directly in public layer/API/UI;
- source withdrawal or changed source terms;
- taxon correction or crosswalk supersession;
- geometry correction or duplicate merge/split;
- access policy misconfiguration;
- reviewer reversal or sensitivity upgrade;
- release manifest points to restricted source instead of public derivative;
- rollback target missing or invalid.

Rollback artifacts should include affected restricted IDs, public derivative IDs, upstream occurrence IDs, release IDs, layer IDs, evidence refs, policy decisions, access logs where applicable, redaction receipts, correction notices, rollback cards, replacement derivatives, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which role/access model governs steward-only Flora exact geometry? | NEEDS VERIFICATION | Resolve in policy/access docs and tests before promotion. |
| Should restricted upstream refs be embedded in public derivatives or stored only in release metadata? | NEEDS VERIFICATION | Decide with API/UI/release stewards. |
| What exact fields are always forbidden from public evidence projection? | NEEDS VERIFICATION | Define public EvidenceBundle projection rules and fixtures. |
| How should source geoprivacy flags map into KFM restricted classes? | NEEDS VERIFICATION | Source registry + sensitivity policy fixtures. |
| Which break-glass/admin pattern is allowed, if any? | PROPOSED / NEEDS VERIFICATION | Requires security/policy review, audit requirements, and documentation. |
| What retention/deletion rules apply to source-withdrawn restricted geometry? | NEEDS VERIFICATION | Source terms, legal/policy review, and correction workflow. |

---

## Related contracts

- `flora_occurrence.md` — umbrella occurrence-class source support.
- `occurrence_public.md` — public-safe derivative counterpart.
- `rare_plant_record.md` — rare/protected plant sensitivity source.
- `specimen_record.md` — voucher/specimen support that may include sensitive collection locality.
- `domain_observation.md` — source observation envelope.
- `plant_taxon.md` and `flora_taxon_crosswalk.md` — taxon identity and public label support.
- `redaction_receipt.md` — public-safe transformation proof.
- `domain_validation_report.md` — validation reports for restricted records and public derivative candidates.
- `range_polygon.md`, `habitat_association.md`, `vegetation_community.md`, `invasive_plant_record.md`, and `phenology_observation.md` — adjacent or downstream users that must not leak restricted details.

---

## Maintainer checklist

- [ ] Confirm this contract against `docs/domains/flora/CANONICAL_PATHS.md` and `docs/domains/flora/OBJECT_FAMILIES.md`.
- [ ] Expand the schema in a separate schema PR.
- [ ] Add fixtures and validator coverage before any restricted Flora occurrence is used for derivative generation.
- [ ] Add policy/access-control tests for rare-plant, steward-only, private-land, source-restricted, candidate, synthetic, stale-state, and public-access-denied cases.
- [ ] Confirm public API/UI/map surfaces consume released `OccurrencePublic` derivatives only and never read restricted exact records directly.
- [ ] Confirm every public derivative generated from a restricted record has release manifest, redaction receipt when transformed, and rollback target.
- [ ] Record any contract/schema/path conflict in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
