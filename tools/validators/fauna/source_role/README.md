<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-fauna-source-role-readme
title: tools/validators/fauna/source_role README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-fauna-steward-plus-source-steward-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; fauna-validator; source-role; source-descriptor; anti-collapse; sensitive-species; geoprivacy; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed Fauna source-role validator lane for checking SourceDescriptor.source_role assignment, seven-class canonical enum posture, source-family separation, aggregator/context/model/observation anti-collapse, sensitive occurrence source-role handling, source registry linkage, evidence/proof linkage, policy/review/release linkage, correction and rollback linkage, and public-surface denial checks while deferring source-role doctrine, source registry authority, Fauna meaning, evidence records, policy decisions, proof records, receipts, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../../domains/fauna/README.md
  - ../../biodiversity/README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ../../../../docs/domains/fauna/SOURCE_ROLES.md
  - ../../../../docs/domains/fauna/SOURCE_REGISTRY.md
  - ../../../../docs/domains/fauna/SOURCE_FAMILIES.md
  - ../../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../../docs/domains/fauna/README.md
  - ../../../../data/registry/sources/fauna/README.md
  - ../../../../data/registry/fauna/sources/README.md
  - ../../../../contracts/domains/fauna/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../schemas/contracts/v1/domains/fauna/
  - ../../../../policy/domains/fauna/
  - ../../../../policy/sensitivity/fauna/
  - ../../../../data/proofs/fauna/
  - ../../../../data/receipts/
  - ../../../../release/
notes:
  - "This README replaces a stray one-character file. It does not confirm executable files."
  - "No broad tools/validators/fauna/README.md was found during this task. The per-domain Fauna validator index remains tools/validators/domains/fauna/README.md."
  - "Fauna SOURCE_ROLES evidence says the canonical source_role enum is SourceDescriptor.source_role with seven classes: observed, regulatory, modeled, aggregate, administrative, candidate, synthetic."
  - "The Fauna source-role crosswalk is not the authority: SourceDescriptor wins over SOURCES.md, and SOURCES.md wins over the crosswalk. This validator must check assignments; it must not re-decide the enum."
  - "Fauna exact occurrence geometry, nests, dens, roosts, hibernacula, spawning sites, breeding sites, telemetry detail, and steward-controlled records remain deny-by-default until governed geoprivacy/redaction/review/policy/release gates close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/fauna/source_role

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-fauna--source--role-informational)
![posture](https://img.shields.io/badge/posture-anti--collapse-critical)
![sensitivity](https://img.shields.io/badge/sensitivity-deny--by--default-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/fauna/source_role/` is the proposed Fauna source-role validator lane for checking that Fauna source descriptors and downstream candidates preserve the canonical `source_role` assignment, source-family boundaries, evidence support, policy/release posture, and sensitive-species public-surface denial.

---

## Purpose

`tools/validators/fauna/source_role/` exists for Fauna source-role checks under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a Fauna source or candidate preserve its admitted `SourceDescriptor.source_role`, source family, authority limit, claim family, sensitivity posture, EvidenceRef/EvidenceBundle support, policy/review state, release linkage, correction lineage, rollback target, and public-surface denial before it is used by catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces?

The answer should be a deterministic validation result. This folder should not create Fauna truth, taxonomic authority, source descriptors, source-role doctrine, source payloads, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/fauna/source_role/README.md` | **CONFIRMED** | This README replaces a stray one-character file. |
| Broad `tools/validators/fauna/README.md` | **NOT FOUND in this task** | No broad parent README was found; the domain-level Fauna validator index remains `tools/validators/domains/fauna/README.md`. |
| Per-domain Fauna validator index | **CONFIRMED README / executable NEEDS VERIFICATION** | The domain index covers source-role posture, occurrence, sensitive-site, geoprivacy, taxon/status, range, migration, mortality, disease, invasive-species, evidence, policy, release, correction, rollback, and public-surface denial. |
| Fauna source registry lane | **CONFIRMED in repo evidence / draft** | `data/registry/sources/fauna/README.md` says Fauna source registry records carry source identity, source family, source role, rights, sensitivity, cadence, authority limits, and release references, but not animal truth. |
| Fauna source-role crosswalk | **CONFIRMED in repo evidence / draft** | `docs/domains/fauna/SOURCE_ROLES.md` maps informal shorthand to canonical seven-class `source_role` and says SourceDescriptor assignment wins. |
| Executable, accepted source-role schema, fixtures, policy bundles, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a validator implementation, source-role enum enforcement, fixture set, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Canonical source-role posture

The current Fauna source-role evidence distinguishes informal shorthand from the repo-bearing enum:

| Informal shorthand | Canonical `source_role` posture | Validator concern |
|---|---|---|
| `authority` | `regulatory` or `aggregate` depending on whether it is a legal/conservation determination or a rolled-up status/rank. | Do not collapse regulatory authority and aggregate rank. |
| `observation` | `observed` for direct records such as field occurrence, acoustic detection, or specimen. | Do not turn observations into regulatory truth or modeled surfaces. |
| `context` | Not a canonical role by itself; realized through governed joins as observed or aggregate context from its owning lane. | Do not treat habitat, landcover, wetland, soil, ownership, or context layers as Fauna truth. |
| `model` | `modeled` for suitability, range, distribution, or similar derived products. | Do not present models as observations or regulatory authority. |
| No shorthand | `administrative`, `candidate`, or `synthetic` when the admitted source or candidate state requires it. | Do not use ingest/admin/synthetic state as observation proof. |

The validator should check for anti-collapse. It should not define the enum, rewrite SourceDescriptors, or decide source admission.

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home |
|---|---|
| Fauna source-role validation lane | `tools/validators/fauna/source_role/` |
| Per-domain Fauna validator index | `tools/validators/domains/fauna/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Biodiversity/cross-domain checks | `tools/validators/biodiversity/`, `tools/validators/cross-domain-joins/` |
| Fauna source-role doctrine/crosswalk | `docs/domains/fauna/SOURCE_ROLES.md`, `docs/domains/fauna/SOURCES.md`, `docs/domains/fauna/SOURCE_FAMILIES.md` |
| SourceDescriptor records | `data/registry/sources/fauna/` or accepted source-registry home |
| Fauna meaning and contracts | `docs/domains/fauna/`, `contracts/domains/fauna/` |
| Machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/fauna/` |
| Policy and sensitivity | `policy/domains/fauna/`, `policy/sensitivity/fauna/`, or accepted policy homes |
| Proofs, receipts, release | `data/proofs/fauna/`, `data/proofs/`, `data/receipts/`, `release/` |

This README does not move, replace, or override those roots. It only defines where Fauna source-role validation may be documented or implemented after verification.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Fauna source-role validator lane | `tools/validators/fauna/source_role/` |
| Fauna domain validator index | `tools/validators/domains/fauna/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Fauna source-role crosswalk/doctrine | `docs/domains/fauna/SOURCE_ROLES.md`, `docs/domains/fauna/SOURCES.md`, `docs/domains/fauna/SOURCE_FAMILIES.md` |
| SourceDescriptor storage/admission state | `data/registry/sources/fauna/` or accepted source-registry home |
| Fauna domain meaning | `docs/domains/fauna/`, `contracts/domains/fauna/` |
| Source and Fauna schemas | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/fauna/` |
| Policy and geoprivacy | `policy/domains/fauna/`, `policy/sensitivity/fauna/`, or accepted policy homes |
| Evidence/proof support | `data/proofs/fauna/`, `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/fauna/source_role/`, `tests/validators/domains/fauna/`, `tests/domains/fauna/`, `fixtures/domains/fauna/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared Fauna source-role, source-family, evidence, policy, geoprivacy, and release-reference rules and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, accepted source-role schema/enum binding, source registry topology, fixture shape, policy bundles, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as Fauna doctrine, source-role enum authority, source registry, source payload storage, schema home, proof storage, receipt storage, policy home, release record store, public runtime surface, taxonomic authority, stewardship authority, geoprivacy authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/fauna/source_role/` include checks that:

- verify every consequential Fauna source or candidate points to an admitted SourceDescriptor or accepted source-registry record;
- verify `source_role` is present, canonical, and consistent with source family, claim family, sensitivity posture, and authority limits;
- detect when informal shorthand is used where the canonical enum is required;
- detect when regulatory, aggregate, observed, modeled, administrative, candidate, or synthetic roles are collapsed;
- detect aggregator traps where an aggregator source is treated as source-role authority rather than as a carrier of records with their own roles;
- detect context-layer collapse where Habitat, Hydrology, Soil, Landcover, People/Land, or administrative context becomes Fauna truth;
- detect when public-bound occurrence, range, migration, mortality, disease, invasive, or taxon/status claims lack source-role, evidence, policy, release, correction, or rollback support;
- emit deterministic findings for downstream review without storing source descriptors, proofs, receipts, or release records.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/fauna/source_role/` | Correct home |
|---|---|
| Source-role doctrine, enum definition, or crosswalk authority | `docs/domains/fauna/SOURCE_ROLES.md`, `docs/domains/fauna/SOURCES.md`, source schemas, or accepted doctrine/schema homes |
| SourceDescriptor records or admission sidecars | `data/registry/sources/fauna/` or accepted source-registry home |
| Fauna source payloads | `data/raw/fauna/`, `data/work/fauna/`, `data/quarantine/fauna/`, `data/processed/fauna/` |
| Fauna domain meaning | `docs/domains/fauna/`, `contracts/domains/fauna/` |
| Schemas and enums | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/fauna/` |
| Policy and geoprivacy rules | `policy/domains/fauna/`, `policy/sensitivity/fauna/`, or accepted policy homes |
| EvidenceBundles, proofs, receipts, validation reports, redaction receipts | `data/proofs/`, `data/receipts/` |
| Release manifests, correction notices, rollback cards, withdrawals | `release/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Public API, UI, map, tile, export, search, graph, Focus Mode, AI runtime code, stewardship decisions, or publication output | governed application/runtime roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Fauna source-role validator posture

Fauna source-role validators must fail closed, deny, abstain, hold, or route to review when a candidate:

- lacks SourceDescriptor linkage, source role, source family, claim family, authority limit, EvidenceRef, EvidenceBundle/proof reference, sensitivity posture, policy posture, review state, release reference, correction path, or rollback target required for its use;
- uses informal shorthand instead of the canonical source-role enum where machine validation requires the canonical value;
- treats regulatory status as occurrence evidence, observation as regulatory truth, modeled suitability as observation, aggregate rank as site proof, administrative roster as observation, candidate material as public fact, or synthetic reconstruction as source evidence;
- treats context layers such as habitat, landcover, wetlands, hydrology, soils, infrastructure, ownership, or administrative units as Fauna truth instead of governed join context;
- treats aggregator records as if the aggregator itself decides the role for all underlying records;
- exposes sensitive taxa, exact occurrences, nests, dens, roosts, hibernacula, spawning sites, breeding/aggregation sites, telemetry detail, steward-controlled records, or reverse-engineerable derivatives without geoprivacy, review, policy, release, correction, and rollback support;
- allows catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces to depend on source-role-collapsed Fauna records;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, stale source descriptors, or incomplete proof closure;
- treats source-role validation as SourceDescriptor creation, EvidenceBundle creation, PolicyDecision creation, release approval, publication, taxonomic authority, stewardship authority, or public API behavior.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `FAUNA_SOURCE_ROLE_PASS` | Configured Fauna source-role checks passed. |
| `FAUNA_SOURCE_ROLE_FAIL` | One or more configured Fauna source-role checks failed. |
| `FAUNA_SOURCE_DESCRIPTOR_MISSING` | Required SourceDescriptor or source-registry pointer is absent. |
| `FAUNA_SOURCE_ROLE_MISSING` | Required source_role value is absent. |
| `FAUNA_SOURCE_ROLE_UNKNOWN` | source_role value is not accepted by configured schema/policy/source profile. |
| `FAUNA_SOURCE_ROLE_SHORTHAND_USED` | Informal shorthand is used where canonical enum value is required. |
| `FAUNA_REGULATORY_OBSERVED_COLLAPSE` | Regulatory status and observed occurrence are conflated. |
| `FAUNA_AGGREGATE_SITE_PROOF_COLLAPSE` | Aggregate rank/status is treated as site-specific occurrence proof. |
| `FAUNA_MODELED_OBSERVED_COLLAPSE` | Modeled suitability/range/distribution is treated as observed occurrence. |
| `FAUNA_ADMINISTRATIVE_OBSERVED_COLLAPSE` | Administrative roster/register is treated as observation. |
| `FAUNA_CANDIDATE_PUBLIC_FACT_COLLAPSE` | Candidate material is treated as public fact. |
| `FAUNA_SYNTHETIC_SOURCE_EVIDENCE_COLLAPSE` | Synthetic reconstruction is treated as source evidence. |
| `FAUNA_CONTEXT_AS_TRUTH_DENIED` | Context layer is treated as Fauna truth. |
| `FAUNA_AGGREGATOR_TRAP` | Aggregator carrier role is confused with underlying record role. |
| `FAUNA_SENSITIVE_OCCURRENCE_DENIED` | Sensitive occurrence/site detail is unsafe for the requested surface. |
| `FAUNA_POLICY_OR_RELEASE_GAP` | Required policy, review, release, correction, or rollback support is absent. |
| `FAUNA_PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `DENY` | Candidate is explicitly disallowed for the requested use. |
| `HOLD` | Candidate requires steward review, closure, quarantine, or source-admission work before use. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/fauna/source_role/
├── README.md
├── test_fauna_source_role.py
└── fixtures/
    ├── valid_observed_occurrence_source/
    ├── valid_regulatory_status_source/
    ├── valid_aggregate_rank_source/
    ├── valid_modeled_range_source/
    ├── missing_source_descriptor/
    ├── shorthand_used_instead_of_enum/
    ├── regulatory_observed_collapse/
    ├── aggregate_site_proof_collapse/
    ├── modeled_as_observed_denied/
    ├── context_as_truth_denied/
    ├── aggregator_trap/
    └── sensitive_occurrence_denied/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/fauna/source_role
```

```bash
python tools/validators/fauna/source_role/validate_fauna_source_role.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_fauna_source_role.py` or the test path exists here.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared SourceDescriptor/source-role schemas, Fauna source docs, source registry records, contracts, and policy rather than defining meaning locally.
- [ ] Canonical source-role enum values remain distinct: observed, regulatory, modeled, aggregate, administrative, candidate, synthetic.
- [ ] Informal shorthand is not accepted where canonical enum is required.
- [ ] Source role, source family, claim family, authority limits, sensitivity, rights, evidence, policy, release, correction, and rollback remain visible.
- [ ] Context layers and aggregators do not become Fauna truth by accident.
- [ ] Sensitive occurrence/site detail fails closed unless geoprivacy, review, policy, release, correction, and rollback support exists.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, stale source descriptors, source-role-collapsed candidates, or incomplete proof closure.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, source admission, taxonomic authority, stewardship authority, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-08 |
| Review state | Draft README replacement for stray one-character Fauna source-role validator file. |
| Next smallest safe change | Verify actual Fauna source-role validator script path, accepted source-role schema/enum binding, source registry topology, fixtures, report destination, receipt emission, policy enforcement, release linkage, geoprivacy behavior, and CI/runtime wiring before promoting this lane beyond draft. |
