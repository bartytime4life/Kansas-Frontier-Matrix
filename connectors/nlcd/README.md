<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-nlcd-readme
title: connectors/nlcd/ — NLCD README-Only Connector Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Source steward · Connector steward · Habitat land-cover steward · Spatial steward · Rights reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-14
policy_label: public-doctrine; connector-boundary; nlcd; usgs; modeled-classification; placement-open; no-publication
truth_posture: CONFIRMED README-only lane / PROPOSED placement / INACTIVE source authority / IMPLEMENTATION NEEDS VERIFICATION
evidence_snapshot: main@b0bb12c11ca7d28e1d290ea1642a5faf2a537803
related:
  - ../README.md
  - ../usgs/README.md
  - ../usgs/nlcd/README.md
  - ../../docs/sources/catalog/usgs/README.md
  - ../../docs/sources/catalog/usgs/nlcd.md
  - ../../docs/architecture/directory-rules.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../contracts/source/source_descriptor.md
  - ../../control_plane/source_authority_register.yaml
  - ../../data/registry/sources/habitat/nlcd.yaml
  - ../../data/registry/habitat/sources/nlcd.yaml
  - ../../pipelines/domains/habitat/land_cover/README.md
  - ../../pipeline_specs/habitat/land_cover/README.md
tags: [kfm, connectors, nlcd, usgs, land-cover, raster, classification, modeled, source-admission, raw, quarantine, governance]
notes:
  - "This file documents a connector boundary; it does not prove executable NLCD connector code."
  - "The repository also contains connectors/usgs/nlcd/; choosing, merging, or moving these lanes requires an explicit topology decision."
  - "NLCD pixels are modeled/classifier-assigned source values, not direct field measurements."
  - "Native class map, release or collection, epoch, sub-product, raster profile, source locator, and digest remain coupled source identity."
  - "Connector output is limited to RAW or QUARANTINE handoff; this lane cannot activate, promote, or publish data."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NLCD README-Only Connector Boundary

> Boundary for proposed National Land Cover Database (NLCD) source admission at `connectors/nlcd/`. Repository evidence at the pinned snapshot proves this README, not a runnable connector. A second README-only boundary exists at `connectors/usgs/nlcd/`; this document does not choose between them.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Implementation: not proven" src="https://img.shields.io/badge/implementation-not__proven-lightgrey">
  <img alt="Placement: open" src="https://img.shields.io/badge/placement-open-orange">
  <img alt="Source role: modeled classification" src="https://img.shields.io/badge/source__role-modeled__classification-red">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Truth posture:** `CONFIRMED` README-only boundary · `PROPOSED` connector placement · source authority `INACTIVE / NOT ESTABLISHED` · executable implementation `NEEDS VERIFICATION`.

> [!CAUTION]
> NLCD classifications are modeled or classifier-assigned source values. They are not direct field measurements, regulatory wetland determinations, crop-specific CDL truth, or habitat assertions by themselves.

**Quick jumps:** [Purpose](#1-purpose) · [Status](#3-status) · [Validation](#8-validation) · [Topology](#connector-topology-and-placement) · [Semantic boundary](#nlcd-semantic-boundary) · [Runtime contract](#proposed-runtime-contract) · [Evidence](#evidence-ledger) · [Backlog](#verification-backlog)

---

## 1. Purpose

`connectors/nlcd/` defines a conservative source-admission boundary for NLCD raster packages and their source metadata.

If executable code is later approved here, it may discover or retrieve an explicitly configured NLCD object, preserve its native bytes and identity, validate only admission preconditions, and hand the result to a domain-owned `RAW` or `QUARANTINE` lane. This README does not activate a source, select a live endpoint, or establish that such code already exists.

The boundary is deliberately narrow:

```text
configured source object
        |
        v
NLCD connector admission
        |
        +----> RAW         only when admission preconditions pass
        |
        `----> QUARANTINE  when identity, integrity, rights, class-map,
                           raster-profile, or routing evidence is unresolved
```

[Back to top ↑](#top)

---

## 2. Authority level

**Authority: IMPLEMENT boundary documentation; no source or publication authority.**

This README may describe what a future connector at this path is allowed to do. It may not:

- ratify `connectors/nlcd/` as the canonical NLCD home;
- supersede the parallel `connectors/usgs/nlcd/` boundary;
- activate NLCD in the source-authority register;
- select between conflicting SourceDescriptor schema locations;
- make either existing Habitat registry placeholder authoritative;
- define NLCD product truth, class semantics, or crosswalk truth;
- define Habitat land-cover observations or habitat claims;
- promote data beyond source admission;
- create release authority or public behavior.

The two Directory Rules copies agree on the connector lifecycle limit but differ in version and status. This README relies only on their shared rule: connectors fetch and parse source material and may write to `RAW` or `QUARANTINE`, not later lifecycle stages. It does not decide which Directory Rules file is authoritative.

---

## 3. Status

| Question | Evidence-backed status |
|---|---|
| Does `connectors/nlcd/README.md` exist? | **CONFIRMED.** |
| Is executable connector code proven in this lane? | **No.** Bounded probes for a package file, module entry points, client, and test README returned no files at the pinned snapshot. |
| Does another NLCD connector boundary exist? | **Yes.** `connectors/usgs/nlcd/README.md` exists and is also documentation-only in bounded probes. |
| Is the canonical connector home resolved? | **No.** The source catalog preserves placement as an open question and names a different alternative path, `connectors/usgs/nlcd_ingester/`, which was not found in a bounded probe. |
| Is `nlcd/` listed in Directory Rules §7.3? | **No.** The listed connector families do not include a top-level NLCD family. |
| Is NLCD activated by the source-authority register? | **No.** The register is `PROPOSED` and its `entries` list is empty. |
| Is a mature, authoritative NLCD SourceDescriptor proven? | **No.** Two Habitat-path YAMLs are `PROPOSED` placeholders and registry topology is itself unresolved. |
| Are downstream land-cover code and publication proven? | **No.** The inspected pipeline and pipeline-spec pages are draft documentation and explicitly leave executable behavior, activation, CI, and release wiring unverified. |

Absence statements above are limited to named repository paths inspected at `main@b0bb12c11ca7d28e1d290ea1642a5faf2a537803`; they are not claims of an exhaustive recursive inventory.

---

## 4. What belongs

If this path is ratified, it may contain connector-local artifacts such as:

- request or object-discovery adapters that take an approved SourceDescriptor reference;
- resumable retrieval helpers with bounded timeouts and retries;
- checksum, content-length, and source-fingerprint verification;
- lossless capture of source sidecars and metadata;
- raster-profile inspection for admission routing;
- native class-map extraction without semantic rewriting;
- deterministic RAW or QUARANTINE handoff envelopes;
- sanitized receipts that reference, rather than redefine, governing records;
- no-network fixtures representing approved structural cases;
- unit and contract tests for the admission boundary.

Every artifact must preserve source identity and fail closed when required evidence is missing or contradictory.

---

## 5. What does NOT belong

| Excluded responsibility | Governing surface or next decision |
|---|---|
| Canonical connector placement | Directory decision or accepted ADR; do not infer from current duplicate paths. |
| NLCD source-family and product doctrine | `docs/sources/catalog/usgs/nlcd.md` and its owning catalog hierarchy. |
| Source activation | `control_plane/source_authority_register.yaml` plus an approved SourceDescriptor and review process. |
| SourceDescriptor schema authority | Resolve the documented singular/plural schema conflict outside this README. |
| Registry topology authority | Resolve duplicate Habitat registry layouts and product/family placement outside this connector. |
| Native class taxonomy | Versioned source class-map evidence; do not recreate it here. |
| Crosswalk policy | Governed domain contracts and review; mappings remain advisory. |
| Land-cover observation semantics | Habitat land-cover contracts and schemas. |
| Normalized or processed rasters | Downstream domain pipelines after admission. |
| Catalog, triplet, tile, or published products | Governed downstream lifecycle and release surfaces. |
| Rights, sensitivity, or public-safety decisions | `policy/` and release review. |
| EvidenceBundle closure | Downstream proof processes. A connector receipt is process evidence only. |
| Public API or UI behavior | Governed application surfaces after publication. |

---

## 6. Inputs

A future connector invocation should accept only explicit, governed inputs. At minimum:

| Input | Required treatment |
|---|---|
| SourceDescriptor reference and revision | Required before retrieval; must resolve to an approved source identity and activation posture. |
| Product identity | Preserve product, sub-product, release or collection, epoch, and class-map version as applicable. |
| Approved source locator | Treat as configuration, not a hard-coded claim in this README. Redact credentials and sensitive query material. |
| Expected object identity | Preserve filename or object key, expected size when known, checksum algorithm and digest when known, and source metadata. |
| Retrieval policy | Bound timeouts, retries, redirects, maximum object size, and resume behavior. |
| Routing context | Name the owning domain and proposed RAW/QUARANTINE destination without granting downstream promotion. |
| Rights and attribution reference | Carry governing record identifiers and unresolved review state; do not decide rights locally. |

Live endpoints, current product suites, formats, cadence, coverage, resolution, and access requirements are version-sensitive external facts. They must be verified in product-specific evidence before implementation or activation; this README intentionally does not pin them.

---

## 7. Outputs

The connector may emit only an atomic source-admission handoff to one of:

```text
data/raw/<owning-domain>/<source-id>/<run-id>/
data/quarantine/<owning-domain>/<source-id>/<run-id>/
```

The exact layout remains subject to governing repository contracts. Conceptually, a handoff should include:

- byte-preserving source payload or an immutable reference permitted by policy;
- source sidecars and native metadata;
- a sanitized request/retrieval manifest;
- product, release or collection, epoch, sub-product, and class-map identity;
- raster profile captured without resampling or reclassification;
- source and content fingerprints;
- observed size and checksum results;
- retrieval timestamps and bounded retry history;
- rights, attribution, and sensitivity references or unresolved flags;
- validation results and deterministic quarantine reasons;
- owning-domain routing and run identity.

The connector must not emit directly to `WORK`, `PROCESSED`, `CATALOG`, `TRIPLETS`, `PUBLISHED`, release, API, or UI surfaces.

---

## 8. Validation

Validation is admission validation, not scientific validation or publication approval.

### Required checks

- source identity and SourceDescriptor revision resolve and are approved for use;
- product, sub-product, release or collection, epoch, and native class-map identity are present where applicable;
- retrieval follows configured scheme, host, redirect, timeout, retry, and size constraints;
- payload is complete and content digest is recorded;
- archive members, if any, are bounded and safe to materialize;
- raster profile can be read without mutation;
- CRS, dimensions, band count, data type, nodata, transform, extent, and native resolution are captured;
- source sidecars and class metadata are retained;
- class codes remain native and unmapped at admission;
- modeled/classifier-assigned source role is retained;
- rights, attribution, sensitivity, and routing references are present or the object is quarantined;
- output destination is limited to RAW or QUARANTINE;
- logs and receipts contain no credentials, signed URLs, or unsafe payload excerpts.

### Quarantine conditions

Quarantine on missing, ambiguous, or conflicting evidence, including:

- unresolved source or product identity;
- missing release, epoch, or class-map identity needed to interpret codes;
- checksum or size mismatch;
- unreadable, truncated, or structurally unsafe content;
- unexpected raster profile or unexplained sidecar conflict;
- silent class-map change across releases;
- unresolved rights, attribution, sensitivity, or routing posture;
- unsupported format or response shape;
- duplicate identity with different bytes;
- any attempt to treat the connector as promotion or publication authority.

### No-network test posture

Tests should be deterministic and no-network by default. Fixtures should cover, at minimum:

- one structurally valid raster package and native class map;
- checksum and size mismatch;
- missing or contradictory epoch/class-map metadata;
- changed class labels or codes between versioned fixtures;
- unreadable or unsafe archive content;
- unexpected CRS, nodata, or band structure;
- duplicate source identity with identical bytes and with conflicting bytes;
- rights or routing state that forces quarantine;
- log-redaction behavior;
- rejection of every output destination beyond RAW or QUARANTINE.

---

## 9. Review burden

Changes here require review proportional to their effect:

| Change | Minimum review burden |
|---|---|
| README clarification with no authority change | Connector steward and docs review. |
| Placement, rename, merge, or removal of either NLCD lane | Architecture/governance review and accepted topology decision. |
| New endpoint, credential flow, or retrieval behavior | Source steward, security review, rights review, and no-network tests. |
| New product, release family, format, or class map | Source steward, domain steward, spatial review, and versioned fixtures. |
| Change to hashes, deduplication, replay, or quarantine rules | Data/validation review with deterministic regression tests. |
| Crosswalk or semantic interpretation | Habitat land-cover contract review; never connector-only approval. |
| Activation, promotion, or public use | Source authority, policy, proof, and release review outside this lane. |

`OWNER_TBD` must be replaced before operational activation. The global CODEOWNERS file does not establish a connector- or NLCD-specific owner at the pinned snapshot.

---

## 10. Related folders

| Path | Relationship |
|---|---|
| [`../README.md`](../README.md) | Root connector boundary and RAW/QUARANTINE limit. |
| [`../usgs/README.md`](../usgs/README.md) | USGS connector-family coordination boundary. |
| [`../usgs/nlcd/README.md`](../usgs/nlcd/README.md) | Parallel README-only NLCD connector boundary; topology unresolved. |
| [`../../docs/sources/catalog/usgs/README.md`](../../docs/sources/catalog/usgs/README.md) | USGS source-family catalog context. |
| [`../../docs/sources/catalog/usgs/nlcd.md`](../../docs/sources/catalog/usgs/nlcd.md) | Draft NLCD product doctrine and open placement questions. |
| [`../../data/registry/sources/habitat/nlcd.yaml`](../../data/registry/sources/habitat/nlcd.yaml) | PROPOSED subtype-first registry placeholder. |
| [`../../data/registry/habitat/sources/nlcd.yaml`](../../data/registry/habitat/sources/nlcd.yaml) | PROPOSED domain-first registry template; not selected here. |
| [`../../pipelines/domains/habitat/land_cover/README.md`](../../pipelines/domains/habitat/land_cover/README.md) | Draft downstream pipeline boundary; not connector implementation proof. |
| [`../../pipeline_specs/habitat/land_cover/README.md`](../../pipeline_specs/habitat/land_cover/README.md) | Draft declarative spec boundary; named executable specs remain unproven. |
| [`../../contracts/domains/habitat/land_cover/class_scheme.md`](../../contracts/domains/habitat/land_cover/class_scheme.md) | Draft class-scheme semantics. |
| [`../../contracts/domains/habitat/land_cover/crosswalk.md`](../../contracts/domains/habitat/land_cover/crosswalk.md) | Draft crosswalk semantics. |
| [`../../contracts/domains/habitat/land_cover/observation.md`](../../contracts/domains/habitat/land_cover/observation.md) | Draft land-cover observation semantics. |
| [`../../tests/domains/habitat/land_cover/class_scheme/README.md`](../../tests/domains/habitat/land_cover/class_scheme/README.md) | Test intent; not executable-test proof by itself. |
| [`../../fixtures/domains/habitat/land_cover/class_scheme/README.md`](../../fixtures/domains/habitat/land_cover/class_scheme/README.md) | Fixture intent; not source authority. |

---

## 11. ADRs

- [`../../docs/adr/README.md`](../../docs/adr/README.md) is the ADR index and process surface.
- [`../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md`](../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md) records the connector-output proposal; its draft/proposed state does not independently create authority.
- No accepted NLCD placement ADR was identified in the bounded evidence review.
- [`../../docs/registers/DRIFT_REGISTER.md`](../../docs/registers/DRIFT_REGISTER.md) had no `NLCD`, `nlcd`, `USGS`, or `MRLC` text match in a bounded scan. That does not mean the duplicate-lane drift is resolved or exhaustively audited.

Required decisions before implementation or activation:

1. Choose the canonical connector topology: top-level `nlcd`, nested `usgs/nlcd`, the catalog-named `usgs/nlcd_ingester`, or another ratified path.
2. Choose the canonical registry topology and source-family ownership.
3. Resolve SourceDescriptor schema authority.
4. Record migration and compatibility handling for every non-canonical path.
5. Define owners, source activation, rights, validation, and rollback gates.

This README does not pre-decide any of those outcomes.

---

## 12. Last reviewed

**2026-07-14**, against repository snapshot `main@b0bb12c11ca7d28e1d290ea1642a5faf2a537803`.

Review scope was bounded to the named connector, catalog, rules, authority, registry, schema, pipeline, contract, test, fixture, policy, ADR, drift, ownership, and workflow surfaces cited here. Re-review after any topology decision, source activation, schema migration, endpoint change, class-map change, rights change, or executable implementation.

---

## Connector topology and placement

Three different connector homes appear in repository evidence:

| Path | Observed state | Interpretation |
|---|---|---|
| `connectors/nlcd/` | This README exists. Named implementation probes found no code or test surface. | Proposed flat product lane. |
| `connectors/usgs/nlcd/` | A second README exists. Named implementation probes found no code or test surface. | Proposed nested USGS product lane. |
| `connectors/usgs/nlcd_ingester/` | Named by the draft source catalog; bounded README probe found no file. | Documented alternative, not proven repository implementation. |

Directory Rules §7.3 does not list `nlcd/` as a connector family. The presence of either README therefore demonstrates documentation placement, not canonicality. Do not copy code across both lanes, split responsibilities between them, add redirects, or delete either path until an explicit topology decision defines migration and compatibility behavior.

---

## NLCD semantic boundary

### Modeled classification, not observation

Every admitted pixel must retain a source role equivalent to **modeled/classifier-assigned classification**. A pixel value does not by itself prove a field observation, site inspection, species presence, habitat condition, management action, legal designation, or current ground truth.

### Coupled identity

Treat the following as one versioned source identity, not interchangeable metadata:

```text
source + product + sub-product + release/collection + epoch
       + native class-map version + raster profile + object locator
       + source fingerprint + content digest
```

The same numeric class code may not mean the same thing across releases or products. Cross-release comparison requires explicit class-map reconciliation downstream; raw pixel-code equality is insufficient.

### Native classes and advisory crosswalks

- preserve native class codes, labels, color tables, nodata, and source legends;
- never replace native values with a common KFM vocabulary during admission;
- version every crosswalk separately from source bytes and class maps;
- retain unmapped, one-to-many, conditional, and lossy cases;
- treat NLCD-to-CDL, LANDFIRE, GAP, or other mappings as advisory downstream interpretations;
- never allow a crosswalk to conceal a source release or class-map change.

### Required limitation language

- NLCD wetland classes are not regulatory wetland determinations.
- NLCD agriculture classes are not crop-specific Cropland Data Layer truth.
- NLCD land-cover classes do not establish habitat presence, quality, suitability, or occupancy by themselves.
- Confidence, accuracy, or change products may support downstream assessment but do not make the connector proof authority.

---

## Proposed runtime contract

No runtime is proven at this path. If implementation is approved, it should follow these fail-closed phases:

1. **Resolve** an approved SourceDescriptor revision, product identity, and source locator.
2. **Plan** a bounded request without exposing credentials or signed material.
3. **Retrieve** into temporary storage with size, timeout, redirect, and retry limits.
4. **Verify** bytes, digest, response identity, sidecars, and expected source metadata.
5. **Inspect** the raster profile and native class information without resampling or reclassification.
6. **Decide** RAW versus QUARANTINE using deterministic admission rules.
7. **Commit** the handoff atomically so partial objects never appear complete.
8. **Record** sanitized process evidence and source/content fingerprints.

Retry only transient, bounded failures. Do not retry authentication failure, forbidden access, schema or class-map contradiction, unsafe archive structure, deterministic checksum mismatch, or unresolved policy state as though those were transient network errors.

### Idempotency, deduplication, and replay

- source identity is not only a URL;
- a locator with changed bytes must create a new, reviewable source/content identity;
- identical verified bytes may be deduplicated only through a governed immutable-reference mechanism;
- duplicate source identity with conflicting bytes must quarantine;
- replay must pin the SourceDescriptor revision, retrieval policy, class-map identity, validation version, and output target;
- replay must not overwrite prior runs or erase earlier quarantine reasons;
- caches may accelerate retrieval but never substitute for integrity validation or provenance.

---

## Evidence ledger

| Evidence surface | Observed state | What it supports | What it does not support |
|---|---|---|---|
| This README | File exists; prior version was draft. | A documented flat connector boundary. | Code, activation, endpoint access, or canonical placement. |
| `connectors/usgs/nlcd/README.md` | Draft README exists. | A parallel nested boundary. | A resolved topology or runnable connector. |
| Draft NLCD source catalog | Detailed product doctrine with open family/home questions. | Modeled-source and class-map cautions. | Current external endpoint facts or accepted placement. |
| Directory Rules copies | Review/draft copies with shared connector rule. | RAW/QUARANTINE lifecycle limit. | Which rules path is canonical or that NLCD is a listed family. |
| Source-authority register | `PROPOSED`; `entries: []`. | No repository-level NLCD activation at snapshot. | Future activation status. |
| Two Habitat NLCD YAMLs | `PROPOSED` placeholders in competing layouts. | Registry work is immature and topology is unresolved. | Mature SourceDescriptor authority. |
| SourceDescriptor contract/schema surfaces | Contract documents singular/plural conflict; one schema is rich and one permissive scaffold. | Schema authority remains unresolved. | Permission to select a schema here. |
| Habitat land-cover pipeline/spec READMEs | Draft documentation exists. | Intended downstream separation. | Executable pipeline, CI, activation, or release wiring. |
| Land-cover contracts | Draft semantic documents exist; inspected schemas are permissive scaffolds. | Semantic work has named homes. | Enforced runtime contracts. |
| Connector/source-descriptor workflows | Inspected workflows are TODO echo-only stubs. | No meaningful automated gate is proven by those files. | Connector readiness or descriptor conformance. |
| CODEOWNERS | Global placeholder; no NLCD-specific rule identified. | Owner remains unresolved. | Operational accountability. |

---

## Rights, sensitivity, and public safety

Repository documentation is not a substitute for current source terms. Before activation, governing records must verify licensing or terms, attribution, redistribution, caching, service constraints, and any product-specific restrictions.

The connector must:

- carry policy record identifiers and review state;
- quarantine when terms or attribution are unresolved;
- keep credentials, tokens, cookies, signed URLs, and sensitive query strings out of commits, manifests, logs, receipts, and exceptions;
- avoid turning land-cover classifications into public claims about regulated wetlands, crop identity, habitat, species, landowner activity, or compliance;
- defer aggregation, generalization, suppression, and public-safe rendering to governed downstream policy and release controls.

Public availability of a source does not mean connector output is automatically approved for KFM publication.

---

## Activation, promotion, and rollback

### Activation prerequisites

Do not activate this connector until all of the following are true:

- topology and ownership are ratified;
- an authoritative SourceDescriptor and schema path are resolved;
- the source-authority register records an approved NLCD entry;
- product-specific endpoint, format, access, cadence, coverage, resolution, and class-map evidence is current;
- rights, attribution, sensitivity, and public-safety reviews are complete;
- bounded retrieval, integrity, raster-profile, redaction, quarantine, replay, and no-network tests pass;
- RAW/QUARANTINE paths and downstream ownership are approved;
- correction, deactivation, and rollback procedures have named owners.

### Promotion boundary

Successful admission means only that a source object entered RAW with required evidence. It does not mean the object is normalized, scientifically validated, cataloged, released, or public. Every later transition belongs to downstream governed stages.

### Correction and deactivation

If source identity, class semantics, bytes, rights, or validation are later found wrong:

1. stop new admissions for the affected configuration;
2. preserve prior immutable bytes, manifests, and receipts;
3. mark affected runs and downstream dependencies for review;
4. quarantine new or replayed material until the contradiction is resolved;
5. issue correction and release actions through their governing surfaces;
6. reactivate only with a new reviewed configuration or SourceDescriptor revision.

Do not rewrite history, silently replace source objects, or delete evidence to simulate rollback.

---

## Verification backlog

- [ ] Ratify one canonical NLCD connector home and document migration for other paths.
- [ ] Record the duplicate-lane drift or accepted decision in the appropriate governance surface.
- [ ] Replace `OWNER_TBD` with accountable reviewers and CODEOWNERS coverage.
- [ ] Resolve USGS versus MRLC family ownership and the canonical registry layout.
- [ ] Resolve SourceDescriptor schema authority and create a conforming NLCD descriptor.
- [ ] Add an approved NLCD entry to the source-authority register before activation.
- [ ] Verify current source endpoints, access requirements, formats, product suite, cadence, coverage, resolution, terms, attribution, and class maps.
- [ ] Implement bounded retrieval with credential redaction, integrity checks, atomic handoff, and deterministic quarantine.
- [ ] Add no-network fixtures and executable tests for structural, class-map, rights, replay, and failure cases.
- [ ] Replace TODO connector and descriptor gates with meaningful validation before treating CI as readiness evidence.
- [ ] Verify downstream pipeline specifications, implementations, contracts, schemas, proof, release, correction, and rollback wiring independently.

---

## Definition of done

This README update is complete when it accurately preserves the current boundary without claiming implementation. The connector itself is not done until every activation prerequisite and verification item above is resolved through its governing surface.

In all states:

- native NLCD identity and class semantics remain intact;
- modeled classification is never relabeled as direct measurement;
- crosswalks remain explicit, versioned, advisory downstream artifacts;
- wetlands, agriculture, and habitat limitations remain attached;
- connector output stops at RAW or QUARANTINE;
- placement, schema, registry, policy, pipeline, proof, release, API, and UI authority remain outside this folder.

---

## Changelog

### v0.2 — 2026-07-14

- Reframed the path as a README-only proposed connector boundary.
- Surfaced the parallel `connectors/usgs/nlcd/` lane and unresolved catalog placement.
- Added evidence-pinned status for authority, registries, schemas, pipelines, tests, workflows, and ownership.
- Tightened the modeled-classification, class-map, crosswalk, wetlands, agriculture, and habitat limitations.
- Added fail-closed retrieval, quarantine, no-network testing, replay, activation, correction, and rollback requirements.
- Preserved the RAW/QUARANTINE-only lifecycle limit and prohibited publication authority.

### v0.1 — 2026-06-19

- Established the initial NLCD connector-lane documentation.

<p align="right"><a href="#top">Back to top</a></p>
