<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-extraction-site
title: ExtractionSite Contract — Geology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Natural-resources steward
  - OWNER_TBD — Extraction-site steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Sensitivity reviewer
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: restricted-by-default; semantic-contract; geology; extraction-site; natural-resources; source-role-aware; release-gated; public-generalized-only
tags: [kfm, contracts, geology, ExtractionSite, extraction-site, mine, quarry, well, natural-resources, resource-context, reclamation, evidence, source-role, sensitivity, policy, release, correction, rollback]
related:
  - ./README.md
  - ../../../docs/domains/geology/SCOPE.md
  - ../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../docs/domains/geology/sublanes/natural_resources.md
  - ../../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../../schemas/contracts/v1/domains/geology/ExtractionSite.schema.json
  - ../../../schemas/contracts/v1/domains/geology/
  - ../../../policy/domains/geology/
  - ../../../policy/sensitivity/geology/
  - ../../../fixtures/domains/geology/
  - ../../../tests/domains/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a thin scaffold into a Geology ExtractionSite semantic contract."
  - "The exact paired schema path schemas/contracts/v1/domains/geology/ExtractionSite.schema.json was not found in this session; schema shape and casing remain NEEDS VERIFICATION."
  - "ExtractionSite is a physical extraction-site evidence object. It does not prove resource estimates, deposit identity, ownership, lease, permit/title, operator authority, production, reclamation status, or hazards risk by itself."
  - "Active/sensitive extraction detail is restricted/generalized by default; public use requires evidence, rights, sensitivity, validation, policy, review, release, correction, and rollback support."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ExtractionSite — Geology

> Semantic contract for Geology `ExtractionSite`: the evidence-bound object for active, historical, candidate, or public-safe extraction-site references, while keeping physical extraction evidence separate from deposits, estimates, permits, operators, title, production, reclamation, and hazards claims.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: ExtractionSite" src="https://img.shields.io/badge/object-ExtractionSite-blue">
  <img alt="Schema: needs verification" src="https://img.shields.io/badge/schema-NEEDS__VERIFICATION-orange">
  <img alt="Boundary: site not title or permit proof" src="https://img.shields.io/badge/boundary-site__not__title__or__permit__proof-critical">
</p>

`contracts/domains/geology/ExtractionSite.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Site classes](#site-classes) · [Source-role rules](#source-role-rules) · [Anti-collapse rules](#anti-collapse-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/ExtractionSite.md`  
> **Schema posture:** exact paired schema path `schemas/contracts/v1/domains/geology/ExtractionSite.schema.json` was **not found** in this session  
> **Truth posture:** the target contract path exists as a scaffold and is now expanded. Geology doctrine identifies `Extraction Site` as an owned object family for sites of past/present extraction, distinct from permit/operator/title claims. Field-level schema shape, fixtures, validators, policy runtime, source registry records, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `ExtractionSite` is a physical/site-context claim. It does **not** prove a `MineralOccurrence`, `ResourceDeposit`, `ResourceEstimate`, permit, lease, ownership/title, operator authority, production quantity, reclamation status, or hazards risk by itself.

---

## Meaning

`ExtractionSite` is the Geology semantic object for a source-supported place where extraction, quarrying, mining, drilling, salt/mineral/resource removal, or related natural-resource activity occurred, was recorded, or is proposed/candidate within admitted evidence.

It answers:

- Which physical extraction site, mine, quarry, pit, shaft, well pad, lease area, plant-adjacent site, or historical operation is being referenced?
- Which source record, source role, site geometry, site time, commodity context, activity state, and evidence support apply?
- Which mineral occurrence, resource deposit, resource estimate, production record, reclamation record, or permit/operator context may be linked without collapsing identity?
- What public-safe geometry or summary, if any, may be shown?
- Which policy decision, review record, redaction/aggregation receipt, release manifest, correction notice, and rollback target govern downstream use?

An extraction site can support natural-resource interpretation and historical/operational context. It is not a legal title system, a permit registry, a reserve statement, a production database, a hazards alert, or public release approval.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Extraction-site meaning | `contracts/domains/geology/ExtractionSite.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/geology/ExtractionSite.schema.json` or accepted variant | NEEDS VERIFICATION; exact path not found |
| Geology scope | `docs/domains/geology/SCOPE.md` | Confirms owned family and adjacent-lane exclusions |
| Object-family reference | `docs/domains/geology/OBJECT_FAMILIES.md` | Confirms purpose, source roles, sensitivity posture, and anti-collapse discipline |
| Natural-resources doctrine | `docs/domains/geology/sublanes/natural_resources.md` | Confirms extraction context and sublane boundaries |
| Source registry | `data/registry/sources/geology/` | Source identity, rights, cadence, authority limits |
| Policy and sensitivity | `policy/domains/geology/`, `policy/sensitivity/geology/` | Allow/deny/abstain and public-safe exposure decisions |
| Fixtures and tests | `fixtures/domains/geology/`, `tests/domains/geology/` | Valid, invalid, restricted, and public-safe proof cases |
| Release | `release/candidates/geology/`, `release/manifests/geology/` | Promotion decisions and rollback targets |

---

## Schema posture

No exact paired schema was confirmed for this casing/path in this session.

| Schema fact | Current posture |
|---|---|
| Requested contract path | `contracts/domains/geology/ExtractionSite.md` |
| Exact schema tried | `schemas/contracts/v1/domains/geology/ExtractionSite.schema.json` |
| Exact schema result | Not found in this session |
| Naming posture | `ExtractionSite` preserved because the user requested this path while Geology docs use the human-readable `Extraction Site` form |
| Field-level enforcement | NEEDS VERIFICATION |

Until the schema is created or located under an accepted name, this contract is semantic guidance only.

---

## Assertions

A reviewed `ExtractionSite` should semantically assert:

1. **Site identity** — deterministic identity for the physical or source-recorded extraction site.
2. **Source identity** — SourceDescriptor, source record ID, source role, source vintage, rights, cadence, and attribution.
3. **Site class** — mine, quarry, pit, shaft, adit, well pad, oil/gas extraction site, salt/mineral operation, historical site, reclamation-linked site, candidate, or public derivative.
4. **Geometry posture** — exact/internal geometry, source polygon, public-safe generalized footprint, aggregate geography, withheld geometry, or unknown geometry.
5. **Commodity/context support** — commodity or material context without converting the site into a deposit, occurrence, estimate, reserve, or production claim.
6. **Operational state** — active, historical, inactive, reclaimed, abandoned, candidate, unknown, or source-native status with source time and valid time.
7. **Evidence linkage** — source records, maps, reports, imagery, field records, regulatory records, EvidenceRefs, and EvidenceBundles.
8. **Cross-object posture** — linked occurrences, deposits, estimates, permits, production records, reclamation records, operator records, or land records remain separate identities.
9. **Sensitivity posture** — active/sensitive detail, rights-limited records, private/operational context, infrastructure-adjacent context, public-safe state, or withheld state.
10. **Governance state** — validation, policy, review, redaction/aggregation, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating an extraction site as a deposit | A site is a place/activity context; deposit identity remains separate. |
| Treating an extraction site as a resource estimate | Estimates are modeled/compiled quantities with separate assumptions and source roles. |
| Treating a permit or lease as site proof | Permits/leases are regulatory/legal context, not physical extraction truth. |
| Treating a site as ownership/title proof | People/Land owns title/ownership claims. Geology must not harden them into geology truth. |
| Treating operator name as authority or ownership | Operator context requires source role and time; it is not title or legal proof. |
| Treating a site as production proof | Production records are separate source/evidence families. |
| Treating a site as reclamation status | `ReclamationRecord` owns reclamation status/plan/observation posture. |
| Treating a site as hazards risk | Hazards owns risk; Geology may supply context only. |
| Treating public generalized geometry as exact | Public-safe geometry is a derivative with caveats. |
| Treating scaffold or pipeline output as release approval | Publication requires release manifest, policy outcome, correction path, and rollback target. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by any verified schema in this session.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM extraction-site identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `geology`. |
| `object_family` | `ExtractionSite` or accepted canonical spelling after naming reconciliation. |
| `site_class` | Mine, quarry, pit, shaft, adit, well pad, extraction complex, processing-adjacent site, historical site, candidate, or source-native class. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, authority limits. |
| `source_role` | Administrative, regulatory, observed, aggregate, modeled, candidate, or synthetic posture as accepted by KFM source-role rules. |
| `source_record_ref` | Source-native extraction-site, mine, quarry, operation, well, or facility ID. |
| `site_name` | Source-native or public-safe site name. |
| `site_aliases` | Historical names, operator names, source aliases, or public-safe aliases. |
| `commodity_refs` | Commodity/material refs or source-native commodity labels. |
| `mineral_occurrence_refs` | Linked mineral occurrence refs, if evidence supports relationship. |
| `resource_deposit_refs` | Linked resource deposit refs, if evidence supports relationship. |
| `resource_estimate_refs` | Linked estimate refs, if evidence supports relationship and caveats. |
| `reclamation_record_refs` | Linked ReclamationRecord refs, not collapsed into site status. |
| `permit_context_refs` | Permit/regulatory context refs, not title or site proof by themselves. |
| `operator_context_refs` | Operator/source context refs with time and role caveats. |
| `production_context_refs` | Production context refs, not production truth inside ExtractionSite. |
| `location_ref_internal` | Access-controlled site point/polygon/footprint ref. |
| `public_geometry_ref` | Generalized or aggregated public-safe geometry ref, if released. |
| `geometry_precision` | Exact, source precision, generalized, aggregate, withheld, unknown. |
| `activity_state` | Active, inactive, historical, abandoned, reclaimed, planned, candidate, unknown, or source-native. |
| `activity_start_time` | Start/opening/first-observed time, if supported. |
| `activity_end_time` | End/closure/last-observed time, if supported. |
| `source_time` | Source assertion or publication time. |
| `valid_time` | Time range the site/activity claim is valid for. |
| `retrieval_time` | Time KFM retrieved the record. |
| `release_time` | Time a public-safe derivative was released. |
| `correction_time` | Time correction/supersession was applied. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `sensitivity_state` | Restricted, generalized-public, aggregate-public, rights-limited, active-sensitive, public-safe, withheld, or unknown. |
| `policy_decision_ref` | Policy result governing use or release. |
| `review_record_ref` | Source, geology, natural-resources, sensitivity, or release review. |
| `redaction_receipt_ref` | Required when site geometry/fields are generalized or withheld for public output. |
| `aggregation_receipt_ref` | Required when sites become aggregate public products. |
| `validation_report_ref` | Validation report for schema, geometry, source-role, sensitivity, or release candidate. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, source update, name change, geometry correction, rights update, supersession, and rollback lineage. |
| `quality_flags` | Source-role conflict, identity collision, geometry uncertainty, rights unknown, sensitivity unknown, operator/title ambiguity, stale source, or incomplete evidence. |

---

## Site classes

| Class | Meaning | Default posture |
|---|---|---|
| `mine` | Surface or underground mine site. | Site context; not deposit/estimate/title proof. |
| `quarry` | Quarry, borrow pit, or aggregate extraction site. | May be public-safe when generalized and rights allow. |
| `pit_shaft_adit` | Specific physical extraction feature. | Often restricted/generalized if detail is sensitive. |
| `well_pad_or_field_site` | Oil/gas or similar extraction footprint. | Regulatory/operator context must remain separate. |
| `extraction_complex` | Multi-feature operation or site complex. | Requires explicit aggregation/geometry semantics. |
| `historical_site` | Historical or legacy extraction site. | Source time and uncertainty are material. |
| `reclamation_linked_site` | Site linked to reclamation record. | Reclamation status remains separate. |
| `candidate_record` | Unreviewed import or unresolved source row. | WORK/QUARANTINE until reviewed. |
| `public_derivative` | Released generalized or aggregated representation. | Requires release manifest and rollback target. |

---

## Source-role rules

| Source pattern | Canonical source-role posture | ExtractionSite posture |
|---|---|---|
| Mine inventory, permit registry, state database, agency list | `administrative` or `regulatory` | Identifies context/status; not ownership/title/deposit proof by itself. |
| Field report, mapped site, observed disturbance, source map feature | `observed` | Supports physical site claim when time, geometry, and evidence resolve. |
| Compiled mineral/resource database or regional summary | `aggregate` | Aggregate support only unless source row resolves. |
| Modeled extraction footprint or inferred historical site | `modeled` | Must remain modeled/inferred with uncertainty. |
| Unreviewed import, fuzzy site match, unresolved operator row | `candidate` | Quarantine until identity, source, rights, and sensitivity resolve. |
| AI-generated or hypothetical extraction-site note | `synthetic` | Reality-boundary disclosure; not source evidence. |

Source role must survive downstream projection. A regulatory row cannot be worded into observed extraction evidence unless independent observation supports it.

---

## Anti-collapse rules

`ExtractionSite` participates in the Natural Resources anti-collapse discipline.

```text
ExtractionSite != MineralOccurrence
ExtractionSite != ResourceDeposit
ExtractionSite != ResourceEstimate
ExtractionSite != PermitRecord
ExtractionSite != ProductionRecord
ExtractionSite != ReserveClaim
ExtractionSite != ReclamationRecord
ExtractionSite != ownership / lease / title proof
ExtractionSite != hazards risk
```

Any join among those identities must be explicit, evidence-bound, source-role-aware, time-aware, and policy-reviewed. Joining one to another as identity equality is a validation failure and should produce `ABSTAIN` or `DENY` depending on exposure risk.

---

## Sensitivity and release

Extraction-site records can combine location, resource, operational, regulatory, land/title, infrastructure-adjacent, and rights-sensitive context. The safe default is restricted/internal handling unless public-safe generalization or aggregation has been reviewed and released.

Rules:

- Exact active/sensitive site detail is not a normal public artifact.
- Public derivatives should use generalized footprints, aggregate regions, public-safe labels, or suppression where needed.
- Operator, permit, lease, production, and title context must be labeled as context only and kept under the owning authority path.
- Public outputs must preserve source role, source time, valid time, activity state, geometry precision, rights posture, and caveats.
- Candidate, synthetic, rights-unknown, sensitivity-unknown, stale, or evidence-incomplete records must not enter public outputs as authoritative site facts.
- Any derivative used by map/API/UI/AI surfaces needs EvidenceBundle support, policy decision, review, release manifest, correction path, and rollback target.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native site rows, names, coordinates, permit/operator context, maps, imagery, and source notes remain source-bound. |
| WORK / QUARANTINE | Candidate sites are normalized, source-role checked, identity-crosswalked, rights/sensitivity-screened, geometry-checked, and evidence-linked. |
| PROCESSED | Reviewed sites receive deterministic identity, source support, geometry posture, activity state, evidence refs, sensitivity state, and correction posture. |
| CATALOG / TRIPLET | Claims may be cataloged only with source role, temporal support, evidence, geometry precision, access state, and caveats preserved. |
| RELEASE CANDIDATE | Public derivatives require validation report, policy decision, review record, redaction/aggregation receipt where needed, release manifest, and rollback target. |
| PUBLISHED | Only released generalized or aggregated public-safe derivatives appear in public clients. |
| CORRECTION | Source update, site identity merge/split, name change, geometry correction, rights change, activity-state update, or stale-state update triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Create or locate the accepted paired schema path.
- [ ] Add valid fixtures for active mine, historical mine, quarry, well-pad/field site, extraction complex, reclamation-linked site, candidate import, and public generalized/aggregated derivative.
- [ ] Add invalid fixtures for missing source descriptor, missing source role, identity collision, operator/title collapse, permit treated as site proof, site treated as deposit/estimate/proven reserve, exact sensitive public geometry, missing policy decision, missing receipt, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, source keys, site class, geometry precision, activity state, temporal support, source role, evidence refs, policy refs, release refs, correction refs, and anti-collapse constraints.
- [ ] Add policy/access tests proving public clients consume released derivatives only.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for source revision, identity merge/split, operator/name changes, geometry correction, rights update, public derivative rebuild, and rollback.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, source role is clear, policy allows, derivative is released | `ANSWER` / public-safe derivative may be shown |
| Evidence, rights, source role, identity, geometry, or activity state is incomplete | `ABSTAIN` |
| Restricted detail would be exposed, rights deny use, or release is absent | `DENY` |
| Schema, validator, source-read, transform, or release-runtime failure | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms the target file existed and was a scaffold before replacement. | Does not prove contract maturity. |
| Geology scope doc | Confirms Geology owns Extraction Site and excludes ownership/title, hazards risk, hydrology measurement, and UI/AI truth. | Records broader naming drift and field realization remains PROPOSED. |
| Geology object-family doc | Confirms ExtractionSite purpose, proposed key fields, material times, sensitivity posture, and source roles. | Does not prove schema or validator enforcement. |
| Natural Resources sublane doc | Confirms extraction context belongs in the resource-focused Geology sublane while permit/lease context must not become deposit or title proof. | Docs-side sublane placement is itself PROPOSED. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized ExtractionSite weakens source integrity, misstates source role, collapses resource/permit/title identities, exposes restricted detail, or depends on superseded source, geometry, rights, or release evidence.

Rollback triggers include:

- source record corrected, withdrawn, merged, or split;
- site name, operator context, activity state, or geometry corrected;
- permit, lease, operator, or title context was presented as site proof;
- site was treated as a deposit, estimate, reserve, production claim, reclamation status, or hazards risk;
- public derivative exposes restricted detail or lacks a redaction/aggregation receipt;
- release manifest lacks policy decision, correction path, or rollback target;
- public API/UI/AI reads RAW/WORK/QUARANTINE or internal records as public truth.

Rollback artifacts should include affected ExtractionSite IDs, source record IDs, site geometry refs, linked occurrence/deposit/estimate/reclamation/context refs, public derivative refs, release IDs, evidence refs, policy decisions, receipts, correction notices, rollback cards, replacement records, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| What is the accepted paired schema path and casing for `ExtractionSite`? | NEEDS VERIFICATION | Schema-home inspection and ADR-0001 alignment. |
| Which site classes should be canonical for Kansas extraction contexts? | NEEDS VERIFICATION | Source registry, fixtures, and natural-resources steward review. |
| Which public geometry classes are acceptable for active or sensitive extraction sites? | NEEDS VERIFICATION | Policy and release fixture review. |
| Where should PermitRecord, ProductionRecord, and ReserveClaim live? | NEEDS VERIFICATION | Natural-resources ADR and cross-lane review. |
| How should operator/lease context be displayed without implying title or legal authority? | NEEDS VERIFICATION | People/Land and UI/API projection review. |
| How should ExtractionSite connect to ReclamationRecord without inheriting reclamation status? | NEEDS VERIFICATION | Companion contract and schema references. |

---

## Related contracts and docs

- `docs/domains/geology/SCOPE.md` — Geology owns/does-not-own boundary.
- `docs/domains/geology/OBJECT_FAMILIES.md` — Geology object-family reference and anti-collapse rules.
- `docs/domains/geology/sublanes/natural_resources.md` — Natural Resources sublane doctrine.
- `schemas/contracts/v1/domains/geology/` — expected machine-shape home, pending verification.
- `policy/domains/geology/` — expected policy home, pending verification.
- `release/manifests/geology/` — expected release/rollback home, pending verification.

---

## Maintainer checklist

- [ ] Create or verify paired schema and fixtures.
- [ ] Add anti-collapse tests for occurrence/deposit/estimate/site/permit/production/reclamation/title distinctions.
- [ ] Add policy tests for restricted/internal vs public-safe derivative access.
- [ ] Add source profiles and SourceDescriptor records before activation.
- [ ] Confirm public map/API/UI surfaces use only released generalized or aggregated derivatives.
- [ ] Confirm EvidenceBundle resolution before public or AI claims.
- [ ] Confirm correction and rollback targets before promotion.
- [ ] Record unresolved path/schema/source-role drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
