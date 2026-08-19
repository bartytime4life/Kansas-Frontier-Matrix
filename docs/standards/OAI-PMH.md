<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/standards/oai-pmh
title: OAI-PMH — KFM Harvesting Guidance and Readiness Boundary
type: standard; interoperability-reference; source-intake-boundary
version: v2.0-draft
status: draft; repository-grounded; upstream-currentness-refreshed; case-collision-hold; no-adoption; no-conformance-proof; no-source-activation; no-release; no-publication
owners:
  - "@bartytime4life — verified GitHub review route through CODEOWNERS"
  - "NEEDS VERIFICATION — source-intake, archives, metadata, rights, sensitivity, security, validation, and release stewards"
created: 2026-05-14
updated: 2026-08-18
policy_label: public
owning_root: docs/
current_path: docs/standards/OAI-PMH.md
responsibility: >
  Explain the OAI-PMH 2.0 protocol, its bounded use as a candidate metadata-harvesting
  mechanism, and the evidence required before any KFM source profile, harvester, mapping,
  release, or public service can claim readiness or conformance.
truth_posture: >
  CONFIRMED current target path and document identity, adopted Directory Rules placement,
  repository-default CODEOWNERS route, uppercase/lowercase case collision, current
  SourceDescriptor contract/schema surfaces, Kansas Memory placeholder-connector boundary,
  absence of a verified dedicated OAI-PMH executable proof in the reviewed repository
  surfaces, and dated official OAI-PMH 2.0 protocol facts / PROPOSED KFM source profile,
  deterministic harvest discipline, security controls, fixtures, validators, mappings,
  receipts, producer/consumer bindings, and graduation sequence / UNKNOWN admitted
  OAI-PMH sources, real endpoint capabilities, production harvester behavior, source rights,
  external interoperability, governed releases, deployments, and public services.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 854cb663dd70a39675280743159872e4cf6e9354
  target_prior_blob: b0d64303b6c1fcbf21a5efcf00cce47bca0f0a79
  lowercase_sibling_blob: f7583d91ec7d4d3b3daeed3e202991d6cb44cee0
  standards_readme_blob: a8cbe5d183448d5f0de37f8a4eacd6fcaca0d71b
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  source_descriptor_schema_blob: 582e70b834278c3c6ca9a8b31efbe0989c96f0bc
  kansas_memory_connector_readme_blob: df917cdd6d4c555630113a684719800b0f688bf8
external_currentness_review:
  access_date: 2026-08-18
  issuing_authority: Open Archives Initiative
  protocol: OAI-PMH 2.0
  protocol_release_date: 2002-06-14
  official_document_version: 2015-01-08
  scope: official protocol and implementation-guideline facts only; not KFM adoption, source admission, implementation, conformance, release, or publication
related:
  - ./README.md
  - ./ARCHIVAL-STANDARDS.md
  - ./DUBLIN-CORE.md
  - ./OAI-PMH.md
  - ./oai-pmh.md
  - ../doctrine/directory-rules.md
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../sources/catalog/kansas/kansas-memory.md
  - ../../contracts/source/source_descriptor.md
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../connectors/kansas_memory/README.md
  - ../../.github/CODEOWNERS
tags: [kfm, standards, oai-pmh, metadata-harvesting, archives, source-intake, xml, dublin-core, rights, sensitivity, validation, correction, rollback]
notes:
  - "Same-path modernization of the uppercase target only."
  - "The lowercase sibling remains a separate conflicting identity under STD-DRIFT-003; this revision does not rename, merge, delete, redirect, or select a canonical winner."
  - "The document records guidance, not an OAI-PMH SourceDescriptor extension, semantic contract, schema, policy, connector, validator, fixture, workflow, receipt, release, or public endpoint."
  - "No live source is contacted or activated, and no real OAI-PMH response or archival record is added."
  - "The prior proposal-era implementation, conformance, path, cadence, digest, token, and Kansas-provider claims are narrowed to current evidence."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="oai-pmh--open-archives-initiative-protocol-for-metadata-harvesting"></a>
<a id="oai-pmh--kfm-harvesting-guidance-and-readiness-boundary"></a>

# OAI-PMH — KFM Harvesting Guidance and Readiness Boundary

> **Operating rule.** OAI-PMH can carry structured metadata from a repository to a harvester. It does not make the repository authoritative for every claim, turn metadata into evidence, settle rights or sensitivity, admit a source, authorize a lifecycle transition, prove interoperability, or permit release or publication.

> [!IMPORTANT]
> **Human-readable guidance only.** [`docs/standards/`](./README.md) owns standards and interoperability explanation. [`contracts/`](../../contracts/source/source_descriptor.md) owns semantic meaning, [`schemas/`](../../schemas/contracts/v1/source/source_descriptor.schema.json) owns machine shape, policy owns admissibility, executable code and tests own bounded behavior, and release objects own release state.

> [!CAUTION]
> **Case-collision HOLD.** Both `docs/standards/OAI-PMH.md` and `docs/standards/oai-pmh.md` exist with different document IDs and content. The standards README records this as `STD-DRIFT-003 — CONFLICTED / HOLD`. This revision changes only the uppercase target requested. It does not declare either file canonical or authorize a case-only migration.

> [!WARNING]
> **No OAI-PMH implementation or conformance proof is established here.** The reviewed repository evidence did not establish a dedicated executable OAI-PMH parser, harvester, fixture family, validator, workflow, real harvest artifact, producer/consumer exchange, governed release, deployment, or public endpoint. The repository-present Kansas Memory lane is explicitly a `0.0.0` placeholder compatibility boundary whose access method remains unknown.

> [!NOTE]
> The official Open Archives Initiative site identifies OAI-PMH Protocol Version `2.0`, released `2002-06-14`, with official document version `2015-01-08`. Upstream stability does not silently create a KFM adoption decision.

## Current status

| Surface | Current evidence | Bounded conclusion |
|---|---|---|
| Uppercase target | `docs/standards/OAI-PMH.md` exists with `doc_id: kfm://doc/standards/oai-pmh` | **CONFIRMED guidance path and identity** |
| Lowercase sibling | `docs/standards/oai-pmh.md` exists with a different document ID | **CONFLICTED / HOLD** |
| Placement | Adopted Directory Rules place human-readable standards guidance in `docs/standards/` | **CONFIRMED same-path placement** |
| GitHub review routing | Repository-default CODEOWNERS routes review to `@bartytime4life` | **CONFIRMED route; stewardship NEEDS VERIFICATION** |
| SourceDescriptor | Semantic contract and singular/plural schema surfaces exist; the schema labels the object family `PROPOSED` and records a compatibility alias | **CONFIRMED repository surfaces; OAI-specific profile not adopted** |
| Kansas Memory | Compatibility connector boundary and `0.0.0` placeholder package exist; API/OAI-PMH/IIIF/export/scrape access method remains unknown | **No source activation or runtime proof** |
| OAI-PMH harvester | No dedicated executable implementation was verified in the reviewed paths and searches | **UNKNOWN / HOLD** |
| Real endpoints and rights | No institution-specific endpoint, terms, format inventory, cadence, or redistribution decision is accepted by this document | **UNKNOWN / fail closed** |
| Conformance | No KFM producer, consumer, release, or independent interoperability exercise was verified | **Documented guidance only** |
| Release/publication | No release manifest, correction drill, rollback drill, deployment, or public service was verified for OAI-PMH-derived material | **No effect** |

**Quick navigation:** [Purpose](#purpose--scope) · [Role](#why-oai-pmh-matters-to-kfm) · [Protocol](#protocol-101-the-six-verbs) · [Posture](#kfm-conformance-posture) · [Collision](#case-collision-hold) · [Source profile](#source-profile-contract) · [Lifecycle](#lifecycle-placement) · [Harvesting](#harvest-semantics) · [Metadata](#metadata-mapping) · [Rights](#rights-and-sensitivity) · [Security](#security-and-resource-limits) · [Outcomes](#protocol-errors-and-kfm-dispositions) · [Examples](#illustrative-requests) · [Validation](#validation) · [Maturity](#graduation-and-adoption-gates) · [Failures](#failure-modes) · [Backlog](#verification-backlog) · [Rollback](#non-effects-and-rollback) · [References](#references)

---

<a id="purpose--scope"></a>

## 1. Purpose & scope

This document explains how OAI-PMH 2.0 could participate in KFM source intake without bypassing the KFM trust membrane.

It covers:

- the official protocol model and six verbs;
- the distinction among repository, item, resource, and record;
- candidate KFM bindings to the existing `SourceDescriptor` family;
- full and selective harvesting, inclusive date windows, sets, deletions, and resumption tokens;
- raw preservation, normalization, rights, sensitivity, evidence, catalog, release, correction, and rollback boundaries;
- XML, network, resource-limit, logging, and replay controls;
- bounded examples and candidate validation questions; and
- the evidence required to progress from documentation to an admitted and tested implementation.

It does **not**:

- adopt OAI-PMH as a required KFM source protocol;
- assert that KFM operates as a Service Provider or Data Provider;
- identify any Kansas institution as a conforming OAI-PMH repository;
- create an OAI-specific contract, schema, enum, policy, connector, fixture, validator, workflow, or data lane;
- admit or activate a source;
- authorize network access, harvesting, redistribution, release, deployment, or publication; or
- resolve the uppercase/lowercase document collision.

[Back to top](#top)

---

<a id="why-oai-pmh-matters-to-kfm"></a>

## 2. Why OAI-PMH may matter to KFM

OAI-PMH is a low-barrier metadata-exchange protocol. A **Data Provider** exposes structured metadata through an OAI-PMH repository; a **Service Provider** operates a harvester and may build services from harvested metadata.

For KFM, a future harvester could be useful when an admitted archival or institutional source exposes stable repository identity, repeatable metadata, useful change datestamps, and rights-compatible records. That utility remains conditional.

### 2.1 Role boundaries

| Role or object | What it can establish | What it cannot establish |
|---|---|---|
| OAI-PMH repository | Protocol responses and metadata records exposed by a Data Provider | Truth of every metadata statement, rights to republish, KFM source admission, or public safety |
| OAI-PMH harvester | Repeatable requests and captured responses | Evidence closure, policy approval, release, or publication |
| OAI identifier | An item identity unique within a repository | The identity of the underlying resource in all systems |
| OAI record | Metadata in one metadata format for an item | A canonical KFM domain object or claim |
| `oai_dc` record | Baseline unqualified Dublin Core metadata | Rich archival semantics, precise geometry, complete rights, or KFM evidence sufficiency |
| KFM `SourceDescriptor` | How an admitted candidate source may be treated | That the source's claims are true |
| KFM evidence/release objects | Support, review, policy, release, correction, and rollback state | Protocol conformance by themselves |

### 2.2 Candidate KFM posture

**PROPOSED:** KFM may act as a Service Provider for a source only after source admission, rights review, sensitivity review, endpoint and capability verification, fixture-backed parsing, finite failure behavior, correction handling, and release-boundary validation.

**UNKNOWN:** No reviewed evidence in this change establishes an operational KFM OAI-PMH Data Provider. Exposing KFM records through OAI-PMH would be a separate product, contract, policy, security, release, and interoperability decision.

[Back to top](#top)

---

<a id="protocol-101-the-six-verbs"></a>

## 3. Protocol 101: model, requests, and six verbs

### 3.1 Official data model

| Concept | Official protocol meaning | KFM handling implication |
|---|---|---|
| Resource | The object the metadata is about | Preserve its source-supplied locator separately from the OAI item identifier |
| Item | Repository constituent from which metadata about one resource can be disseminated in one or more formats | Scope its identifier to the source repository |
| Record | Metadata in one format, returned as XML | Preserve the raw XML and format identity before normalization |
| Header | Identifier, datestamp, zero or more `setSpec` values, and optional deleted status | Treat as source metadata, not KFM release state |
| Metadata | The format-specific metadata payload | Map only through a reviewed profile; retain source bytes |
| `about` | Optional repeatable schema-valid information about the metadata record | Preserve when present; do not assume a universal rights or provenance vocabulary |
| Set | Optional grouping for selective harvesting | Treat as source-native organization; do not assume exhaustive or semantically authoritative coverage |

The protocol identifier identifies an **item within a repository**. It is not automatically the identifier of the described resource. A future KFM profile must preserve both where available.

### 3.2 Transport and common response rules

OAI-PMH uses a repository base URL and HTTP `GET` or `POST`. Protocol responses are XML encoded as UTF-8 and are governed by the OAI-PMH response schema. HTTP transport failures and OAI-PMH protocol errors are distinct.

A KFM implementation must not interpret `HTTP 200` as a successful harvest without also parsing the OAI-PMH response and checking for protocol error elements.

### 3.3 The six verbs

| Verb | Official purpose | Candidate KFM use |
|---|---|---|
| `Identify` | Describe repository identity and protocol capabilities | Capability snapshot before admission or harvest |
| `ListMetadataFormats` | List metadata formats available from a repository or item | Select an accepted mapping profile |
| `ListSets` | List optional repository sets | Discover source-native selection boundaries |
| `ListIdentifiers` | Return headers, optionally filtered by datestamp or set | Change discovery or deletion reconciliation |
| `ListRecords` | Return records, optionally filtered by datestamp or set | Metadata capture |
| `GetRecord` | Return one record by item identifier and `metadataPrefix` | Targeted audit, repair, or correction re-fetch |

### 3.4 Mandatory baseline format

A conforming repository must disseminate unqualified Dublin Core under the reserved `metadataPrefix` `oai_dc`. A repository may expose richer formats as well.

KFM must not infer that `oai_dc` is semantically sufficient merely because it is protocol-mandatory. Richer formats may be needed for archival description, agents, hierarchy, rights, or relationships, and every mapping still requires source-specific verification.

[Back to top](#top)

---

<a id="kfm-conformance-posture"></a>

## 4. KFM conformance posture

The word **conformance** must be scoped to an actor, revision, behavior, and evidence level.

### 4.1 Separate evidence axes

| Axis | Question | Current result |
|---|---|---|
| Upstream currentness | Is the official protocol/version identified? | **CONFIRMED for OAI-PMH 2.0** |
| Documentation | Does KFM have human-readable guidance? | **CONFIRMED** |
| Adoption | Has KFM accepted an OAI-PMH profile or required role? | **Not established** |
| Source admission | Is a specific endpoint admitted with rights and sensitivity decisions? | **Not established** |
| Shape validation | Do representative responses pass protocol and metadata-profile validation? | **Not established** |
| Negative validation | Do malformed, hostile, partial, stale, deletion, token, rights, and sensitivity cases fail correctly? | **Not established** |
| Producer behavior | Does a named KFM harvester emit governed artifacts at a pinned revision? | **Not established** |
| Consumer behavior | Does a named KFM consumer preserve semantics and failure states? | **Not established** |
| Release binding | Does a governed release bind source, profile, evidence, policy, correction, and rollback? | **Not established** |
| External interoperability | Has an independent exchange been observed and recorded? | **Not established** |

### 4.2 Claim grammar

Acceptable current wording:

- “KFM documents a candidate OAI-PMH harvesting boundary.”
- “The official OAI-PMH protocol is Version 2.0.”
- “A future source profile would require the checks in this document.”
- “No dedicated executable OAI-PMH proof was verified in this review.”

Wording that remains unsupported:

- “KFM conforms to OAI-PMH.”
- “KFM harvests Kansas archives.”
- “Kansas Memory uses OAI-PMH.”
- “OAI-PMH records are KFM evidence.”
- “A successful parser run authorizes publication.”

[Back to top](#top)

---

<a id="case-collision-hold"></a>

## 5. Case-collision HOLD

The repository contains both:

```text
docs/standards/OAI-PMH.md
docs/standards/oai-pmh.md
```

They have different document IDs, titles, metadata, content, and implied posture. This is not a harmless alias on every filesystem.

This update preserves the requested uppercase path and its existing document ID. It does not:

- copy the lowercase document wholesale;
- assert that the uppercase path is canonical;
- add a redirect, tombstone, mirror, or generated relationship;
- repair all inbound links;
- change either file's consumers; or
- perform a case-only rename.

A later structural decision requires:

1. identity and content comparison;
2. complete inbound-link, fragment, generator, test, and consumer inventory;
3. a single-write and compatibility strategy;
4. case-insensitive checkout testing;
5. Git-history and external-link preservation;
6. documentation-graph and stale-reference closure; and
7. a reviewed rollback path.

[Back to top](#top)

---

<a id="source-profile-contract"></a>

## 6. Candidate source-profile binding

This section is guidance for a future profile. It does not amend the existing `SourceDescriptor` contract or schemas.

### 6.1 Existing SourceDescriptor authority

The reviewed SourceDescriptor schema:

- describes source identity, role, authority, rights, sensitivity, cadence, access, citation, source-head metadata, admissibility, review, release, and lifecycle posture;
- labels the object family `PROPOSED`;
- identifies `schemas/contracts/v1/sources/source_descriptor.schema.json` as its canonical schema path and the singular `source/` path as a legacy compatibility path; and
- does not establish an accepted OAI-PMH-specific discriminator in the evidence reviewed for this update.

A future OAI-PMH profile must reuse or extend the accepted SourceDescriptor authority rather than creating a documentation-local object.

### 6.2 Existing fields that would need binding

| Existing SourceDescriptor concern | OAI-PMH question to resolve |
|---|---|
| `source_id`, `title`, `source_type`, `source_role` | What stable KFM source identity and authority role apply to the repository? |
| `authority_rank`, `publisher`, `owner_or_steward` | Who operates the repository, and what can that institution authoritatively assert? |
| `rights` | What terms govern harvesting, storage, transformation, attribution, and redistribution? |
| `sensitivity_default` | What default and per-record sensitivity review is required? |
| `cadence` | What source-supported refresh and staleness policy applies? |
| `access` | What base URL, method, allowlist, authentication posture, redirect policy, and rate limits apply? |
| `citation` | How must records and the repository be cited? |
| `source_head` | What `Identify`/capability snapshot, retrieval time, and digest bind a run? |
| `admissibility_limits` | What response-size, record-count, date-range, set, metadata-format, and content restrictions apply? |
| `public_release` | What may be publicly exposed, transformed, generalized, or withheld? |
| `review_state`, `release_state`, `lifecycle` | What decision state is required before each transition? |

### 6.3 OAI capability snapshot questions

A future source-specific capability record or accepted extension should capture, at minimum:

- repository `baseURL`, `repositoryName`, `protocolVersion`, and `adminEmail`;
- `earliestDatestamp`, `granularity`, and `deletedRecord` policy;
- optional compression and repository descriptions from `Identify`;
- each `metadataPrefix`, schema URL, and namespace URI;
- sets actually selected, if any, and why;
- retrieval time, response digest, HTTP status, redirect chain, and content length;
- source terms and rights review date;
- parser/profile version; and
- observed limitations or conflicts.

**NEEDS VERIFICATION:** Which of these belong directly in SourceDescriptor, in `source_head`, in a capability-snapshot object, or in a run receipt. Documentation must not decide that machine shape by example.

### 6.4 Source-specific admission packet

Before any live fetch beyond an approved capability probe, require:

1. accepted source identity and owner;
2. official base URL and allowed redirect targets;
3. protocol/capability snapshot;
4. terms, harvesting permission, attribution, storage, and redistribution decision;
5. sensitivity and cultural/sovereignty review where applicable;
6. accepted metadata formats and mappings;
7. cadence, rate, timeout, byte, page, and record limits;
8. correction and deletion strategy;
9. fixture-safe sample rights;
10. accountable reviewer and activation decision; and
11. no-network tests proving the negative paths.

[Back to top](#top)

---

<a id="lifecycle-placement"></a>

## 7. Lifecycle placement

Format and protocol do not determine lifecycle state.

```text
admitted source profile
  -> approved fetch attempt
  -> RAW response bytes + retrieval metadata
  -> WORK parse and mapping candidates
  -> QUARANTINE when rights, sensitivity, integrity, identity, or parsing is unresolved
  -> PROCESSED validated derivative
  -> CATALOG / TRIPLET derived discovery and relation surfaces
  -> governed release decision
  -> PUBLISHED public-safe derivative
```

### 7.1 Stage responsibilities

| Stage | OAI-PMH material | Required boundary |
|---|---|---|
| Pre-RAW / source edge | Capability probe or scheduled candidate | Source activation, host allowlist, terms, and run authorization |
| RAW | Exact response bytes and HTTP/request metadata | Immutable capture or governed reference; no semantic cleanup |
| WORK | Parsed headers, metadata, mappings, and candidate relations | Parser version, source role, uncertainty, and validation report |
| QUARANTINE | Malformed, hostile, partial, ambiguous-rights, sensitive, conflicted, or unsupported material | Reason code, reviewer path, no public access |
| PROCESSED | Validated source-preserving derivative | Identity, temporal, mapping, rights, and sensitivity closure appropriate to scope |
| CATALOG/TRIPLET | Derived discovery/provenance/relation records | Must point back to evidence and source lineage; not sovereign truth |
| PUBLISHED | Released public-safe metadata or product | Policy/review/release state, correction, withdrawal, and rollback |

### 7.2 Public-client boundary

Ordinary public clients must not:

- query a live OAI-PMH endpoint through a browser as a substitute for governed ingestion;
- read RAW or QUARANTINE responses;
- expose admin emails, opaque tokens, source diagnostics, or restricted fields without review;
- infer deletion, rights, location, or identity from missing data; or
- treat harvested metadata as a released claim.

[Back to top](#top)

---

<a id="harvest-semantics"></a>

## 8. Harvest semantics, replay, and correction

### 8.1 Full and selective harvesting

`ListRecords` and `ListIdentifiers` support optional `from`, `until`, and `set` arguments. Date bounds are inclusive. Repositories must support day granularity and may support seconds granularity as declared by `Identify`.

A future KFM incremental strategy should:

1. read and validate source granularity;
2. repeat or overlap the last successful boundary intentionally;
3. deduplicate replayed records deterministically;
4. avoid converting local clock time directly into unsupported source granularity;
5. preserve the exact request window and source response time;
6. distinguish complete, partial, empty, and failed runs; and
7. periodically reconcile when deletion guarantees or source behavior require it.

The overlap width, high-water rule, and reconciliation cadence are **source-profile decisions**, not universal constants in this document.

### 8.2 Sets are optional and not necessarily exhaustive

A repository may expose sets, and an item may belong to multiple sets or no set. Harvesting every set is not guaranteed to retrieve every item.

Therefore:

- `noSetHierarchy` is not proof that the repository is unusable;
- a set-filtered harvest must state that scope;
- duplicate records across sets are expected;
- set names and hierarchy are source-native metadata, not KFM domain truth; and
- an exhaustive harvest uses an unfiltered list request when permitted and appropriate.

### 8.3 Resumption tokens

A repository may partition a list response and return a `resumptionToken`. The token is opaque to the harvester. A continuation request uses the verb and token according to the protocol; the harvester must not reconstruct or modify token contents.

KFM-specific controls are **PROPOSED**:

- keep the raw token only in internal transient run state when needed;
- never place raw tokens in public logs, examples, receipts, issue bodies, or UI;
- record a token digest, sequence number, issue/expiry metadata if supplied, and page outcome;
- cap pages, elapsed time, records, bytes, and token loops;
- detect repeated tokens and non-progress;
- treat an invalid or expired token as an incomplete run, not a silent success; and
- retain enough last-good state for a governed restart without claiming gap-free recovery.

### 8.4 Deletion policies

| `deletedRecord` value | Official meaning | KFM implication |
|---|---|---|
| `no` | Repository does not maintain deletion information and must not reveal deleted status | Continued incremental harvesting cannot discover deletions; do not infer absence as deletion |
| `transient` | Repository may reveal deleted status but does not guarantee persistent or consistent retention | Preserve observed tombstones; plan source-specific reconciliation |
| `persistent` | Repository keeps deletion history without a time limit and consistently reveals deleted status | Convert observed deletion headers into correction/withdrawal candidates; do not auto-delete released KFM records |

An OAI deletion is a source-record state. It is not automatically a KFM correction, withdrawal, erasure, or release decision. The downstream effect depends on evidence, rights, review, release lineage, and dependent products.

### 8.5 Identity and deterministic replay

The protocol identifies a record version by repository item identifier, `metadataPrefix`, and datestamp. A future KFM implementation should also bind:

- admitted `source_id`;
- exact base-URL/source identity;
- raw record digest;
- parser and mapping profile version;
- retrieval time and request scope; and
- deletion status.

**PROPOSED decision point:** distinguish a stable record lineage key from a record-version key. Do not bake the datestamp into the only durable identity if KFM needs explicit revision lineage.

[Back to top](#top)

---

<a id="metadata-mapping"></a>

## 9. Metadata mapping

### 9.1 Preserve before mapping

Every accepted response should retain:

- exact RAW bytes or an immutable governed reference;
- HTTP and request metadata;
- OAI header fields;
- metadata format prefix, schema URL, and namespace;
- optional `about` blocks;
- source and parser version; and
- validation findings.

A normalized record is a derivative. It must not overwrite the source representation.

### 9.2 `oai_dc` baseline

The baseline `oai_dc` format uses unqualified Dublin Core. KFM mapping must remain conservative.

| Dublin Core element | Candidate KFM interpretation | Boundary |
|---|---|---|
| `dc:title` | Source-supplied title | Preserve language and repetitions |
| `dc:creator`, `dc:contributor` | Agent-name candidates | Do not assert person identity without authority resolution |
| `dc:subject` | Source-supplied subjects | Do not silently treat as a controlled KFM vocabulary |
| `dc:description` | Source description | Preserve source wording; not generated evidence |
| `dc:publisher` | Source-supplied publisher | Distinguish repository operator, publisher, and rights holder |
| `dc:date` | Temporal candidate | Preserve literal value; parse only with explicit uncertainty |
| `dc:type` | Source type hint | Does not select a KFM contract by itself |
| `dc:format` | Source format statement | Validate independently when operationally material |
| `dc:identifier` | Resource or alternate identifier candidate | Keep separate from the OAI item identifier |
| `dc:source` | Source relation candidate | Requires relation and authority review |
| `dc:language` | Source language statement | Normalize only through an accepted profile |
| `dc:relation` | Relation candidate | Graph projection requires evidence and relation semantics |
| `dc:coverage` | Spatial or temporal text hint | **Never treat as authoritative geometry** |
| `dc:rights` | Rights input | Free text does not by itself authorize reuse or release |

[`DUBLIN-CORE.md`](./DUBLIN-CORE.md) records the broader KFM Dublin Core boundary. This document does not create a second Dublin Core application profile.

### 9.3 Richer formats

A source may expose MODS, MARCXML, EAD-family, or local formats. A future profile must verify the exact `metadataPrefix`, schema, namespace, semantics, rights, and parser behavior before preferring a richer format.

Retaining `oai_dc` for comparison may be useful, but duplicate representations must not become duplicate canonical claims. Cross-format parity, loss, and conflict need explicit tests.

### 9.4 Spatial caution

Text such as “Ellsworth County, Kansas” or coordinate-like values in `dc:coverage` are source metadata, not geometry proof. Geocoding creates a WORK-tier candidate with method, confidence, ambiguity, source, and review state. Harmful precision or sensitive location must be generalized, staged, or denied before public exposure.

[Back to top](#top)

---

<a id="rights-and-sensitivity"></a>

## 10. Rights, sensitivity, and source authority

### 10.1 Rights do not arrive automatically

OAI-PMH defines transport and metadata exchange. It does not supply one universal rights vocabulary. Rights information may occur in source metadata or an `about` container, but KFM must independently verify:

- permission to harvest;
- permission to retain source responses;
- permission to transform;
- attribution requirements;
- redistribution and commercial-use limits;
- record-level exceptions;
- takedown and correction obligations; and
- whether terms changed since the last verification.

Public accessibility of an endpoint is not permission to republish its metadata or linked resources.

### 10.2 Sensitivity and sovereignty

Archive metadata can expose living people, precise archaeological or burial locations, sacred or culturally restricted knowledge, private land, security-relevant infrastructure, vulnerable communities, or other harmful precision.

When scope or authority is unclear, prefer:

- metadata-only capture without linked resource retrieval;
- field minimization;
- quarantine;
- redaction or generalization;
- delayed or staged access;
- qualified cultural, tribal, privacy, domain, or security review;
- abstention; or
- denial.

A source set name or public flag does not override KFM sensitivity policy.

### 10.3 Source-role anti-collapse

Repository metadata may be administrative, descriptive, contextual, or derived. Its source role must remain visible. A catalog description can support a claim that an institution describes an item in a certain way; it may not support every historical, geographic, biographical, or legal claim implied by that description.

[Back to top](#top)

---

<a id="security-and-resource-limits"></a>

## 11. Security and resource limits

A future harvester crosses a network and parses untrusted XML. Source admission and protocol conformance are not substitutes for application security.

### 11.1 Network controls

Require:

- explicit allowed schemes, hosts, ports, and base paths;
- DNS and resolved-address checks appropriate to the runtime;
- denial of loopback, link-local, private, metadata-service, and otherwise prohibited destinations unless explicitly governed;
- redirect limits with allowlist revalidation after every redirect;
- connection, read, total-run, and idle timeouts;
- response-byte and decompression-ratio limits;
- rate limits, backoff, cancellation, and concurrency caps;
- respect for `Retry-After` where applicable;
- no credential material in URLs or logs; and
- no browser-direct proxying of arbitrary user-supplied OAI endpoints.

### 11.2 XML controls

Require a parser configuration that:

- disables DTD processing and external entity resolution;
- prevents entity-expansion and quadratic-blowup attacks;
- limits element depth, attributes, text size, namespaces, records, and total nodes;
- validates UTF-8 and well-formedness before mapping;
- validates the OAI-PMH envelope and accepted metadata schemas where required;
- preserves malformed bytes in QUARANTINE when policy permits diagnostic retention;
- never executes processing instructions, scripts, stylesheets, or embedded links; and
- treats schema locations and linked resources as data, not automatic fetch instructions.

### 11.3 Flow-control limits

Bound:

- maximum pages per list sequence;
- maximum records and bytes per run;
- maximum token repeats and zero-progress pages;
- maximum elapsed time and retries;
- maximum date range for a single run;
- maximum number of accepted formats and sets; and
- maximum diagnostic detail returned to public clients.

Exceeding a limit yields a bounded failure or HOLD. It must not silently truncate while marking the run complete.

### 11.4 Logging and receipts

Do not log or publish:

- raw resumption tokens;
- credentials, cookies, authorization headers, or signed URLs;
- unreviewed response bodies;
- personal or sensitive record content;
- internal network diagnostics; or
- protected quarantine reasons that create new exposure.

A future receipt should record safe request scope, source and profile identity, response digests, counts, limits, timings, outcomes, and restart state—not the sensitive payload itself.

[Back to top](#top)

---

<a id="protocol-errors-and-kfm-dispositions"></a>

## 12. Protocol errors and KFM dispositions

OAI-PMH protocol errors are separate from HTTP status and parser failures. This document does not create a new executable outcome enum; implementation must reuse the owning KFM contract.

| OAI-PMH result | Protocol meaning | Candidate governed disposition |
|---|---|---|
| `badArgument` | Illegal, missing, repeated, or malformed argument | Implementation/configuration error; stop the affected request |
| `badResumptionToken` | Invalid or expired token | Mark list sequence incomplete; retain last-good state; bounded restart |
| `badVerb` | Unknown or illegal verb | Implementation/configuration error |
| `cannotDisseminateFormat` | Requested format unavailable | HOLD source/profile or record scope; do not substitute silently |
| `idDoesNotExist` | Requested identifier is unknown or illegal | Record not resolved; investigate before correction/withdrawal |
| `noMetadataFormats` | No metadata formats available for the specified item | HOLD targeted item/profile; do not infer repository-wide failure |
| `noRecordsMatch` | No records match the request criteria | Valid empty result; emit no-change evidence without catalog churn |
| `noSetHierarchy` | Repository does not support sets | Record capability; use unfiltered/date-based strategy if admitted |
| HTTP `503` with `Retry-After` | Service unavailable with retry guidance | Respect bounded delay; no busy loop |
| Malformed or hostile XML | Response cannot be safely parsed | ERROR or QUARANTINE according to owning contract |
| Rights or sensitivity unresolved | Protocol may succeed, but admissibility is unresolved | DENY/HOLD public progression |
| Resource limit exceeded | Run cannot complete within admitted limits | Incomplete/error outcome; never label complete |

Reason codes, precedence, public-safe messages, and retry eligibility belong in contracts/policy/code—not in this prose alone.

[Back to top](#top)

---

<a id="illustrative-requests"></a>

## 13. Illustrative requests

These examples are synthetic, non-executable documentation. `example.invalid` is intentionally non-resolving. They are not fixtures, endpoint claims, or proof of support.

### 13.1 Capability discovery

```text
GET https://archives.example.invalid/oai?verb=Identify
GET https://archives.example.invalid/oai?verb=ListMetadataFormats
GET https://archives.example.invalid/oai?verb=ListSets
```

A source that returns `noSetHierarchy` may still support OAI-PMH; sets are optional.

### 13.2 Date-bounded list request

```text
GET https://archives.example.invalid/oai
  ?verb=ListIdentifiers
  &metadataPrefix=oai_dc
  &from=2026-08-01
  &until=2026-08-18
```

The actual request must use the repository's declared granularity. Bounds are inclusive, so a replay strategy must deduplicate the repeated boundary intentionally.

### 13.3 Resumption continuation

```text
GET https://archives.example.invalid/oai
  ?verb=ListIdentifiers
  &resumptionToken=<opaque-token-supplied-by-the-repository>
```

The token is illustrative and must not be decoded, fabricated, committed, or exposed publicly.

### 13.4 Minimal source-preserving record sketch

```xml
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/">
  <ListRecords>
    <record>
      <header>
        <identifier>oai:example.invalid:item-0001</identifier>
        <datestamp>2026-08-18</datestamp>
        <setSpec>public-demo</setSpec>
      </header>
      <metadata>
        <oai_dc:dc
          xmlns:oai_dc="http://www.openarchives.org/OAI/2.0/oai_dc/"
          xmlns:dc="http://purl.org/dc/elements/1.1/">
          <dc:title>Synthetic demonstration record</dc:title>
          <dc:identifier>https://example.invalid/resource/item-0001</dc:identifier>
          <dc:rights>Illustrative only; no reuse grant</dc:rights>
        </oai_dc:dc>
      </metadata>
    </record>
  </ListRecords>
</OAI-PMH>
```

This sketch omits required envelope fields and schema-location detail for brevity. It must not be used as a conformance fixture.

[Back to top](#top)

---

<a id="validation"></a>

## 14. Validation matrix

The rows below describe evidence needs. Paths and tools are not created or adopted by this document.

| Layer | Positive evidence | Required negative evidence |
|---|---|---|
| Document | Metadata, links, anchors, official references, case-collision disclosure | No broken citations, unsupported adoption, fake endpoint, secret, or harmful example |
| Source admission | Accepted SourceDescriptor and activation decision | Unknown terms, blocked host, stale review, prohibited source role |
| HTTP | Allowed host, bounded response, retry behavior | Redirect escape, SSRF target, timeout, decompression bomb, oversized response |
| XML envelope | UTF-8, well-formed, accepted OAI-PMH response | DTD/entity attack, excessive depth, malformed namespace, invalid envelope |
| `Identify` | Version/capability fields captured | Missing/conflicting fields, unsafe base URL, unsupported granularity |
| Formats | `oai_dc` plus accepted richer formats | Schema/namespace mismatch, unsupported substitution |
| Sets | Correct selected scope and duplicate handling | Unsupported sets, non-exhaustive assumption, hierarchy loop |
| Date windows | Inclusive replay with deterministic deduplication | Granularity mismatch, clock-gap assumption, invalid range |
| Tokens | Complete bounded list sequence | Expired token, repeated token, zero progress, page/byte/time limit |
| Deletions | Correct `no`/`transient`/`persistent` behavior | Inferred deletion, automatic KFM erasure, missed tombstone |
| Mapping | Source-preserving normalized output | Ambiguous date, false geometry, identity overreach, lossy cross-format merge |
| Rights/sensitivity | Reviewed permissions and public-safe transform | Unknown reuse rights, harmful precision, living-person or cultural exposure |
| Evidence/catalog | Resolvable lineage and source role | Catalog record treated as proof or canonical truth |
| Release | Manifest, policy/review state, correction and rollback | Direct RAW-to-public path, missing withdrawal propagation |
| Interoperability | Independent exchange at pinned revisions | Self-declared conformance without external observation |

### 14.1 Minimum synthetic fixture families

A future implementation should include, at minimum:

- valid `Identify` for each granularity and deletion policy;
- valid `ListMetadataFormats` with `oai_dc` and a richer format;
- `noSetHierarchy`;
- complete and multi-page list sequences;
- repeated, expired, malformed, and non-progress tokens;
- `noRecordsMatch`;
- created, modified, and deleted headers;
- duplicate records returned through multiple sets;
- malformed XML, DTD/entity payloads, deep nesting, oversized text, and decompression limits;
- schema/namespace mismatch;
- ambiguous dates, `dc:coverage` false-precision candidates, and identity conflicts;
- unknown and conflicting rights;
- sensitive and public-safe records;
- partial-run replay and correction propagation; and
- release-denial and rollback fixtures.

Fixtures must be synthetic or demonstrably reusable. Do not copy real archival records merely because they are publicly viewable.

[Back to top](#top)

---

<a id="graduation-and-adoption-gates"></a>

## 15. Graduation and adoption gates

| Level | Evidence required | Current state |
|---|---|---|
| G0 — Reference | Official protocol identified and guidance bounded | **This document** |
| G1 — Source discovery | Candidate endpoint, operator, terms, capabilities, formats, cadence, and risks verified | **Not established** |
| G2 — Admission packet | Accepted source identity, rights/sensitivity decisions, limits, and activation state | **Not established** |
| G3 — Offline implementation | Parser/harvester with synthetic positive and negative fixtures, deterministic replay, no-network tests | **Not established** |
| G4 — Controlled capability probe | Approved limited network probe with receipts and no downstream promotion | **Not established** |
| G5 — Shadow harvest | Complete bounded runs into RAW/QUARANTINE with correction and deletion rehearsal | **Not established** |
| G6 — Producer/consumer verification | Named producer and consumer pass profile, security, mapping, and replay tests at pinned revisions | **Not established** |
| G7 — Governed release | Evidence, policy/review, release manifest, correction, withdrawal, rollback, and public-safe delivery close | **Not established** |
| G8 — External interoperability | Independent exchange observed and limitations recorded | **Not established** |

Progression is not automatic. A source can remain at a lower level indefinitely, and a higher level can be revoked or rolled back when terms, security, source behavior, or KFM policy changes.

An adoption decision must specify:

- KFM actor role;
- accepted protocol and profile version;
- admitted source classes;
- semantic and machine bindings;
- policy and security requirements;
- validators, fixtures, producers, consumers, and workflows;
- failure and stale-state behavior;
- correction and rollback; and
- supersession/currentness review.

[Back to top](#top)

---

<a id="failure-modes"></a>

## 16. Failure modes and anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Treating endpoint reachability as source admission | Network access does not settle authority, terms, rights, sensitivity, or release |
| Treating `HTTP 200` as harvest success | OAI-PMH errors can occur in a valid HTTP response |
| Decoding or editing resumption tokens | Tokens are opaque repository state |
| Logging raw tokens or response bodies | May expose state, personal data, or restricted metadata |
| Using one universal cadence | Source granularity, change behavior, terms, and risk differ |
| Using the prior high-water mark without overlap | Inclusive boundaries, clock behavior, and delayed updates can create gaps |
| Treating `noRecordsMatch` as an error | It is a valid empty selection |
| Treating `noSetHierarchy` as nonconformance | Sets are optional |
| Harvesting every set to claim completeness | Items can belong to no set or multiple sets |
| Treating `dc:coverage` as geometry | Creates unsupported location and false precision |
| Treating `dc:rights` text as a release grant | Rights require source-specific interpretation and review |
| Auto-deleting KFM records from an OAI tombstone | Source deletion is not a KFM release/correction decision |
| Skipping raw preservation | Removes the ability to audit mapping, corrections, or parser changes |
| Fetching schema locations or linked resources automatically | Expands network and SSRF surface outside the admitted source |
| Creating docs-local schema, policy, reason-code, or receipt authority | Produces parallel trust objects |
| Claiming conformance from documentation or happy-path tests | Omits negative, producer, consumer, release, and interoperability evidence |
| Renaming one case-collision file directly | Risks broken checkouts, links, identities, consumers, and parallel writes |

[Back to top](#top)

---

<a id="verification-backlog"></a>

## 17. Verification backlog

Priority indicates dependency and trust significance, not authorization to implement.

| Priority | Item | Closure evidence |
|---|---|---|
| P0 | Resolve `OAI-PMH.md` / `oai-pmh.md` identity and writable-home conflict | Content/link/consumer inventory, decision authority, case-safe migration test, compatibility and rollback |
| P0 | Determine whether KFM adopts an OAI-PMH role or profile at all | Accepted decision with actor, scope, bindings, non-goals, failure behavior, and currentness review |
| P0 | Define source-admission, rights, sensitivity, and security requirements for any first candidate | Source packet, qualified reviews, allowlist, limits, negative fixtures, activation decision |
| P1 | Reconcile SourceDescriptor singular/plural schema authority before an OAI extension | Accepted schema-home/alias disposition and consumer compatibility proof |
| P1 | Decide OAI capability snapshot and run-receipt machine ownership | Contract/schema decision without documentation-local authority |
| P1 | Select one synthetic fixture family and implement safe XML parsing and flow control | No-network positive/negative tests and deterministic replay |
| P1 | Define deletion, correction, withdrawal, and dependent-product propagation | Synthetic `no`/`transient`/`persistent` drill with rollback |
| P1 | Verify Kansas Memory access method instead of assuming OAI-PMH | Official source evidence, terms, capabilities, and repository decision |
| P2 | Define metadata-format profiles and cross-format parity tests | Accepted mappings, fixtures, loss/conflict reporting, producer/consumer tests |
| P2 | Establish operational observability without sensitive logs | Metrics/receipt contract, redaction tests, incident and stale-state runbook |
| P2 | Prove one controlled shadow harvest if a source is admitted | Approved run, complete receipts, limits, corrections, no public promotion |
| P3 | Run independent interoperability exercises | External consumer/provider result, pinned versions, limitations, correction path |

[Back to top](#top)

---

<a id="non-effects-and-rollback"></a>

## 18. Non-effects and rollback

### 18.1 Non-effects

This document update does not:

- adopt OAI-PMH or any KFM application profile;
- establish KFM as a Service Provider or Data Provider;
- resolve the uppercase/lowercase collision;
- add or alter a contract, schema, policy, enum, source descriptor, connector, fixture, validator, test, workflow, dependency, receipt, proof, catalog record, release object, runtime, route, deployment, or public artifact;
- activate a source or perform network access;
- harvest, store, transform, map, release, or publish real records;
- authenticate rights, sensitivity, cultural authority, evidence, conformance, review, or release state;
- promote lifecycle state;
- weaken a gate; or
- change repository settings.

### 18.2 Rollback

Before merge, close the draft pull request and abandon or delete only its task branch.

After an authorized merge, revert the documentation commit or restore prior blob `b0d64303b6c1fcbf21a5efcf00cce47bca0f0a79` through the normal reviewed path. Then rerun metadata, Markdown, links, anchors, documentation graph, stale-reference, citation, and changed-area checks.

No source deactivation, data/schema migration, credential rotation, runtime restart, cache invalidation, release withdrawal, or public correction is required because this change is documentation-only.

[Back to top](#top)

---

<a id="references"></a>

## 19. References

### 19.1 Authoritative upstream

- [Open Archives Initiative — OAI-PMH core resources](https://www.openarchives.org/pmh/)
- [The Open Archives Initiative Protocol for Metadata Harvesting — Version 2.0](https://www.openarchives.org/OAI/openarchivesprotocol.html)
- [OAI-PMH Implementation Guidelines](https://www.openarchives.org/OAI/2.0/guidelines.htm)

### 19.2 Current KFM repository evidence

- [`docs/standards/README.md`](./README.md) — standards-lane authority boundary and `STD-DRIFT-003`
- [`docs/standards/ARCHIVAL-STANDARDS.md`](./ARCHIVAL-STANDARDS.md) — archival interoperability and preservation boundary
- [`docs/standards/DUBLIN-CORE.md`](./DUBLIN-CORE.md) — Dublin Core guidance
- [`docs/standards/oai-pmh.md`](./oai-pmh.md) — conflicting lowercase sibling; **HOLD**, not canonicalized here
- [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) — adopted placement bytes through ADR-0029
- [`docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) — Directory Rules adoption decision
- [`contracts/source/source_descriptor.md`](../../contracts/source/source_descriptor.md) — SourceDescriptor semantic guidance
- [`schemas/contracts/v1/source/source_descriptor.schema.json`](../../schemas/contracts/v1/source/source_descriptor.schema.json) — singular compatibility schema surface reviewed here
- [`schemas/contracts/v1/sources/source_descriptor.schema.json`](../../schemas/contracts/v1/sources/source_descriptor.schema.json) — plural schema surface named by the singular schema as canonical
- [`connectors/kansas_memory/README.md`](../../connectors/kansas_memory/README.md) — Kansas Memory placeholder compatibility boundary
- [`docs/sources/catalog/kansas/kansas-memory.md`](../sources/catalog/kansas/kansas-memory.md) — source documentation with access method unresolved
- [`.github/CODEOWNERS`](../../.github/CODEOWNERS) — GitHub review routing only

### 19.3 Revision ledger

| Revision | Date | Material change |
|---|---|---|
| `v1` | 2026-05-14 | Initial proposal-era OAI-PMH guidance |
| `v2.0-draft` | 2026-08-18 | Grounds the uppercase document in current repository evidence and official OAI-PMH sources; removes broken citation tokens and unsupported implementation/conformance/provider claims; corrects deletion, set, date-window, token, XML-security, mapping, rights, lifecycle, case-collision, validation, graduation, and rollback boundaries |

[Back to top](#top)
