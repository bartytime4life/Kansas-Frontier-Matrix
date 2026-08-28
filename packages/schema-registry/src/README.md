<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION/packages-schema-registry-src-readme
title: Schema Registry Package Source README
type: readme
version: v1
status: draft
owners: OWNER_TBD
created: NEEDS VERIFICATION — target file existed before this repair but contained only placeholder text
updated: 2026-06-15
policy_label: public
related: [packages/schema-registry/README.md, packages/hashing/README.md, packages/identity/README.md, packages/envelopes/README.md, packages/README.md, docs/doctrine/directory-rules.md, docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md, docs/architecture/contract-schema-policy-split.md, schemas/contracts/v1/, contracts/, policy/, data/receipts/, data/proofs/, release/]
tags: [kfm, packages, schema-registry, src, json-schema, schema-id, canonical-schema, versioning, validation, contracts]
notes: ["Source-directory guide for schema loading and schema-reference helper code.", "This directory may contain source code for read-only schema loading, registry indexing, versioned ID resolution, alias checks, schema-ref validation, hash-adapter helpers, and synthetic fixtures only.", "It must not own canonical schemas, semantic contracts, policy rules, lifecycle data, source registries, receipts, proofs, release decisions, API routes, UI surfaces, source records, or AI truth claims."]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Schema Registry Package Source

Source-code envelope for KFM schema-registry helpers: read-only schema loading, registry indexing, versioned schema ID resolution, alias checks, schema-ref validation, validation-adapter support, and synthetic fixtures.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Implementation: proposed" src="https://img.shields.io/badge/implementation-PROPOSED-orange">
  <img alt="Root: packages" src="https://img.shields.io/badge/root-packages-blue">
  <img alt="Path: src" src="https://img.shields.io/badge/path-src-lightgrey">
  <img alt="Schema home: schemas/contracts/v1" src="https://img.shields.io/badge/schema__home-schemas%2Fcontracts%2Fv1-blue">
  <img alt="Authority: helper only" src="https://img.shields.io/badge/authority-helper__only-lightgrey">
</p>

> [!IMPORTANT]
> **Status:** PROPOSED source-directory README  
> **Path:** `packages/schema-registry/src/README.md`  
> **Owning responsibility root:** `packages/`  
> **Package lane:** `packages/schema-registry/`  
> **Import/package layout:** NEEDS VERIFICATION  
> **Canonical schema authority:** `schemas/contracts/v1/`, not this source tree  
> **Semantic contract authority:** `contracts/`, not this source tree  
> **Policy authority:** `policy/`, not this source tree  
> **Receipt/proof authority:** `data/receipts/` and `data/proofs/`, not this source tree  
> **Release authority:** `release/`, not this source tree  
> **Repo implementation depth:** UNKNOWN for package metadata, import style, tests, CI workflows, schema publication bindings, validation reports, branch protections, and runtime behavior.

## Scope

`packages/schema-registry/src/` is the proposed source-code root for the Schema Registry package.

This directory is for importable helper code used by validators, governed APIs, pipelines, release gates, receipts, proof builders, replay tools, local developer tools, and tests when they need deterministic schema lookup semantics.

This source tree may support helpers for:

- loading JSON Schemas from explicit canonical schema roots in read-only mode;
- resolving versioned schema IDs, `$id` values, aliases, package-resource paths, and local canonical paths;
- checking that schema refs point to admitted canonical schemas rather than ad hoc local copies;
- building in-memory or read-only registry indexes from explicit schema files;
- validating schema documents for stable IDs, draft/version declaration, title, type, status metadata, and expected KFM extension fields when required;
- exposing schema lookup results to validators and release preflight helpers;
- preserving schema path, schema id, schema version, draft, contract ref, content hash, spec hash, and registry index metadata;
- detecting missing schemas, duplicate IDs, stale versions, invalid aliases, hash mismatches, and untrusted roots;
- building deterministic no-network fixtures for valid schemas, missing schemas, duplicate IDs, stale versions, incompatible aliases, invalid refs, and untrusted roots.

This source tree must not author canonical schemas, redefine semantic contracts, decide policy, write schema files as authority, store lifecycle data, write receipts or proofs, approve release, expose public routes, render UI, fetch source data, or generate truth claims.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Schema registry source code may validate machine-shape references during governed workflows. It does not own lifecycle state, source authority, contract meaning, policy decisions, receipt state, proof state, release state, or public truth.

[⬆ Back to top](#top)

---

## Repo fit

```text
packages/schema-registry/src/
```

`packages/` is the responsibility root for shared reusable code. `schema-registry/` is the package segment. `src/` is the source-code envelope.

| Relationship | Expected home | Boundary rule |
| --- | --- | --- |
| Schema-registry source code | `packages/schema-registry/src/` | Loader, resolver, index, schema-ref validation, and hash-adapter helpers only. |
| Importable module | `packages/schema-registry/src/schema_registry/` or repo-confirmed namespace | Package namespace, subject to repo package convention verification. |
| Package entry README | `packages/schema-registry/README.md` | Explains the package as a whole. |
| Canonical JSON Schemas | `schemas/contracts/v1/` | Owns machine-readable schema authority. |
| Semantic contracts | `contracts/` | Owns meaning and normative behavior. |
| Policy rules | `policy/` | Owns policy decisions and obligations. |
| Hash helpers | `packages/hashing/` | Computes schema/spec/content hashes and replay comparisons. |
| Identity helpers | `packages/identity/` | Handles schema ids, object ids, refs, aliases, and deterministic identity grammar. |
| Runtime envelopes | `packages/envelopes/` | Maps validation outcomes into finite governed response envelopes. |
| Validators/tools | `tools/`, `pipelines/`, or repo-confirmed validator roots | May call source helpers but own execution behavior. |
| Lifecycle data | `data/<phase>/` | Owns RAW/WORK/QUARANTINE/PROCESSED/CATALOG/TRIPLET/PUBLISHED state. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Stores validation receipts and proof artifacts. |
| Release decisions | `release/` | Owns promotion, publication, correction, rollback, and supersession. |
| Public API and UI | `apps/`, `ui/`, `web/`, or repo-confirmed equivalents | Consume governed validation status; source internals are not public authority. |
| Tests and fixtures | `tests/packages/schema-registry/`, `fixtures/packages/schema-registry/`, or repo-confirmed equivalents | Proves deterministic behavior with synthetic schema fixtures. |

> [!WARNING]
> A source-code directory is not the schema home. It may load and index schemas; it must not create a parallel canonical schema tree.

[⬆ Back to top](#top)

---

## Accepted inputs

Functions in this source tree should accept explicit values from governed callers. They should not fetch missing facts from source systems, raw stores, hidden globals, UI state, operator memory, or generated language.

| Input family | Accepted examples | Required handling |
| --- | --- | --- |
| Schema location | canonical schema root, explicit schema file paths, package resource root | Read only from supplied/repo-confirmed schema roots. |
| Schema identity | `$id`, versioned id, title, schema draft, alias, package path | Resolve deterministically and detect duplicates. |
| Contract context | contract ref, object family, domain, schema family, compatibility profile | Preserve refs; do not redefine meaning. |
| Validation context | instance type, schema id, validator profile, strictness, draft | Produce validation-ready lookup results. |
| Hash context | schema hash, spec hash, content hash, registry index hash | Consume from hashing helpers or explicit caller input. |
| Release context | release ref, promotion gate, schema version pin, rollback ref | Preserve refs; do not approve release. |
| Fixture context | synthetic valid/missing/duplicate/stale/incompatible schemas and instances | Keep fixtures deterministic and public-safe. |

[⬆ Back to top](#top)

---

## Exclusions

| Do not put here | Correct home or owner | Reason |
| --- | --- | --- |
| Canonical JSON Schema files | `schemas/contracts/v1/` | Schemas need a single canonical home. |
| Semantic contract documents | `contracts/` | Contracts define meaning; schemas define machine shape. |
| Policy rules | `policy/` | Policy owns decisions and obligations. |
| Source descriptors and source registries | `data/registry/` or repo-confirmed registry homes | Source authority is not schema registry authority. |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | `data/<phase>/` | Lifecycle state must remain phase-visible. |
| Receipts, proof packs, validation reports | `data/receipts/`, `data/proofs/` | Trust artifacts must remain separately auditable. |
| Release manifests, rollback cards, correction notices | `release/` | Publication is a governed state transition. |
| Public API routes or serializers | `apps/` or repo-confirmed API app | Public clients must use governed APIs. |
| UI components, dashboards, controls | `apps/`, `ui/`, `web/`, or observability roots | Presentation is downstream from governed validation status. |
| AI-generated schemas as canonical truth | governed intake/review plus schema governance | Generated schema drafts require review before becoming canonical. |
| Secrets, private source content, protected-location examples, real personal/DNA data | Nowhere in package fixtures | Fixtures must remain synthetic or public-safe. |

[⬆ Back to top](#top)

---

## Expected source layout

> [!NOTE]
> The tree below is PROPOSED. Confirm package metadata, language conventions, import namespace, test layout, and CI before committing code beyond README files.

```text
packages/schema-registry/src/
├── README.md                # This file: source-code boundary and trust rules
└── schema_registry/
    ├── README.md            # PROPOSED: importable namespace guide
    ├── __init__.py          # PROPOSED export boundary
    ├── loader.py            # PROPOSED read-only schema loading helpers
    ├── registry.py          # PROPOSED registry/index helpers
    ├── ids.py               # PROPOSED schema id and alias helpers
    ├── validation.py        # PROPOSED schema-ref/registry validation helpers
    ├── hashing.py           # PROPOSED hash adapter helpers
    ├── fixtures.py          # PROPOSED synthetic fixtures
    └── py.typed             # PROPOSED if typed package convention is confirmed
```

Preferred import posture, subject to package verification:

```python
from schema_registry.loader import load_schema_catalog
from schema_registry.registry import SchemaRegistry
from schema_registry.validation import validate_schema_ref
```

[⬆ Back to top](#top)

---

## Schema-registry helper outcomes

| Helper outcome | Use when | Runtime posture |
| --- | --- | --- |
| `RESOLVED` | Schema id/path/alias resolves to one canonical schema. | Candidate for validation; not proof of semantic correctness. |
| `UNRESOLVED` | Schema id/path/alias cannot be found. | Fail closed or abstain depending on caller. |
| `DUPLICATE_ID` | More than one schema claims the same canonical id. | Block validation/release and require review. |
| `STALE_VERSION` | Schema ref points to a superseded or disallowed version. | Block or hold according to caller policy. |
| `HASH_MISMATCH` | Schema content hash/spec hash differs from expected value. | Fail closed and require drift review. |
| `INVALID_SCHEMA` | Schema document itself fails schema-registry checks. | Fail closed with validation metadata. |
| `UNTRUSTED_ROOT` | Schema was requested outside admitted schema roots. | Deny/hold; do not load. |
| `ERROR` | Runtime failure prevents a valid local helper result. | Fail closed with error metadata. |

`RESOLVED` is not proof of truth, contract meaning, policy allow, evidence closure, publication, or release. It only means one schema was located for the supplied ref.

[⬆ Back to top](#top)

---

## Trust-boundary flow

```mermaid
flowchart LR
    A[Validator / pipeline / API caller] --> B[packages/schema-registry/src]
    B --> C[Importable schema-registry helpers]
    C --> D{Schema id / path / alias lookup}
    D -->|RESOLVED| E[Schema lookup result]
    D -->|UNRESOLVED| F[Missing schema metadata]
    D -->|DUPLICATE_ID| G[Drift / conflict metadata]
    D -->|STALE_VERSION| H[Version hold metadata]
    D -->|HASH_MISMATCH| I[Fail-closed drift metadata]
    D -->|INVALID_SCHEMA or ERROR| J[Fail-closed metadata]
    E --> K[Instance validator]
    K --> L[Receipt/proof/release workflows]
    L --> M[Governed API / audit / replay]

    C -. must not author .-> N[Canonical schemas]
    C -. must not define .-> O[Contracts]
    C -. must not decide .-> P[Policy]
    C -. must not write .-> Q[Receipts / proofs]
```

[⬆ Back to top](#top)

---

## Source anti-collapse rules

| Boundary | Preserve as | Never collapse into |
| --- | --- | --- |
| Schema lookup result | Candidate for validation | Contract meaning or public truth |
| Canonical schema root | Read-only input root | Package-owned schema authority |
| Schema id alias | Explicit resolver mapping | Silent path rewrite |
| Registry index | Deterministic local index | Release record or source registry |
| Schema hash | Integrity metadata | Proof of evidence or policy allow |
| Validation adapter | Consumer of schema lookup | Receipt/proof store or public API authority |
| Fixture schema | Synthetic test fixture | Canonical production schema |

[⬆ Back to top](#top)

---

## Development rules

1. Prefer pure functions with explicit schema roots and registry inputs.
2. Preserve schema id, version, draft, contract ref, file path, content hash, spec hash, registry index hash, release ref, rollback ref, and validation profile supplied by callers.
3. Do not make network calls from `src` helpers unless a future ADR explicitly permits constrained schema fetches.
4. Do not read directly from RAW, WORK, QUARANTINE, unpublished candidates, source systems, source credentials, canonical stores outside admitted schema roots, private keys, or model runtimes.
5. Do not write schema files, lifecycle data, release records, receipts, proofs, policy rules, source registries, catalog records, API responses, or UI components.
6. Do not approve release, decide policy, resolve evidence as truth, define contract meaning, or generate public claims.
7. Do not create schemas, contracts, policy source rules, source registries, pipeline DAGs, API routes, public answers, release decisions, key policies, or connector behavior from this source tree.
8. Do not store raw provider payloads, secrets, credentials, private source records, sensitive-location examples, living-person identifiers, DNA/genomic context, or unrestricted sensitive context.
9. Return typed finite outcomes instead of implicit schema allow, warning-only duplicate IDs, hidden hash mismatch, or validation against local ad hoc schema copies.
10. Add deterministic tests for every behavior-changing helper and every negative path.
11. Keep fixtures synthetic, sanitized, and public-safe.

[⬆ Back to top](#top)

---

## Validation checklist

- [ ] Confirm `packages/schema-registry/src/` exists in the mounted repo with this README as its source-directory guide.
- [ ] Confirm package manager and import convention (`pyproject.toml`, package.json, workspace config, or equivalent).
- [ ] Confirm whether this source tree is Python-only, TypeScript-only, or mixed-language.
- [ ] Confirm import namespace and whether it is `schema_registry`, `kfm_schema_registry`, or repo-specific.
- [ ] Confirm owners and CODEOWNERS path coverage.
- [ ] Confirm canonical schema home from ADR-0001 and current repo layout.
- [ ] Confirm schema `$id` conventions, versioning rules, alias rules, and hash expectations.
- [ ] Confirm relationship with validators, `packages/hashing/`, `packages/identity/`, `packages/envelopes/`, receipt/proof homes, and release gates.
- [ ] Confirm tests for `RESOLVED`, `UNRESOLVED`, `DUPLICATE_ID`, `STALE_VERSION`, `HASH_MISMATCH`, `INVALID_SCHEMA`, `UNTRUSTED_ROOT`, and `ERROR` paths.
- [ ] Confirm helpers do not write schemas, receipts, proofs, release manifests, catalog records, API responses, credentials, permissions, UI state, or lifecycle data.
- [ ] Confirm helpers do not load schemas from ad hoc roots unless an ADR or test fixture explicitly admits them.

Suggested inspection commands:

```bash
find packages/schema-registry/src -maxdepth 5 -type f | sort
find schemas/contracts/v1 -maxdepth 5 -type f | sort | head -200
git grep -n "schema_registry\|SchemaRegistry\|\$id\|draft/2020-12\|schemas/contracts/v1\|DUPLICATE_ID\|HASH_MISMATCH" -- packages docs contracts schemas policy tests fixtures tools apps 2>/dev/null || true
git grep -n "from schema_registry\|import schema_registry\|packages/schema-registry/src" -- . 2>/dev/null || true
```

[⬆ Back to top](#top)

---

## Rollback

Rollback is required if this source tree:

- creates a parallel authority home for canonical schemas, contracts, policy, registries, lifecycle data, receipts, proofs, releases, API routes, UI surfaces, credentials, key-management, model runtimes, or source data;
- writes schema files, mutates canonical schema IDs, rewrites aliases, emits receipts/proofs, approves release, or publishes artifacts as a source helper;
- lets public clients or normal UI surfaces access RAW, WORK, QUARANTINE, unpublished candidates, source systems, direct model outputs, or unreleased artifacts;
- treats schema resolution as proof of truth, evidence closure, admissibility, public safety, policy allow, or release;
- hides duplicate IDs, schema drift, stale versions, hash mismatches, or untrusted roots behind warning-only logs;
- stores secrets, credentials, private source records, real living-person identifiers, DNA/genomic context, or protected-location examples in fixtures.

Rollback target: revert the schema-registry source PR, keep any generated audit notes as review evidence, and file the affected behavior in `docs/registers/DRIFT_REGISTER.md` or `docs/registers/VERIFICATION_BACKLOG.md` if the mounted repo uses those registers.

[⬆ Back to top](#top)

---

## Evidence boundary

| Source | Status | Supports | Limits |
| --- | --- | --- | --- |
| Current target file | CONFIRMED | `packages/schema-registry/src/README.md` existed and required replacement from placeholder content. | Did not prove source implementation maturity. |
| Parent package README | CONFIRMED repo doc | `packages/schema-registry/` is a shared helper-code package for canonical JSON Schema loading, indexing, serving, and versioned ID resolution. | Does not prove source files, package metadata, tests, or CI. |
| `packages/README.md` | CONFIRMED repo doc | `packages/` is for shared libraries used by apps, workers, pipelines, and tools. | Does not define this source namespace. |
| `docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md` | CONFIRMED repo search result | ADR exists stating schema home convention. | Content was not re-read in full for this source README pass. |
| Current file-generation pass | CONFIRMED request | User-requested target path and README repair/replacement. | Does not inspect package metadata, tests, CI logs, dashboards, deployment posture, validator behavior, or branch protection. |

[⬆ Back to top](#top)
