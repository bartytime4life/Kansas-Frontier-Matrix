<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-people-dna-readme
title: data/processed/people/dna/README.md — People DNA Compatibility Processed Data README
version: v0.2.0
type: readme; data-lifecycle-sublane; processed-stage-guide; compatibility-lane; people-dna-land-dna-sublane; restricted-dna-derivative-lane
status: repository-grounded draft; PROPOSED compatibility path; payload/runtime enforcement unverified
owners: NEEDS VERIFICATION — People/DNA/Land steward · DNA steward · Consent steward · Privacy reviewer · Rights steward · Sensitivity reviewer · Data steward · Evidence steward · Policy steward · Release steward · Docs steward
updated: 2026-07-25
supersedes: prior README at the same path; no payload, lifecycle, release, runtime, consent, or publication state
prepared_under_prompt: KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent v5.0.0
policy_label: restricted-review; compatibility-only; deny-by-default; no-direct-public-path; consent-bound; release-gated
tags: [kfm, data, processed, people, dna, people-dna-land, compatibility-path, privacy, consent, revocation, tombstone, re-identification, aggregate, k-anonymized, transformed-derivative, evidence, policy, correction, rollback]
related:
  - ../../people-dna-land/README.md
  - ../../../processed/README.md
  - ../../../../docs/domains/people-dna-land/README.md
  - ../../../../policy/domains/people-dna-land/
  - ../../../../policy/sensitivity/people-dna-land/
  - ../../../../policy/consent/people-dna-land/
  - ../../../../contracts/domains/people-dna-land/
  - ../../../../schemas/contracts/v1/domains/people-dna-land/
  - ../../../raw/people-dna-land/
  - ../../../work/people-dna-land/
  - ../../../quarantine/people-dna-land/
  - ../../../catalog/domain/people-dna-land/
  - ../../../triplets/
  - ../../../published/
  - ../../../proofs/
  - ../../../receipts/
  - ../../../registry/sources/people-dna-land/
  - ../../../../release/candidates/people-dna-land/
notes:
  - "This file preserves the existing `data/processed/people/dna/` path while aligning it to the current `data/processed/` authority contract."
  - "The canonical data-domain segment remains `people-dna-land`; this shorter path is compatibility-only unless an ADR explicitly changes the data-lifecycle segment."
  - "This lane may hold only processed, consent-bound, privacy-reviewed DNA derivatives or compatibility metadata. It must never contain raw DNA, segment-level data, vendor identifiers, private match tables, triangulation outputs, living-person linkage, consent secrets, or public payloads."
  - "Consent revocation, legal restriction, source withdrawal, correction, or privacy failure requires downstream tombstoning, derivative invalidation, cache cleanup, and rollback where applicable."
  - "Prior blob and rollback target: dc527e94dc6f201a99786d3101c6dd3a05cb5e05."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/processed/people/dna/` — Restricted DNA Compatibility Candidates

> **One-line purpose.** Preserve a bounded compatibility lane for processed, consent-bound, privacy-reviewed DNA derivatives without creating a second People/DNA/Land authority, a public lookup surface, or a bypass around the canonical `people-dna-land` lifecycle segment.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status)
[![Lane: compatibility only](https://img.shields.io/badge/lane-compatibility%20only-d97706?style=flat-square)](#authority-level)
[![Sensitivity: deny by default](https://img.shields.io/badge/sensitivity-deny%20by%20default-d1242f?style=flat-square)](#privacy-consent-and-re-identification)
[![Exposure: non-public](https://img.shields.io/badge/exposure-non--public-8250df?style=flat-square)](#outputs)

> [!IMPORTANT]
> Directory placement, de-identification, aggregation, a successful check, a pull request, or a merge does not create consent, truth, evidence closure, policy permission, catalog admission, release approval, or KFM publication.

> [!CAUTION]
> Raw DNA, segment-level data, vendor account identifiers, private match tables, triangulation outputs, living-person linkage, consent secrets, and re-identification-enabling metadata do not belong in this lane. Unknown or disputed material fails closed to quarantine or approved restricted systems.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Privacy](#privacy-consent-and-re-identification) · [Revocation](#revocation-correction-and-tombstoning) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

`data/processed/people/dna/` is an existing **compatibility path** under the PROCESSED lifecycle stage. It may describe or hold only bounded DNA-derived candidates that have passed applicable WORK checks and privacy/consent review but have not thereby become cataloged, released, public, or authoritative identity conclusions.

The current canonical parent coordination path is:

```text
data/processed/people-dna-land/
```

This README therefore acts as a containment and migration boundary. It does not establish `people/dna` as a second canonical domain segment.

## Authority level

**PROPOSED compatibility responsibility; non-public and deny-by-default.**

This path may own only lane-local compatibility metadata and policy-admitted processed derivatives. It does not own:

- domain identity or canonical segment selection;
- object meaning or machine shape;
- consent or policy authority;
- EvidenceBundle or proof closure;
- catalog, triplet, release, or publication decisions;
- public API, UI, map, download, Focus Mode, AI-answer, identity, genealogy, or medical interpretation behavior.

Those responsibilities remain under their governed roots and interfaces.

## Status

| Field | Bounded result |
|---|---|
| Path | `data/processed/people/dna/` |
| Version | `v0.2.0` |
| Lifecycle role | `PROCESSED` compatibility lane |
| Canonical data-domain segment | `people-dna-land` unless an accepted ADR changes it |
| Prior blob | `dc527e94dc6f201a99786d3101c6dd3a05cb5e05` |
| Recursive payload inventory | `UNKNOWN` |
| Active writers and consumers | `UNKNOWN` |
| Consent-policy enforcement | `NEEDS VERIFICATION` |
| Public readiness | `DENY BY DEFAULT` |

**CONFIRMED:** the target path exists; `data/processed/people-dna-land/` exists as the current parent lane; People/DNA/Land doctrine treats living-person fields, raw DNA, private person-parcel joins, and DNA-derived hypotheses as deny-by-default; consent is revocable; raw DNA and vendor segment data do not cross the public boundary.

**PROPOSED:** this shorter path remains compatibility-only and may hold restricted derivatives or migration/disposition metadata.

**UNKNOWN / NEEDS VERIFICATION:** recursive contents, accepted ADR disposition, accountable owners, contracts, schemas, validators, fixtures, CI enforcement, access controls, receipts, EvidenceBundles, policy decisions, release linkage, downstream consumers, erasure drills, and cache invalidation.

## What belongs here

Subject to consent, rights, privacy, policy, and access review, bounded contents may include:

- aggregate or k-anonymized DNA-derived summaries that do not expose raw segments or living-person identity;
- consent-reviewed DNA evidence summaries with explicit claim scope and restriction state;
- transformed derivatives whose source detail and re-identification risk have been reviewed;
- compatibility aliases, migration maps, or disposition inventories that point to canonical `people-dna-land` records without duplicating truth;
- restriction, revocation, tombstone, correction, and withdrawal support metadata when it is not itself the authoritative consent or receipt record;
- review-ready linkage metadata that preserves source role, EvidenceRef, consent posture, restriction posture, transform lineage, and correction state;
- lane-local README, inventory, digest, and limitation sidecars that explain the boundary without becoming public outputs or authority records.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| Raw DNA files, BAM/VCF-like source data, segment-level data, vendor exports, source-native reports, account or kit identifiers | `data/raw/people-dna-land/` or approved restricted source systems; never public repository paths when prohibited |
| Private match tables, triangulation outputs, kinship candidate matrices, living-person DNA linkage, or re-identification features | `data/quarantine/people-dna-land/` or approved restricted review systems |
| In-process transforms, consent review scratch, redaction experiments, notebooks, unresolved joins, or privacy testing | `data/work/people-dna-land/` |
| Unresolved consent, rights, sovereignty, source-role, privacy, sensitivity, or withdrawal state | `data/quarantine/people-dna-land/` |
| Consent authority, revocation decisions, policy rules, proofs, receipts, source registry records, schemas, validators, tests, fixtures, release decisions | Their canonical responsibility roots |
| Identity adjudication, genealogy proof, medical or genetic advice, title or property claims, public DNA lookup, person-search products | Deny or route to separately governed, evidence-bounded processes |
| Credentials, consent secrets, transform secrets, suppression thresholds, exact linkage keys, private endpoints, or access-control material | Approved secret or restricted operational systems |
| Direct public API/UI/map/download/AI payloads | Governed released interfaces only after explicit authorization |

## Inputs

Inputs must originate from governed WORK products or resolved QUARANTINE exits and, where applicable, resolve:

- stable artifact identity and content digest;
- source identity, source role, rights, sovereignty, and restriction posture;
- scoped and revocable consent state;
- living-person status and sensitivity tier;
- transformation method and privacy objective;
- aggregation, suppression, k-anonymity, or other disclosure-control posture;
- re-identification risk review;
- temporal scope, correction state, and withdrawal state;
- contract/schema references where accepted;
- validation, transform, consent, redaction, policy, review, and access receipts;
- downstream EvidenceRef/EvidenceBundle support;
- correction, tombstone, invalidation, and rollback targets.

An input with missing consent, unresolved rights, unknown living-person linkage, raw segment detail, unresolved re-identification risk, or ambiguous withdrawal state fails closed.

## Outputs

Permitted outputs are non-public candidates for:

- canonical processed placement under `data/processed/people-dna-land/dna/` if that sublane is accepted;
- catalog or triplet review under the canonical People/DNA/Land segment;
- EvidenceBundle assembly;
- restricted analytical review;
- release-candidate review for highly aggregated, policy-safe representations only;
- correction, tombstone, withdrawal, and rollback processing.

This lane must not be read directly by public clients, map renderers, search interfaces, Focus Mode, AI answer generation, exports, or downloads.

## Privacy, consent, and re-identification

| Control | Required posture |
|---|---|
| Living-person data | Deny or restrict by default; public exposure requires explicit authority and narrowly scoped consent where allowed. |
| Raw DNA and segment data | Prohibited from public promotion and prohibited from this processed compatibility lane. |
| Consent | Scoped, recorded, revocable, and linked to the specific derivative and use. Absence or ambiguity means deny. |
| Rights and sovereignty | Source rights, community or tribal interests, cultural sensitivity, and jurisdictional limits must be reviewed independently of technical validity. |
| Re-identification | Review combination risk, small groups, rare attributes, family linkage, geographic linkage, and auxiliary-data joins. |
| Aggregation | Aggregation alone is not safety proof. Group size, uniqueness, sparsity, and disclosure risk must be reviewed. |
| k-anonymization or suppression | Treat as one transform among several, not a blanket authorization. Parameters and fitness must be reviewed without exposing attack-enabling details. |
| Source role | Observed, administrative, modeled, aggregate, candidate, and synthetic material must remain distinguishable. |
| AI-generated summaries | Synthetic language is not evidence and may not infer identity, kinship, health, ancestry, title, or consent. |

> [!WARNING]
> DNA can identify relatives and communities even when direct names are removed. De-identification claims must account for linkage and inference risk, not only obvious identifiers.

## Revocation, correction, and tombstoning

Consent revocation, legal restriction, source withdrawal, corrected identity evidence, privacy failure, or newly discovered re-identification risk must trigger a governed response rather than a silent edit.

Minimum expected actions, subject to accepted policy and implementation evidence:

1. Record the revocation, withdrawal, correction, or privacy finding in the authoritative policy/receipt system.
2. Identify all derived artifacts, catalogs, triplets, indexes, caches, releases, exports, and AI/vector representations that depend on the affected material.
3. Hold or deny further use immediately where risk warrants.
4. Tombstone, supersede, redact, or delete derivatives according to policy, rights, retention, and legal requirements.
5. Invalidate caches and derived indexes where applicable.
6. Issue correction or withdrawal records for any released representation.
7. Verify rollback or cleanup completion through auditable receipts.

This README does not claim that these mechanisms are currently implemented; enforcement remains **NEEDS VERIFICATION**.

## Validation

Validate at least:

- path classification and compatibility status;
- absence of raw DNA, segment-level data, vendor identifiers, private match tables, and consent secrets;
- identity, digest, source role, rights, sovereignty, and lineage;
- consent scope, revocation, expiry, restriction, and tombstone state;
- living-person and family-linkage sensitivity;
- re-identification and auxiliary-data join risk;
- transform lineage and limitation disclosure;
- aggregation and suppression fitness;
- contract/schema references and negative fixtures where accepted;
- validation, consent, redaction, policy, review, access, correction, and release receipts;
- EvidenceRef/EvidenceBundle resolution for consequential claims;
- downstream cleanup and rollback dependencies;
- links, anchors, metadata, and accidental sensitive-content exposure.

No complete lane-wide validator or runtime enforcement was verified. A pass proves only the declared scope of the specific check.

## Review burden

Accountable ownership remains **NEEDS VERIFICATION**. Changes involving payloads, consent, living persons, raw or derived DNA, family linkage, community or tribal sensitivity, rights, migration, public serving, correction, deletion, or rollback require specialist review appropriate to the risk.

At minimum, higher-risk changes should involve independent privacy, consent, rights, domain, evidence, and release review. CODEOWNERS routing or author approval is not evidence of consent or release authorization.

## Related folders

- Canonical processed parent: [`../../people-dna-land/README.md`](../../people-dna-land/README.md)
- Parent PROCESSED contract: [`../../../processed/README.md`](../../../processed/README.md)
- Domain doctrine: [`../../../../docs/domains/people-dna-land/README.md`](../../../../docs/domains/people-dna-land/README.md)
- Lifecycle inputs: [`../../../raw/people-dna-land/`](../../../raw/people-dna-land/) · [`../../../work/people-dna-land/`](../../../work/people-dna-land/) · [`../../../quarantine/people-dna-land/`](../../../quarantine/people-dna-land/)
- Downstream: [`../../../catalog/domain/people-dna-land/`](../../../catalog/domain/people-dna-land/) · [`../../../triplets/`](../../../triplets/) · [`../../../published/`](../../../published/)
- Trust support: [`../../../proofs/`](../../../proofs/) · [`../../../receipts/`](../../../receipts/) · [`../../../registry/sources/people-dna-land/`](../../../registry/sources/people-dna-land/)
- Authority: [`../../../../policy/domains/people-dna-land/`](../../../../policy/domains/people-dna-land/) · [`../../../../policy/sensitivity/people-dna-land/`](../../../../policy/sensitivity/people-dna-land/) · [`../../../../policy/consent/people-dna-land/`](../../../../policy/consent/people-dna-land/) · [`../../../../release/candidates/people-dna-land/`](../../../../release/candidates/people-dna-land/)

## ADRs

The unresolved `people` versus `people-dna-land` segment conflict is ADR-class. This README resolves nothing by repetition or path existence. Before promoting this compatibility path, moving payloads, creating redirects, or authoring parallel schema/contract/policy homes, require:

- an accepted ADR identifying the canonical segment and migration posture;
- an inventory of affected paths, writers, consumers, links, catalogs, receipts, proofs, and releases;
- a reversible migration plan;
- privacy, consent, and rights review;
- validation and rollback evidence.

Until then, `data/processed/people-dna-land/` remains the canonical coordination path and this lane remains compatibility-only.

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Compatibility-lane disposition | `NEEDS VERIFICATION` | Accepted ADR, migration record, or explicit stewardship decision |
| Recursive subtree and payload inventory | `UNKNOWN` | Pinned tree, LFS/external stores, artifact classes, sensitivity review |
| Writers and consumers | `UNKNOWN` | Pipelines, tools, APIs, UI, exports, vector indexes, caches, external consumers |
| Consent and revocation enforcement | `NEEDS VERIFICATION` | Policy bundle, fixtures, negative tests, emitted decisions, cleanup drill |
| Contract/schema enforcement | `UNKNOWN` | Accepted versions, validators, fixtures, CI and failure cases |
| Re-identification review | `NEEDS VERIFICATION` | Review method, thresholds, auxiliary-data analysis, sign-off |
| Evidence/catalog/release closure | `UNKNOWN` | EvidenceBundles, identity parity, review, release and rollback links |
| Tombstone and downstream invalidation | `NEEDS VERIFICATION` | Dependency inventory, receipts, cache/index cleanup, rollback drill |
| Public serving | `UNKNOWN` | Governed routes, access controls, release state, monitoring and withdrawal behavior |

Unknowns narrow claims and block higher-risk transitions; they do not invite plausible defaults.

## No-loss ledger

| Prior element | Disposition |
|---|---|
| Stable path and document identity | Preserved |
| Compatibility-only classification | Preserved and strengthened |
| Canonical `people-dna-land` coordination path | Preserved |
| Deny-by-default privacy and consent posture | Preserved and strengthened |
| Raw-DNA and direct-identifier exclusions | Preserved and expanded |
| Evidence, policy, review, release, correction, and rollback boundaries | Preserved |
| Revocation and tombstone duties | Preserved and made operationally explicit |
| Prior blob and rollback target | Recorded |
| Payload, move, deletion, redirect, migration, consent, or public-state change | None |

### Change history

#### v0.2.0 — 2026-07-25

- aligned the compatibility README to the current `data/processed/` authority contract;
- strengthened raw-DNA, living-person, consent, revocation, re-identification, sovereignty, correction, and rollback controls;
- preserved the unresolved segment conflict and avoided creating parallel authority;
- changed Markdown only.

[Back to top](#top)
