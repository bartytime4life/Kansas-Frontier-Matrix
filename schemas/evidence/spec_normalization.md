# Spec Normalization — Legacy Evidence Compatibility Pointer

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-evidence-spec-normalization
title: Spec Normalization — Legacy Evidence Compatibility Pointer
type: compatibility-note; migration-guardrail; lineage-pointer; schema-boundary
authority_class: non-authoritative-compatibility
version: v0.2
status: draft; PROPOSED; root-level-compatibility-path; CONFLICTED placement; NEEDS VERIFICATION before retirement
owners:
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Identity steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — short scaffold existed before v0.2 replacement
updated: 2026-07-22
policy_label: public
tags: [kfm, schemas, evidence, compatibility, migration, spec-normalization, deterministic-identity, no-parallel-authority]
related:
  - ./README.md
  - ../README.md
  - ../contracts/v1/evidence/README.md
  - ../contracts/v1/evidence/spec_normalization.md
  - ../contracts/v1/common/spec_hash.schema.json
  - ../../contracts/evidence/README.md
  - ../../policy/evidence/README.md
  - ../../fixtures/contracts/v1/evidence/README.md
  - ../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../docs/adr/ADR-0013-spec_hash-and-run_id-identity-grammar.md
  - ../../docs/domains/agriculture/IDENTITY_MODEL.md
  - ../../docs/domains/fauna/IDENTITY_MODEL.md
  - ../../docs/domains/geology/IDENTITY_MODEL.md
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../docs/registers/VERIFICATION_BACKLOG.md
notes:
  - "This document replaces a short PROPOSED scaffold with an explicit compatibility and migration pointer."
  - "It does not define, copy, or override the proposed normalization profile under schemas/contracts/v1/evidence/."
  - "The legacy path remains visible because at least one inspected domain identity document names it directly."
  - "No schema, contract, fixture, validator, policy, evidence record, receipt, proof, release state, or publication behavior is changed by this document."
[/KFM_META_BLOCK_V2] -->

This file preserves the legacy path `schemas/evidence/spec_normalization.md` without allowing it to become a second normalization authority.

**Current role:** compatibility, lineage, and migration guidance only  
**Active authoring route:** [`schemas/contracts/v1/evidence/spec_normalization.md`](../contracts/v1/evidence/spec_normalization.md)  
**Schema-family index:** [`schemas/contracts/v1/evidence/README.md`](../contracts/v1/evidence/README.md)  
**Truth posture:** CONFIRMED path and inspected repository relationships; PROPOSED normalization profile; CONFLICTED hash grammar and EvidenceBundle naming; NEEDS VERIFICATION for ownership, implementation parity, incoming-reference closure, and retirement.

> [!IMPORTANT]
> Do not implement normalization behavior from this file. Do not expand it into a competing profile. Active evidence-family normalization work belongs in the versioned evidence schema family and remains subject to accepted ADRs, paired contracts, fixtures, validators, tests, policy, review, and release controls.

## Quick navigation

[Status](#status-and-authority) · [Purpose](#purpose) · [Routing](#canonical-routing) · [Lineage](#legacy-lineage) · [Compatibility](#compatibility-contract) · [Conflicts](#open-conflicts) · [Migration](#migration-and-retirement-gates) · [Validation](#validation-and-acceptance) · [Evidence](#evidence-ledger) · [Rollback](#correction-and-rollback)

## Status and authority

| Surface | Current repository evidence | Safe conclusion |
|---|---|---|
| `schemas/evidence/spec_normalization.md` | CONFIRMED legacy root-level scaffold, now represented by this compatibility note | Preserve as a pointer while verified incoming references or migration needs remain; do not treat as normative. |
| `schemas/evidence/README.md` | CONFIRMED compatibility and migration guardrail | This root-level evidence lane is non-authoritative and must not become a parallel schema family. |
| `schemas/contracts/v1/evidence/spec_normalization.md` | CONFIRMED richer evidence-family note marked `PROPOSED` | This is the active authoring route for normalization guidance, but it is not yet an accepted hashing implementation. |
| `schemas/contracts/v1/evidence/README.md` | CONFIRMED versioned evidence-family index | Use it to navigate current evidence machine-shape work. |
| Directory Rules | CONFIRMED `schemas/` owns machine-checkable shape and names `schemas/contracts/v1/...` as the default schema home | A second root-level evidence authority would violate the no-parallel-home rule. |
| ADR-0001 | CONFIRMED file, status `proposed` | It proposes the versioned schema home; do not describe it as accepted. |
| ADR-0013 | CONFIRMED file, status `proposed` | It proposes deterministic identity and `jcs:sha256:<hex>`; current schema parity is unresolved. |
| `common/spec_hash.schema.json` | CONFIRMED `PROPOSED` schema accepting `sha256:<64-lower-hex>` | Its accepted form conflicts with ADR-0013's proposed `jcs:sha256:<64-lower-hex>` grammar. |
| EvidenceBundle schemas | CONFIRMED underscore and hyphen filename variants with materially different shapes | Canonical naming and compatibility treatment remain unresolved; do not normalize the conflict away in prose. |

### Truth labels

- **CONFIRMED** — directly inspected in the repository snapshot used for this revision.
- **PROPOSED** — a design, profile, path decision, or behavior not established as accepted implementation.
- **CONFLICTED** — inspected sources or machine shapes disagree and require explicit resolution.
- **UNKNOWN** — available evidence is insufficient for a bounded claim.
- **NEEDS VERIFICATION** — a specific check remains open before implementation, promotion, migration, or retirement.

## Purpose

This document has four bounded jobs:

1. keep a legacy path resolvable for older domain documentation and inventories;
2. route maintainers to the versioned evidence-family normalization note;
3. prevent duplicate normalization, canonicalization, hashing, or `$id` rules from evolving here;
4. record the checks required to migrate or retire the path without breaking references or losing lineage.

This document does **not** define canonical JSON, transient-field exclusions, hash algorithms, hash string forms, derived identifiers, schema fields, runtime outcomes, or release behavior. It does not validate an EvidenceRef, resolve an EvidenceBundle, establish claim sufficiency, clear rights or sensitivity, emit a receipt, approve promotion, or authorize publication.

## Canonical routing

| Need | Use | Do not use this file to |
|---|---|---|
| Evidence-family normalization guidance | [`../contracts/v1/evidence/spec_normalization.md`](../contracts/v1/evidence/spec_normalization.md) | Maintain a copied or divergent profile. |
| Evidence schema-family inventory | [`../contracts/v1/evidence/README.md`](../contracts/v1/evidence/README.md) | Invent another family index. |
| Current `spec_hash` machine shape | [`../contracts/v1/common/spec_hash.schema.json`](../contracts/v1/common/spec_hash.schema.json) | Pretend the ADR/schema grammar conflict is resolved. |
| Schema-home placement decision | [`ADR-0001`](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) and Directory Rules | Promote a compatibility path into authority. |
| Proposed identity grammar | [`ADR-0013`](../../docs/adr/ADR-0013-spec_hash-and-run_id-identity-grammar.md) | Claim proposed JCS behavior is the current executable contract. |
| Evidence object meaning | [`contracts/evidence/README.md`](../../contracts/evidence/README.md) | Define EvidenceRef or EvidenceBundle semantics. |
| Evidence admissibility and release posture | [`policy/evidence/README.md`](../../policy/evidence/README.md) | Turn shape rules into allow, deny, restrict, or abstain decisions. |
| Valid and invalid evidence examples | [`fixtures/contracts/v1/evidence/README.md`](../../fixtures/contracts/v1/evidence/README.md) | Store fixture payloads beside this note. |
| Drift and unresolved migration work | [`DRIFT_REGISTER.md`](../../docs/registers/DRIFT_REGISTER.md) and [`VERIFICATION_BACKLOG.md`](../../docs/registers/VERIFICATION_BACKLOG.md) | Resolve governance conflicts through undocumented convention. |

## Legacy lineage

The predecessor scaffold listed three domain identity models as its source documents. Inspection supports a more precise statement:

| Source document | Verified relationship to normalization | Treatment |
|---|---|---|
| [`agriculture/IDENTITY_MODEL.md`](../../docs/domains/agriculture/IDENTITY_MODEL.md) | CONFIRMED direct reference to `schemas/evidence/spec_normalization.md`, marked `NEEDS_VERIFICATION` in that document | Preserve the legacy pointer until the incoming reference is migrated or intentionally retained. |
| [`fauna/IDENTITY_MODEL.md`](../../docs/domains/fauna/IDENTITY_MODEL.md) | CONFIRMED direction that exact normalization rules should live under `schemas/contracts/v1/evidence/...` | Aligns with the active versioned route; no authority should be inferred for this legacy file. |
| [`geology/IDENTITY_MODEL.md`](../../docs/domains/geology/IDENTITY_MODEL.md) | CONFIRMED expectation of a spec-normalization standard; exact final fields and hash policy remain open | Use the versioned evidence-family profile and accepted identity ADRs when those questions are resolved. |

The existence of a link or expectation does not prove an implementation. Domain documents may describe proposed behavior, outdated paths, or unresolved identity rules. Their references are migration evidence, not authority to duplicate the active profile.

## Compatibility contract

While this path remains in the repository:

- **Authors MUST NOT** add canonical normalization rules, schema fields, executable examples, or hash vectors here.
- **Authors SHOULD** update the versioned evidence-family note and its paired schemas, contracts, fixtures, validators, tests, and migration records as one reviewed change when behavior changes.
- **Readers SHOULD** follow the active-authoring link and inspect its maturity labels before relying on any rule.
- **Tools MUST NOT** load this Markdown file as executable configuration or as the source of validator behavior.
- **Migration work MUST** preserve the distinction between content identity (`spec_hash`) and activity identity (`run_id`).
- **Release work MUST NOT** treat schema validity or hash equality alone as proof of evidence truth, admissibility, review, or publication readiness.
- **Public and AI surfaces MUST** continue to resolve evidence through governed interfaces and apply cite-or-abstain, rights, sensitivity, policy, release, correction, and rollback controls.

If an older consumer requires this exact path, maintain a pointer or documented redirect. Do not copy the versioned profile into this file to satisfy that consumer.

## Open conflicts

### `spec_hash` grammar

Current repository evidence contains two incompatible proposed forms:

| Surface | Observed form | Status |
|---|---|---|
| ADR-0013 | `jcs:sha256:<64-lower-hex>` for ordinary JSON normalized with RFC 8785/JCS | PROPOSED |
| `common/spec_hash.schema.json` | `sha256:<64-lower-hex>` | CONFIRMED machine shape / schema status PROPOSED |

Until resolved, this file must not select a winner, invent a compatibility window, or imply that validators accept both. Resolution should update the accepted ADR, common schema, dependent `$ref` consumers, fixtures, validators, tests, migration notes, and downstream contract documentation together.

### EvidenceBundle naming and shape

The versioned evidence family contains both `evidence_bundle.schema.json` and `evidence-bundle.schema.json`. The inspected files differ materially: the underscore form is strict and fielded; the hyphen form is a permissive scaffold. This is a duplicate-authority risk, not a harmless filename alias.

Do not derive normalization behavior from both. Canonical naming, deprecation, redirects, fixture ownership, and validator treatment require an explicit steward-approved migration decision.

### Implementation proof

The active normalization note describes proposed gates and expected validator/fixture lanes. This compatibility file does not prove that cross-runtime canonicalization, duplicate-key rejection, Unicode handling, transient-field exclusion, hash parity, migration compatibility, or runtime enforcement is complete. Treat each as NEEDS VERIFICATION until repository tests, CI, or runtime evidence establishes it.

## Migration and retirement gates

This path may be frozen, redirected, or retired only after all applicable gates are satisfied:

- [ ] inventory tracked repository references, generated documentation, configs, workflows, scripts, and external integration instructions that name this path;
- [ ] migrate authoritative references to `schemas/contracts/v1/evidence/spec_normalization.md` or document why a compatibility pointer must remain;
- [ ] confirm an Evidence steward, Identity steward, Schema steward, and Docs steward for the decision;
- [ ] resolve or explicitly defer the `spec_hash` grammar conflict without hiding it;
- [ ] resolve the EvidenceBundle underscore/hyphen authority conflict or record a governed compatibility plan;
- [ ] verify links, schema references, fixtures, validators, tests, and CI after reference migration;
- [ ] record the migration or deprecation decision in the appropriate ADR/register surface;
- [ ] define a rollback target and compatibility window for affected consumers;
- [ ] preserve Git history and lineage; do not replace a governed migration with an unexplained deletion.

Retirement of this pointer does not promote the versioned normalization profile. Promotion has its own ADR, schema, fixture, validator, review, and release burden.

## Validation and acceptance

For a documentation-only revision of this file, the acceptance boundary is:

| Check | Expected result |
|---|---|
| Markdown structure | One H1; balanced fenced blocks; readable tables and callouts. |
| Link integrity | Every repository-relative link resolves at the reviewed commit. |
| Authority discipline | The file identifies itself as non-authoritative and routes active work to the versioned family. |
| Conflict visibility | `spec_hash` grammar and EvidenceBundle naming conflicts remain explicit. |
| Scope discipline | No schema, contract, fixture, validator, test, policy, receipt, proof, release, or runtime file changes are implied. |
| Publication boundary | No statement equates schema/hash conformance with truth, admissibility, or release. |

Passing these checks proves only that the compatibility document is internally coherent at the reviewed snapshot. It does not prove normalization implementation, evidence closure, policy clearance, or publication readiness.

## Evidence ledger

| Evidence | What it supports |
|---|---|
| [`schemas/evidence/README.md`](README.md) | Root-level evidence lane is a compatibility and migration guardrail. |
| [`schemas/README.md`](../README.md) | `schemas/` owns machine-checkable shape and separates it from contracts, policy, fixtures, validators, data, and release. |
| [`schemas/contracts/v1/evidence/README.md`](../contracts/v1/evidence/README.md) | Versioned evidence family, duplicate EvidenceBundle risk, and active routing. |
| [`schemas/contracts/v1/evidence/spec_normalization.md`](../contracts/v1/evidence/spec_normalization.md) | Proposed normalization profile, open gates, and current mismatch ledger. |
| [`schemas/contracts/v1/common/spec_hash.schema.json`](../contracts/v1/common/spec_hash.schema.json) | Current proposed bare `sha256:` machine shape. |
| [`ADR-0001`](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | Proposed versioned schema-home decision and no-divergent-authority rationale. |
| [`ADR-0013`](../../docs/adr/ADR-0013-spec_hash-and-run_id-identity-grammar.md) | Proposed deterministic identity grammar and JCS-tagged hash form. |
| Attached Directory Rules | Canonical placement doctrine: machine shape belongs under `schemas/`; the default schema home is `schemas/contracts/v1/...`; parallel schema homes require ADR treatment. |

## Correction and rollback

A documentation correction should update this file and any directly contradicted compatibility index in one reviewable change, while leaving active machine behavior untouched unless separately authorized and tested.

Rollback for this revision is an ordinary Git revert of this file. If a later migration changes incoming references or removes the compatibility path, rollback must also restore the prior link targets or redirect behavior and re-run the repository's documentation, link, schema, and contract checks. Never roll back released evidence identity by silently rewriting `spec_hash` values or moving files; use governed correction and rollback records for affected released artifacts.

## Maintainer handoff

- Keep this file short enough to remain a pointer, not a shadow copy of the active profile.
- Preserve the direct Agriculture lineage reference until migrated.
- Do not describe proposed ADRs as accepted.
- Keep hash grammar and duplicate-schema conflicts visible until they are resolved by reviewed repository changes.
- Prefer honest `NEEDS VERIFICATION` labels over claims inferred from documentation alone.
