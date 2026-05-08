<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION-ADR-GEOLOGY-PUBLIC-SAFE-GEOMETRY
title: ADR-geology-public-safe-geometry
type: standard
version: v1
status: draft
owners: OWNER_TBD_NEEDS_VERIFICATION
created: 2026-05-08
updated: 2026-05-08
policy_label: NEEDS_VERIFICATION
related: [./README.md, ./ADR-0001-schema-home.md, ../domains/geology/README.md, ../../README.md, ../../policy/README.md]
tags: [kfm, adr, geology, natural-resources, public-safe-geometry, sensitivity, evidence, release, rollback]
notes: [Replaces placeholder ADR text at docs/adr/ADR-geology-public-safe-geometry.md. Decision remains proposed until policy, validator, fixture, release, and rollback evidence are verified. Owners, policy label, CODEOWNERS routing, source terms, and enforcement maturity remain NEEDS VERIFICATION.]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-geology-public-safe-geometry

Decision record for separating exact/internal geology geometry from public-safe geology and natural-resource geometry in KFM.

<p align="center">
  <img alt="ADR status: proposed" src="https://img.shields.io/badge/ADR-proposed-lightgrey">
  <img alt="document status: draft" src="https://img.shields.io/badge/doc-draft-f59e0b">
  <img alt="owners: needs verification" src="https://img.shields.io/badge/owners-NEEDS%20VERIFICATION-b60205">
  <img alt="geometry posture: public safe" src="https://img.shields.io/badge/geometry-public--safe-0a7ea4">
  <img alt="policy posture: fail closed" src="https://img.shields.io/badge/policy-fail--closed-critical">
  <img alt="rollback: required" src="https://img.shields.io/badge/rollback-required-5319e7">
</p>

<p align="center">
  <a href="#adr-header">Header</a> ·
  <a href="#context">Context</a> ·
  <a href="#decision">Decision</a> ·
  <a href="#geometry-roles">Geometry roles</a> ·
  <a href="#policy-rules">Policy rules</a> ·
  <a href="#impact-map">Impact</a> ·
  <a href="#validation">Validation</a> ·
  <a href="#rollback-and-supersession">Rollback</a> ·
  <a href="#open-verification">Open verification</a>
</p>

> [!IMPORTANT]
> **Decision status:** `proposed`.
>
> **Enforcement status:** `NEEDS VERIFICATION`.
>
> This ADR records the decision KFM should use for geology public-safe geometry. It does **not** prove that geology schemas, policy rules, validators, fixtures, release manifests, redaction receipts, MapLibre layers, Evidence Drawer payloads, Focus Mode behavior, or CI enforcement already exist.

> [!CAUTION]
> Public-safe geometry is not a cosmetic simplification. It is a governed publication decision that must preserve source role, source scale, evidence support, policy state, review state, transform receipt, release state, correction path, and rollback target.

---

## ADR header

| Field | Value |
|---|---|
| ADR ID | `ADR-geology-public-safe-geometry` |
| Target path | `docs/adr/ADR-geology-public-safe-geometry.md` |
| Title | `ADR-geology-public-safe-geometry` |
| Status | `proposed` |
| Decision date | `2026-05-08` |
| Authors / owners | `OWNER_TBD_NEEDS_VERIFICATION` |
| Reviewers | `REVIEWER_TBD_NEEDS_VERIFICATION` |
| Policy label | `NEEDS_VERIFICATION` |
| Scope | Geology and non-biological natural-resource public geometry, map layers, Evidence Drawer payloads, governed API payloads, Focus Mode context, release gates, correction, and rollback |
| Affected paths | `docs/adr/`, `docs/domains/geology/`, `schemas/contracts/v1/`, `policy/`, `tests/`, `fixtures/`, `tools/validators/`, `data/registry/`, `data/receipts/`, `data/proofs/`, `data/published/`, `release/`, `apps/` |
| Related ADRs | [`./ADR-0001-schema-home.md`](./ADR-0001-schema-home.md), geology source-role and schema-home ADRs `NEEDS VERIFICATION` |
| Supersedes | Placeholder ADR text in this file |
| Superseded by | `none` |
| Decision confidence | `PROPOSED decision` / `NEEDS VERIFICATION enforcement` |
| Review state | `draft` |
| Rollback target | `ROLLBACK_TARGET_TBD` |

[Back to top](#top)

---

## Context

The existing ADR placeholder establishes that KFM needs a geology public-safe geometry decision, but it does not yet define the governing rule, geometry roles, validation burden, public-client behavior, or rollback path.

The geology lane handles public-facing and steward-facing material with different exposure risk: bedrock and surficial map units, interpreted boundaries, structures, stratigraphy, boreholes, well logs, cores, measured sections, geophysics, geochemistry, mineral occurrences, resource estimates, extraction context, production context, and reclamation context. These are not epistemically interchangeable.

KFM’s broader trust law requires:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Public clients and ordinary UI surfaces must consume governed APIs, released artifacts, and EvidenceBundle-backed payloads. They must not read RAW, WORK, QUARANTINE, unpublished candidates, exact/internal stores, source-system side effects, secrets, or direct model runtime outputs.

### Problem

Geology geometry can look authoritative simply because it renders well on a map. That is dangerous.

A public layer may display an interpreted source-scale boundary, a generalized derivative, a redacted resource feature, an aggregate index, a modeled potential surface, or a display-only geometry. If KFM does not label those roles explicitly, public users may mistake:

- exact borehole or sample coordinates for publishable public facts;
- generalized display geometry for canonical evidence geometry;
- modeled potential for a known occurrence, deposit, reserve, or extraction claim;
- permit, lease, operator, parcel, or production data for physical geology;
- MapLibre styling for evidence;
- AI or Focus language for reviewed source support.

### Why this is architecture-significant

This decision controls a public trust boundary. It affects source descriptors, schemas, source-role policy, sensitivity rules, redaction/generalization receipts, release manifests, layer descriptors, Evidence Drawer payloads, Focus Mode behavior, correction notices, rollback cards, and validator fixtures.

A routine implementation note is not enough.

[Back to top](#top)

---

## Evidence basis

| Evidence item | Source / path | What it supports | Truth label |
|---|---|---|---|
| Existing target ADR placeholder | `docs/adr/ADR-geology-public-safe-geometry.md` | The ADR path exists and currently needs real decision language. | `CONFIRMED repo evidence` |
| ADR directory README | `docs/adr/README.md` | ADRs are decision records; decisions must not imply enforcement without evidence. | `CONFIRMED repo evidence` |
| ADR template | `docs/adr/ADR-TEMPLATE.md` | KFM ADRs should include evidence basis, requirements, options, impact map, validation, rollback, and open questions. | `CONFIRMED repo evidence` |
| Root README | `README.md` | KFM is governed, evidence-first, map-first, time-aware, and treats inspectable claims as the durable public unit. | `CONFIRMED repo evidence` |
| Geology domain README | `docs/domains/geology/README.md` | Geology lane already distinguishes exact/internal references, public-safe layers, source roles, EvidenceBundle resolution, Focus outcomes, and public-safe geometry rules needing verification. | `CONFIRMED repo evidence` |
| Schema-home ADR | `docs/adr/ADR-0001-schema-home.md` | Contracts define meaning, schemas validate machine-checkable shape, policy decides admissibility. | `CONFIRMED repo evidence` / status still `proposed` |
| Policy README | `policy/README.md` | Policy is the decision surface for rights, sensitivity, review, correction, release, and deny-by-default behavior. | `CONFIRMED repo evidence` |
| Geology architecture corpus | KFM geology architecture report | Geology public-safe geometry should separate exact/internal references from public generalized/redacted derivatives and require redaction fixtures. | `CONFIRMED doctrine` / implementation `PROPOSED` |
| Directory Rules | KFM directory governance | ADRs belong under `docs/adr/`; domain work belongs under responsibility roots, not new root-level domain folders. | `CONFIRMED doctrine` |

> [!NOTE]
> Repeated planning documents are useful lineage, not implementation proof. This ADR only treats repository connector evidence and directly supplied KFM doctrine as strong evidence.

[Back to top](#top)

---

## Decision

KFM geology and non-biological natural-resource geometry must use an explicit **geometry exposure contract** before any public release.

### Chosen rule

A geology feature may be public only when its geometry is:

1. appropriate to the source role and source scale;
2. supported by resolvable evidence;
3. policy-safe for the requested public surface;
4. labeled with a machine-readable `geometry_role`;
5. linked to a release state;
6. linked to a transform receipt when generalized, redacted, rounded, aggregated, or display-derived;
7. visible in the Evidence Drawer as exact, interpreted, generalized, redacted, aggregate, modeled, or display-only; and
8. covered by rollback and correction lineage.

Exact/internal geology geometry is **restricted by default** when it relates to boreholes, private wells, samples, cores, measured sections, geochemistry, geophysics, sensitive resources, extraction sites, resource estimates, or any source/steward-controlled location where public exposure could create rights, safety, privacy, cultural, ecological, infrastructure, landowner, or resource-security risk.

### One-line decision rule

> Public geology geometry must be source-scale appropriate, evidence-backed, policy-reviewed, geometry-role labeled, release-linked, and transform-receipted when public output differs from internal evidence geometry.

### One-line boundary rule

> Public clients must never infer exact geology truth from display geometry, styling, generalized tiles, modeled surfaces, Focus text, or administrative records.

[Back to top](#top)

---

## Geometry roles

The following role vocabulary is proposed for schemas, policy, validators, layer descriptors, and Evidence Drawer payloads. Final enum names remain `NEEDS VERIFICATION` until the accepted schema home and geology schema wave are implemented.

| Geometry role | Meaning | Public default | Required public burden |
|---|---|---:|---|
| `source_native_exact` | Source-native exact point, line, polygon, raster cell, or 3D coordinate captured from source material. | `DENY` unless source and policy explicitly allow. | Source rights, sensitivity review, evidence support, release state, and exact-public approval. |
| `internal_exact_reference` | KFM-preserved exact coordinate used for steward review, joins, subsurface references, or rollback. | `DENY` | Never exposed to ordinary public surfaces; may support public derivative generation. |
| `canonical_interpreted_boundary` | Interpreted geologic boundary at source scale, such as bedrock or surficial geologic unit boundary. | `ALLOW_WITH_CAVEATS` when rights, source scale, and review pass. | Source scale, publication date, source role, EvidenceBundle, layer release, and no precision upgrade. |
| `public_generalized_geometry` | Generalized public derivative of an internal or source geometry. | `ALLOW` only after gates pass. | Generalization method, tolerance/scale, reason, receipt, source linkage, and release manifest. |
| `public_redacted_geometry` | Public derivative with sensitive components removed, suppressed, or spatially altered. | `ALLOW` only after gates pass. | Redaction reason, transform receipt, reviewer, policy decision, and correction path. |
| `public_aggregate_geometry` | County, HUC, grid, basin, quadrangle, region, or other aggregate geometry used for public-safe summary. | `ALLOW_WITH_CAVEATS` | Aggregation rule, support threshold, source coverage, uncertainty, and release state. |
| `public_rounded_coordinate` | Rounded or snapped coordinate used where approximate public location is allowed. | `RESTRICTED` | Rounding precision, disclosure review, transform receipt, and no exact recovery path. |
| `display_only_geometry` | Geometry used only for rendering context, label placement, symbology, or visual grouping. | `ALLOW_WITH_LABEL` | Must not support exact claims; UI must label as display-only when consequential. |
| `derived_modeled_surface` | Interpolated, modeled, potential, susceptibility, or prediction surface. | `ALLOW_WITH_CAVEATS` | Model identity, inputs, uncertainty, source role, and prohibition on treating potential as occurrence/reserve. |
| `restricted_or_embargoed_geometry` | Geometry blocked by rights, sensitivity, steward review, source terms, or embargo. | `DENY` | Reason code, review path, and no public layer exposure. |

### Public-safe does not mean false precision

Public-safe geometry may be an interpreted map-unit boundary at the scale of its source. It may also be a generalized or redacted derivative. In both cases, KFM must prevent silent precision upgrades.

If source support is at 1:100,000, a public surface must not imply parcel-scale, borehole-scale, or sample-scale certainty.

[Back to top](#top)

---

## Policy rules

### Normative rules after acceptance

Once this ADR is accepted and enforced, geology public geometry must follow these rules.

1. **Exact/internal separation.** Exact borehole, private well, sample, core, measured-section, geochemical, geophysical, sensitive-resource, and extraction coordinates are internal or restricted by default.
2. **Public derivative requirement.** Public release of restricted exact geometry requires a public-safe derivative with a transform receipt.
3. **Source-scale fidelity.** Public geologic-unit and boundary layers must carry source scale and must not be represented as more precise than their source support.
4. **Geometry-role label.** Every public geology feature or layer must carry `geometry_role` or a repo-approved equivalent.
5. **Evidence lookup.** Public features must expose an `evidence_lookup_ref` or equivalent path to EvidenceBundle resolution.
6. **Release linkage.** Public features must carry `release_id`, release digest, or repo-approved release linkage.
7. **Source-role compatibility.** The source role must support the claim type. Administrative records cannot prove physical deposits.
8. **Model/potential boundary.** Modeled potential surfaces cannot be promoted to known occurrence, deposit, resource, reserve, or extraction claims without higher-burden evidence.
9. **Unknown rights fail closed.** Unknown source rights, unknown source terms, unknown sensitivity, or missing steward review blocks public geometry.
10. **UI truth cues.** Map popups, Evidence Drawer, exports, and Focus Mode must expose geometry role, public-safety posture, review state, and caveats for consequential claims.
11. **AI cannot upgrade geometry.** Focus Mode may explain released evidence; it must not infer exact locations or remove caveats.
12. **Rollback required.** Every public geometry release must have a rollback target and correction path.

### Decision matrix

| Input condition | Expected policy outcome | Reason-code family |
|---|---|---|
| Exact borehole coordinate requested for public layer with no explicit public allowance | `DENY` | `exact_internal_geometry_public_request` |
| Source rights or source terms unresolved | `QUARANTINE` or `DENY` | `source_terms_unverified` |
| Geologic boundary is source-scale interpreted and rights/review pass | `ALLOW_WITH_CAVEATS` | `source_scale_interpreted_boundary` |
| Public feature is generalized and receipt/release state exist | `ALLOW` | `public_generalization_receipt_present` |
| Redaction receipt missing for sensitive-resource derivative | `DENY` | `missing_redaction_receipt` |
| Modeled potential labeled as known deposit or reserve | `DENY` | `modeled_potential_claim_upgrade` |
| Permit/lease/operator record used as physical deposit proof | `DENY` | `administrative_source_role_mismatch` |
| EvidenceRef does not resolve to EvidenceBundle | `ABSTAIN` or `ERROR` | `unresolved_evidence_ref` |
| Map feature has no release linkage | `DENY` | `missing_release_ref` |
| Focus answer asks for restricted geometry details | `DENY` | `restricted_geometry_focus_request` |

[Back to top](#top)

---

## Requirements and constraints

### KFM invariants checked

| Invariant | Impact | Status |
|---|---|---|
| `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED` | Exact and public-safe geometry are separated by lifecycle state and transform receipts. | `CONFIRMED doctrine` / enforcement `NEEDS VERIFICATION` |
| Public clients use governed interfaces | Public geology layers and popups use released artifacts and governed APIs only. | `PROPOSED` |
| `EvidenceRef -> EvidenceBundle` closure | Public geometry claims require evidence resolution before claim display or Focus answer. | `PROPOSED` |
| Promotion is a governed state transition | Geometry release requires validation, policy, review, proof, release manifest, and rollback target. | `PROPOSED` |
| AI is interpretive only | Focus cannot invent, infer, or expose restricted exact geometry. | `PROPOSED` |
| Derived surfaces stay derived | Generalized, redacted, modeled, aggregate, and display-only geometry do not overwrite source evidence geometry. | `PROPOSED` |
| Rights and sensitivity fail closed | Unknown public-release posture blocks public geometry. | `PROPOSED` |
| Receipts, proofs, catalogs, releases remain separate | Transform receipts and proof packs are not schemas, not policies, and not canonical truth. | `PROPOSED` |
| Rollback and correction are planned before publication | Public geometry release requires correction and rollback paths. | `PROPOSED` |

### Non-goals

This ADR does **not** decide:

- the final geology schema path if a successor schema-home ADR changes the current proposed home;
- exact KGS, KCC, KDHE, USGS, or other source endpoints;
- whether any specific live source is authorized for ingestion;
- exact route names, component names, DTO names, or MapLibre layer IDs;
- resource classification schemes for reserves or estimates;
- emergency, hazard-warning, mineral-rights, title, lease, ownership, or parcel truth;
- whether 3D/subsurface views are enabled;
- production access-control implementation.

[Back to top](#top)

---

## Options considered

| Option | Description | Benefits | Risks / costs | Outcome |
|---|---|---|---|---|
| Public exposes exact/source-native geology geometry by default | Treat source geometry as public unless blocked. | Simple to implement. | High leakage risk; weakens rights, sensitivity, source-scale, steward, and rollback controls. | Rejected |
| Hide all geology geometry until fully mature | Deny all public geology layers until every source is reviewed. | Very safe. | Blocks useful public geologic-unit and source-scale map outputs that can be safely released with caveats. | Rejected |
| Public-safe geometry role contract | Label geometry roles, restrict exact/internal geometry by default, require derivative receipts, and expose caveats. | Preserves evidence, source scale, public value, and safety. | Requires schemas, policy, validators, fixtures, and UI trust cues. | Accepted as proposed decision |
| Treat redaction/generalization as a styling concern | Let map rendering decide what to show. | Appears fast. | Styling becomes hidden policy; no receipt, rollback, or evidence trail. | Rejected |
| Use domain-specific exceptions without shared policy | Handle each geology case ad hoc. | Flexible. | Produces inconsistent public geometry behavior and makes release review brittle. | Rejected |

[Back to top](#top)

---

## Impact map

### File and documentation impact

| Area | Required update | Status |
|---|---|---|
| `docs/adr/` | This ADR replaces placeholder text and should be linked from the ADR index. | `PROPOSED` |
| `docs/domains/geology/` | Update README/indexes to point to this ADR and geometry-role policy once accepted. | `PROPOSED` |
| `docs/architecture/geology/` | Add or update trust path, object model, and lifecycle docs to reflect exact/internal vs public-safe geometry. | `PROPOSED` |
| `docs/runbooks/geology/` | Add public-safe geometry review, promotion, rollback, and validation procedures. | `PROPOSED` |
| `contracts/` | Add semantic meaning for geometry roles if contract docs are active. | `PROPOSED` |
| `schemas/` | Add machine-checkable fields for geometry role, transform receipt refs, release refs, evidence refs, and sensitivity state. | `PROPOSED` / schema home `NEEDS VERIFICATION` |
| `policy/` | Add deny-by-default rules for exact-public leakage, unknown rights, source-role mismatch, missing receipts, and missing release refs. | `PROPOSED` |
| `tests/` / `fixtures/` | Add pass/fail fixtures for exact-public deny, generalized public allow, redaction missing deny, source-scale caveat, modeled-potential mismatch, Focus deny. | `PROPOSED` |
| `tools/validators/` | Add or adapt validator for public-safe geometry, transform receipt linkage, evidence closure, catalog closure, and release linkage. | `PROPOSED` |
| `data/registry/` | Add source-role, sensitivity, geometry-role, resource-classification, layer, and status registry entries. | `PROPOSED` |
| `data/receipts/` | Store redaction/generalization receipts as process memory. | `PROPOSED` |
| `data/proofs/` | Store proof-pack artifacts supporting release-significant geometry decisions. | `PROPOSED` |
| `data/published/` | Publish only release-backed public-safe geology artifacts by digest. | `PROPOSED` |
| `release/` | Include release manifests, promotion decisions, rollback cards, and correction notices for public geometry releases. | `PROPOSED` |
| `apps/` / `packages/` | Governed API, MapLibre, Evidence Drawer, and Focus consumers must display or enforce geometry role and policy state. | `PROPOSED`; exact paths `UNKNOWN` |
| `.github/workflows/` | Add CI gates only after repo-native tooling is verified. | `PROPOSED`; workflow execution `NEEDS VERIFICATION` |

### Lifecycle impact

| Lifecycle stage | Geometry rule |
|---|---|
| SOURCE REGISTRY | SourceDescriptor records source role, rights, scale, sensitivity, geometry role, and caveats before activation. |
| RAW | Source-native exact geometry is captured but never exposed to public clients. |
| WORK | Candidate transforms may produce generalized or redacted geometry with receipts. |
| QUARANTINE | Unknown rights, sensitivity, source role, or geometry-role mismatch stays blocked. |
| PROCESSED | Normalized objects preserve internal geometry and public-safe derivative distinction. |
| CATALOG / TRIPLET | Catalog records and relation edges must distinguish evidence geometry, public geometry, and display geometry. |
| PUBLISHED | Only release-backed public-safe artifacts are exposed through governed APIs and map layers. |

[Back to top](#top)

---

## Validation

Validation is `PROPOSED` until repo-native schemas, policies, validators, fixtures, and workflow runs are verified.

### Required checks

| Check | Expected result |
|---|---|
| Geometry-role schema validation | Every public geology feature has a valid `geometry_role` or accepted equivalent. |
| Exact-public leak check | Exact/internal sensitive geometry fails public promotion. |
| Source-scale check | Source-scale interpreted boundaries include scale/caveat metadata and no precision-upgrade flag. |
| Transform receipt check | Generalized, redacted, rounded, aggregated, or modeled public outputs link to a transform receipt. |
| Evidence closure check | `evidence_lookup_ref` resolves to an EvidenceBundle before public claim display. |
| Source-role compatibility check | Source role supports the claim type; administrative records cannot prove physical geology. |
| Rights/sensitivity check | Unknown or restricted rights/sensitivity blocks public release. |
| Catalog/proof/release closure check | Public artifact has catalog record, proof support, release manifest, rollback card, and correction path. |
| Runtime envelope check | Governed API / Focus returns only finite outcomes: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`. |
| Negative-path fixture check | Invalid fixtures fail with stable reason codes. |

### Proposed fixture set

| Fixture | Purpose | Expected outcome |
|---|---|---|
| `valid_source_scale_geologic_unit_public.json` | Source-scale interpreted boundary with evidence and caveats. | `PASS` |
| `valid_public_generalized_resource_context.json` | Resource context generalized with receipt and release linkage. | `PASS` |
| `valid_public_aggregate_geochemistry.json` | Aggregate public surface with support threshold. | `PASS` |
| `invalid_exact_borehole_public.json` | Exact internal borehole requested for public layer. | `DENY` |
| `invalid_missing_redaction_receipt.json` | Sensitive resource derivative lacks transform receipt. | `DENY` |
| `invalid_unknown_source_terms.json` | Source rights or terms unresolved. | `QUARANTINE` or `DENY` |
| `invalid_modeled_potential_as_reserve.json` | Modeled potential promoted to reserve claim. | `DENY` |
| `invalid_admin_record_as_physical_deposit.json` | Permit/lease/operator used as deposit proof. | `DENY` |
| `invalid_no_evidence_lookup_ref.json` | Public feature cannot resolve EvidenceBundle. | `ABSTAIN` or `ERROR` |
| `invalid_focus_restricted_geometry_request.json` | Focus request seeks restricted exact details. | `DENY` |

### Illustrative policy input

This example is documentation-only. It is not a schema and not implementation proof.

```json
{
  "surface": "map_layer",
  "domain": "geology",
  "feature_id": "example-public-geology-feature",
  "claim_type": "mineral_occurrence_context",
  "source_roles": ["authoritative_interpreted", "derived_modeled"],
  "geometry_role": "public_generalized_geometry",
  "internal_geometry_available": true,
  "public_geometry_available": true,
  "transform_receipt_ref": "data/receipts/geology/example.generalization_receipt.json",
  "evidence_lookup_ref": "kfm://evidence/example",
  "rights_state": "reviewed_public_allowed",
  "sensitivity_state": "public_safe_after_generalization",
  "review_state": "approved_for_release",
  "release_ref": "kfm://release/example",
  "rollback_ref": "kfm://rollback/example"
}
```

[Back to top](#top)

---

## Runtime and UI behavior

### Governed API

The governed API should return public geometry with explicit trust cues rather than relying on the client to guess.

Required outward fields or equivalents:

| Field family | Why it matters |
|---|---|
| `geometry_role` | Tells users whether geometry is exact, interpreted, generalized, redacted, aggregate, modeled, or display-only. |
| `evidence_lookup_ref` | Lets Evidence Drawer resolve support. |
| `release_ref` | Ties geometry to a governed release. |
| `source_scale` / `source_publication` | Prevents precision upgrade. |
| `policy_state` / `reason_codes` | Explains allow, deny, restrict, generalize, or abstain. |
| `transform_receipt_ref` | Shows why public geometry differs from internal evidence geometry. |
| `correction_state` / `rollback_ref` | Keeps public geometry reversible and correctable. |

### MapLibre shell

Map layers should make public-safety state visible at the point of use.

A public layer should not simply render a feature. It should provide:

- geometry role;
- source role;
- source scale and temporal scope;
- public-safety posture;
- evidence lookup;
- release state;
- correction state;
- “exact/internal withheld” cue where applicable;
- caveats for modeled, generalized, redacted, aggregate, or display-only outputs.

### Evidence Drawer

The Evidence Drawer should show enough context for a maintainer or user to understand why a geometry is public:

- source(s) and source role(s);
- whether public geometry is source-scale, generalized, redacted, rounded, aggregated, modeled, or display-only;
- transform receipt when applicable;
- policy decision and reason codes;
- release manifest reference;
- rollback/correction path;
- unresolved verification items.

### Focus Mode / governed AI

Focus Mode may answer geology geometry questions only from released, policy-safe EvidenceBundles.

| Request type | Expected behavior |
|---|---|
| “What does this public geologic unit boundary represent?” | `ANSWER` with source scale, evidence, caveats, and citations. |
| “Give me the exact borehole coordinate behind this generalized feature.” | `DENY`. |
| “Is this modeled resource potential a proven reserve?” | `ABSTAIN` or `DENY` unless reserve evidence exists. |
| “Which permit proves this deposit?” | `ABSTAIN`; permit/lease/operator records do not prove physical geology by themselves. |
| Missing EvidenceBundle | `ABSTAIN` or `ERROR`, not a generated answer. |

[Back to top](#top)

---

## Consequences

### Positive consequences

- Prevents exact/internal geology geometry from leaking into ordinary public surfaces.
- Keeps source-scale interpreted geology useful without implying false precision.
- Makes generalized and redacted public geometry inspectable through receipts.
- Preserves source-role distinctions between physical geology, modeled surfaces, and administrative records.
- Gives validators and reviewers concrete negative-path fixtures.
- Makes MapLibre, Evidence Drawer, Focus Mode, exports, and release artifacts downstream of evidence and policy.
- Creates a rollback path for public geometry mistakes.

### Tradeoffs and risks

| Risk | Mitigation | Residual status |
|---|---|---|
| More metadata is required before public release. | Use a small first fixture slice and validator-first rollout. | `ACCEPTED TRADEOFF` |
| Source-scale boundaries may be misunderstood as exact. | Require source scale, caveats, and Evidence Drawer labels. | `NEEDS VERIFICATION` |
| Generalization may obscure useful context. | Keep internal exact evidence for steward review and expose public-safe rationale. | `NEEDS VERIFICATION` |
| Validators may lag policy. | Tie policy changes to fixtures, CI, and release-gate checks. | `NEEDS VERIFICATION` |
| Existing layer or API consumers may lack geometry-role fields. | Add compatibility notes and migration fixtures before enforcement. | `UNKNOWN` |
| Over-redaction could reduce public utility. | Use steward review and release records to choose least-restrictive safe public geometry. | `PROPOSED` |

[Back to top](#top)

---

## Rollback and supersession

### Rollback plan

If public geometry is found to expose restricted exact detail, overstate precision, mislabel a modeled surface, omit source caveats, or lack evidence closure:

1. Withdraw or disable the affected layer alias, API route payload, tile reference, story node, export, or Focus context.
2. Preserve the released artifact for audit; do not delete history.
3. Publish a `CorrectionNotice` or equivalent record if public users could have relied on the artifact.
4. Repoint the public alias only through a governed correction or rollback gate.
5. Regenerate public-safe geometry from validated internal/source geometry.
6. Re-run exact-public, transform receipt, evidence closure, catalog closure, policy, release, and Focus citation checks.
7. Update this ADR only through revision note or successor ADR if the policy changes materially.

### Rollback triggers

| Trigger | Required action |
|---|---|
| Exact/internal sensitive geometry appears in public artifact | Emergency withdrawal, correction notice, incident review, and redaction/generalization rebuild. |
| Source rights or terms become unclear after release | Quarantine source outputs and block public aliases until review closes. |
| Geometry role is missing or wrong | Block promotion or withdraw affected release. |
| Transform receipt missing | Block promotion; if published, issue correction and regenerate. |
| Modeled potential promoted to occurrence/reserve | Withdraw claim and reclassify as modeled derivative. |
| Permit/lease/operator used as physical geology proof | Replace with relation edge or abstain. |
| Focus exposes restricted geometry | Disable affected Focus pathway and preserve AI receipt. |
| Rollback target missing | Block release until rollback card or equivalent exists. |

### Supersession rule

This ADR may be superseded only by a later ADR that:

- identifies the successor decision;
- preserves this ADR as lineage;
- explains changed policy, source, schema, validator, or release evidence;
- updates affected indexes and registers;
- includes migration and rollback instructions;
- retains compatibility notes for public layer, API, and Evidence Drawer consumers.

[Back to top](#top)

---

## Open verification

| Question | Why it matters | Verification path | Owner |
|---|---|---|---|
| Who owns geology public-safe geometry policy review? | Required for acceptance. | CODEOWNERS or governance register. | `OWNER_TBD_NEEDS_VERIFICATION` |
| What is the accepted geology schema home? | Geometry-role fields need canonical schema placement. | Accepted schema-home or geology schema ADR. | `OWNER_TBD_NEEDS_VERIFICATION` |
| Which KGS geologic map layers are source-of-record and at what scale? | Prevents false precision. | Verified source descriptors and source metadata. | `SOURCE_STEWARD_TBD` |
| Which borehole, well-log, core, sample, geochemistry, or geophysics fields can be public exactly? | Prevents location leakage. | Source terms, legal/steward review, sensitivity policy. | `POLICY_STEWARD_TBD` |
| Which resource or extraction locations are sensitive? | Resource-security and landowner sensitivity. | Sensitivity registry and resource classification policy. | `POLICY_STEWARD_TBD` |
| Which validators exist now? | This ADR cannot claim enforcement without them. | Inspect `tools/validators/`, `tests/`, `.github/workflows/`, and run outputs. | `CI_STEWARD_TBD` |
| What is the actual governed API path? | Prevents invented route names. | Inspect `apps/`, packages, contracts, and OpenAPI files. | `API_STEWARD_TBD` |
| What is the actual MapLibre shell path? | Prevents invented UI component names. | Inspect `apps/`, `web/`, `ui/`, and layer registry. | `UI_STEWARD_TBD` |
| Does policy tooling use OPA/Conftest or another runner? | Policy snippets and commands depend on repo-native tooling. | Inspect workflows, lockfiles, Makefile, and policy docs. | `CI_STEWARD_TBD` |
| Are release manifests, rollback cards, and correction notices implemented? | Public geometry rollback depends on them. | Inspect `release/`, `data/proofs/`, `data/receipts/`, and tests. | `RELEASE_STEWARD_TBD` |

[Back to top](#top)

---

## Review checklist

<details>
<summary>Pre-acceptance checklist</summary>

- [ ] ADR status, meta block, title, and path are synchronized.
- [ ] Owner and reviewer placeholders are replaced or deliberately left as `NEEDS VERIFICATION`.
- [ ] ADR index links to this file.
- [ ] Geology domain README links to this file.
- [ ] Geometry-role enum or equivalent is defined in the accepted schema home.
- [ ] Source-role compatibility rules are defined or linked.
- [ ] Sensitivity rules are defined for exact/internal geology geometry.
- [ ] Redaction/generalization receipt shape is defined or linked.
- [ ] At least one valid public geologic-unit fixture passes.
- [ ] At least one valid generalized public resource-context fixture passes.
- [ ] Exact borehole public exposure fixture fails.
- [ ] Missing transform receipt fixture fails.
- [ ] Modeled-potential-as-reserve fixture fails.
- [ ] Administrative-record-as-deposit-proof fixture fails.
- [ ] EvidenceBundle closure is tested for public geometry features.
- [ ] Map layer descriptor includes geometry role, evidence lookup, release ref, and policy state.
- [ ] Evidence Drawer payload includes source role, source scale, transform receipt, and public-safety explanation.
- [ ] Focus Mode returns `DENY` for restricted exact geometry requests.
- [ ] Release manifest and rollback card behavior are tested or explicitly marked `NEEDS VERIFICATION`.
- [ ] Rollback and correction paths are documented.
- [ ] No implementation claim in this ADR exceeds repository evidence.

</details>

<details>
<summary>Minimal acceptance signal</summary>

This ADR can move from `proposed` to `accepted` when maintainers can point to:

1. accepted owner/reviewer routing;
2. accepted or verified schema home;
3. geometry-role schema or equivalent contract;
4. source-role compatibility policy;
5. public-safe geometry policy rules;
6. pass/fail fixture set;
7. validator output;
8. release/rollback evidence;
9. docs/index updates;
10. PR, validation report, receipt, or other repo-native acceptance artifact.

</details>

[Back to top](#top)
