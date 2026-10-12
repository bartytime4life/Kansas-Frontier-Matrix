<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kansas-kbs-herbarium-readme
title: connectors/kansas/kbs_herbarium/ — KANU Herbarium Connector Admission Lane
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Kansas source steward · Flora steward · Rights reviewer · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-12
policy_label: public-doctrine; provisional-path; specimen-admission; rights-gated; sensitivity-gated; no-publication
current_path: connectors/kansas/kbs_herbarium/README.md
truth_posture: CONFIRMED current path and inspected bytes / CONFLICTED future adapter name / PROPOSED connector contract / UNKNOWN runtime depth
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 55c4e537f14386ea503a5879a2a4dfbaebef5384
  prior_blob: 32571d70efc57be1bfe4654e06ca41a72ebbb7b0
related:
  - ../README.md
  - ../../README.md
  - ../../../CONTRIBUTING.md
  - ../../../.github/CODEOWNERS
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../docs/sources/catalog/kansas/kbs.md
  - ../../../docs/sources/catalog/kansas/ku-herbarium.md
  - ../../../docs/standards/Darwin_Core.md
  - ../../../docs/domains/flora/README.md
  - ../../../docs/domains/flora/OBJECT_FAMILIES.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../data/registry/sources/README.md
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../release/
tags: [kfm, connectors, kansas, kbs, kanu, herbarium, flora, specimen, darwin-core, source-admission, rights, sensitivity, raw, quarantine, governance]
notes:
  - "The current path is verified at the pinned base commit; this document does not ratify `kbs_herbarium` as the final adapter name."
  - "Repository source pages propose both `connectors/kansas/kbs/` and `connectors/kansas/ku-herbarium/`; no move or rename is authorized by this change."
  - "KANU specimen material and KBS Natural Heritage Inventory rankings remain separate source surfaces with separate roles and descriptors."
  - "SourceDescriptor authority is conflicted: the substantive singular-path schema labels itself legacy, the plural canonical-path schema is an empty PROPOSED scaffold, and the draft Source Descriptor Standard uses a different role vocabulary." 
  - "Only this Markdown file is in scope. No connector code, descriptor, fixture, policy, schema, workflow, receipt, release object, or source activation is created."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KANU Herbarium Connector Admission Lane

> [!IMPORTANT]
> **Document lifecycle:** `draft`  
> **Component maturity:** `experimental` documentation; connector runtime `UNKNOWN`  
> **Owner:** `OWNER_TBD`  
> **Truth posture:** `CONFIRMED` current path and inspected repository evidence · `CONFLICTED` future adapter name and source-role vocabulary · `PROPOSED` connector contract  
> **Boundary:** source admission for KU R. L. McGregor Herbarium (KANU) specimen material only. This folder does not activate a source, publish a claim, or own KBS Natural Heritage Inventory authority records.

**Quick links:** [Purpose](#purpose) · [Authority level](#authority-level) · [Status](#status) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review burden](#review-burden) · [Related folders](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Evidence basis](#evidence-basis) · [Anti-collapse rules](#source-role-and-anti-collapse-rules) · [Lifecycle](#lifecycle-boundary) · [Definition of done](#definition-of-done) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

<a id="scope"></a>

## Purpose

`connectors/kansas/kbs_herbarium/` documents the admission boundary for future KANU herbarium connector work at the path that exists in the pinned repository snapshot.

The lane may support source-specific retrieval, parsing, provenance capture, and a governed handoff of specimen material to `RAW` or `QUARANTINE`. It does **not** establish botanical truth, conservation status, source-descriptor authority, policy, schema, evidence closure, release authority, or publication.

The durable downstream unit is an inspectable, evidence-backed claim. A specimen record may support such a claim after the rest of the KFM lifecycle closes; this connector README cannot create that authority by itself.

[Back to top](#top)

---

<a id="repo-fit"></a>

## Authority level

**Implementation-bearing folder, provisional path.**

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Parent responsibility root | **CONFIRMED** | Source-specific fetch and admission belong under `connectors/`; the Kansas family belongs under `connectors/kansas/`. |
| Current path | **CONFIRMED** | `connectors/kansas/kbs_herbarium/README.md` and the checked placeholder `.gitkeep` exist at base commit `55c4e537f14386ea503a5879a2a4dfbaebef5384`. |
| Final adapter name | **CONFLICTED** | The KBS umbrella page proposes `connectors/kansas/kbs/`, while the KANU per-surface page proposes `connectors/kansas/ku-herbarium/`. The current repository path is `kbs_herbarium/`. |
| Path migration | **NOT IN SCOPE** | This revision neither moves nor renames the folder. A later path decision must preserve history, references, validation, and rollback under Directory Rules migration discipline. |
| SourceDescriptor authority | **OUTSIDE THIS FOLDER** | Source identity, role, rights, sensitivity, cadence, access, citation, review, and activation state belong in the governed source registry. |
| Publication authority | **NONE** | Connector work may hand off only to `RAW` or `QUARANTINE`; all later lifecycle gates remain downstream. |

This README records the conflict rather than silently choosing a future canonical slug.

[Back to top](#top)

---

## Status

| Item | Status | Meaning |
|---|---:|---|
| README contract | **DRAFT / implementation-bearing documentation** | A reviewable connector boundary; a commit or pull request is not KFM publication. |
| Connector code and package surface | **UNKNOWN** | No runtime, parser, package, dependency, import graph, or execution proof is asserted here. |
| Live KANU source activation | **NEEDS VERIFICATION / fail closed** | Treat live access as disabled until a current descriptor, explicit activation decision, rights review, sensitivity review, fixtures, and validation exist. |
| KANU endpoint, archive cadence, and terms | **NEEDS VERIFICATION** | The repository doctrine identifies DwC-A/IPT as the intended source shape, but current endpoint and terms are not pinned here. |
| KBS NHI relationship | **CONFIRMED distinction** | KBS NHI rankings and KANU specimen records are related institutional surfaces but are not interchangeable source roles or descriptors. |
| Public release | **DENY by default** | No connector output is public. Sensitive and rights-uncertain records remain quarantined, restricted, generalized, or denied until governed release. |
| Owner assignment | **UNKNOWN** | `OWNER_TBD` is deliberate; current CODEOWNERS provides only a repository-wide fallback for this path. |

[Back to top](#top)

---

<a id="accepted-inputs"></a>

## What belongs here

The following material may belong in this connector lane when separately authorized and reviewed:

- source-specific connector code for KANU retrieval and admission;
- parsing and normalization helpers for a verified Darwin Core Archive or equivalent KANU distribution;
- source-head checks such as `ETag`, `Last-Modified`, version, or checksum when the current endpoint supports them;
- references to the accepted KANU `SourceDescriptor` and activation decision;
- provenance-preserving adapters that retain upstream identifiers, record-level rights, source timestamps, retrieval metadata, and content hashes;
- handoff code that writes only to the governed `RAW` or `QUARANTINE` boundary;
- connector-local operational notes that do not duplicate the canonical source standard, schema, policy, or source registry;
- pointers to no-network valid and invalid fixtures in their canonical fixture or test home.

Expected specimen identity and evidence fields include, where supplied and lawful to retain:

- `institutionCode`;
- `collectionCode`;
- `catalogNumber`;
- `occurrenceID`;
- `basisOfRecord`;
- `scientificName` and the recorded identification;
- `eventDate`;
- collector or recorder metadata subject to living-person review;
- geometry, coordinate uncertainty, and geodetic metadata;
- `license`, `rightsHolder`, `datasetID`, and attribution;
- upstream archive or record version and retrieval time.

Missing, withheld, conflicting, or sensitive fields must not be invented. Route the record to a structured review or quarantine outcome.

[Back to top](#top)

---

<a id="exclusions"></a>

## What does NOT belong here

This folder must not contain or imply authority over:

- KBS Natural Heritage Inventory rankings or other natural-heritage authority records;
- authoritative plant nomenclature, conservation status, legal status, listed status, range, habitat, or current-population claims;
- `SourceDescriptor` instances or source-activation decisions;
- semantic contracts, JSON Schemas, rights policy, sensitivity policy, or release policy;
- public occurrence layers, public map tiles, public APIs, dashboards, or ordinary UI payloads;
- direct writes to `data/processed/`, `data/catalog/`, `data/triplets/`, `data/published/`, proof stores, or release-decision stores;
- exact rare-plant locations or other sensitive geometry in committed examples, fixtures, logs, or documentation;
- credentials, access tokens, private URLs, signed URLs, or source-account secrets;
- AI-generated taxonomic, locality, sensitivity, or rights assertions treated as evidence;
- silently corrected or overwritten specimen identifications without preserved lineage;
- a duplicate copy of normative Darwin Core, SourceDescriptor, policy, or release requirements when a canonical link is available.

[Back to top](#top)

---

<a id="admission-posture"></a>

## Inputs

A connector run may accept source material only after all of the following are resolvable:

1. a current `SourceDescriptor` for the KANU surface;
2. an explicit activation state or source-activation decision that permits the requested mode;
3. verified access method, current terms, attribution requirements, redistribution posture, and cadence;
4. sensitivity defaults and rare-taxa handling rules;
5. a pinned source head, archive identity, or equivalent retrieval fingerprint;
6. no-network fixtures and negative cases sufficient to exercise fail-closed behavior.

The intended source shape in current repository doctrine is a KANU Darwin Core Archive distributed through an IPT-like surface. That is **doctrine-supported but operationally NEEDS VERIFICATION** here: this README does not pin an endpoint, account, archive URL, rate limit, version, or license.

A fixture may enter the lane without live activation only when it is synthetic, minimized, public-safe, rights-safe, and clearly labeled `fixture_only`.

[Back to top](#top)

---

## Outputs

Connector output is limited to a caller-owned, auditable handoff:

```text
SourceDescriptor + activation gate
  -> KANU connector
     -> data/raw/flora/<source_id>/<run_id>/
     -> data/quarantine/flora/<reason>/<run_id>/
```

An allowed handoff should carry or resolve:

- source and descriptor identifiers;
- retrieval time and upstream content identity;
- checksums;
- the preserved source-role value;
- rights and attribution fields;
- sensitivity and geometry-review state;
- a connector or ingest receipt candidate;
- a structured outcome and reason when admission is held, quarantined, denied, or fails.

The exact output DTO, sink interface, reason-code vocabulary, receipt storage path, and idempotency contract remain **NEEDS VERIFICATION**. This README does not invent them.

No connector output is `PROCESSED`, cataloged, evidence-closed, released, or published merely because retrieval succeeded.

[Back to top](#top)

---

<a id="validation"></a>

## Validation

### Record and admission checks

Before implementation can be treated as active, validation must cover at least:

- a resolvable and reviewed KANU `SourceDescriptor`;
- activation state consistent with the requested live, fixture-only, restricted, or disabled mode;
- archive identity, source head, retrieval timestamp, and checksum preservation;
- Darwin Core archive structure and required source fields;
- deterministic cross-source matching using `institutionCode + catalogNumber + eventDate` where those fields exist;
- preservation of `license`, `rightsHolder`, `datasetID`, citation, and attribution;
- taxonomy fields without silently replacing the specimen's recorded determination;
- geometry validity, coordinate uncertainty, datum/CRS metadata, and intentional handling of withheld coordinates;
- restricted-taxa and exact-location negative cases;
- explicit quarantine for unknown rights, unresolved source role, schema drift, malformed identity, ambiguous taxonomy, or unsafe geometry;
- proof that connector code cannot write beyond `RAW` or `QUARANTINE`;
- no-network fixtures for success, quarantine, deny, and operational error paths.

### SourceDescriptor authority and source-role conflict

The pinned repository contains three incompatible surfaces:

- the draft Source Descriptor Standard uses doctrinal roles such as `observed`;
- the substantive schema at `schemas/contracts/v1/source/source_descriptor.schema.json` labels itself a legacy path and accepts machine values including `observation` and `occurrence_evidence`, but not `observed`;
- the nominal canonical-path schema at `schemas/contracts/v1/sources/source_descriptor.schema.json` is an empty `PROPOSED` scaffold with no enforceable field vocabulary.

Therefore:

> [!WARNING]
> **Do not create or activate a KANU descriptor by copying `observed` from narrative docs or by treating either schema path as silently authoritative.** Resolve schema-home and vocabulary drift through the governing contract and ADR process first. Until then, prose should describe KANU as *specimen-backed occurrence evidence* without pretending the machine enum is settled.

### Documentation checks for this file

A review of this README should verify:

- exactly one H1 and a coherent heading hierarchy;
- balanced comment, code-fence, table, and callout syntax;
- preserved KFM metadata and final newline;
- relative links resolve at the feature-branch head;
- no remote tracking badge or external image was introduced;
- no secret, personal record, sensitive locality, rights-restricted source content, or live endpoint was embedded;
- claims remain bounded to the pinned evidence snapshot;
- the diff contains only this requested Markdown file.

Repository-wide executable validation is **NOT ESTABLISHED** by this README. The inspected `tools/validate_all.py` is a placeholder, and no Markdown-specific lint configuration was verified in the bounded inspection.

[Back to top](#top)

---

## Review burden

At minimum, substantive connector or activation work should involve:

- connector steward;
- Kansas source steward;
- Flora domain steward;
- rights reviewer;
- sensitivity reviewer;
- validation steward;
- docs steward.

The inspected `.github/CODEOWNERS` applies the repository-wide `@kfm/maintainers` fallback to this path but does not name a connector-specific owner. Team existence, assignment, and reviewer availability remain **NEEDS VERIFICATION**; this README does not invent accounts or request reviewers.

Additional review is required before:

- choosing or moving to a final adapter path;
- accepting a live endpoint or access method;
- approving source terms or redistribution;
- setting or changing source-role vocabulary;
- exposing any sensitive or generalized geometry;
- treating a connector receipt as sufficient evidence or release proof.

[Back to top](#top)

---

## Related folders

| Surface | Relationship | Status in the pinned snapshot |
|---|---|---:|
| [`../README.md`](../README.md) | Canonical Kansas connector-family coordination. | **CONFIRMED file** |
| [`../../README.md`](../../README.md) | Connector-root responsibility boundary. | **CONFIRMED file** |
| [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) | Placement, connector lifecycle, README contract, and migration discipline. | **CONFIRMED file** |
| [`../../../docs/sources/catalog/kansas/kbs.md`](../../../docs/sources/catalog/kansas/kbs.md) | KBS umbrella; separates NHI authority from KANU specimen evidence. | **CONFIRMED file / draft** |
| [`../../../docs/sources/catalog/kansas/ku-herbarium.md`](../../../docs/sources/catalog/kansas/ku-herbarium.md) | KANU per-surface source catalog entry. | **CONFIRMED file / draft** |
| [`../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md`](../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md) | Human-facing SourceDescriptor doctrine. | **CONFIRMED file / draft** |
| [`../../../schemas/contracts/v1/source/source_descriptor.schema.json`](../../../schemas/contracts/v1/source/source_descriptor.schema.json) | Substantive inspected schema at the self-declared legacy singular path. | **CONFIRMED file / authority CONFLICTED** |
| [`../../../schemas/contracts/v1/sources/source_descriptor.schema.json`](../../../schemas/contracts/v1/sources/source_descriptor.schema.json) | Nominal canonical-path schema; currently an empty proposed scaffold. | **CONFIRMED file / not enforceable** |
| [`../../../data/registry/sources/README.md`](../../../data/registry/sources/README.md) | Source registry responsibility and admission boundary. | **CONFIRMED file / implementation details mixed** |
| [`../../../docs/standards/Darwin_Core.md`](../../../docs/standards/Darwin_Core.md) | KFM Darwin Core conformance guidance. | **CONFIRMED file / draft** |
| [`../../../docs/domains/flora/README.md`](../../../docs/domains/flora/README.md) | Flora domain ownership and sensitivity posture. | **CONFIRMED file / draft** |
| [`../../../docs/domains/flora/OBJECT_FAMILIES.md`](../../../docs/domains/flora/OBJECT_FAMILIES.md) | Flora missing/planned-files register despite its filename. | **CONFIRMED file / planning register** |
| [`../../../policy/rights/`](../../../policy/rights/) | Rights decisions and enforcement. | **Outside connector; contents NEEDS VERIFICATION** |
| [`../../../policy/sensitivity/`](../../../policy/sensitivity/) | Sensitivity and redaction policy. | **Outside connector; contents NEEDS VERIFICATION** |
| [`../../../release/`](../../../release/) | Release decisions, correction, withdrawal, and rollback. | **Outside connector** |

[Back to top](#top)

---

## ADRs

- Directory Rules govern the current responsibility root and require transparent migration discipline for a later move.
- The repository repeatedly references `ADR-0001` for schema-home intent, but the exact file `docs/adr/ADR-0001-schema-home.md` was not found in the pinned direct probe. Meanwhile, both singular and plural SourceDescriptor schema paths exist with conflicting maturity. ADR acceptance, current filename, and machine authority remain **CONFLICTED / NEEDS VERIFICATION**.
- No accepted path-specific ADR was verified that chooses among:
  - `connectors/kansas/kbs_herbarium/` (current path);
  - `connectors/kansas/kbs/` with a KANU child (KBS umbrella proposal);
  - `connectors/kansas/ku-herbarium/` (KANU per-surface proposal).
- This revision does not make that decision. A future rename or split requires explicit scope, reference updates, history preservation, validation, and rollback.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Review date | `2026-07-12` |
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Base ref | `main` |
| Pinned base commit | `55c4e537f14386ea503a5879a2a4dfbaebef5384` |
| Prior README blob | `32571d70efc57be1bfe4654e06ca41a72ebbb7b0` |
| Review scope | Target README, checked placeholder, parent connector docs, KBS/KANU source docs, Directory Rules, current SourceDescriptor schema, SourceDescriptor standard, Darwin Core standard, Flora docs, contribution guidance, CODEOWNERS, pull-request template, validation placeholder, open PR/branch search |
| Reviewer identity | `OWNER_TBD` — no semantic owner assignment made by this document |

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence basis

| Evidence | What it supports | What it does not prove |
|---|---|---|
| Target README at the pinned base, blob `32571d70...` | Exact editing baseline, current metadata, stale statements, current path. | Runtime or source activation. |
| Creation commit `2329514cbe88932e95b3f5c1ef85bb3e87aa24eb` | The v0.1 README replaced a blank placeholder; the old “blank before this update” statement is historical residue. | That returning to a blank file is now the right rollback. |
| Directory Rules §7.3 and §15 | Connector output boundary and required folder-README contract. | Whether this child slug is canonical. |
| Kansas connector parent README | Parent family responsibility and sublane rules. | Complete child inventory or passing implementation. |
| KBS umbrella and KANU per-surface catalog pages | Separate NHI/KANU roles, intended DwC-A/IPT posture, sensitivity, and competing path proposals. | Current endpoint, terms, cadence, descriptor, adapter, or runtime. |
| Singular-path SourceDescriptor JSON Schema | Substantive machine fields, enum, and fail-closed requirements; the file declares itself legacy. | Canonical schema-home authority or a KANU descriptor instance. |
| Plural-path SourceDescriptor JSON Schema | The nominal canonical path exists. | Field validation; it is currently an empty `PROPOSED` scaffold. |
| Source Descriptor Standard | Intended admission doctrine and older seven-role vocabulary. | Machine-schema conformance; its role vocabulary conflicts with the substantive schema. |
| Darwin Core and Flora docs | Intended occurrence vocabulary, domain ownership, and sensitivity posture. | Implemented parser, validator, policy, or release behavior. |
| Direct exact-path probes | Proposed `connectors/kansas/kbs/README.md`, `connectors/kansas/ku-herbarium/README.md`, and proposed descriptor paths were not found at the pinned ref. | Absence of every differently named or unindexed implementation. |

Absence claims are bounded to the exact paths and searches inspected. They do not establish a complete recursive inventory.

[Back to top](#top)

---

<a id="anti-collapse-rules"></a>

## Source-role and anti-collapse rules

1. **KANU specimen evidence is not KBS NHI authority.** Keep separate descriptors, source roles, access methods, rights, and downstream claims.
2. **A specimen is evidence of a collected and curated record, not automatic nomenclatural truth.** Preserve the recorded determination, the determining party where available, and later re-identification lineage.
3. **A specimen record is not automatically current range, current population, habitat suitability, rarity, legal status, or conservation-status truth.**
4. **Specimen-backed occurrence evidence may carry more direct support than a crowd observation for the same voucher-backed event, but disagreement must remain visible; do not erase or silently overwrite the competing record.**
5. **Original geometry and public geometry are different objects.** Exact sensitive localities remain internal or quarantined until a policy-approved transform and review produce a public-safe derivative.
6. **Aggregates, modeled distributions, checklists, maps, tiles, and AI explanations are derived carriers.** They require their own roles, evidence, receipts, policy decisions, and release state.
7. **Doctrinal prose and machine enums are not interchangeable.** Resolve `observed` versus `observation` / `occurrence_evidence` before creating machine records.
8. **Successful retrieval is not admission, evidence closure, release, or publication.**

[Back to top](#top)

---

<a id="lifecycle-diagram"></a>

## Lifecycle boundary

```text
KANU source material
  -> SourceDescriptor resolution
  -> activation / rights / sensitivity gate
  -> connector retrieval and immutable source capture
  -> RAW
     or QUARANTINE with reason
  -> downstream normalization and validation
  -> PROCESSED
  -> CATALOG / TRIPLET with EvidenceBundle closure
  -> release review and manifest
  -> PUBLISHED public-safe derivative
  -> correction / withdrawal / rollback
```

Only the retrieval and `RAW`/`QUARANTINE` handoff belong to this connector lane. Every later arrow is owned by downstream pipelines, contracts, schemas, policies, validators, proofs, and release controls.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This lane is not ready for active source use until:

- [ ] the final adapter path is ratified or this path is explicitly retained with a recorded rationale;
- [ ] one KANU `SourceDescriptor` exists in the governed registry and conforms to the accepted schema;
- [ ] the source-role vocabulary conflict is resolved;
- [ ] the current endpoint or archive access method, terms, attribution, redistribution posture, cadence, and source-head strategy are verified;
- [ ] live access is disabled by default and requires an explicit activation state;
- [ ] parser and normalizer behavior is covered by no-network valid and invalid fixtures;
- [ ] rights, taxonomy, identity, geometry, uncertainty, sensitivity, and restricted-taxa negative paths fail closed;
- [ ] outputs are proven to stop at caller-owned `RAW` or `QUARANTINE` handoff;
- [ ] deterministic matching and re-identification lineage are tested;
- [ ] no public claim, exact sensitive geometry, or direct downstream-store write can be produced by connector code;
- [ ] documentation links, owner routing, applicable CI, and rollback evidence are verified.

[Back to top](#top)

---

<a id="rollback"></a>

## Rollback

Before merge, leave the draft pull request unmerged and abandon the scoped branch if the revision is rejected. Closing the pull request or deleting the branch is a separate repository action.

After merge, create a transparent revert commit or revert pull request. For this revision, the prior target is:

```text
base commit: 55c4e537f14386ea503a5879a2a4dfbaebef5384
prior blob:  32571d70efc57be1bfe4654e06ca41a72ebbb7b0
path:        connectors/kansas/kbs_herbarium/README.md
```

Re-run applicable documentation and connector-boundary validation after rollback. Do not reset, force-push, or rewrite shared history.

[Back to top](#top)

---

<a id="verification-backlog"></a>

## Verification backlog

| Item | Status | Evidence needed |
|---|---:|---|
| Final adapter path and naming convention | **CONFLICTED** | Accepted ADR, migration note, or path-specific maintainer decision reconciling current path, KBS umbrella proposal, and KANU per-surface proposal. |
| KANU SourceDescriptor identifier and home | **NEEDS VERIFICATION** | Accepted registry entry and schema-valid descriptor. |
| SourceDescriptor schema home and source-role vocabulary | **CONFLICTED** | Accepted ADR or equivalent decision; reconciled contract, substantive schema, standard, fixtures, and validator. |
| Current KANU endpoint and archive format | **NEEDS VERIFICATION** | Source-steward review of the current distribution and metadata. |
| Rights, attribution, redistribution, and image-record distinction | **NEEDS VERIFICATION** | Current terms and rights review captured in the descriptor. |
| Retrieval cadence and source-head strategy | **NEEDS VERIFICATION** | Endpoint metadata and validated watcher/connector design. |
| Parser, package, dependencies, and import surface | **UNKNOWN** | Bounded recursive inventory or mounted checkout. |
| Darwin Core mapping and required-field policy | **NEEDS VERIFICATION** | Accepted profile, parser fixtures, and validator results. |
| Sensitive-location and restricted-taxa policy behavior | **NEEDS VERIFICATION** | Policy tests, invalid fixtures, and review evidence. |
| Re-identification and correction lineage | **NEEDS VERIFICATION** | Contract, schema, fixtures, and correction-path tests. |
| Connector-specific CODEOWNERS | **NEEDS VERIFICATION** | Accepted ownership rule or team assignment. |
| Repository-native Markdown checks and substantive connector CI | **UNKNOWN** | Verified workflow/configuration and observed check results. |

[Back to top](#top)

---

<a id="maintainer-note"></a>

## Maintainer note

Keep this folder narrowly focused on KANU specimen admission while the path decision remains open. Do not let the existence of `kbs_herbarium/` create a second source registry, a second policy surface, an implicit KBS NHI adapter, or a shortcut to public flora claims.

[Back to top](#top)
