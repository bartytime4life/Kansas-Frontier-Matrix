<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-proofs-citation-validation-readme
title: data/proofs/citation_validation/README.md — Citation Validation Proof Family
version: v0.2
status: repository-grounded draft; payload/runtime enforcement unverified
owners: NEEDS VERIFICATION — evidence, citation-validation, proof, policy, release, domain, and UI/Evidence Drawer stewards
updated: 2026-07-25
policy_label: restricted-review; no-direct-public-path; release-gated
current_path: data/proofs/citation_validation/README.md
truth_posture: CONFIRMED exact path, canonical parent proof contract, and present Atmosphere/Flora child READMEs / PROPOSED normalized citation-validation operating contract / UNKNOWN recursive records, active writers and consumers, resolver runtime, routes, caches, and release state / NEEDS VERIFICATION accepted profiles, schemas, validators, fixtures, CI, retention, correction propagation, invalidation, and rollback drills
related:
  - ../README.md
  - atmosphere/README.md
  - flora/README.md
  - ../atmosphere/README.md
  - ../atmosphere/pm25_2026/README.md
  - ../flora/README.md
  - ../../catalog/domain/
  - ../../processed/
  - ../../receipts/
  - ../../registry/sources/
  - ../../triplets/
  - ../../published/
  - ../../../contracts/
  - ../../../schemas/
  - ../../../policy/
  - ../../../release/
  - ../../../docs/architecture/ui/EVIDENCE_DRAWER.md
  - ../../../docs/architecture/evidence-drawer.md
  - ../../../docs/architecture/governed-ai/BOUNDARIES.md
notes:
  - "Citation validation is proof support, not factual truth, EvidenceBundle authority, policy approval, release authority, or public serving."
  - "EvidenceRef resolution must end in a finite result; missing, stale, conflicting, role-incompatible, restricted, superseded, withdrawn, or unreleased support must not be completed by plausible generation."
  - "Receipts, source registry records, EvidenceBundles, catalog records, policy decisions, release records, corrections, withdrawals, and rollback cards remain in their own governed homes."
  - "Rollback target for this modernization is prior blob SHA 8964f5cb9ea517a6ba881aa1a606983b18f5d76d."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/proofs/citation_validation/` — Citation Validation Proof Support

> Validate that a claim’s citations and `EvidenceRef` dependencies resolve to compatible, current, governed evidence before the claim can proceed to review, release, an Evidence Drawer, or another governed answer surface.

<p>
  <img alt="Status: grounded draft" src="https://img.shields.io/badge/status-grounded__draft-yellow">
  <img alt="Authority: proof support" src="https://img.shields.io/badge/authority-proof__support-blue">
  <img alt="Posture: cite or abstain" src="https://img.shields.io/badge/posture-cite--or--abstain-green">
  <img alt="Exposure: no direct public path" src="https://img.shields.io/badge/exposure-no__direct__public__path-critical">
</p>

> [!IMPORTANT]
> A citation-validation record can show whether declared dependencies resolved under a stated profile. It does **not** make the claim true, create an `EvidenceBundle`, grant rights, decide sensitivity, approve policy, authorize release, or publish anything.

> [!CAUTION]
> Missing or incompatible support must produce a finite governed outcome such as `ABSTAIN`, `HOLD`, `RESTRICT`, `DENY`, or `ERROR`. Do not replace failed resolution with guessed citations, generated rationale, or silent fallback to internal stores.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Operating contract](#operating-contract) · [Children](#current-bounded-child-lane-index) · [Correction](#correction-withdrawal-and-rollback) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

`data/proofs/citation_validation/` is the proof-family lane for citation-resolution results. It supports inspection of whether a claim, catalog row, triplet, release candidate, Evidence Drawer payload, or governed answer has compatible and resolvable evidence dependencies.

Citation validation should answer bounded questions such as:

- Does each declared `EvidenceRef` resolve through the governed resolver to the intended `EvidenceBundle` or accepted proof packet?
- Does the resolved evidence support the exact claim identity, domain object, geography, time, variable, units, source role, and confidence posture being asserted?
- Are rights, sensitivity, caveats, policy/review, release, correction, withdrawal, and rollback dependencies present and compatible?
- Is the support current, non-conflicting, non-superseded, and non-withdrawn for the decision being made?

## Authority level

**Canonical citation-validation proof-family responsibility under `data/proofs/`.**

This lane owns citation-validation support records and indexes under accepted profiles. It does not own:

- source or processed domain data;
- canonical EvidenceBundle content;
- semantic contracts or schemas;
- receipts or source registry truth;
- policy, sensitivity, access, or stewardship decisions;
- catalog or triplet authority;
- release, correction, withdrawal, or rollback authority;
- public routes, API/UI payload authority, or factual truth.

## Status

| Field | Bounded result |
|---|---|
| Path | `data/proofs/citation_validation/` |
| Version | `v0.2` |
| Prior blob | `8964f5cb9ea517a6ba881aa1a606983b18f5d76d` |
| Canonical parent | `data/proofs/README.md` — confirmed present and normalized |
| Confirmed child READMEs | `atmosphere/README.md`; `flora/README.md` |
| Recursive record inventory | `UNKNOWN` |
| Active writers/consumers | `UNKNOWN` |
| Resolver/runtime enforcement | `UNKNOWN` |
| Direct public readiness | `DENY BY DEFAULT` |

## What belongs here

Citation-validation proof material may include:

- citation-closure results under a named and versioned validation profile;
- claim-to-`EvidenceRef` maps and resolution summaries;
- digest, version, identity, and dependency agreement checks;
- source-role, rights, sensitivity, spatial/temporal scope, units, caveat, freshness, policy/review, and release compatibility results;
- negative-state records explaining `ABSTAIN`, `HOLD`, `RESTRICT`, `DENY`, or `ERROR`;
- correction, supersession, withdrawal, invalidation, and rollback dependency summaries;
- domain child-lane indexes and limitations;
- README, inventory, migration, or disposition sidecars that do not create parallel authority.

A record should be immutable or versioned once relied upon, with a replacement or supersession link rather than silent mutation.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads | Their governed lifecycle lanes |
| Canonical `EvidenceBundle` records or proof packets | Accepted evidence/proof profile homes under `data/proofs/` |
| Run, transform, validation, redaction, aggregation, policy, review, or publication receipts as primary records | `data/receipts/` or accepted receipt homes |
| Source descriptors or source-admission decisions | `data/registry/sources/` |
| Contracts, schemas, policy, or release decisions | `contracts/`, `schemas/`, `policy/`, `release/` |
| Correction notices, withdrawals, promotion decisions, or rollback cards as authority records | `release/` or accepted correction/rollback authority homes |
| Public map/API/UI payloads, answer text, alerts, medical/legal guidance, or generated claims | Governed delivery and answer surfaces after release |
| Secrets, private endpoints, harmful-precision data, protected geometry, or unsafe logs | Approved restricted storage and access-controlled systems |

## Inputs

Inputs may include:

- claim identity and version;
- `EvidenceRef` identifiers and expected evidence profile;
- admitted source and source-role references;
- processed, catalog, and triplet identities and digests;
- contracts and schema versions;
- validation, citation, transform, model, aggregation, redaction, and review receipts;
- rights, sensitivity, policy, and access decisions;
- release, correction, supersession, withdrawal, and rollback references;
- the requested answer or delivery context.

Inputs must remain references to their governing records. This lane must not duplicate protected content merely to validate it.

## Outputs

A citation-validation result should identify:

- the claim or artifact evaluated;
- the validation profile and version;
- each `EvidenceRef` and resolution result;
- resolved evidence identity and digest where disclosure is allowed;
- compatibility findings for source role, claim scope, space/time, units, rights, sensitivity, caveats, policy/review, and release;
- stale, conflict, supersession, withdrawal, or invalidation findings;
- a finite outcome and stable finding codes;
- limitations, unresolved dependencies, correction linkage, and rollback dependency.

Outputs support review and governed resolution. They are not themselves public claims or release approvals.

## Validation

At minimum, a citation-validation profile should test:

1. placement, metadata, stable identity, version, and digest;
2. claim-to-citation completeness and duplicate/alias handling;
3. governed `EvidenceRef` resolution without bypassing access controls;
4. expected-versus-resolved evidence profile and domain ownership;
5. source-role compatibility and anti-collapse rules;
6. geography, time, variable, units, method, confidence, and caveat scope;
7. rights, sensitivity, redaction/generalization, and disclosure compatibility;
8. contract/schema and catalog/triplet identity agreement;
9. receipt, policy, review, release, correction, withdrawal, and rollback dependencies;
10. stale, conflict, supersession, withdrawal, and invalidation propagation;
11. no secret, protected, harmful-precision, or internal-only content leakage;
12. deterministic finite outcomes and stable finding identifiers.

No complete family-wide validator, schema, fixture suite, or CI enforcement was verified. A pass proves only the declared profile and evidence snapshot.

## Review burden

Accountable ownership remains **NEEDS VERIFICATION**.

Changes should involve evidence, citation-validation, proof, policy, release, and affected domain stewards. UI/Evidence Drawer review is required when record shape or projections change. Independent rights/sensitivity review is required when protected content, living-person data, cultural material, precise infrastructure, ecology, archaeology, or other harmful-precision evidence could be exposed.

CODEOWNERS assignment, automated checks, or schema validity do not substitute for approval evidence.

## Related folders

- Parent proof contract: [`../README.md`](../README.md)
- Confirmed children: [`atmosphere/`](atmosphere/README.md) · [`flora/`](flora/README.md)
- Domain proofs: [`../atmosphere/`](../atmosphere/README.md) · [`../flora/`](../flora/README.md)
- Lifecycle context: [`../../processed/`](../../processed/README.md) · [`../../catalog/`](../../catalog/README.md) · [`../../triplets/`](../../triplets/README.md) · [`../../published/`](../../published/README.md)
- Trust support: [`../../receipts/`](../../receipts/README.md) · [`../../registry/`](../../registry/README.md)
- Authority: [`../../../contracts/`](../../../contracts/README.md) · [`../../../schemas/`](../../../schemas/README.md) · [`../../../policy/`](../../../policy/README.md) · [`../../../release/`](../../../release/README.md)
- UI doctrine: [`../../../docs/architecture/ui/EVIDENCE_DRAWER.md`](../../../docs/architecture/ui/EVIDENCE_DRAWER.md) · [`../../../docs/architecture/evidence-drawer.md`](../../../docs/architecture/evidence-drawer.md)

## ADRs

Relevant proposed decisions include receipt/proof/catalog/release separation, connector-output boundaries, public-client trust-membrane rules, EvidenceBundle profile authority, and correction/rollback propagation. This README accepts none by implication.

An accepted ADR plus migration, compatibility, validation, and rollback plan is required before this lane becomes an EvidenceBundle store, receipt store, policy engine, release authority, public service, or replacement for domain proof lanes.

## Last reviewed

- **Date:** 2026-07-25
- **Evidence inspected:** exact target README, canonical `data/proofs/README.md`, and the present Atmosphere child README
- **Recursive payload/runtime inspection:** not performed
- **Owners, accepted profiles, retention, deployed resolver behavior, correction propagation, and rollback drills:** need verification

Re-review when evidence profiles, resolver behavior, domain child lanes, policy, release, public consumers, correction handling, or rollback dependencies change—or within six months.

## Operating contract

For each evaluated claim or artifact:

1. identify the claim and expected evidence profile;
2. resolve every declared `EvidenceRef` through the governed resolver;
3. verify evidence identity, integrity, source role, scope, rights, sensitivity, caveats, policy/review, and release compatibility;
4. check stale, conflict, supersession, correction, withdrawal, and rollback dependencies;
5. emit a deterministic finite result with limitations;
6. allow downstream use only through the appropriate governed interface and current release state.

Missing support narrows or blocks the claim. It never authorizes plausible completion.

## Current bounded child-lane index

| Child lane | Evidence-backed status | Hard boundary |
|---|---|---|
| [`atmosphere/`](atmosphere/README.md) | `CONFIRMED` README present; payloads, validators, resolver, and runtime remain unverified | Not AQI advisory, regulatory, medical, emergency, or public-output authority |
| [`flora/`](flora/README.md) | `CONFIRMED` README present; payloads, validators, resolver, and runtime remain unverified | Not rare-plant discovery, exact-location disclosure, or stewardship authority |
| Other domain child lanes | `PROPOSED / NEEDS VERIFICATION` | Do not infer a lane from this index or create it without Directory Rules and domain evidence |

Omission from this bounded index is not retirement, deletion, or proof that another lane does not exist.

## Correction, withdrawal, and rollback

When a source, EvidenceBundle, claim, receipt, policy decision, review, catalog record, triplet, release, or correction dependency changes:

- identify affected validation records and downstream claims;
- mark prior results stale, superseded, invalid, or withdrawn as appropriate;
- preserve the prior record and reason;
- rerun the accepted profile against the new evidence snapshot;
- propagate the finite outcome to review, release, governed routes, caches, and Evidence Drawer projections where implemented;
- retain a rollback target and verify that rollback does not reactivate withdrawn or unsafe support.

This section defines expected governance. Correction propagation, cache invalidation, and rollback drills remain **NEEDS VERIFICATION**.

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Recursive record inventory | `NEEDS VERIFICATION` | Pinned tree, record families, external stores, owners, retention, rights/sensitivity |
| Writers and consumers | `UNKNOWN` | Pipelines, validators, resolvers, API/UI, Evidence Drawer, workflows, deployed consumers |
| Profiles and machine enforcement | `UNKNOWN` | Accepted schemas, fixtures, validators, negative cases, CI, stable finding codes |
| Evidence/receipt/catalog/release closure | `UNKNOWN` | Emitted instances, digest and identity agreement, policy/review and release links |
| Correction and withdrawal propagation | `UNKNOWN` | Dependency index, stale marking, invalidation, route/cache propagation, drills |
| Public serving | `DENY BY DEFAULT` | Governed resolver and release-resolved projection evidence |

Unknowns narrow claims and block higher-risk transitions; they do not invite plausible defaults.

## No-loss ledger

| Prior element | Disposition |
|---|---|
| Stable path and document identity | Preserved |
| Parent citation-validation proof-family role | Preserved and aligned to the canonical proof contract |
| `EvidenceRef` → `EvidenceBundle` resolution purpose | Preserved and strengthened |
| Finite negative outcomes | Preserved and expanded to include restriction, stale, conflict, supersession, withdrawal, and invalidation |
| Confirmed Atmosphere and Flora child lanes | Preserved as bounded, evidence-backed entries |
| Proposed domain child concepts | Collapsed to a bounded verification statement; not retired |
| Source-role, rights, sensitivity, caveat, release, correction, and rollback controls | Preserved and strengthened |
| Payload, schema, validator, workflow, route, runtime, release, or public-state change | None |
| Documentation rollback target | Prior blob `8964f5cb9ea517a6ba881aa1a606983b18f5d76d` |

### Change history

#### v0.2 — 2026-07-25

- normalized the parent lane to the current proofs authority model;
- bounded child-lane claims to evidence verified in this pass;
- strengthened resolver, finite-outcome, correction, withdrawal, invalidation, and no-direct-public-path controls;
- changed Markdown only.

[Back to top](#top)
