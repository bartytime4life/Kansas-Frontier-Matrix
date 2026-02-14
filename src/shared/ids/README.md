# 🧭 KFM Shared IDs (`src/shared/ids`)

![governance](https://img.shields.io/badge/governance-governed-critical)
![policy](https://img.shields.io/badge/policy-fail--closed-important)
![ids](https://img.shields.io/badge/ids-deterministic%20%2B%20stable-blue)

Central, shared **identifier + addressing** rules for Kansas Frontier Matrix (KFM).

This directory exists so **every layer** (pipelines, catalogs, APIs, UI/Focus Mode, and governance tooling) agrees on:
- *What an ID means*
- *How it is constructed*
- *How it is validated*
- *How it becomes resolvable evidence (URI + resolver contract)*

> [!IMPORTANT]
> IDs are not “just strings” in KFM. They are part of the governance contract:
> - Promotion gates require deterministic checksums and provenance anchors.
> - Evidence UX requires resolvable references (not “some S3 path that might change”).
> - Sensitive assets must not leak precision/PII through identifiers.

---

## Table of contents

- [Purpose](#purpose)
- [Scope](#scope)
- [Non-goals](#non-goals)
- [Design principles](#design-principles)
- [ID taxonomy](#id-taxonomy)
- [Canonicalization & hashing](#canonicalization--hashing)
  - [`spec_hash` (deterministic build spec identity)](#spec_hash-deterministic-build-spec-identity)
  - [Artifact / record checksums](#artifact--record-checksums)
  - [Evidence bundle digest addressing](#evidence-bundle-digest-addressing)
- [URI schemes & resolvers](#uri-schemes--resolvers)
- [Storage path conventions](#storage-path-conventions)
- [Security & sensitivity rules](#security--sensitivity-rules)
- [Reference implementation contract](#reference-implementation-contract)
- [Cross-language determinism](#cross-language-determinism)
- [Tests & test vectors](#tests--test-vectors)
- [Change control](#change-control)
- [Definition of done](#definition-of-done)
- [Troubleshooting](#troubleshooting)
- [References](#references)

---

## Purpose

Provide a **single authoritative home** for:
1. **Stable identifiers** used in KFM catalogs and APIs (dataset IDs, run IDs, entity canonical IDs, etc.)
2. **Deterministic hashes** that make provenance and reproducibility possible (`spec_hash`, checksums)
3. **Canonical addressing** rules so clients can always answer “where is the evidence?” without relying on implementation-specific storage paths

---

## Scope

This module covers:

- ID *formats*, *validation*, and *parsing*
- Deterministic hashing rules and canonicalization requirements
- Canonical “href/address” strategy (e.g., digest addressing → gateway resolver)
- Shared TypeScript types that enforce correctness at compile time

---

## Non-goals

- Defining database primary key choices (Postgres/Neo4j IDs are infrastructure-layer details)
- Implementing policy engines (OPA/Rego) — we only provide **IDs that policies target**
- Encoding secrets or sensitive information into identifiers (explicitly forbidden)

---

## Design principles

1. **Deterministic where it matters**
   - Anything used for provenance equivalence (e.g., `spec_hash`) must be reproducible byte-for-byte across environments.

2. **Stable & human-meaningful only when safe**
   - Prefer *opaque* identifiers for sensitive domains.
   - Human-friendly slugs are allowed for dataset naming, but must be carefully constrained.

3. **Resolvable evidence references**
   - IDs must map to resolvable URIs or resolver endpoints so a citation can be verified.

4. **Prefix + type safety**
   - Prefer typed wrappers (branded types) to avoid mixing `run_id` with `dataset_id`.

5. **No leakage**
   - Identifiers must not embed precise coordinates, personal data, or access-controlled hints.

---

## ID taxonomy

> [!NOTE]
> KFM documents sometimes use `dataset_id` to mean “dataset slug” (human identifier) and sometimes to mean “stable identifier derived from spec hash.”
> This module makes that explicit by separating **dataset identity** from **dataset version / build identity**.

| Concept | Canonical name | Deterministic? | Example (illustrative) | Primary use |
|---|---|---:|---|---|
| Dataset identity (human stable) | `dataset_slug` | ✅ | `usgs_nhd` | pathing, UI labels, DCAT/STAC IDs |
| Dataset identifier (catalog/API) | `dataset_id` | ✅ | `usgs_nhd` | DCAT dataset key, API routes |
| Dataset build/version identity | `spec_hash` | ✅ | `sha256:4b3f…` | processed folder key, “same build” equivalence |
| Pipeline run identity | `run_id` | ❌ | `run_01J…` | run receipts, PROV activities |
| Evidence bundle identity | `bundle_digest` | ✅ | `sha256:ab12…` | OCI digest addressing of evidence bundles |
| Artifact checksum | `sha256` | ✅ | `sha256:ff09…` | file/asset integrity checks |
| Record checksum | `record_sha256` | ✅ | `sha256:…` | sensitive record control / tamper evidence |
| Entity canonical identity | `canonical_id` | ✅* | `kfm:person:…` | graph entities, STAC item properties |
| Upstream record identity | `source_record_id` | source-defined | `KDHE:12345` | citations and trace-back |

\* Deterministic if minted from stable inputs; if curated/manual, stability is enforced by governance, not math.

---

## Canonicalization & hashing

### `spec_hash` (deterministic build spec identity)

**Normative definition (KFM standard):**

- `spec_hash = sha256(JCS(spec))`
- `spec` MUST be a **schema-defined object**
- `spec` MUST carry:
  - `spec_schema_id`
  - `spec_recipe_version`
- Canonicalization MUST follow **RFC 8785 JCS** (JSON Canonicalization Scheme)

**Why:** Without canonicalization, hashes become incomparable and provenance cannot establish equivalence.

#### Inputs

`spec` should represent “what was built” in a stable way, e.g.:

- dataset identity fields (`dataset_id`/`dataset_slug`)
- source endpoints / parameters (excluding secrets)
- time window or selection criteria
- normalization/transformation recipe version
- expected output formats

#### Output format

This module recommends representing hashes as:
- `sha256:<64 lowercase hex>` (OCI-like form)

…but validators SHOULD accept a plain 64-hex form as well, if encountered in legacy artifacts.

#### Pseudocode

```ts
// Pseudocode (normative behavior; exact API names may differ)
const canonicalJsonUtf8: Uint8Array = rfc8785CanonicalizeToUtf8(spec);
const digestHex: string = sha256Hex(canonicalJsonUtf8);
return `sha256:${digestHex}`;
```

---

### Artifact / record checksums

KFM promotion gates and provenance require deterministic checksums for promoted artifacts.

This module standardizes:
- `sha256:<hex>` as the checksum encoding
- lowercase hex
- UTF-8 normalization for any “text-to-hash” operations (unless hashing raw bytes)

Use cases:
- raw acquisition manifests
- processed asset integrity
- record-level tamper evidence (`record_sha256`)

---

### Evidence bundle digest addressing

Evidence bundles SHOULD be **digest-addressed** (OCI digest identity preferred). Stable retrieval should follow a hierarchy:

1. **OCI digest address** (primary identity)
2. **Stable gateway URL derived from digest** (canonical fetch path)
3. **Storage URLs (S3/GCS paths)** as an implementation detail (never used as stable identifiers)

---

## URI schemes & resolvers

KFM evidence UX requires that every citation reference is resolvable through governed API endpoints.

Supported schemes (conceptual):
- `prov://…`
- `stac://…`
- `dcat://…`
- `doc://…`
- `graph://…`

### Canonical resolver endpoints (recommended contract)

- `GET /bundles/{bundle_digest}` → resolve/stream an evidence bundle by digest  
- `GET /prov/runs/{run_id}` → fetch run receipt / PROV record  
- `GET /dcat/datasets/{dataset_id}` → dataset metadata  
- `GET /stac/collections/{dataset_id}` and `GET /stac/items/{id}` → STAC assets  
- `GET /graph/entities/{canonical_id}` → entity record and provenance links  

> [!IMPORTANT]
> Do not “leak” storage-layer URLs into citations. Citations must remain valid if storage backends change.

---

## Storage path conventions

KFM’s unified “data zones” layout uses:

- `raw/` for immutable snapshots
- `work/` for intermediate
- `processed/` keyed by deterministic identifiers

Recommended platform tree fragment:

```text
data/
  raw/
    <domain>/<source>/<YYYY-MM-DD>/...
  processed/
    <domain>/<dataset_slug>/<spec_hash>/...
prov/
  runs/
    <domain>/<run_id>.json
  bundles/
    <bundle_digest>.manifest.json
bundles/
  <bundle_digest>/   (optional local materialization)
```

This module should provide helpers to **compose and parse** these canonical paths *without* hardcoding backend storage details.

---

## Security & sensitivity rules

### Never encode sensitive information in IDs

IDs must NOT contain:
- precise coordinates or site locations
- personal data (names, email, phone, etc.)
- credentials, tokens, access keys
- internal-only security posture details

### Split public vs restricted assets

Where data is sensitive (e.g., precise archaeology site geometry), assets should be split:
- generalized geometry in public
- precise geometry in restricted store
- access controlled at read time via policy (OPA)

This module contributes by ensuring:
- public IDs do not hint at restricted materialization locations
- restricted assets remain referenced via digest/receipt links that enforce policy at resolver time

---

## Reference implementation contract

> [!NOTE]
> The exact file names may vary by repo, but the **exports** should follow this contract so other modules can depend on stable behavior.

### Required exports (recommended)

#### Types

- `DatasetId` (branded string)
- `DatasetSlug` (branded string)
- `RunId` (branded string)
- `SpecHash` (branded string)
- `Sha256Digest` (branded string)
- `BundleDigest` (branded string)
- `CanonicalId` (branded string)
- `KfmUri` (branded string)

#### Generators / canonicalizers

- `toDatasetSlug(input: string): DatasetSlug`
- `toDatasetId(slug: DatasetSlug): DatasetId`
- `computeSpecHash(spec: unknown, opts?: { schemaId: string; recipeVersion: string }): SpecHash`
- `sha256Digest(bytes: Uint8Array): Sha256Digest`
- `makeRunId()` *(non-deterministic; sortable strongly preferred)*
- `makeKfmUri(kind: "prov"|"stac"|"dcat"|"doc"|"graph", path: string): KfmUri`

#### Validators / parsers (fail-closed)

- `assertDatasetId(x: string): asserts x is DatasetId`
- `parseSpecHash(x: string): SpecHash` *(accepts `sha256:<hex>` and optionally legacy forms)*
- `parseBundleDigest(x: string): BundleDigest`
- `isSha256Digest(x: string): boolean`

#### Path builders (pure, no IO)

- `processedPath(args: { domain: string; datasetSlug: DatasetSlug; specHash: SpecHash }): string`
- `provRunPath(args: { domain: string; runId: RunId }): string`

---

## Cross-language determinism

Because KFM pipelines and services may be implemented in multiple languages, the spec-hash algorithm must produce identical outputs in:

- TypeScript/Node
- Go (backend services)
- Python (data tooling)

### Minimum requirement

Maintain a `test-vectors.json` (or `.yaml`) with:
- input `spec` objects
- expected canonical JCS string (optional but recommended)
- expected `spec_hash`

Then each language implementation must run the same vectors.

---

## Tests & test vectors

### Unit tests (must-have)

- `computeSpecHash()` returns expected value for test vectors
- validators reject malformed IDs (fail-closed)
- parsers are strict about allowed alphabets and separators
- path builders are stable and do not normalize away meaningful characters incorrectly

### Integration/contract tests (recommended)

- A sample run receipt can be created and linked to:
  - a bundle digest
  - a processed path keyed by `spec_hash`
  - a resolvable URI

---

## Change control

IDs are governed artifacts. Changes to any ID format, canonicalization rule, or resolver mapping must:

1. Be versioned (semver recommended)
2. Include a migration strategy (if breaking)
3. Update test vectors
4. Update this README
5. Pass CI policy gates

> [!WARNING]
> Never silently change canonicalization rules. That creates “hash drift” and breaks provenance equivalence.

---

## Definition of done

- [ ] All new/changed ID functions have unit tests
- [ ] Test vectors updated (and verified in other language implementations where applicable)
- [ ] Any new ID format includes:
  - [ ] explicit regex/pattern
  - [ ] examples
  - [ ] parser + validator
- [ ] No ID embeds sensitive info
- [ ] Resolver contract documented (what endpoint resolves what ID)
- [ ] Downstream modules updated to use shared functions (no duplicated ad-hoc ID logic)

---

## Troubleshooting

<details>
<summary><strong>My spec_hash differs between environments</strong></summary>

Common causes:
- hashing *non-canonical* JSON (property order differs)
- float/number formatting differences
- Unicode normalization differences
- mixing “pretty JSON” serialization with canonicalization

Fix:
- enforce RFC 8785 JCS canonicalization
- hash UTF-8 bytes of canonical output only
</details>

<details>
<summary><strong>We have a storage URL, but no stable evidence reference</strong></summary>

KFM requires digest/receipt-based addressing. Storage URLs must be treated as implementation detail.

Fix:
- publish an evidence bundle (OCI) and use its digest as canonical identity
- add `/bundles/{digest}` resolver support
</details>

---

## References

### Internal KFM sources (governed)

- **KFM Comprehensive Data Source Integration Blueprint v1.0 (2026-02-12)**
  - Non-negotiables: trust membrane, fail-closed, promotion gates, cite-or-abstain
- **KFM Integration Report for KFM New Ideas 2-8-26 (2026-02-12)**
  - `spec_hash` standardization (`sha256(JCS(spec))`, RFC 8785, schema + recipe version)
  - digest addressing hierarchy + canonical resolver contract (`/bundles/{digest}`)
  - platform tree conventions (`processed/<domain>/<dataset_slug>/<spec_hash>/...`)
- **KFM Next-Gen Blueprint & Primary Guide v1.2 (internal draft)**
  - resolvable reference schemes (`prov://`, `stac://`, `dcat://`, `doc://`, `graph://`)
- **Integrating “New Ideas Feb-2026” Into Knowledge-First Management**
  - spec_hash standard entry + acceptance harness expectations

### External standards

- RFC 8785 — JSON Canonicalization Scheme (JCS)
- SHA-256 (FIPS 180-4)
- OCI image/spec digest conventions (`sha256:<hex>`) for bundle addressing

---

