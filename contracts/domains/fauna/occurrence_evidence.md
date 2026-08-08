<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-fauna-occurrence-evidence
title: Occurrence Evidence Contract
type: semantic-contract
version: v0.3
status: draft; DRAFT_SCHEMA; fixture-first validator; NEEDS VERIFICATION before promotion
owners: OWNER_TBD — Fauna steward · Occurrence steward · Evidence steward · Source steward · Sensitivity reviewer · Policy steward · Schema steward · Validation steward · Release steward
created: 2026-06-21
updated: 2026-08-08
policy_label: public; semantic-contract; fauna; occurrence-evidence; pre-sensitivity-split; source-role-aware; sensitivity-aware; no-publication-authority
tags: [kfm, contracts, fauna, occurrence-evidence, source-role, rights, sensitivity, geoprivacy, validation, correction, rollback]
related:
  - ./README.md
  - ./occurrence_public.md
  - ./occurrence_restricted.md
  - ../../../docs/domains/fauna/SOURCES.md
  - ../../../docs/domains/fauna/SOURCE_ROLES.md
  - ../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../docs/domains/fauna/SCHEMAS.md
  - ../../../schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json
  - ../../../data/registry/sources/fauna/
  - ../../../policy/domains/fauna/
  - ../../../policy/sensitivity/fauna/
  - ../../../fixtures/domains/fauna/occurrence_evidence/
  - ../../../tests/domains/fauna/test_occurrence_evidence.py
  - ../../../tools/validators/domains/fauna/occurrence/validate_occurrence_evidence.py
notes:
  - "v0.3 realizes Pass 3 card KFM-P3-PROG-0001 at the current responsibility-rooted Fauna paths."
  - "The paired schema is now a closed Draft 2020-12 DRAFT_SCHEMA rather than an empty permissive scaffold."
  - "The implementation uses the repository's canonical seven-class source_role vocabulary and represents source-native occurrence form through observation.basis_of_record."
  - "OccurrenceEvidence is source-bound evidence before the public/restricted sensitivity split; it is never publication authority by itself."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Occurrence Evidence

> Semantic contract for a Fauna source-bound occurrence-evidence record before policy and review decide whether any public-safe or restricted derivative may exist.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Schema: draft machine shape" src="https://img.shields.io/badge/schema-DRAFT__SCHEMA-orange">
  <img alt="Validation: fixture first" src="https://img.shields.io/badge/validation-fixture--first-blueviolet">
  <img alt="Boundary: pre-sensitivity split" src="https://img.shields.io/badge/boundary-pre__sensitivity__split-critical">
</p>

`contracts/domains/fauna/occurrence_evidence.md`

## Status

> [!IMPORTANT]
> **Status:** draft semantic contract with a closed `DRAFT_SCHEMA` and deterministic no-network validator.  
> **Schema:** `schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json`  
> **Validator:** `tools/validators/domains/fauna/occurrence/validate_occurrence_evidence.py`  
> **Truth posture:** placement, schema shape, deterministic identity, fixture polarity, and focused tests are CONFIRMED for this repository slice. Source admission, current rights, taxonomic authority, policy execution, steward review, EvidenceBundle resolution, public/restricted conversion, release, API/UI behavior, and publication remain held or NEEDS VERIFICATION.

> [!CAUTION]
> `OccurrenceEvidence` is not `OccurrencePublic`. A schema or validator pass does not authorize exact geometry exposure, geoprivacy transformation, release, or publication.

## Meaning

`OccurrenceEvidence` records **source-bound evidence or context associating an animal taxon, specimen, sample, detection, report, administrative or regulatory record, aggregate, model output, candidate, or synthetic reconstruction with a place/time/support scope**.

It preserves:

- source-native record identity and source family;
- canonical source role and source-native basis of record;
- taxon identity and observation time/method;
- exact/internal and public-safe spatial support as separate fields;
- normalized rights and sensitivity posture;
- SourceDescriptor, raw-artifact, and EvidenceRef linkage; and
- deterministic identity plus finite validation state.

It is the **pre-sensitivity-split** record. Downstream contracts and policy decide whether it remains held, becomes `OccurrenceRestricted`, or supports a separately reviewed `OccurrencePublic` derivative.

## Responsibility split

| Responsibility | Owning surface |
|---|---|
| Source-bound occurrence meaning | `contracts/domains/fauna/occurrence_evidence.md` |
| Machine shape | `schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json` |
| Executable validation | `tools/validators/domains/fauna/occurrence/` |
| Synthetic examples and expected findings | `fixtures/domains/fauna/occurrence_evidence/` |
| Enforceability | `tests/domains/fauna/test_occurrence_evidence.py` and the focused workflow |
| Source identity, rights, cadence, and role assignment | `data/registry/sources/fauna/` |
| Admissibility and geoprivacy | `policy/domains/fauna/`, `policy/sensitivity/fauna/` |
| Evidence/proof | EvidenceRef/EvidenceBundle contracts and `data/proofs/` |
| Release, correction, withdrawal, rollback | `release/` and their owning contracts |

This slice creates no competing root, schema home, policy home, source registry, proof store, or release authority.

## Machine contract

The closed Draft 2020-12 schema requires:

| Field | Semantic responsibility |
|---|---|
| `object_type`, `schema_version` | Object family and schema edition. |
| `spec_hash`, `occurrence_evidence_id` | Deterministic content identity. |
| `source_record_id`, `source_family`, `source_role` | Source-native identity, source family, and canonical role. |
| `taxon` | Scientific and accepted name plus rank. |
| `observation` | Event date/time, basis of record, method, optional observer and count. |
| `geometry` | Internal precision/geoprivacy plus an explicit public-safe representation. |
| `rights` | License, redistribution, commercial-use, and attribution posture. |
| `sensitivity` | Sensitive-species, exact-location, generalization, withholding, and review flags. |
| `provenance` | Source URI, retrieval, publisher, ingestion run, raw-artifact reference, SourceDescriptor, EvidenceRefs. |
| `validation` | Finite result, canonical reason codes, seven readiness booleans, evidence strength, validator version/time. |

Top-level and nested objects are closed. A future extension requires a reviewed successor schema or an explicitly named extension point; undeclared fields are denied.

### Finite states

`validation.validator_result` is one of:

- `pass` — the draft schema and all bounded gates pass, no reason codes remain, and required review is complete;
- `quarantine` — structurally valid but held for evidence, rights, sensitivity, or steward review;
- `deny` — the declared use is prohibited by the bounded profile or an external decision;
- `error` — machine shape, identity, or validation consistency failed.

A valid `quarantine` fixture proves that **schema-valid does not mean public or release-ready**.

## Identity and hashing

The validator computes RFC 8785 JCS + SHA-256 over exactly:

```json
{
  "accepted_taxon_name": "<taxon.accepted_scientific_name>",
  "event_date": "<observation.event_date>",
  "normalized_geometry": {
    "geoprivacy_status": "<geometry.geoprivacy_status>",
    "latitude": "<geometry.latitude or null>",
    "longitude": "<geometry.longitude or null>",
    "precision_class": "<geometry.precision_class>",
    "public_safe_geometry": "<geometry.public_safe_geometry or null>"
  },
  "source_record_id": "<source_record_id>"
}
```

The executable receives typed JSON values; the placeholders above are explanatory. Upstream normalization must happen before hashing. The validator does not round coordinates, infer geometry, rewrite taxonomy, or alter source identifiers.

`spec_hash` is `sha256:<64 lowercase hex>`. `occurrence_evidence_id` is `kfm://occurrence/<the same digest>`. A mismatch is an `identity.*` error.

## Source-role anti-collapse

The current repository's seven-class vocabulary controls `source_role`. `observation.basis_of_record` carries the source-native occurrence form.

| `source_role` | Required basis posture | Meaning boundary |
|---|---|---|
| `observed` | direct observation, specimen, sample, or literature basis | May support occurrence evidence when source, method, rights, sensitivity, and evidence resolve. |
| `regulatory` | `regulatory_record` | Regulatory context; not an observed occurrence. |
| `modeled` | `model_output` | Model context; never observed reality. |
| `aggregate` | `aggregate_summary` | Roll-up; not exact event or site truth. |
| `administrative` | `administrative_record` | Administrative context; not direct observation truth. |
| `candidate` | `candidate_report` | Unreviewed intake; not authoritative or publishable. |
| `synthetic` | `synthetic_reconstruction` | Generated/reconstructed context; never observed reality. |

The validator rejects role/basis mismatches. Source family remains separate: using an aggregator such as GBIF does not automatically change the originating record's source role.

## Rights and sensitivity

The four rights fields are required. Nullable booleans preserve unresolved posture, but unresolved rights cannot claim `pass` or `checks.rights_resolved: true`.

Public-safe geometry rules preserved by this slice:

- source geoprivacy and KFM public precision are separate;
- non-open, generalized, or withheld cases require an explicit `public_safe_geometry` object;
- withheld public geometry has no coordinates;
- generalization-required geometry cannot retain exact public precision;
- `exact_location_public_safe` conflicts with private/withheld/generalized state;
- sensitive-species records require review posture; and
- review-required records without `steward_reviewed` evidence strength may be valid `quarantine` or `deny`, but never `pass`.

The schema and validator check consistency only. They do not decide which taxon or site is sensitive, perform a transform, or approve exposure.

## Validation findings

Stable code families are:

- `prov.*` — provenance and raw-artifact support;
- `rights.*` — rights resolution;
- `geom.*` — exact/public-safe geometry consistency;
- `sens.*` — sensitivity, withholding, and review posture;
- `taxon.*` — accepted-name normalization;
- `obs.*` — source-role/basis semantics;
- `identity.*` — deterministic hash and URI identity; and
- `schema.*` — machine shape, canonical arrays, declared-check consistency, fixture replay, and finite-state discipline.

Findings expose only code and JSON Pointer path; they never print protected values.

### Confirmed in this slice

- closed Draft 2020-12 schema with all Pass 3 required top-level fields;
- deterministic JCS + SHA-256 identity and URI binding;
- source-role anti-collapse and required raw-artifact support;
- four-field rights posture with fail-closed unresolved-rights behavior;
- exact/public-safe geometry, generalization, withholding, and review checks;
- finite states and seven readiness booleans;
- three synthetic valid fixtures, including a sensitive held record;
- five synthetic negative fixtures;
- exact expected-finding manifest, focused no-network tests, CI wiring, and generated receipt.

### Still held

- live source descriptors, endpoints, terms, rights, cadence, and field mappings;
- accepted taxonomy authority and crosswalks;
- binding policy and named steward assignments;
- EvidenceRef-to-EvidenceBundle resolution and proof closure;
- canonical conversion to `OccurrenceRestricted` or `OccurrencePublic`;
- RedactionReceipt, PolicyDecision, ReviewRecord, ReleaseManifest, correction, withdrawal, and rollback behavior;
- governed API, MapLibre/Evidence Drawer, export, search, graph, or AI behavior; and
- live ingestion, lifecycle writes, release, deployment, or publication.

## Lifecycle boundary

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This object can move through non-public lifecycle stages only under their owning controls. Public exposure requires a separately governed public-safe object and release state. Watchers, validators, fixtures, tests, commits, and pull requests are not promotion.

## Open questions

| ID | Question | Status |
|---|---|---|
| OQ-FAUNA-OE-001 | Which source-native basis values and source-family mappings are admitted? | NEEDS VERIFICATION |
| OQ-FAUNA-OE-002 | Which source-native IDs may be stored directly, hashed, or hidden behind EvidenceRef? | NEEDS VERIFICATION |
| OQ-FAUNA-OE-003 | Which policy splits this object into restricted versus public derivatives? | NEEDS VERIFICATION |
| OQ-FAUNA-OE-004 | Which redaction/generalization receipt family is canonical? | NEEDS VERIFICATION |
| OQ-FAUNA-OE-005 | How are misidentification, duplicate, taxonomic change, withdrawal, and rights/sensitivity change represented in correction lineage? | NEEDS VERIFICATION |
| OQ-FAUNA-OE-006 | Should a successor schema add named extension points or remain fully closed? | NEEDS VERIFICATION |

## Evidence and rollback

**Evidence basis:** Pass 3 card `KFM-P3-PROG-0001` supplies the candidate fields, source families, rights and sensitivity blocks, identity rule, finite states, and fixture pressure. Accepted ADR-0029 controls placement. Current Fauna source-role docs control the seven-class vocabulary. The prior schema blob `bd1f00f7872aeaf441dbf297044d264fba547dc4` proves that machine shape was previously empty and permissive; prior contract blob `6ad0646746abf86b4b11cbb757e208b7398794bc` preserved the semantic boundary and listed the implementation backlog.

Rollback if this contract or its companions are used to claim source admission, EvidenceBundle closure, policy/steward approval, exact sensitive-location publication, release readiness, or public occurrence authority.

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the additive packet and restore the prior contract and schema blobs named above. No live source, lifecycle data, API route, UI component, release, deployment, or public artifact is activated, so rollback is repository-only.

<p align="right"><a href="#top">Back to top</a></p>
