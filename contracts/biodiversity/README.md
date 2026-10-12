<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-biodiversity-readme
title: contracts/biodiversity/ — Biodiversity Cross-Domain Compatibility Index
type: readme; directory-readme; compatibility-index; cross-domain
version: v0.2
status: draft; repository-grounded; cross-domain; compatibility-index; non-canonical; geoprivacy-sensitive
owners: OWNER_TBD — Biodiversity composition steward · Fauna steward · Flora steward · Habitat steward · Contract steward · Schema steward · Sensitivity steward · Policy steward · Release steward · Docs steward
created: 2026-06-20
updated: 2026-09-07
policy_label: public-with-gates; contracts; biodiversity; cross-domain; no-parallel-authority; geoprivacy-sensitive; cite-or-abstain
related:
  - ../README.md
  - ../cross_domain/README.md
  - ../joins/cross_lane_join_assessment.md
  - ../../docs/architecture/ecology-cross-domain.md
  - ../../docs/domains/fauna/README.md
  - ../../docs/domains/flora/README.md
  - ../../docs/domains/habitat/README.md
  - ../../docs/domains/habitat/SENSITIVITY_AND_GEOPRIVACY.md
  - ../../docs/runbooks/SENSITIVITY_ESCALATION.md
  - ../../schemas/contracts/v1/domains/fauna/README.md
  - ../../schemas/contracts/v1/domains/flora/README.md
  - ../../schemas/contracts/v1/domains/habitat/README.md
  - ../../policy/domains/fauna/README.md
  - ../../policy/domains/flora/README.md
  - ../../policy/domains/habitat/README.md
  - ../../fixtures/ecology/README.md
  - ../../fixtures/domains/fauna/README.md
  - ../../fixtures/domains/flora/README.md
  - ../../fixtures/domains/habitat/README.md
  - ../../tests/domains/fauna/README.md
  - ../../tests/domains/flora/README.md
  - ../../tests/domains/habitat/README.md
  - ../../tools/validators/biodiversity/README.md
  - ../../tools/validators/atmosphere_biodiversity/README.md
  - ../../control_plane/domain_lane_register.yaml
  - ../../control_plane/cross_domain_seam_register.yaml
  - ../../control_plane/policy_gate_register.yaml
tags: [kfm, contracts, biodiversity, ecology, cross-domain, fauna, flora, habitat, geoprivacy, sensitivity, source-role, evidence, governance]
notes:
  - "Ecology is an umbrella concern, not a registered sovereign KFM domain at the current evidence snapshot."
  - "This path coordinates composite meanings while atomic facts remain owned by Fauna, Flora, Habitat, and other bounded lanes."
  - "The direct inventory is README.md plus .gitkeep; no biodiversity contract file is established by this directory."
  - "Sensitive or reconstructable ecological locations fail closed; public-safe derivatives require governed transformation, policy, review, receipts, release, correction, and rollback."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Biodiversity Cross-Domain Compatibility Index

This README records how the historical contracts/biodiversity path relates to domain-owned semantic contracts, machine schemas, policy, fixtures, tests, and cross-domain seams. It is a compatibility and coordination index, not a new Ecology or Biodiversity authority.

## Contents

- [Status](#status)
- [Placement and ownership](#placement-and-ownership)
- [Direct inventory](#direct-inventory)
- [Scope and non-goals](#scope-and-non-goals)
- [Composite contract posture](#composite-contract-posture)
- [Sensitivity and geoprivacy](#sensitivity-and-geoprivacy)
- [Lifecycle and trust boundary](#lifecycle-and-trust-boundary)
- [Current neighboring surfaces](#current-neighboring-surfaces)
- [Validation and maintenance](#validation-and-maintenance)
- [Evidence ledger](#evidence-ledger)
- [Definition of done](#definition-of-done)
- [Rollback and review note](#rollback-and-review-note)

## Status

> [!IMPORTANT]
> **Status:** draft / compatibility index / cross-domain composition  
> **Path:** contracts/biodiversity/  
> **Current posture:** retained for navigation and composite-meaning coordination; non-canonical and not a sovereign domain root.  
> **Ecology posture:** the repository architecture describes Ecology as an umbrella concern; no registered Ecology domain or generic active join policy is established.  
> **Sensitivity posture:** exact or reconstructable sensitive locations fail closed by default.

The current main tree contains this README and a .gitkeep placeholder only. The previous README incorrectly described the target as blank and used an invalid blank-file rollback SHA; this update replaces those claims with current tree evidence.

## Placement and ownership

Current implementation truth is the exact GitHub repository state. Accepted placement guidance is [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) together with the adopted [Directory Rules](../../docs/doctrine/directory-rules.md). The [contracts root](../README.md) owns semantic meaning, while schemas, policy, fixtures, tests, validators, lifecycle data, proofs, and release decisions remain in their responsibility roots.

The current architecture boundary is [Ecology as a Cross-Domain Concern](../../docs/architecture/ecology-cross-domain.md): ecological questions compose evidence from bounded domain lanes through named, reviewable seams. This path cannot register a domain, authorize a join, or transfer ownership.

| Surface | Current posture | Role in a biodiversity composition |
| --- | --- | --- |
| [contracts/domains/fauna/](../domains/fauna/README.md) | Fauna semantic-contract lane; mixed maturity | Owns animal taxon, occurrence, range, sensitive-site, monitoring, mortality, disease, and related animal meaning |
| [contracts/domains/flora/](../domains/flora/README.md) | Flora contract lane; greenfield/proposed posture remains visible | Owns plant taxon, occurrence, specimen, rare-plant, phenology, invasive-plant, and related botanical meaning |
| [contracts/domains/habitat/](../domains/habitat/README.md) | Habitat semantic-contract lane; draft/proposed before promotion | Owns habitat patch, land-cover, ecoregion, suitability, connectivity, restoration, stewardship, and uncertainty meaning |
| [contracts/cross_domain/](../cross_domain/README.md) | Cross-domain semantic coordination lane | Use for a named seam or composite contract; do not hide a relation under one endpoint domain |
| contracts/biodiversity/ | This compatibility path | Point to owning lanes and record unresolved composite placement only |
| [schemas/contracts/v1/domains/fauna/](../../schemas/contracts/v1/domains/fauna/README.md) | Fauna machine-shape lane | Pair Fauna contracts with schemas; no schema authority is created here |
| [schemas/contracts/v1/domains/flora/](../../schemas/contracts/v1/domains/flora/README.md) | Flora machine-shape lane | Pair Flora contracts with schemas; no schema authority is created here |
| [schemas/contracts/v1/domains/habitat/](../../schemas/contracts/v1/domains/habitat/README.md) | Habitat machine-shape lane | Pair Habitat contracts with schemas; no schema authority is created here |
| [policy/domains/fauna/](../../policy/domains/fauna/README.md), [flora/](../../policy/domains/flora/README.md), [habitat/](../../policy/domains/habitat/README.md) | Domain policy lanes | Decide admissibility, restriction, denial, or abstention; policy is not contract meaning |
| [contracts/joins/cross_lane_join_assessment.md](../joins/cross_lane_join_assessment.md) | Proposed, fixture-first, dry-run, local-only assessment contract | Candidate assessment only; not relationship truth or release approval |
| [fixtures/ecology/](../../fixtures/ecology/README.md) | Synthetic public-safe ecology examples | Exercise cross-domain behavior without creating an Ecology domain |
| [tools/validators/biodiversity/](../../tools/validators/biodiversity/README.md) | README-only parent/routing boundary with partial coverage | Do not infer executable biodiversity enforcement from the directory name |

## Direct inventory

The direct contents observed on current main are:

~~~text
contracts/biodiversity/
├── .gitkeep
└── README.md
~~~

No biodiversity object-family contract, JSON Schema, policy rule, fixture, test, validator, source record, proof, release manifest, or runtime implementation is established by this folder.

## Scope and non-goals

This README may:

- identify the compatibility path and direct contents;
- point to owning Fauna, Flora, Habitat, and other bounded lanes;
- describe composite meanings that preserve atomic ownership;
- record named seams, unresolved placement questions, evidence gaps, and rollback references;
- summarize repository evidence without promoting design lineage or proposed scaffolds.

This README does not:

- create an Ecology or Biodiversity domain;
- redefine Fauna, Flora, Habitat, Soil, Hydrology, Atmosphere, Hazards, Agriculture, Geology, Archaeology, or other domain-owned facts;
- define JSON Schema, executable validators, policy bundles, source descriptors, lifecycle data, evidence bundles, receipts, release manifests, public API DTOs, UI behavior, map behavior, or AI answers;
- authorize a cross-domain join, graph edge, inference, source activation, review, release, or publication;
- expose rare-species, protected-resource, culturally sensitive, private-land, or otherwise restricted locations;
- make a fixture, helper, validator README, model output, tile, catalog entry, or generated prose into sovereign evidence.

## Composite contract posture

A future biodiversity-shaped contract may describe a derived or joined meaning such as:

| Candidate composite | Current status | Required ownership and proof |
| --- | --- | --- |
| Biodiversity index or richness layer | PROPOSED / NEEDS VERIFICATION | Name each contributing domain, source role, method, uncertainty, EvidenceBundle, sensitivity tier, correction path, and release state |
| Public-safe occurrence summary | PROPOSED / NEEDS VERIFICATION | Derive from domain-owned occurrences; require approved generalization, aggregation or redaction, receipts, policy, review, and rollback |
| Habitat-linked biodiversity surface | PROPOSED / NEEDS VERIFICATION | Keep Habitat meaning separate from Fauna/Flora occurrence truth; evaluate join-induced sensitivity |
| Invasive-species composite | PROPOSED / NEEDS VERIFICATION | Preserve plant/animal subtype, source authority, rights, temporal state, and owning-domain correction path |
| Conservation or suitability composite | PROPOSED / NEEDS VERIFICATION | Distinguish modeled suitability from observed occurrence, protected designation, or official conservation decision |

These are candidate meanings, not current implementations. A composite contract belongs in a named cross-domain seam or another accepted responsibility-root path after an ADR or migration decision. Absence of a file in this directory is not a missing permission to add one.

Every composite contract should state:

- participating domains and the owner of each atomic fact;
- relation meaning, identity, temporal basis, spatial/coverage basis, and uncertainty;
- source role, knowledge character, rights, sensitivity, and audience tier;
- EvidenceRef and EvidenceBundle dependencies;
- policy decision, review state, transformation receipts, release state, correction path, and rollback target;
- paired schema, fixture, validator, test, and registry references;
- explicit exclusions and finite outcomes such as ANSWER, ABSTAIN, DENY, or ERROR.

## Sensitivity and geoprivacy

Sensitive ecological joins can be more sensitive than either endpoint. Preserve these defaults:

- rare or protected species, exact occurrences, nests, dens, roosts, hibernacula, spawning sites, telemetry, steward-controlled records, culturally sensitive places, and private or restricted locations fail closed;
- habitat, hydrology, soil, land-cover, ownership, hazard, or atmosphere context can raise sensitivity when joined to a sensitive occurrence;
- exact coordinates, re-identifying joins, transform parameters, and internal policy reasons do not belong in public-safe documentation or ordinary public responses;
- public outputs require a governed safe representation: approved redaction, generalization, aggregation, omission, or delay plus policy decision, review, receipts, release state, correction path, and rollback support;
- generalized or aggregated outputs must not be reverse-joined to reveal the protected record;
- public API, map, dashboard, and AI surfaces must cite or abstain and must not bypass the governed trust membrane.

See the [Habitat sensitivity and geoprivacy posture](../../docs/domains/habitat/SENSITIVITY_AND_GEOPRIVACY.md) and [Sensitivity Escalation runbook](../../docs/runbooks/SENSITIVITY_ESCALATION.md). A contract's existence is not publication permission.

## Lifecycle and trust boundary

Use this sequence for any future cross-domain work:

1. Identify the atomic records and confirm their owning domain lanes.
2. Resolve source role, rights, sensitivity, temporal/spatial basis, and evidence references for each endpoint.
3. Give the relation or composite a stable seam/object identity; do not use biodiversity as an omnibus join.
4. Validate endpoint shape and relationship shape in the owning schema/seam lanes.
5. Evaluate an accepted policy profile. The current generic cross-lane join policy is not established as active.
6. Emit or preserve candidate, review, receipt, correction, and rollback records as required.
7. Release only a public-safe transformed representation after review and policy gates close.
8. Keep the result separate from raw, work, quarantine, candidate, unreleased, and exact-sensitive records.

A matching fixture, helper ALLOW, schema pass, workflow success, map rendering, catalog entry, or AI explanation does not by itself prove relationship truth, public safety, review approval, release, or publication.

## Current neighboring surfaces

The following direct inventories are observed on current main. Counts describe immediate directory entries and do not prove completeness or runtime wiring.

| Lane | Current direct inventory | Maturity / boundary |
| --- | --- | --- |
| contracts/domains/fauna/ | 21 files | Semantic Fauna lane; several scaffolds/proposed contracts remain |
| contracts/domains/flora/ | 37 files plus source_readiness/ | Flora semantic lane with mixed casing and proposed/supporting records |
| contracts/domains/habitat/ | 19 files plus ecoregions/ and land_cover/ | Habitat semantic lane; draft/proposed child surfaces remain |
| schemas/contracts/v1/domains/fauna/ | 35 files plus receipts/ | Fauna schema lane; proposed shapes and registry/validator completeness need verification |
| schemas/contracts/v1/domains/flora/ | 39 files plus source_readiness/ | Flora schema lane; proposed shapes and completeness need verification |
| schemas/contracts/v1/domains/habitat/ | 31 files plus ecoregions/ and land_cover/ | Habitat schema lane; land-cover scaffold confirmed, broader coverage needs verification |
| policy/domains/fauna/ | 8 files | Includes Rego, rights/redistribution, sensitivity, and tile allowlist surfaces; activation maturity varies |
| policy/domains/flora/ | 20 files plus four directories | Policy surface exists; binding and release completeness remain scoped questions |
| policy/domains/habitat/ | 19 files plus three directories | Habitat policy surface exists; promotion and enforcement remain bounded |
| fixtures/domains/fauna/ | README plus nine directories | One bounded validation corpus and synthetic/valid/invalid/sensitivity lanes |
| fixtures/domains/flora/ | README plus 20 directories | Public-safe synthetic and domain fixture lanes; broader coverage needs verification |
| fixtures/domains/habitat/ | README plus eight directories | Synthetic habitat, land-cover, patch, ecoregion, and thin-slice lanes |
| tests/domains/fauna/ | README, 16 files, nine directories | Includes no-leak, evidence, split, redaction, publication, rollback, taxonomy, and tile checks |
| tests/domains/flora/ | README, 16 files, 16 directories | Includes no-network, policy, rights, schema, sensitivity, temporal, and rollback checks |
| tests/domains/habitat/ | README, 10 files, 16 directories | Includes geoprivacy, source-role, modeled-vs-critical, release, and thin-slice checks |
| tools/validators/atmosphere_biodiversity/ | README-only seam/index posture | Executable enforcement and dedicated tests are not established by the README |
| control_plane/cross_domain_seam_register.yaml | Proposed navigational/review projection | Does not authorize a seam or public join |

## Validation and maintenance

### Confirmed

- Current main is 0bcea4ae10d53a9067652c1c5a12e87e86fb3efa.
- contracts/biodiversity/ contains only .gitkeep and this README.
- Ecology architecture treats Ecology as an umbrella concern rather than a sovereign domain and says generic join policy is inactive.
- Fauna, Flora, and Habitat have separate contract, schema, policy, fixture, and test responsibility-root lanes.
- The cross-lane assessment contract is proposed, fixture-first, dry-run, local-only, and non-authoritative.
- Biodiversity and Atmosphere × Biodiversity validator paths document routing/index boundaries; their directory names do not prove executable enforcement.

### Still unproven

- A canonical biodiversity-wide contract or schema home.
- A generic active cross-domain join evaluator, policy bundle, or public decision emitter.
- Complete cross-domain contract/schema/fixture/validator/test coverage.
- Scientific validity, source freshness, taxonomy authority, rights, CARE/sovereignty posture, sensitivity clearance, or public-release eligibility for any composite.
- API, MapLibre, dashboard, catalog, graph, or AI-consumer safety for biodiversity-shaped outputs.
- Runtime, CI, release, correction, and rollback integration beyond the bounded surfaces explicitly linked above.

### Documentation update checklist

For future edits:

- Re-pin current main and inspect the direct target tree.
- Fetch every linked lane whose status, ownership, or role is being changed.
- Keep atomic ownership, relation meaning, policy admissibility, review, release, and publication distinct.
- Recheck relative links, anchors, tables, code fences, and counts.
- Re-fetch the branch blob and compare changed paths before opening or updating a draft PR.
- Report repository tests, schema validation, policy evaluation, hosted checks, browser/runtime checks, release checks, and live connectors as not run unless actually executed.

## Evidence ledger

| Evidence | Exact reference | Role |
| --- | --- | --- |
| Current main | [0bcea4a](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/0bcea4ae10d53a9067652c1c5a12e87e86fb3efa) | Base for this update |
| Prior target README | [267222a](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/contracts/biodiversity/README.md) | Previous blob and rollback target |
| Target placeholder | [e69de29](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/contracts/biodiversity/.gitkeep) | Confirms no direct contract file is present |
| Ecology architecture | [d1f156d2](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/architecture/ecology-cross-domain.md) | Umbrella/cross-domain boundary; generic join policy inactive |
| Cross-domain contract index | [58c2f1bf](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/contracts/cross_domain/README.md) | Named seam coordination boundary |
| Fauna contract README | [192f680b](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/contracts/domains/fauna/README.md) | Atomic fauna semantic ownership |
| Flora contract README | [f14d7842](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/contracts/domains/flora/README.md) | Flora responsibility-root evidence |
| Habitat contract README | [65b5b259](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/contracts/domains/habitat/README.md) | Habitat semantic ownership and boundary |
| Habitat geoprivacy | [0ea40247](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/domains/habitat/SENSITIVITY_AND_GEOPRIVACY.md) | Join-induced and derivation-induced sensitivity |
| Sensitivity runbook | [e4dc0cb9](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/runbooks/SENSITIVITY_ESCALATION.md) | Escalation and fail-closed reference |
| Fauna schema README | [4bd3dd86](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/schemas/contracts/v1/domains/fauna/README.md) | Fauna machine-shape lane |
| Flora schema README | [5c15731f](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/schemas/contracts/v1/domains/flora/README.md) | Flora machine-shape lane |
| Habitat schema README | [ab7563e3](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/schemas/contracts/v1/domains/habitat/README.md) | Habitat machine-shape lane |
| Cross-lane assessment | [f6322ecb](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/contracts/joins/cross_lane_join_assessment.md) | Proposed fixture-first assessment only |
| Biodiversity validator boundary | [64f7e286](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/tools/validators/biodiversity/README.md) | README-only parent/routing posture |
| Atmosphere × Biodiversity validator boundary | [cbe4dd09](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/tools/validators/atmosphere_biodiversity/README.md) | Cross-schema index; executable enforcement unestablished |
| Domain lane register | [1bfc6f91](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/control_plane/domain_lane_register.yaml) | Proposed domain projection; cannot create a domain |
| Cross-domain seam register | [dc87ea9c](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/control_plane/cross_domain_seam_register.yaml) | Proposed navigational/review projection |
| Policy-gate register | [bc8185b4](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/control_plane/policy_gate_register.yaml) | Proposed index; does not evaluate policy |
| Drive atlas lineage | [KFM Full Atlas seed cards](https://docs.google.com/document/d/1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho/edit?usp=drivesdk) | Read-only design lineage; proposed ideas do not establish repository authority |

Notion search found no direct current biodiversity coordination page. Notion remains a coordination projection, and Google Drive remains read-only lineage. Current GitHub evidence and accepted governance control implementation claims.

## Definition of done

- [ ] The path remains explicitly compatibility/cross-domain unless an accepted ADR changes that posture.
- [ ] Every composite has a named seam or owning responsibility-root location.
- [ ] Atomic Fauna, Flora, Habitat, and other domain ownership is preserved.
- [ ] Each composite has paired schema, fixture, validator, test, policy, evidence, review, release, correction, and rollback references or an explicit gap.
- [ ] Sensitivity, rights, sovereignty/CARE, taxonomy authority, and public audience tier are explicit.
- [ ] Exact or reconstructable sensitive locations are denied unless a governed safe transformation is approved and receipted.
- [ ] Public API, UI, map, graph, catalog, and AI surfaces remain behind the trust membrane.
- [ ] Exact-head validation is recorded with PASS, FAIL, SKIPPED, NOT_RUN, or UNKNOWN labels.
- [ ] The change remains reviewable, draft, reversible, and unmerged until independently approved.

## Rollback and review note

The rollback target for this update is the prior target blob [267222a1cbc6fdd7c67646a21a85badd7ad04ae2](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/0bcea4ae10d53a9067652c1c5a12e87e86fb3efa/contracts/biodiversity/README.md). Do not delete .gitkeep as part of a README-only change. Any new cross-domain contract, schema, policy, fixture, validator, or lifecycle artifact requires its own responsibility-root review, migration decision, and rollback plan.

Last reviewed: 2026-09-07 against main@0bcea4ae10d53a9067652c1c5a12e87e86fb3efa. This is a documentation-only draft update; it does not merge, mark ready, approve, release, deploy, publish, activate a source, change settings, or create a biodiversity domain.

<p align="right"><a href="#top">Back to top</a></p>

