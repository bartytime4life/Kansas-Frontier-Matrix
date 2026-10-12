<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/catalog-trust-extension
title: Catalog Trust Extension Contract
type: semantic-contract
version: v0.1.0
status: draft; DRAFT_SCHEMA; fixture-first; non-authoritative
owners: OWNER_TBD — Catalog steward · Evidence steward · Source steward · Contract steward · Schema steward · Validation steward · Release steward
created: 2026-08-08
updated: 2026-08-08
policy_label: public; catalog; stac; dcat; prov; provenance; source-role; no-publication-authority
owning_root: contracts/
responsibility: Define the semantic meaning and authority boundary of the shared catalog trust-extension payload.
truth_posture: PROPOSED semantic contract and schema; CONFIRMED synthetic validation evidence; cite-or-abstain
related:
  - ./README.md
  - ../../docs/standards/STAC_KFM_PROFILE.md
  - ../../docs/sources/catalog/README.md
  - ../../schemas/contracts/v1/data/catalog_trust_extension.schema.json
  - ../../tools/validators/catalog_trust_extension/validate_catalog_trust_extension.py
  - ../../fixtures/data/catalog_trust_extension/
  - ../../tests/validators/test_validate_catalog_trust_extension.py
  - ../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, catalog, stac, dcat, prov, run-receipt, proof, trust-class, source-role]
notes:
  - "Realizes Pass 3 card KFM-P3-IDEA-0004 as a bounded shared trust-extension payload."
  - "The extension describes trust context on STAC Items, DCAT Distributions, and PROV Activities; it does not validate the complete host record."
  - "The four source-derived fields remain literal: kfm:run_receipt_ref, kfm:proof_ref, kfm:trust_class, and kfm:source_role."
  - "A valid extension never creates catalog, proof, policy, review, promotion, release, publication, or public-use authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Catalog Trust Extension

> A closed, machine-checkable KFM payload for carrying receipt, proof, trust-class, and source-role context across STAC Items, DCAT Distributions, and PROV Activities without turning catalog metadata into evidence or release authority.

## Status and source-derived requirement

**Status:** `draft` / `DRAFT_SCHEMA` / fixture-first validation.

Pass 3 card `KFM-P3-IDEA-0004` requires KFM catalog carriers to expose four namespaced fields:

| Field | Meaning |
|---|---|
| `kfm:run_receipt_ref` | Link to the run receipt that produced or materially transformed the host artifact. |
| `kfm:proof_ref` | Link to a proof or DSSE-bound proof object when one exists. |
| `kfm:trust_class` | Finite carrier classification: `receipt`, `proof`, `catalog`, or `publication`. |
| `kfm:source_role` | Canonical source role fixed at admission: `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, or `synthetic`. |

This contract realizes only that common payload and the minimum anti-collapse relationships required to validate it. It does not fork STAC, DCAT, or PROV; define a new external standard; register an upstream STAC extension; or claim that existing catalog records conform.

## Responsibility split

| Responsibility | Home |
|---|---|
| Semantic meaning | `contracts/data/catalog_trust_extension.md` |
| Machine shape | `schemas/contracts/v1/data/catalog_trust_extension.schema.json` |
| Deterministic validator | `tools/validators/catalog_trust_extension/` |
| Synthetic fixtures | `fixtures/data/catalog_trust_extension/` |
| Focused tests | `tests/validators/test_validate_catalog_trust_extension.py` |
| Host-profile guidance | `docs/standards/`, including the existing STAC KFM profile |
| Catalog instances | `data/catalog/{stac,dcat,prov,domain}/` after their own governed process |
| Release decisions | `release/`; never this extension |

Directory Rules v2 places semantic meaning under `contracts/`, machine shape under `schemas/`, executable validation under `tools/`, enforceability under `fixtures/` and `tests/`, catalog projections under `data/catalog/`, and release authority under `release/`. No new root or parallel catalog authority is created.

## Object meaning

`CatalogTrustExtension` is a bounded payload attached to or projected from one host catalog record.

| Field | Rule |
|---|---|
| `object_type` | Exactly `CatalogTrustExtension`. |
| `schema_version` | Exactly `1.0.0`. |
| `extension_id` | Stable identity for this extension instance. |
| `host_profile` | One of `STAC_ITEM`, `DCAT_DISTRIBUTION`, or `PROV_ACTIVITY`. |
| `host_record_ref` | Stable reference to the host record; the validator does not dereference it. |
| `namespace` | Exactly `kfm`. |
| `hash_profile` | Exactly `RFC8785-JCS`. |
| `spec_hash` | SHA-256 over RFC 8785 canonical bytes with only `spec_hash` omitted. |
| four `kfm:*` fields | The source-derived trust payload described above. |
| `governance` | Explicit false authority flags proving that this payload cannot self-authorize stronger state. |

The object is intentionally flat at the namespaced field boundary. A host-specific adapter may place the four fields in STAC `properties`, map them to DCAT predicates, or expose them on a PROV Activity, but the adapter must preserve the exact values and source-role meaning.

## Semantic invariants

1. `kfm:run_receipt_ref` is always present.
2. `kfm:proof_ref` is required when `kfm:trust_class` is `proof` or `publication`.
3. A `candidate` source role cannot claim `publication` trust class.
4. Every governance authority flag remains false.
5. `spec_hash` binds the exact extension payload under RFC 8785 JCS.
6. Unknown fields fail the closed schema.
7. Diagnostics report stable codes and JSON-pointer paths, never untrusted values.
8. Validation performs no network access and does not dereference host, receipt, or proof references.

## Trust-class interpretation

| Class | Bounded interpretation | What it does not mean |
|---|---|---|
| `receipt` | The host points to process memory. | Proof closure, catalog closure, or release. |
| `proof` | The host points to a proof reference and run receipt. | Policy approval or publication. |
| `catalog` | The host is represented in a catalog context. | Canonical truth or public release. |
| `publication` | The host describes a separately released/publication-class record. | This extension authorized or performed publication. |

A valid `publication` value is descriptive only. The actual release decision, review, correction path, and rollback target remain outside this object and must resolve through their owning families.

## Host mapping boundary

### STAC Item

The four namespaced fields may be carried under Item `properties`. Full STAC core and extension validation remains the responsibility of the STAC profile and host validator.

### DCAT Distribution

An adapter may map the fields to KFM namespace predicates on a Distribution. RDF syntax, graph consistency, and DCAT conformance remain outside this validator.

### PROV Activity

An adapter may map the fields to KFM namespace predicates on a PROV Activity. PROV entity/activity/agent semantics remain outside this validator.

## Finite validator result

The validator emits:

- `PASS` when closed schema and semantic checks succeed;
- `FAIL` for reviewable schema or semantic violations; and
- `ERROR` when the input or schema cannot be read safely.

A result includes stable finding codes and fields plus `authority_created: false`.

## Non-effects

A valid extension does not:

- validate a complete STAC, DCAT, or PROV record;
- create or resolve a SourceDescriptor, EvidenceBundle, receipt, proof, policy decision, or review record;
- establish catalog closure;
- authorize promotion, release, publication, or public use;
- write to `data/catalog/`, `data/published/`, or `release/`;
- activate a source, connector, watcher, API route, map layer, Evidence Drawer surface, or AI response.

## Review and graduation

Graduation beyond `DRAFT_SCHEMA` requires review of:

- field names and exact source-role vocabulary;
- host-profile adapter mappings;
- reference URI policy;
- whether trust class belongs at host-record, asset/distribution, or both levels;
- schema registry integration;
- policy obligations for publication-class records;
- compatibility with existing STAC KFM profile text; and
- downstream catalog-closure validators.

## Rollback

Before merge, close the pull request and delete its feature branch. After an authorized merge, revert the additive contract/schema/validator/fixture/test/workflow/receipt packet. No catalog record, source, release, API, cache, deployment, or public artifact requires rollback because this slice performs no runtime or lifecycle writes.

<p align="right"><a href="#top">Back to top</a></p>
