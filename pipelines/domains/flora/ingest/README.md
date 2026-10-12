<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-flora-ingest-readme
title: Flora Ingest Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <flora-pipeline-owner>
  - <flora-domain-steward>
  - <source-steward>
  - <taxonomy-steward>
  - <evidence-steward>
  - <geoprivacy-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-rare-flora-ingest-and-geoprivacy-gates
path: pipelines/domains/flora/ingest/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/flora/README.md
  - docs/domains/flora/README.md
  - docs/domains/flora/DATA_LIFECYCLE.md
  - docs/domains/flora/SOURCES.md
  - docs/domains/flora/SOURCE_FAMILIES.md
  - docs/domains/flora/SOURCE_REGISTRY.md
  - docs/domains/flora/IDENTITY_MODEL.md
  - docs/domains/flora/CROSSWALKS.md
  - docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - pipeline_specs/flora/ingest.yaml
  - contracts/domains/flora/
  - schemas/contracts/v1/domains/flora/
  - policy/domains/flora/
  - policy/sensitivity/flora/
  - data/raw/flora/
  - data/work/flora/
  - data/quarantine/flora/
  - data/processed/flora/
  - data/catalog/domain/flora/
  - data/triplets/flora/
  - data/published/layers/flora/
  - data/registry/sources/flora/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/flora/
  - release/manifests/flora/
tags:
  - kfm
  - pipelines
  - domains
  - flora
  - ingest
  - source-admission
  - raw-capture
  - quarantine
  - plant-taxon
  - flora-occurrence
  - specimen
  - vegetation-community
  - phenology
  - invasive-plants
  - geoprivacy
  - source-role
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/flora/ingest path as a nested executable Flora ingest sublane."
  - "Flora ingest logic is executable implementation support only; it does not own source descriptors, connectors, schemas, contracts, policy, taxonomy authority, lifecycle data, catalog truth, geoprivacy decisions, or release decisions."
  - "Ingest admits source captures or fixture payloads into RAW, WORK, or QUARANTINE posture; it does not normalize into accepted truth, publish, or bypass validation."
  - "Source family profiles and per-source admission decisions remain separate from this executable lane."
  - "Rare, protected, culturally sensitive, steward-reviewed, join-sensitive, and rights-unclear flora records fail closed during ingest."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Ingest Pipeline

> Executable Flora sublane for admitting approved source captures, fixture payloads, and intake envelopes into governed RAW, WORK, or QUARANTINE posture — while preserving source identity, source role, rights, taxonomic uncertainty, exact-location sensitivity, geoprivacy posture, evidence refs, receipts, and downstream validation boundaries.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-flora%20ingest-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20ingest%20logic-0a7ea4)
![geoprivacy](https://img.shields.io/badge/rare%20flora-fail%20closed-d62728)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/flora/ingest/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Flora  
**Sublane:** Ingest / source-admission execution  
**Placement posture:** nested executable sublane under `pipelines/domains/flora/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; ingest outputs remain raw captures, work candidates, quarantine records, receipts, or downstream validation inputs until governed promotion, catalog, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Ingest anti-collapse rules](#3-ingest-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Source-family intake posture](#6-source-family-intake-posture)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal ingest candidate record](#11-minimal-ingest-candidate-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/flora/ingest/` is the executable sublane for Flora source-admission and ingest processing.

It supports candidate processing for:

- admitted Flora source captures and fixture payloads;
- plant-taxonomy, occurrence, specimen, vegetation-community, invasive-plant, phenology, restoration, range, and distribution source material;
- GBIF, iDigBio, iNaturalist-derived, herbarium, KDWP, NatureServe, USFWS ECOS, USDA PLANTS, Kansas Biological Survey, and other admitted source-family inputs;
- immutable RAW capture receipts, retrieval metadata, source-vintage refs, rights refs, source-role refs, payload hashes, and intake run receipts;
- initial WORK candidates when source material passes minimal admission checks but still needs normalization, validation, and policy review;
- QUARANTINE records for source descriptor gaps, rights uncertainty, sensitive exact geometry, taxonomy conflicts, malformed payloads, stale feeds, join-induced sensitivity, or source-role ambiguity;
- handoffs to normalize, validate, catalog, triplet, EvidenceBundle, release-review, correction, and rollback workflows.

This directory implements or will implement the **how** of Flora ingest. It does not own source descriptors, source connectors, source profiles, taxonomy authority, schemas, policy, geoprivacy decisions, lifecycle data, processed truth, catalog truth, release decisions, or public map/API output.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/flora/`? | Flora is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; behavior NEEDS VERIFICATION |
| Why `ingest/`? | This is a narrow executable sublane for Flora source admission into RAW, WORK, or QUARANTINE posture. | PROPOSED / NEEDS VERIFICATION |
| Is this a connector? | No. Connectors fetch; ingest receives admitted captures or fixture payloads and routes them into lifecycle posture. | CONFIRMED separation |
| Does this own source profiles? | No. Source-family profiles and per-source admission registers remain in docs/registry homes. | CONFIRMED source separation |
| Does this own geoprivacy decisions? | No. It preflights and fails closed when geoprivacy/policy is unresolved. | CONFIRMED sensitivity posture |
| Can this sublane publish? | No. It may prepare raw/work/quarantine handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Flora ingest is not botanical truth. A successful ingest run means material was captured or routed with receipts; it does not mean the taxon identity is accepted, the occurrence is verified, exact geometry is public, or a release is approved.

[⬆ Back to top](#top)

---

## 3. Ingest anti-collapse rules

Flora ingest must preserve source identity, source role, rights, sensitivity, geoprivacy, and lifecycle state.

Disallowed collapses:

```text
ingested record -> accepted Flora truth
watcher event -> admitted RAW payload
connector success -> source admission approval
source family profile -> SourceDescriptor
source role hint -> final source role
raw occurrence -> verified occurrence
specimen record -> field occurrence without basis
taxon name string -> accepted taxon identity
exact rare-plant geometry -> public geometry
rights-unclear payload -> public candidate
pre-RAW event -> processed record
generated summary -> evidence
pipeline run -> release approval
```

Required distinctions:

- source family, admitted source, connector result, pre-RAW event, RAW capture, WORK candidate, QUARANTINE hold, processed object, catalog record, release candidate, and published artifact remain distinct;
- source roles are recorded at admission and never silently edited in place;
- rare/protected/culturally sensitive/steward-reviewed/join-sensitive material defaults to quarantine, withholding, generalization, aggregation, staged review, or denial;
- source-vintage, retrieval time, observed time, valid time, processing time, and release time remain distinct;
- rights and license uncertainty fail closed;
- every downstream claim resolves evidence or abstains.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Flora ingest routing.

Appropriate contents include:

- fixture-only ingest dry-run entrypoints;
- intake-envelope validators;
- RAW capture routing helpers;
- WORK candidate envelope builders;
- QUARANTINE routing helpers;
- source descriptor resolution checks;
- source-role and source-vintage preflight validators;
- rights/license preflight validators;
- rare-flora and exact-geometry sensitivity preflight validators;
- taxonomy-name and taxon-backbone conflict preflight checks;
- payload hash, retrieval metadata, and receipt emitters;
- handoff helpers for normalization, validation, catalog, and release-review workflows.

A good placement test:

> If the code receives an already approved source capture or fixture payload and routes it into RAW, WORK, or QUARANTINE posture with receipts, it may belong here. If it fetches from an upstream, defines a SourceDescriptor, normalizes final domain objects, decides policy/geoprivacy/release, writes catalog truth, or serves public API/map output, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Upstream fetchers and API clients | `connectors/<source>` or accepted connector home |
| Source-family profiles | `docs/domains/flora/SOURCE_FAMILIES.md` and source docs |
| Source descriptors / source registry entries | `data/registry/sources/flora/` or approved registry home |
| Flora doctrine and object meaning | `docs/domains/flora/`, `contracts/domains/flora/` |
| Taxonomic authority decisions | Taxonomy contracts/registries and steward review roots |
| JSON Schemas | `schemas/contracts/v1/domains/flora/` or accepted schema home |
| Policy, rights, sensitivity, geoprivacy, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/flora/...` |
| Fixtures | `fixtures/domains/flora/ingest/` or accepted fixture home |
| Tests | `tests/pipelines/domains/flora/ingest/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Catalog and triplet builders | `pipelines/domains/flora/catalog/`, `data/catalog/domain/flora/`, `data/triplets/flora/` |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Release decisions and manifests | `release/...` responsibility roots |

[⬆ Back to top](#top)

---

## 6. Source-family intake posture

| Source family | Ingest posture | Fail-closed triggers |
|---|---|---|
| KDWP flora / listed-species context | Regulatory/admin context; sensitive by default. | Rights unclear, exact locality, role ambiguity. |
| KDWP ecological review / stewardship outputs | Steward-review required before public derivative. | Administrative record treated as observation. |
| Kansas Biological Survey / KU herbarium | Specimen-backed source material. | Sensitive specimen locality or rights gap. |
| USFWS ECOS plant context | Status/listing context, not occurrence truth. | Status upcast into observed occurrence. |
| NatureServe Explorer / Explorer Pro | Conservation status/rank context. | License or redistribution uncertainty. |
| GBIF vascular-plant downloads | Snapshot-based occurrence aggregate. | Missing DOI/snapshot, per-record rights gap, sensitive join. |
| iDigBio specimen records | Digitized specimen source material. | Precise sensitive locality or source ambiguity. |
| iNaturalist-derived observations | Candidate/observed context depending admission. | Verification gap, privacy setting conflict, sensitive taxon. |

Every admitted feed must resolve to a source descriptor and retain source-vintage, role, rights, sensitivity, and citation metadata before it can leave ingest posture.

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Flora ingest run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, connector-emitted source captures, or intake envelopes that already have source identity and admission context.
2. **Verify** source descriptor, source role, rights/license, citation, source vintage, retrieval time, payload hash, taxon-name presence, geometry/sensitivity posture, and minimum structural parseability.
3. **Write or reference** immutable RAW capture only when admission checks pass.
4. **Emit** WORK candidate envelopes only for material that still needs normalization, taxonomic reconciliation, validation, EvidenceBundle closure, and policy review.
5. **Quarantine** source descriptor gaps, rights uncertainty, sensitive exact geometry, malformed payloads, source-role ambiguity, taxonomy conflicts, stale feeds, and join-induced sensitivity.
6. **Emit receipts** for every accepted, rejected, quarantined, or abstained ingest action.
7. **Never publish directly.**

Ingest is the first lifecycle gate after source admission. It is not processing, cataloging, or release.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Flora ingest run must check or explicitly fail closed on:

1. **SourceDescriptor gate** — source identity, source family, source role, rights, citation, and cadence/vintage are present.
2. **Source-role gate** — observed, regulatory, administrative, aggregate, model, candidate, synthetic, and generated-context material remains distinct.
3. **Rights/license gate** — unresolved licenses, terms, redistribution rights, or steward controls quarantine.
4. **Payload integrity gate** — retrieval metadata, content hash, format, schema hint, and parser version are recorded.
5. **Taxon-name gate** — source taxon strings are present but are not accepted identity until reconciliation.
6. **Geometry/geoprivacy gate** — exact rare/protected/culturally sensitive/steward-reviewed/join-sensitive geometry fails closed.
7. **Temporal gate** — observed, event, source-vintage, retrieval, processing, and release times remain distinct.
8. **Sensitivity join gate** — joins that reconstruct sensitive locations are denied or quarantined pending review.
9. **Quarantine reason gate** — every denied/held record has a structured reason code and receipt.
10. **Lifecycle gate** — ingest writes only to accepted RAW/WORK/QUARANTINE/receipt homes.
11. **No-direct-catalog gate** — ingest does not write catalog/triplet records as a side effect.
12. **No-direct-publish gate** — ingest does not write public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/flora/ingest/
├── README.md                         # this file
├── INGEST_CONTRACT.md                # PROPOSED: Flora ingest execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/generalized/redacted fixture only
├── validate_intake_envelope.py       # PROPOSED
├── resolve_source_descriptor.py      # PROPOSED
├── validate_source_role.py           # PROPOSED
├── validate_rights_license.py        # PROPOSED
├── validate_payload_integrity.py     # PROPOSED
├── validate_taxon_name_presence.py   # PROPOSED
├── validate_geoprivacy_preflight.py  # PROPOSED
├── route_raw_work_quarantine.py      # PROPOSED
├── emit_ingest_receipt.py            # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/flora/ingest.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/raw/flora/`, `data/work/flora/`, `data/quarantine/flora/`, and `data/receipts/` before downstream normalization, validation, catalog, release, and published-layer roots.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/flora/ingest/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Connector source capture | Connector-owned output ref | Fetching is not owned here. |
| Intake envelope | `data/work/flora/<run_id>/` or accepted pre-RAW/event home | Candidate admission envelope. |
| RAW capture | `data/raw/flora/<source_id>/<run_id>/` | Immutable source capture only after admission checks. |
| WORK candidate | `data/work/flora/<run_id>/` | Candidate for normalization/validation. |
| QUARANTINE record | `data/quarantine/flora/<reason>/<run_id>/` | Failed, restricted, malformed, stale, or unresolved material. |
| Receipt | `data/receipts/pipeline/flora/ingest/<run_id>.yml` or accepted receipt home | Records inputs, checks, source refs, hashes, and output refs. |
| Downstream handoff | normalize/validate/catalog sublanes | Handoff only; no promotion by file move. |

[⬆ Back to top](#top)

---

## 11. Minimal ingest candidate record

The final schema is not defined here. This example shows the minimum information a Flora ingest candidate should preserve.

```yaml
schema_version: kfm.flora_ingest_candidate.v1
ingest_candidate_id: flora_ingest_<source_id>_<run_id>_<hash>
pipeline_id: domains.flora.ingest
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
source:
  source_id: <source_id>
  source_family: <gbif|idigbio|inaturalist|kdwp|usfws_ecos|natureserve|herbarium|other>
  source_role: <observed|regulatory|administrative|aggregate|modeled|candidate|synthetic|generated_context>
  source_descriptor_ref: data/registry/sources/flora/<source_id>.yml
  source_vintage: null
  citation_ref: null
  rights_state: needs_review
payload:
  raw_capture_ref: null
  input_hash: sha256:<hash>
  format: <dwca|json|csv|geojson|xml|other>
  parser_hint: null
flora_content:
  taxon_name_present: false
  accepted_taxon_ref: null
  occurrence_candidate_count: null
  specimen_candidate_count: null
  vegetation_candidate_count: null
sensitivity:
  exact_geometry_present: false
  sensitive_taxon_hint: needs_review
  geoprivacy_state: needs_review
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_DESCRIPTOR_RIGHTS_GEOPRIVACY_OR_SCHEMA_NOT_RESOLVED
anti_collapse:
  ingest_is_processed_truth: false
  source_family_profile_is_source_descriptor: false
  taxon_name_string_is_accepted_identity: false
  exact_sensitive_geometry_is_public: false
  connector_success_is_admission: false
outputs:
  raw_ref: null
  work_ref: data/work/flora/run_YYYYMMDDThhmmssZ/ingest_candidate.yml
  quarantine_ref: null
  receipt_ref: data/receipts/pipeline/flora/ingest/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until ingest specs, source descriptors, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/flora/ingest/
├── test_no_network_dry_run.py              # PROPOSED
├── test_source_descriptor_required.py      # PROPOSED
├── test_source_role_required.py            # PROPOSED
├── test_rights_unclear_quarantines.py      # PROPOSED
├── test_payload_hash_required.py           # PROPOSED
├── test_taxon_name_not_identity.py         # PROPOSED
├── test_rare_flora_geoprivacy_preflight.py # PROPOSED
├── test_sensitive_join_quarantines.py      # PROPOSED
├── test_malformed_payload_quarantines.py   # PROPOSED
├── test_raw_write_requires_admission.py    # PROPOSED
├── test_no_catalog_side_effect.py          # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, source descriptors and source roles are required, rights-unclear material quarantines, taxon names are not accepted identities, rare-flora geometry fails closed, receipts are deterministic, and no run writes directly to catalog, triplet, public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Flora ingest pipelines may prepare raw captures, work candidates, quarantine records, and receipts. They do not publish.

Required chain:

```text
admitted source capture / fixture
  -> ingest checks
  -> RAW capture or WORK candidate or QUARANTINE hold
  -> normalization
  -> validation report
  -> EvidenceBundle closure
  -> processed Flora object
  -> catalog / triplet handoff
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, malformed, restricted, stale, conflicted, and quarantined ingest runs remain auditable;
- receipts preserve source refs, source-role refs, rights refs, taxon-name refs, sensitivity refs, payload hashes, parser refs, and failure reasons;
- raw captures are immutable; corrected records are superseded through governed state transitions;
- downstream artifacts are invalidated if source refs, source-role refs, rights refs, EvidenceBundle refs, geoprivacy refs, policy refs, review refs, correction refs, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/flora/ingest/README.md` file;
- identifies this directory as a nested executable Flora ingest sublane;
- prevents connector, source-profile, schema, contract, policy, fixture, test, data, proof, public API, UI, geoprivacy decision, catalog, and release authority from being placed here;
- preserves source descriptor, source family, source role, source vintage, rights, payload hash, taxon-name uncertainty, geometry/geoprivacy posture, lifecycle, quarantine, evidence, policy, correction, and rollback boundaries;
- blocks ingest-as-truth, watcher-event-as-RAW, connector-success-as-admission, taxon-name-as-identity, exact-sensitive-geometry-as-public, generated-summary-as-evidence, catalog side effects, and direct publication writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor fixtures, no-network tests, schema-backed intake envelopes, contract conformance, source-role/rights/geoprivacy/quarantine/no-catalog/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `FLORA-INGEST-001` | Should Flora ingest remain one sublane, or split into source-family-specific ingest lanes such as GBIF, iDigBio, iNaturalist, KDWP, ECOS, NatureServe, PLANTS, and herbarium ingest? | NEEDS VERIFICATION / ADR |
| `FLORA-INGEST-002` | Which connector outputs are allowed as direct inputs to this ingest lane? | NEEDS VERIFICATION |
| `FLORA-INGEST-003` | Which schema owns SourceIntakeRecord, ingest envelope, quarantine reason codes, and ingest receipts? | NEEDS VERIFICATION |
| `FLORA-INGEST-004` | Which source-family fixtures are approved for first-wave dry runs? | NEEDS VERIFICATION |
| `FLORA-INGEST-005` | Which CI job owns Flora ingest invariant tests? | UNKNOWN |
| `FLORA-INGEST-006` | Should pre-RAW watcher envelopes be handled here, in a watcher lane, or in a shared intake edge? | NEEDS VERIFICATION / ADR |
| `FLORA-INGEST-007` | Which geoprivacy preflight is required before exact flora geometry can enter WORK instead of QUARANTINE? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/generalized/redacted fixture-only dry runs and negative tests. Do not add live source fetching, source-profile editing, schema authority, policy authority, geoprivacy-decision authority, direct catalog writes, direct public API code, direct UI code, release-manifest writes, public layer writes, or generated botanical summaries until source roles, source descriptors, rights, payload integrity, geoprivacy preflight, review state, and rollback are proven.
