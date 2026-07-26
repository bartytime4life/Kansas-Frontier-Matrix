<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-people-readme
title: data/processed/people/README.md — People Processed Data Compatibility README
version: v0.2.0
type: readme; data-lifecycle-sublane; processed-stage-guide; compatibility-lane; people-dna-land-people-sublane; assertion-evidence-lane
status: repository-grounded draft; PROPOSED compatibility path; payload/runtime enforcement unverified
owners: NEEDS VERIFICATION — People/DNA/Land steward · People sublane steward · Privacy reviewer · Consent steward · Rights steward · Sensitivity reviewer · Data steward · Evidence steward · Policy steward · Release steward · Docs steward
updated: 2026-07-25
supersedes: prior README at the same path; no payload, lifecycle, release, runtime, or publication state
prepared_under_prompt: KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent v5.0.0
policy_label: restricted-review; compatibility-only; no-direct-public-path; living-person-protected; consent-aware; release-gated
tags: [kfm, data, processed, people, people-dna-land, compatibility, person-assertion, genealogy, living-person, consent, privacy, evidence, correction, rollback]
related:
  - ../people-dna-land/README.md
  - dna/README.md
  - ../../processed/README.md
  - ../../../docs/domains/people-dna-land/README.md
  - ../../../docs/domains/people-dna-land/sublanes/people/README.md
  - ../../../policy/domains/people-dna-land/
  - ../../../policy/sensitivity/people/
  - ../../../policy/consent/people/
  - ../../../contracts/domains/people-dna-land/
  - ../../../schemas/contracts/v1/domains/people-dna-land/
  - ../../raw/people-dna-land/
  - ../../work/people-dna-land/
  - ../../quarantine/people-dna-land/
  - ../../catalog/domain/people-dna-land/
  - ../../triplets/
  - ../../published/
  - ../../proofs/
  - ../../receipts/
  - ../../registry/sources/people-dna-land/
  - ../../../release/candidates/people-dna-land/
notes:
  - "This file preserves the existing `data/processed/people/` path while clarifying that `data/processed/people-dna-land/` remains the current canonical data-lifecycle segment."
  - "This compatibility lane may hold bounded person/genealogy derivatives or migration/disposition metadata, but it must not become a parallel authority."
  - "Person assertions are evidence, not facts; living-person data, identity joins, and genealogy hypotheses remain restricted or denied by default until policy, consent, evidence, review, and release controls permit a safer representation."
  - "Consent revocation requires tombstoning, downstream invalidation, correction, withdrawal, and cache/index cleanup where applicable."
  - "Prior blob and rollback target: b0a8b76cbdf43ea0e76e16b7b1b3a944423ac943."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/processed/people/` — People Compatibility Candidates

> **One-line purpose.** Preserve a bounded compatibility lane for normalized person and genealogy assertion candidates without creating a second People authority, a public identity service, or a bypass around the canonical `people-dna-land` lifecycle segment.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status)
[![Lane: compatibility](https://img.shields.io/badge/lane-compatibility-f97316?style=flat-square)](#authority-level)
[![Lifecycle: PROCESSED](https://img.shields.io/badge/lifecycle-PROCESSED-8250df?style=flat-square)](#operating-contract)
[![Exposure: deny by default](https://img.shields.io/badge/exposure-deny%20by%20default-d1242f?style=flat-square)](#privacy-consent-and-living-person-controls)

> [!IMPORTANT]
> Directory placement, a normalized identity candidate, a resolved name match, a generated family relationship, a pull request, or a merge does not create identity truth, consent, evidence closure, policy permission, catalog admission, release approval, or KFM publication.

> [!WARNING]
> Living-person fields, direct identifiers, private family relationships, person-parcel joins, DNA-linked identity context, and other harmful or re-identifying detail must remain restricted, transformed, quarantined, or denied unless an evidence-backed policy and release path explicitly allows exposure.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Assertion semantics](#assertion-semantics) · [Privacy and consent](#privacy-consent-and-living-person-controls) · [Validation](#validation) · [Review](#review-burden) · [Correction](#correction-revocation-and-rollback) · [Related](#related-folders) · [ADRs](#adrs) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

`data/processed/people/` is an existing compatibility path for processed person and genealogy assertion candidates associated with the People / Genealogy / DNA / Land domain.

The current canonical data-lifecycle coordination path is:

```text
data/processed/people-dna-land/
```

This README therefore defines containment, not promotion. The shorter `people/` path may preserve bounded derivatives, aliases, migration metadata, or reconciliation artifacts, but it must not silently become a second domain authority or public-serving source.

## Authority level

**Compatibility-only PROCESSED responsibility; non-public by default.**

This path may own normalized person/genealogy assertion candidates and lane-local explanatory sidecars. It does not own:

- canonical domain placement;
- source-native records;
- object meaning or machine shape;
- consent, privacy, sensitivity, or rights decisions;
- EvidenceBundle or proof authority;
- catalog, triplet, release, or publication decisions;
- public API, UI, map, download, Focus Mode, AI, identity, genealogy, or lookup behavior.

Those responsibilities remain under their governed roots and interfaces.

## Status

| Field | Bounded result |
|---|---|
| Path | `data/processed/people/` |
| Canonical data segment | `people-dna-land` unless an accepted ADR changes it |
| Lane class | `PROPOSED compatibility` |
| Lifecycle | `PROCESSED` |
| Prior blob | `b0a8b76cbdf43ea0e76e16b7b1b3a944423ac943` |
| Recursive payload inventory | `UNKNOWN` |
| Active writers and consumers | `UNKNOWN` |
| Public readiness | `DENY BY DEFAULT` |
| Segment-disposition ADR | `NEEDS VERIFICATION` |

## What belongs here

Subject to policy, consent, rights, privacy, and local convention, this lane may contain:

- normalized person assertions and source-traced identity evidence candidates;
- `NameAssertion`, `LifeEvent`, `ResidenceEvent`, `MigrationEvent`, `GenealogyRelationship`, `FamilyGroup`, `RelationshipAssertion`, and `RelationshipHypothesis` derivatives;
- consent-reviewed and privacy-reviewed summaries that remain non-public;
- de-identified, aggregated, delayed, or otherwise transformed compatibility artifacts;
- controlled aliases, predecessor/successor links, migration maps, or disposition inventories that do not duplicate sovereign truth;
- validation references, limitations, uncertainty, correction lineage, and digest sidecars that are not receipts, proofs, policy decisions, catalog records, or release artifacts;
- documentation explaining compatibility and migration boundaries.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| Raw records, source-native family trees, images, OCR inputs, source media, vendor exports, direct source identifiers, or original logs | `data/raw/people-dna-land/` |
| Identity-matching experiments, genealogy workbench output, unresolved joins, notebooks, consent-review scratch, privacy-review scratch, or transform trials | `data/work/people-dna-land/` |
| Unresolved living-person data, disputed identity, unresolved consent or rights, unsafe joins, culturally sensitive context, or public-risk material | `data/quarantine/people-dna-land/` |
| Canonical processed People/DNA/Land coordination | `data/processed/people-dna-land/` |
| DNA-derived artifacts | Canonical or compatibility DNA lane after policy review; never collapse DNA into People assertions |
| Land instruments, ownership assertions, parcel versions, or title reasoning | People/DNA/Land land-ownership lane |
| Catalog, triplet, proof, receipt, source-registry, policy, consent, schema, validator, release, or published artifacts | Their governed responsibility roots |
| Identity adjudication, genealogy proof, public person search, background-check product, legal advice, medical/genetic advice, or title evidence | Deny or route to the proper governed authority |
| Credentials, consent secrets, redaction parameters, suppression thresholds, private endpoints, or unsafe logs | Approved secret and restricted operational systems |

## Inputs

Only governed WORK products or resolved QUARANTINE exits should enter this compatibility lane. As applicable, each candidate should resolve:

- stable candidate identity and content digest;
- source identity, source role, rights, and citation;
- assertion type and claim scope;
- subject resolution posture without asserting canonical identity;
- source, event, valid, retrieval, correction, and release times where material;
- consent, restriction, revocation, and tombstone state;
- living-person and sensitivity posture;
- transformation, aggregation, suppression, or de-identification context;
- validation references, evidence references, review state, correction path, and rollback target.

Inputs missing required consent, rights, source-role, privacy, or identity-scope support fail closed to WORK or QUARANTINE.

## Outputs

Permitted outputs are non-public candidates for:

- reconciliation with `data/processed/people-dna-land/people/` if that child convention is accepted;
- catalog/triplet preparation after evidence and policy closure;
- proof assembly and review packets;
- release-candidate evaluation after privacy, consent, rights, and sensitivity review;
- correction, withdrawal, tombstone, or migration workflows.

This path does not emit released public bytes or direct public responses.

## Assertion semantics

Person and genealogy objects remain assertion-first.

| Concept | Required boundary |
|---|---|
| Person assertion | Evidence-backed statement about a person; not canonical identity fact by directory placement alone. |
| Name assertion | A source-specific name statement; not automatic proof that two records describe the same person. |
| Life, residence, or migration event | Time- and source-bounded event assertion; uncertainty and conflicting evidence remain visible. |
| Genealogy relationship | Evidence-backed relationship assertion; not biological, legal, or social certainty without scoped support. |
| Relationship hypothesis | Explicit hypothesis or candidate; never silently promoted to fact. |
| Family group | Derived grouping with method and evidence scope; not a sovereign family identity. |
| Canonical person view | Derived, reviewable projection over assertions; not an immutable fact and not owned by this compatibility lane. |

Conflicting assertions must coexist with provenance and review state rather than being silently overwritten.

## Privacy, consent, and living-person controls

- Living-person status or uncertainty must be explicit where material.
- Living-person direct identifiers and private relationships default to deny or restricted handling.
- Consent must be scoped to purpose, subject, fields, audience, and duration where doctrine requires it.
- Consent is revocable; revocation must not be treated as a documentation-only change.
- Person-parcel, DNA-person, health, financial, contact, and private-family joins require explicit policy and specialist review.
- De-identification and aggregation do not automatically eliminate re-identification risk.
- Small groups, rare combinations, precise dates, precise locations, and linkage-rich records require re-identification review.
- Cultural, tribal, community, and sovereignty-sensitive records require appropriate authority and rights review.
- Synthetic AI summaries, entity-resolution scores, and model output are interpretive candidates, not evidence.

> [!CAUTION]
> Do not expose this directory as a public identity service, genealogy service, people search, background-check source, direct API, UI, download, Focus Mode answer, AI-answer source, or map layer.

## Validation

No complete lane-wide validator was verified. A pass proves only the check's declared scope.

At minimum, validation should cover:

- canonical-path and compatibility-lane classification;
- stable identity, version, and digest;
- source role, rights, citation, and provenance;
- assertion type and bounded claim scope;
- living-person, consent, restriction, revocation, and tombstone posture;
- duplicate, conflict, merge, split, and predecessor/successor handling;
- time semantics and correction lineage;
- de-identification, aggregation, suppression, and re-identification risk;
- cross-domain joins, especially DNA, land, health, contact, and parcel linkage;
- evidence resolution, review state, catalog readiness, release dependencies, and rollback target;
- direct-public-path and sensitive-content denial.

Negative fixtures should demonstrate rejection or hold for unresolved consent, direct identifiers, unsafe living-person detail, unsupported identity merges, genealogy-as-fact collapse, DNA or land-title collapse, and direct public exposure.

## Review burden

Accountable owners and enforcement remain **NEEDS VERIFICATION**. Material changes should include:

- People/DNA/Land domain review;
- privacy and living-person review;
- consent review;
- rights and sovereignty review where applicable;
- evidence and validation review;
- security/access-control review for restricted material;
- independent release review before any public representation.

CODEOWNERS routing, a test pass, or documentation approval is not consent or release evidence.

## Correction, revocation, and rollback

Corrections must preserve the original assertion, correction reason, supporting evidence, review state, affected derivatives, and successor identity where applicable.

Consent revocation or newly discovered privacy risk may require:

1. immediate hold or withdrawal;
2. tombstoning or restricted replacement;
3. downstream catalog, graph, index, cache, search, export, and AI-retrieval invalidation;
4. correction or withdrawal notices;
5. release supersession or rollback where public derivatives exist;
6. verification that stale copies are no longer served.

Documentation rollback target: restore blob `b0a8b76cbdf43ea0e76e16b7b1b3a944423ac943` or revert the modernization commit.

## Related folders

- Canonical processed parent: [`../people-dna-land/`](../people-dna-land/README.md)
- Compatibility DNA child: [`dna/`](dna/README.md)
- Processed parent contract: [`../../processed/`](../../processed/README.md)
- Domain doctrine: [`../../../docs/domains/people-dna-land/`](../../../docs/domains/people-dna-land/README.md)
- Lifecycle: [`../../raw/people-dna-land/`](../../raw/people-dna-land/) · [`../../work/people-dna-land/`](../../work/people-dna-land/) · [`../../quarantine/people-dna-land/`](../../quarantine/people-dna-land/) · [`../../catalog/domain/people-dna-land/`](../../catalog/domain/people-dna-land/) · [`../../published/`](../../published/)
- Trust support: [`../../proofs/`](../../proofs/) · [`../../receipts/`](../../receipts/) · [`../../registry/sources/people-dna-land/`](../../registry/sources/people-dna-land/)
- Authority: [`../../../contracts/domains/people-dna-land/`](../../../contracts/domains/people-dna-land/) · [`../../../schemas/contracts/v1/domains/people-dna-land/`](../../../schemas/contracts/v1/domains/people-dna-land/) · [`../../../policy/domains/people-dna-land/`](../../../policy/domains/people-dna-land/) · [`../../../release/candidates/people-dna-land/`](../../../release/candidates/people-dna-land/)

## ADRs

The `people` versus `people-dna-land` segment conflict remains unresolved in the inspected evidence. This README accepts no naming ADR and does not promote the compatibility path. An accepted ADR, migration inventory, alias policy, link plan, validation plan, correction plan, and rollback target are required before canonicalization, relocation, duplication, or retirement.

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Compatibility-path disposition | `NEEDS VERIFICATION` | Accepted ADR or documented migration decision |
| Recursive payload inventory | `UNKNOWN` | Pinned tree, payload families, LFS/external stores, owners, rights, sensitivity |
| Writers and consumers | `UNKNOWN` | Pipelines, tools, workflows, runtime, API/UI, search/index, export, and AI retrieval inventory |
| Contract/schema/policy enforcement | `UNKNOWN` | Accepted versions, fixtures, validators, CI, negative cases, consent decisions |
| Living-person and re-identification controls | `NEEDS VERIFICATION` | Access rules, field controls, join restrictions, privacy testing, audit evidence |
| Receipt/proof/catalog/release closure | `UNKNOWN` | Emitted instances, identity agreement, review, release, correction, and rollback links |
| Revocation and tombstone propagation | `NEEDS VERIFICATION` | Cleanup procedures, invalidation evidence, cache/index/search removal, drills |

Unknowns narrow claims and block higher-risk transitions; they do not invite plausible defaults.

## No-loss ledger

| Prior element | Disposition |
|---|---|
| Stable path and document identity | Preserved |
| Compatibility-only posture | Preserved and strengthened |
| Canonical `people-dna-land` coordination | Preserved |
| Assertion-first semantics | Preserved and expanded |
| Living-person, consent, privacy, evidence, release, correction, and rollback controls | Preserved and strengthened |
| DNA and land/title separation | Preserved |
| Prior rollback target | Replaced with the immediate prior blob for reversible documentation change |
| Payload, move, deletion, redirect, migration, release, or public-state change | None |

### Change history

#### v0.2.0 — 2026-07-25

- aligned the README with the current `data/processed/` authority contract;
- preserved compatibility-only status and canonical `people-dna-land` coordination;
- strengthened assertion semantics, living-person controls, consent revocation, correction, and rollback requirements;
- added validation, specialist review, ADR, verification, and no-loss sections;
- changed Markdown only.

[Back to top](#top)
