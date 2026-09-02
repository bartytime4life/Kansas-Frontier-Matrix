<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kansas-kdwp-readme
title: connectors/kansas/kdwp/ — KDWP Source-Family Admission Lane
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Kansas source steward · Fauna steward · Flora steward · Habitat steward · Rights reviewer · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-12
policy_label: public-doctrine; kansas-family; provisional-product-layout; regulatory-and-observation-source; sensitivity-gated; rights-gated; no-publication
current_path: connectors/kansas/kdwp/README.md
truth_posture: CONFIRMED current path and inspected repository evidence / CONFLICTED SourceDescriptor authority and product-lane layout / PROPOSED connector contract / UNKNOWN runtime depth
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 2b7213e4f3f49e55e1ad1dff306fcce720e8c69f
  prior_blob: e4c887164772a97ced3097da7e848325b3c56849
related:
  - ../README.md
  - ../../README.md
  - ../../kdwp/README.md
  - ../../kdwp/src/README.md
  - ../../kdwp/tests/README.md
  - ../kdwp_flora/README.md
  - ../kdwp_ert/README.md
  - ../../kdwp_ert/README.md
  - ../../../CONTRIBUTING.md
  - ../../../.github/CODEOWNERS
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/sources/catalog/kansas/kdwp.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../docs/domains/fauna/SOURCES.md
  - ../../../docs/domains/flora/README.md
  - ../../../docs/domains/habitat/README.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../data/registry/sources/README.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../release/
tags: [kfm, connectors, kansas, kdwp, sinc, wildlife, fauna, flora, habitat, source-admission, regulatory-context, occurrence-evidence, rights, sensitivity, raw, quarantine, governance]
notes:
  - "The current path is verified under the Kansas connector family and remains the KDWP coordination lane in this revision."
  - "Repository evidence also shows a noncanonical top-level KDWP compatibility package plus KDWP Flora and Ecological Review Tool sibling lanes; this revision documents those surfaces without moving, deleting, or ratifying them."
  - "KDWP is a source family, not one homogeneous dataset. Listed-status, SINC-rank, range, monitoring, habitat, and review-tool products require product-specific identity, rights, sensitivity, role, cadence, and activation decisions."
  - "SourceDescriptor authority is conflicted: the populated singular-path schema declares itself legacy, the plural-path schema is an empty PROPOSED scaffold, and narrative doctrine uses a different role vocabulary."
  - "Only this Markdown file is in scope. No connector code, descriptor, fixture, policy, schema, workflow, receipt, release object, source activation, path move, or public artifact is created."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KDWP Source-Family Admission Lane

> [!IMPORTANT]
> **Document lifecycle:** `draft`  
> **Component maturity:** documentation contract; connector runtime `UNKNOWN`  
> **Owner:** `OWNER_TBD`  
> **Truth posture:** `CONFIRMED` current path and inspected repository evidence · `CONFLICTED` product-lane layout and `SourceDescriptor` authority · `PROPOSED` admission contract  
> **Boundary:** source admission for Kansas Department of Wildlife and Parks products only. This folder does not activate a source, decide public sensitivity, issue a regulatory determination, serve an ecological review, publish a map, or authorize release.

**Quick links:** [Purpose](#purpose) · [Authority level](#authority-level) · [Status](#status) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review burden](#review-burden) · [Related folders](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Evidence basis](#evidence-basis) · [Product boundaries](#kdwp-product-and-role-boundaries) · [Descriptor conflict](#sourcedescriptor-authority-conflict) · [Lifecycle](#lifecycle-boundary) · [Anti-collapse](#anti-collapse-and-sensitive-data-rules) · [Definition of done](#definition-of-done) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

<a id="scope"></a>

## Purpose

`connectors/kansas/kdwp/` is the current KDWP coordination and source-admission lane under the Kansas connector family.

It may host or coordinate product-specific retrieval, source-shape parsing, provenance capture, and governed `RAW` or `QUARANTINE` handoff for KDWP material after a product-level `SourceDescriptor`, activation decision, rights review, and sensitivity review exist.

It does not make source claims true. It preserves enough identity, role, time, rights, sensitivity, and provenance for downstream KFM validation to decide what the material can support.

[Back to top](#top)

---

<a id="repo-fit"></a>

## Authority level

**Implementation-bearing connector folder, with a confirmed parent placement and unresolved product layout.**

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Responsibility root | **CONFIRMED** | Source-specific fetch and admission belong under `connectors/`; connector output is bounded to `RAW` or `QUARANTINE` plus process-memory receipt handoff. |
| Kansas family placement | **CONFIRMED** | KDWP work belongs under `connectors/kansas/`; the KDWP source catalog explicitly records this path as already correct. |
| Current KDWP path | **CONFIRMED** | `connectors/kansas/kdwp/README.md` and `.gitkeep` exist at the pinned base. |
| Product implementation below this path | **UNKNOWN** | Direct probes found no `pyproject.toml`, `src/README.md`, or `tests/README.md` below this path. That does not prove no differently named implementation exists. |
| Parallel top-level KDWP package | **CONFIRMED / NONCANONICAL** | `connectors/kdwp/` contains a placeholder package and compatibility READMEs; its own documentation points canonical work here. |
| Flora and ERT lanes | **CONFLICTED / NEEDS VERIFICATION** | `connectors/kansas/kdwp_flora/` and `connectors/kansas/kdwp_ert/` exist as sibling documentation lanes, while their final child-versus-sibling placement remains unresolved. A top-level `connectors/kdwp_ert/` compatibility lane also exists. |
| Source identity and activation | **OUTSIDE THIS FOLDER** | Product-level descriptors and activation state belong in governed registry/control-plane surfaces. |
| Policy and publication | **NONE** | Rights, sensitivity, redaction, proof closure, release, correction, and rollback are owned outside the connector. |

This revision records the current layout and conflicts. It does not move a path, bless a compatibility package, or turn a sibling README into an accepted product architecture.

[Back to top](#top)

---

## Status

| Item | Status | Meaning |
|---|---:|---|
| This README | **DRAFT** | Reviewable folder contract; not KFM publication or source activation. |
| Canonical parent lane | **CONFIRMED** | The Kansas connector family and this KDWP path exist in the current repository snapshot. |
| KDWP product inventory | **NEEDS VERIFICATION** | The source catalog names several product classes, but no accepted repository inventory or activation set was verified. |
| Live source access | **DISABLED / NEEDS VERIFICATION** | No product may be fetched merely because this folder exists. |
| Product-level `SourceDescriptor`s | **NOT VERIFIED** | The directly probed `kdwp-sinc` descriptor path was absent, and the machine source-authority register is empty. |
| `SourceDescriptor` schema and role vocabulary | **CONFLICTED** | The populated singular schema self-identifies as legacy; the plural schema is an empty scaffold; narrative doctrine uses different role tokens. |
| Current endpoints, terms, and cadence | **NEEDS VERIFICATION** | KDWP access is described as mixed web, PDF, CSV, request-based, and occasional GIS export; current product details are not accepted here. |
| Public release | **DENY BY DEFAULT** | No connector output is public. Exact sensitive ecological locations and unclear-rights records fail closed. |
| Owner assignment | **UNKNOWN** | The inspected CODEOWNERS file provides only the repository-wide fallback for this path. |

[Back to top](#top)

---

<a id="accepted-inputs"></a>

## What belongs here

Subject to accepted placement and product-level governance, this lane may contain:

- source-family and product navigation;
- opt-in KDWP source clients that remain inactive without an accepted descriptor and activation decision;
- parsers for verified source-native formats such as reviewed HTML tables, PDFs, spreadsheets, delimited files, archives, or GIS exports;
- source-head checks using a supported version, checksum, `ETag`, `Last-Modified`, or documented manual release identifier;
- product dispatch that keeps SINC/listed-status, range, monitoring, stewardship, and review-tool products distinguishable;
- source-native identifier and citation preservation;
- field normalization that does not upgrade or replace source meaning;
- explicit role-mapping helpers after the machine vocabulary is ratified;
- preservation of geometry, coordinate uncertainty, withholding state, and original-versus-public geometry intent;
- preservation of source, observed, valid/effective, retrieval, and correction time where material;
- caller-owned `RAW` or `QUARANTINE` handoff builders;
- process-memory retrieval, probe, denial, or admission receipt candidates that do not claim evidence or release closure;
- references to small, synthetic, redacted, generalized, or rights-reviewed no-network fixtures in the repository's accepted fixture/test home;
- compatibility adapters whose only purpose is a transparent migration from noncanonical KDWP paths.

No item in this list is evidence that the corresponding implementation already exists.

[Back to top](#top)

---

<a id="exclusions"></a>

## What does not belong here

This folder must not own or imply authority over:

- a single all-purpose descriptor for “KDWP” as an institution;
- source activation or product admission decisions;
- `SourceDescriptor` instances or source-authority registry entries;
- canonical object contracts, machine schemas, or source-role vocabulary decisions;
- rights, sensitivity, redaction, access, or public-precision policy;
- taxonomy-backbone decisions;
- legal-status determinations created by KFM rather than preserved from a cited KDWP product;
- public ecological-review decisions or an operational Ecological Review Tool service;
- public exact locations for sensitive taxa, nests, dens, roosts, hibernacula, spawning sites, rare plants, sacred places, private-land records, or sensitive facilities;
- emergency, closure, hunting/fishing, or life-safety advisory authority;
- direct writes to `WORK`, `PROCESSED`, `CATALOG`, `TRIPLET`, `PUBLISHED`, proof, or release stores;
- EvidenceBundle, proof-pack, catalog, release-manifest, correction, or rollback authority;
- public APIs, map layers, tiles, summaries, dashboards, or AI answers;
- credentials, tokens, cookies, private URLs, or unreviewed source payloads;
- independent evolution of `connectors/kdwp/`, `connectors/kdwp_ert/`, or another compatibility path as a second canonical KDWP implementation;
- generated language presented as regulatory, occurrence, range, habitat, sensitivity, or release truth.

A retrieved file is not an admitted source. An admitted source is not validated evidence. Validated evidence is not a released public claim.

[Back to top](#top)

---

<a id="admission-posture"></a>

## Inputs

A connector operation requires product-specific, reviewable inputs:

| Input | Required posture |
|---|---|
| Product identity | Stable KDWP program/product identity; do not use agency name alone. |
| `SourceDescriptor` reference | Resolvable to the accepted descriptor for the exact product and version. |
| Activation state | Explicitly allows the requested fixture-only, restricted, or live operation. |
| Access surface | Reviewed URL, file, archive, request workflow, or service definition; credentials supplied only through approved secret handling. |
| Rights state | Current terms, attribution, redistribution, and downstream-use limits. Unknown rights fail closed. |
| Sensitivity state | Dataset and record-level sensitivity inputs, including steward-controlled or exact-location restrictions. |
| Source role mapping | Product/record meaning mapped through the accepted machine vocabulary; never inferred from filename or convenience. |
| Source head | Upstream version, release date, checksum, or other reproducible identity evidence. |
| Temporal context | Source/release time and, where applicable, observation and validity/effective time. |
| Caller-owned handoff | Explicit `RAW` and `QUARANTINE` sinks or envelope interfaces; no implicit filesystem destination. |

Typical product material is described in [KDWP product and role boundaries](#kdwp-product-and-role-boundaries). Each product is governed independently.

[Back to top](#top)

---

## Outputs

Permitted connector outputs are narrow and caller-owned:

1. **A `RAW` handoff candidate** that preserves the immutable or reproducibly referenced source payload, source head, product identity, retrieval time, checksum, descriptor reference, and admission metadata.
2. **A `QUARANTINE` handoff candidate** with a structured reason when rights, role, identity, taxonomy, geometry, sensitivity, temporal support, source shape, or activation is unresolved.
3. **A process-memory receipt candidate** for retrieval, probe, denial, no-op, or handoff behavior when the accepted receipt contract provides one.
4. **A deterministic operational failure** when the connector cannot safely produce one of the governed outcomes above.

The exact DTOs, reason-code vocabulary, sink protocol, idempotency contract, and receipt type are **PROPOSED / NEEDS VERIFICATION**. This README does not mint them.

The connector must not emit a processed record, EvidenceBundle, public geometry, catalog item, triplet, released layer, public answer, or publication decision.

[Back to top](#top)

---

## Validation

### Admission and record checks

Before any implementation can be treated as active, tests and validators must cover at least:

- product-level descriptor resolution and activation;
- no-network default behavior;
- source-head and retrieval identity preservation;
- checksum or immutable-reference preservation;
- product identity and source-program preservation;
- source-role mapping without mixed-role collapse;
- source, observed, valid/effective, retrieval, and correction-time separation where applicable;
- taxon identity, status/rank meaning, authority anchoring, and disagreement preservation;
- geometry validity, coordinate uncertainty, datum/CRS metadata, withholding state, and original-versus-public geometry separation;
- rights, attribution, redistribution, and terms-review state;
- rare-species, rare-plant, private-land, cultural, infrastructure, and exact-location negative cases;
- explicit quarantine for unknown rights, unresolved role, unresolved taxonomy/status meaning, malformed identity, unsafe geometry, stale source head, or source-shape drift;
- proof that connector code cannot write beyond caller-owned `RAW` or `QUARANTINE` handoff and process-memory receipt candidates;
- fixture safety: no unreviewed precise ecological location, private record, credential, or unclear-rights payload in the repository;
- refusal to treat compatibility paths as independent canonical implementations;
- success, quarantine/hold, deny/no-activation, no-op, and operational-error paths as applicable to the accepted contract.

### `SourceDescriptor` authority gate

The current repository contains incompatible authority surfaces:

- the draft Source Descriptor Standard uses narrative roles such as `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, and `synthetic`;
- the populated schema at `schemas/contracts/v1/source/source_descriptor.schema.json` declares the plural path canonical and itself legacy, while using machine values such as `regulatory_context`, `observation`, `occurrence_evidence`, and `steward_review_source`;
- the nominal plural-path schema at `schemas/contracts/v1/sources/source_descriptor.schema.json` is an empty `PROPOSED` scaffold;
- the KDWP source catalog includes an illustrative `source_role: regulatory` skeleton that is explicitly not a contract.

> [!WARNING]
> Do not create or activate a KDWP descriptor by copying a narrative role token into a machine record. Resolve schema-home and role-vocabulary authority through the governing contract/ADR process, then update descriptors, fixtures, validators, and this README together.

### Documentation checks for this file

Review should verify:

- one H1 and a coherent heading hierarchy;
- balanced KFM metadata, code fences, tables, callouts, and links;
- preserved `doc_id`, `created` date, final newline, and prior-blob rollback target;
- no remote badge or tracking image;
- no credential, private source URL, specimen record, sensitive locality, or rights-restricted payload;
- current-state claims remain bounded to the pinned repository evidence;
- the diff contains only `connectors/kansas/kdwp/README.md`.

Repository-wide executable validation is not established by this README. The inspected `tools/validate_all.py` and pre-commit configuration are placeholders; trusted CI results must be reported by workflow and scope rather than generalized into runtime proof.

[Back to top](#top)

---

## Review burden

At minimum, substantive connector, descriptor, activation, or product-layout work should involve:

- connector steward;
- Kansas source steward;
- Fauna steward for listed-status, occurrence, mortality, disease, and sensitive-site material;
- Flora steward for rare-plant and listed-plant context;
- Habitat steward for natural-community, habitat, and stewardship layers;
- rights reviewer;
- sensitivity reviewer;
- validation/test steward;
- docs steward.

The inspected `.github/CODEOWNERS` file applies a repository-wide `@kfm/maintainers` fallback but does not assign a connector-specific or KDWP-specific owner. Team existence, ownership assignment, and reviewer availability remain **NEEDS VERIFICATION**; this document does not invent usernames or request reviewers.

Additional governed review is required before:

- approving a live product or source endpoint;
- accepting or changing rights/redistribution posture;
- accepting a source-role machine mapping;
- changing product-lane placement or migrating compatibility code;
- exposing generalized ecological geometry;
- defining the operational tie-breaker among KDWP SINC, NatureServe, KBS NHI, or other authority inputs;
- treating an ERT/review output as support for a public claim;
- treating an ingest receipt as evidence closure or release proof.

[Back to top](#top)

---

## Related folders

| Surface | Relationship | Status in the pinned snapshot |
|---|---|---:|
| [`../README.md`](../README.md) | Kansas connector-family boundary and sublane rules. | **CONFIRMED file / child inventory stale** |
| [`../../README.md`](../../README.md) | Connector-root source-admission boundary. | **CONFIRMED file** |
| [`../../kdwp/README.md`](../../kdwp/README.md) | Top-level KDWP compatibility lane. | **CONFIRMED / NONCANONICAL** |
| [`../../kdwp/src/README.md`](../../kdwp/src/README.md) | Compatibility source-layout README. | **CONFIRMED / modules largely unverified** |
| [`../../kdwp/tests/README.md`](../../kdwp/tests/README.md) | Compatibility test contract. | **CONFIRMED / test files unverified** |
| [`../kdwp_flora/README.md`](../kdwp_flora/README.md) | Flora/listed-species sibling lane. | **CONFIRMED file / placement unresolved** |
| [`../kdwp_ert/README.md`](../kdwp_ert/README.md) | Kansas-family ERT/stewardship sibling lane. | **CONFIRMED file / placement unresolved** |
| [`../../kdwp_ert/README.md`](../../kdwp_ert/README.md) | Top-level ERT compatibility lane. | **CONFIRMED / NONCANONICAL** |
| [`../../../docs/sources/catalog/kansas/kdwp.md`](../../../docs/sources/catalog/kansas/kdwp.md) | Human-facing KDWP source-family and product doctrine. | **CONFIRMED file / draft** |
| [`../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md`](../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md) | Narrative descriptor doctrine. | **CONFIRMED file / draft** |
| [`../../../docs/domains/fauna/SOURCES.md`](../../../docs/domains/fauna/SOURCES.md) | Fauna source-family and role crosswalk. | **CONFIRMED file / draft** |
| [`../../../schemas/contracts/v1/source/source_descriptor.schema.json`](../../../schemas/contracts/v1/source/source_descriptor.schema.json) | Populated schema at a self-declared legacy path. | **CONFIRMED file / authority CONFLICTED** |
| [`../../../schemas/contracts/v1/sources/source_descriptor.schema.json`](../../../schemas/contracts/v1/sources/source_descriptor.schema.json) | Nominal canonical-path schema scaffold. | **CONFIRMED file / not enforceable** |
| [`../../../data/registry/sources/README.md`](../../../data/registry/sources/README.md) | Source registry responsibility boundary. | **CONFIRMED file** |
| [`../../../control_plane/source_authority_register.yaml`](../../../control_plane/source_authority_register.yaml) | Machine source-authority register. | **CONFIRMED file / currently empty** |
| [`../../../policy/rights/`](../../../policy/rights/) | Rights decisions and enforcement. | **Outside connector / implementation depth NEEDS VERIFICATION** |
| [`../../../policy/sensitivity/`](../../../policy/sensitivity/) | Sensitivity and redaction policy. | **Outside connector / implementation depth NEEDS VERIFICATION** |
| [`../../../release/`](../../../release/) | Release, correction, withdrawal, and rollback decisions. | **Outside connector** |

[Back to top](#top)

---

## ADRs

- Directory Rules govern the `connectors/` responsibility root, the `RAW`/`QUARANTINE` output boundary, the required folder-README contract, and migration discipline.
- Repository documents repeatedly reference `ADR-0001` for schema-home authority, but the directly probed path `docs/adr/ADR-0001-schema-home.md` was not found. The populated singular schema, empty plural schema, and conflicting narrative vocabulary leave the authority state **CONFLICTED / NEEDS VERIFICATION**.
- No accepted path-specific ADR was verified that resolves:
  - migration of the noncanonical `connectors/kdwp/` package;
  - the final home of Flora-specific KDWP work;
  - the final home of Ecological Review Tool/stewardship-output work;
  - whether compatibility paths remain redirects, mirrors, transitional packages, or are removed.
- This README update does not trigger an ADR by itself: it changes one existing Markdown file, does not move a path, does not create a parallel authority home, and does not change a lifecycle boundary.
- Any later move must preserve history, references, fixtures, tests, descriptors, receipts, deprecation state, validation, and rollback under Directory Rules migration discipline.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Review date | `2026-07-12` |
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Base ref | `main` |
| Pinned base commit | `2b7213e4f3f49e55e1ad1dff306fcce720e8c69f` |
| Prior README blob | `e4c887164772a97ced3097da7e848325b3c56849` |
| README introduction commit | `cc850ced483fbfcfabb93816c35891305c26064e` |
| Review scope | Target README/history; checked placeholder; parent connector docs; KDWP catalog; compatibility package and tests READMEs; KDWP Flora/ERT lanes; Directory Rules; descriptor standard and both schema paths; source-authority register; Fauna source-role doc; contribution guidance; CODEOWNERS; PR template; validation placeholders; branch/PR search |
| Reviewer identity | `OWNER_TBD` — no semantic owner assignment made by this document |

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence basis

| Evidence | What it supports | What it does not prove |
|---|---|---|
| Target blob `e4c887164772a97ced3097da7e848325b3c56849` at the pinned base | Exact editing baseline, current path, stale historical language, and unresolved rollback placeholder. | Runtime, source activation, or product readiness. |
| Introduction commit `cc850ced483fbfcfabb93816c35891305c26064e` | The v0.1 README replaced a blank placeholder; “blank before this update” is historical residue. | That a blank file is now the appropriate rollback. |
| Directory Rules §7.3, §14, and §15 | Connector responsibility, output boundary, migration discipline, and folder-README contract. | Which KDWP products are active or how they are fetched. |
| KDWP source catalog | Parent placement, product classes, Kansas regulatory/stewardship role, sensitivity implications, rights/cadence gaps, and one-product-per-descriptor posture. | Current product terms, machine endpoints, accepted descriptors, or runtime. |
| Current canonical-path probes | This README and `.gitkeep` exist; common package/test paths below this folder were not found. | Complete recursive absence of differently named code. |
| `connectors/kdwp/` package surfaces | A noncanonical compatibility package, placeholder `pyproject.toml`, empty package initializer, and README-only source/test contracts exist. | A functioning parser, client, fixture set, or test suite. |
| KDWP Flora/ERT and top-level ERT READMEs | Multiple product/compatibility documentation lanes exist. | Their final accepted placement or implementation. |
| Source Descriptor Standard and both schema paths | Doctrine and machine-shape surfaces exist but disagree on path and role vocabulary. | An accepted descriptor authority or valid KDWP descriptor. |
| Empty source-authority register and absent probed `kdwp-sinc` descriptor | No accepted KDWP entry was found in the exact inspected authority paths. | Absence from every differently named registry file. |
| Fauna source-role documentation | KDWP-like products require regulatory-versus-observed anti-collapse and rights verification. | Machine enum authority; the doc conflicts with the populated schema. |

Absence claims are bounded to exact paths, searches, and the pinned commit. This README does not assert a complete recursive repository inventory.

[Back to top](#top)

---

## KDWP product and role boundaries

KDWP is an institutional source family. Admission must identify the specific product and what kind of support it provides.

| Product or record class | Human meaning to preserve | Admission posture | Must not become |
|---|---|---|---|
| Endangered, threatened, and SINC lists | Kansas regulatory/listed-status determinations | Product-level descriptor; authority and effective-date preservation; high sensitivity impact. | A field observation or a KFM-created legal determination. |
| SINC ranks for species or natural communities | State-level sensitivity/stewardship input | Preserve rank system, scope, vintage, issuing program, and disagreement with parallel authorities. | Automatic public-location permission or an uncited global rank. |
| KDWP range products | Agency-published regulatory or stewardship spatial context | Preserve product/version, scale, geometry method, caveats, and release limits. | A point occurrence, current population count, or certain habitat occupancy. |
| Survey, monitoring, mortality, disease, eDNA, acoustic, or telemetry records | Agency observation evidence tied to method, place, and time | Preserve event identity, protocol, quality flags, geometry uncertainty, and withholding state. | Regulatory status, public precise location, or complete range truth. |
| Habitat, natural-community, WMA, or stewardship layers | Administrative, stewardship, or contextual spatial material depending on product | Determine role per product; preserve management versus ecological meaning. | A per-place animal/plant occurrence or unrestricted facility inventory. |
| Ecological Review Tool or review outputs | Administrative/regulatory review evidence generated for a bounded request | Preserve request scope, review status, inputs, output version, expiry, and limitations. | A KFM release decision, legal clearance, public occurrence layer, or reusable site truth. |
| Mixed files | Multiple meanings combined in one upstream package | Split into product/record-specific mappings or quarantine until role can be represented safely. | One untyped all-purpose “KDWP” feed. |
| Aggregates or models | Derived summaries, density surfaces, suitability, or other analytical outputs | Preserve aggregation unit or model/run identity, inputs, uncertainty, and receipt references. | A direct observation or regulatory determination. |

Use human descriptions in prose until the accepted machine enum is settled. A product's role is fixed at admission and is not upgraded by promotion.

[Back to top](#top)

---

## `SourceDescriptor` authority conflict

The current repository does not provide one enforceable, internally consistent descriptor authority:

| Surface | Current evidence | Consequence |
|---|---|---|
| Source Descriptor Standard | Draft doctrine with seven narrative role classes. | Useful meaning, but not machine conformance by itself. |
| Singular schema path | Populated Draft 2020-12 schema; its own metadata calls the plural path canonical and the singular path legacy. | Substantive field validation exists, but authority is conflicted. |
| Plural schema path | Empty `PROPOSED` scaffold with unrestricted properties. | Cannot validate a KDWP descriptor. |
| KDWP catalog skeleton | Illustrative `source_role: regulatory`; explicitly “NOT a contract.” | Must not be copied into a live descriptor as if schema-valid. |
| Source-authority register | File exists with `entries: []`. | No machine activation/authority record was verified. |
| Exact `kdwp-sinc` registry probe | Not found at the inspected path. | Descriptor existence remains `NEEDS VERIFICATION`, not disproven globally. |

Until this is resolved:

1. keep live access disabled;
2. do not mint a KDWP descriptor from prose examples;
3. do not silently translate `regulatory` to `regulatory_context`, or `observed` to `observation`/`occurrence_evidence`;
4. preserve product meaning in connector-local intermediate metadata without declaring schema conformance;
5. route candidate records to review or quarantine;
6. resolve the authority conflict through the accepted contract, schema, ADR, fixture, validator, and migration process.

[Back to top](#top)

---

<a id="lifecycle-diagram"></a>

## Lifecycle boundary

```text
KDWP product or release
  -> product-level SourceDescriptor resolution
  -> activation + rights + sensitivity + role gate
  -> source-head verification and connector retrieval
  -> caller-owned RAW handoff
       or QUARANTINE handoff with reason
       plus process-memory retrieval/admission receipt candidate
  -> downstream normalization and validation
  -> PROCESSED
  -> CATALOG / TRIPLET with EvidenceBundle closure
  -> release review and ReleaseManifest
  -> PUBLISHED public-safe derivative
  -> correction / withdrawal / rollback
```

Only source-head verification, retrieval, source-preserving parsing, and the `RAW`/`QUARANTINE` plus process-memory receipt handoff belong to this connector lane. Every later transition is owned by downstream contracts, schemas, policy, pipelines, validators, proof systems, and release controls.

Publication remains a governed state transition. A Git commit, pull request, successful fetch, parser result, or connector receipt is not KFM `PUBLISHED`.

[Back to top](#top)

---

<a id="anti-collapse-rules"></a>

## Anti-collapse and sensitive-data rules

1. **Agency is not product.** “KDWP” is not a sufficient source identity; lists, ranks, ranges, observations, habitat layers, and review outputs require distinct product identities and usually distinct descriptors.
2. **Regulatory determination is not observation.** Listed status and SINC ranks cannot be cited as a field event; an observation cannot be upgraded into legal or regulatory authority.
3. **Range is not occurrence.** A range polygon is spatial context with scale and method, not proof that a taxon occurred at every point.
4. **Review output is not release approval.** An ERT or stewardship review is upstream evidence with a bounded request and expiry; it is not a KFM policy or publication decision.
5. **Rank is not permission.** A sensitivity rank informs downstream restrictions; it never authorizes exact public geometry.
6. **Original geometry is not public geometry.** Precise source geometry remains internal or quarantined when required. A public-safe derivative needs an accepted transform profile, `RedactionReceipt`, review state, and release decision outside this connector.
7. **Origin and distributor stay separate.** Material merely redistributed by KDWP retains the originating source and authority; access path does not mint source authority.
8. **Mixed roles fail closed.** If one source file cannot be mapped without collapsing regulatory, observation, administrative, aggregate, or model meaning, split it or quarantine it.
9. **Authority disagreement remains visible.** KDWP SINC, NatureServe, KBS NHI, federal listings, and taxonomy authorities may disagree. Preserve each assertion and defer operational resolution to the accepted policy/steward process.
10. **Sensitive joins remain sensitive.** Rare species/plants, private parcels, living persons, cultural places, and precise infrastructure can become more revealing through joins; the strictest applicable rule governs.
11. **Operational notices are not life-safety authority.** Closures, seasons, advisories, and similar content require scope/expiry and official-channel redirection; KFM must not substitute for authoritative alerts.
12. **Derived carriers do not become truth.** Aggregates, models, maps, tiles, graphs, search indexes, screenshots, and AI explanations require their own provenance and release state and never replace source evidence.
13. **Retrieval is not admission.** A successful HTTP/file operation does not prove rights, role, validation, evidence closure, or release.
14. **Compatibility is not canonicality.** Existing top-level packages remain compatibility surfaces until an accepted migration changes that status.

[Back to top](#top)

---

## Definition of done

This lane is not ready for active product use until:

- [ ] the current KDWP product inventory is accepted, with one stable product identity per admitted surface;
- [ ] the noncanonical `connectors/kdwp/` package has an accepted migration, redirect, mirror, retirement, or bounded compatibility decision;
- [ ] the placement of Flora and ERT product work is ratified;
- [ ] `SourceDescriptor` schema-home and role-vocabulary conflicts are resolved;
- [ ] product-level descriptors exist in the governed registry and conform to the accepted schema;
- [ ] activation decisions exist for fixture-only, restricted, or live modes;
- [ ] current access methods, endpoints/files, terms, attribution, redistribution, cadence, and source-head methods are verified per product;
- [ ] live network access is disabled by default;
- [ ] source-role, product identity, taxon/status/rank, temporal, rights, geometry, sensitivity, and disagreement behavior is covered by no-network valid and invalid fixtures;
- [ ] exact sensitive geometry, private/cultural/infrastructure details, and unclear-rights material fail closed;
- [ ] connector output is proven to stop at caller-owned `RAW` or `QUARANTINE` and process-memory receipt handoff;
- [ ] no connector path can produce a public claim, map, layer, ERT decision, advisory, EvidenceBundle, or release object;
- [ ] idempotency, retry, no-op, source-drift, correction, and replay behavior is specified and tested;
- [ ] documentation links, owner routing, substantive CI, review records, and rollback evidence are verified.

[Back to top](#top)

---

## Rollback

Before merge, leave the draft pull request unmerged and abandon the scoped branch if the revision is rejected. Closing the pull request or deleting the branch is a separate repository action.

After merge, create a transparent revert commit or revert pull request. Restore the prior README blob:

```text
base commit: 2b7213e4f3f49e55e1ad1dff306fcce720e8c69f
prior blob:  e4c887164772a97ced3097da7e848325b3c56849
path:        connectors/kansas/kdwp/README.md
```

The historical blank placeholder predates introduction commit `cc850ced483fbfcfabb93816c35891305c26064e`; returning to blank is not the default rollback for this revision.

Re-run applicable documentation and connector-boundary validation after rollback. Do not reset, force-push, or rewrite shared history.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Evidence needed |
|---|---:|---|
| Complete canonical-path child inventory | **UNKNOWN** | Non-truncated recursive tree or mounted checkout; direct probes currently show README and `.gitkeep` only. |
| Top-level KDWP package disposition | **CONFLICTED** | Accepted ADR/migration note, compatibility class, old→new path map, tests, and rollback. |
| Flora and ERT product placement | **CONFLICTED** | Accepted product-lane convention or path-specific ADR/migration decision. |
| KDWP product/source inventory | **NEEDS VERIFICATION** | Source-steward inventory of lists, ranks, ranges, surveys, habitat, ERT, operational, and other products. |
| Product-level descriptor IDs and homes | **NEEDS VERIFICATION** | Accepted registry entries and schema-valid descriptors. |
| Descriptor schema and role vocabulary | **CONFLICTED** | Accepted ADR/contract; reconciled schemas, standard, fixtures, validator, and migration. |
| Source activation state | **NEEDS VERIFICATION** | Reviewed activation decisions; source-authority register is currently empty. |
| Current access methods and source heads | **NEEDS VERIFICATION** | Product documentation, stable URLs/files, version identifiers, checksums, and probe evidence. |
| Rights, attribution, and redistribution | **NEEDS VERIFICATION** | Current per-product terms and rights review. |
| Cadence, staleness, and correction behavior | **NEEDS VERIFICATION** | Source history, watcher/connector design, and stale/correction tests. |
| Taxonomy, status, rank, and place anchoring | **NEEDS VERIFICATION** | Accepted crosswalk contracts, fixtures, validators, and disagreement reports. |
| Sensitive geometry and public transforms | **NEEDS VERIFICATION** | Policy bundles, transform profiles, negative fixtures, `RedactionReceipt`, and review evidence. |
| ERT/review-output semantics and expiry | **NEEDS VERIFICATION** | Product documentation, contract, fixtures, and steward decision. |
| Output envelopes, reason codes, receipts, and sinks | **UNKNOWN** | Accepted contracts/schemas and caller integration tests. |
| Idempotency, retries, no-op, drift, replay, and correction | **UNKNOWN** | Connector contract and deterministic tests. |
| Substantive package/tests/CI | **UNKNOWN** | Implemented code, fixtures, workflow configuration, and observed results. |
| Connector-specific ownership | **NEEDS VERIFICATION** | Accepted CODEOWNERS or steward assignment. |
| Cross-authority disagreement policy | **NEEDS VERIFICATION** | Steward/policy decision for KDWP SINC, NatureServe, KBS NHI, and federal conflicts. |

[Back to top](#top)

---

## Maintainer note

Keep this lane product-specific, evidence-preserving, policy-subordinate, and reversible. The existence of a KDWP folder does not activate an agency feed; the existence of a status list does not publish a location; the existence of a review output does not approve a project; and the existence of a connector receipt does not close evidence or release.

[Back to top](#top)
