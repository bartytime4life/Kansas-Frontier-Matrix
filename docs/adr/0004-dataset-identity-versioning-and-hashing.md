<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/5a4e0b41-64f2-4d2f-9f4c-7b9b7b8e6a6a
title: "ADR 0004 — Dataset identity, versioning, and hashing"
type: adr
version: v1
status: draft
owners: kfm-core (TODO: confirm via CODEOWNERS)
created: 2026-03-01
updated: 2026-03-01
policy_label: public
related:
  - docs/adr/0001-*.md (TODO: verify)
  - docs/adr/0002-*.md (TODO: verify)
  - docs/adr/0003-*.md (TODO: verify)
tags: [kfm, adr, identity, versioning, hashing, provenance, promotion-contract]
notes:
  - Establishes the canonical identity + hashing contract required by Promotion Contract Gate A.
  - This ADR is contract-first and intentionally avoids repo-specific commands until verified.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR 0004 — Dataset identity, versioning, and hashing

![status](https://img.shields.io/badge/status-draft-yellow)
![domain](https://img.shields.io/badge/domain-governance%20%2B%20provenance-blue)
![gate](https://img.shields.io/badge/promotion-gate%20A-important)
![hash](https://img.shields.io/badge/hash-sha256-informational)

**Status:** Draft  
**Date:** 2026-03-01  
**Decision type:** Core invariant (IDs / catalogs / trust membrane)

**Quick links:** [Context](#context) · [Decision](#decision) · [Consequences](#consequences) · [Alternatives](#alternatives-considered) · [Rollback](#rollback-plan) · [Verification](#verification-checklist)

---

## Context

KFM requires stable dataset identity and deterministic hashing to support:

- **Promotion Contract Gate A** (identity/versioning) and related gates that require **run receipts**, **artifact digests**, and **promotion manifests** before serving any dataset version to runtime surfaces.
- **Reproducibility** (same inputs + same spec ⇒ same outputs, or the run must record why not).
- **Citations and evidence** (DCAT/STAC/PROV cross-linking and EvidenceRef resolution without guessing).
- **Cacheability** and safe change detection (distinguish “new version” vs “same version” vs “drift”).

This ADR defines the canonical identifier families, naming conventions, versioning scheme, and hashing rules used across:
- dataset registry + onboarding specs,
- PROV run receipts and promotion manifests,
- DCAT/STAC catalogs,
- policy checks and CI drift tests,
- API/UI evidence surfaces and Focus Mode citations.

> NOTE: This ADR records the **contract**. Implementations (CLI utilities, validators, schemas) are expected to conform, but are not assumed to exist unless confirmed in-repo.

---

## Decision

### Decision summary

We adopt the following canonical identity and hashing contract:

1. **Dataset identity uses explicit URI-like identifier families** (dataset, dataset-version, artifact, run, evidence).
2. **Dataset ID (`dataset_id` / `dataset_slug`) is stable, human-readable, and date-free.**
3. **`spec_hash` is deterministic and platform-stable**:
   - `spec_hash = sha256( RFC8785_canonical_json(spec) )`
4. **`dataset_version_id` is immutable** and derived from a stable slice key plus a short, stable hash prefix:
   - `dataset_version_id = <slice_key> "." <spec_hash_short>`
5. **Every artifact (raw, processed, catalogs) is digest-addressed** (sha256) and listed in checksums/receipts/manifests.
6. Promotion outputs MUST include:
   - run receipt(s),
   - checksums,
   - catalog triplet (DCAT + STAC + PROV),
   - promotion manifest referencing all digests.

---

### 1) Identifier families

KFM uses explicit, URI-like identifiers with stable prefixes, avoiding environment-specific hostnames in canonical IDs.

| Family | Purpose | Example |
|---|---|---|
| `kfm://dataset/<dataset_id>` | Stable dataset family identifier | `kfm://dataset/noaa_ncei_storm_events` |
| `kfm://dataset/<dataset_id>@<dataset_version_id>` | Immutable dataset version | `kfm://dataset/noaa_ncei_storm_events@2026-02.abcd1234` |
| `kfm://artifact/sha256:<digest>` | Content-addressable artifact identity | `kfm://artifact/sha256:2222...` |
| `kfm://run/<run_id>` | Pipeline run identity | `kfm://run/2026-02-20T12:34Z.noaa.abcd1234` |
| `kfm://evidence/<...>` | Evidence entrypoint for resolvers | `kfm://evidence/...` |

**Rule:** Canonical IDs MUST NOT embed environment hostnames. Hostnames belong in distribution URLs (DCAT distributions / STAC hrefs), not canonical IDs.

---

### 2) Dataset ID (`dataset_id` / `dataset_slug`)

**Definition:** `dataset_id` is the stable identifier for a dataset family across the entire system (registry, catalogs, UI, citations).

**Rules (normative):**
- MUST be **lowercase**
- MUST use **underscore** separation
- MUST NOT include dates (date belongs to `dataset_version_id`)
- SHOULD include upstream authority when useful
- MUST match a conservative slug pattern (recommended): `^[a-z0-9_]+$`

---

### 3) Spec hash (`spec_hash`)

**Definition:** `spec_hash` is the deterministic identity of the dataset onboarding spec content. It binds:
- upstream configuration,
- normalization rules,
- validation rules,
- output plan,
- policy label intent,
- expected cadence.

**Normative algorithm:**
- Canonicalize the spec using **RFC 8785 canonical JSON**
- Hash the canonical bytes with **SHA-256**
- Store as `spec_hash = "sha256:" + <64-hex>` (lowercase hex)

**Constraints:**
- The `spec_hash` MUST be stable across platforms (OS / language / JSON serializer differences).
- The canonicalized spec used to compute `spec_hash` MUST be stored (or reproducibly generated) so drift can be tested.

> WARNING: Do not hash “pretty-printed” JSON/YAML. Always canonicalize first.

---

### 4) Dataset version ID (`dataset_version_id`)

**Definition:** `dataset_version_id` identifies a specific promoted dataset version. It is immutable and must never be overwritten.

**Normative construction:**

~~~text
dataset_version_id := <slice_key> "." <spec_hash_short>
~~~

Where:
- `slice_key` is a stable, dataset-defined slice identifier (typically a transaction-time bucket such as `YYYY-MM` for monthly cadence, or `YYYY-MM-DD` for daily cadence).
- `spec_hash_short` is the first **8 hex chars** of the full `spec_hash` digest (default), for readability and stable paths.
- The **full** `spec_hash` MUST still be stored in receipts/manifests/catalog metadata.

**Immutability rule:**
- If any promoted artifact digest changes, the system MUST publish a **new** `dataset_version_id` (never overwrite an existing one).
- If the upstream can republish within the same `slice_key`, the dataset MUST use a granular enough `slice_key` or add a deterministic disambiguator.

**Recommended disambiguation (when needed):**

~~~text
dataset_version_id := <slice_key> "." <spec_hash_short> "." <inputs_digest_short>
~~~

Where `inputs_digest_short` is derived from a deterministic digest over the ordered list of raw input digests.

> NOTE: This disambiguation is required only when upstream “same slice” re-issues are possible.

---

### 5) Artifact digests and content addressing

**Digest algorithm:** SHA-256 is the required default for:
- raw acquisitions,
- processed artifacts,
- catalog artifacts (DCAT/STAC/PROV),
- QA reports,
- promotion manifests,
- run receipts.

**Rules (normative):**
- Every processed and catalog artifact MUST have a sha256 digest.
- Every artifact digest MUST be listed in:
  - `checksums.json` for the dataset version folder, and
  - run receipt outputs, and
  - promotion manifest artifacts/catalogs.
- Artifacts SHOULD be referenceable as `kfm://artifact/sha256:<digest>` in PROV.

---

### 6) Canonical storage layout and linkability

Truth-path rule: **the truth path is navigable without a database**.

- Keep manifests and receipts close to artifacts.
- Ensure each promoted artifact is traceable to exactly one producing run receipt.
- Ensure DCAT and/or STAC can discover the run receipt (direct link or bundle pointer).

Example layout (illustrative; actual repo/object store may differ):

~~~text
data/                                                      | # Governed data lifecycle zones (Truth Path) + catalogs + receipts (policy-aware)
├─ raw/                                                     | # Immutable acquisition snapshots (inputs as captured; may be externalized in prod)
│  └─ <dataset_slug>/                                       | # Dataset bucket (stable slug)
│     └─ <acquisition_id>/                                  | # One acquisition event (source snapshot ID; not a DatasetVersion yet)
│        ├─ manifest.json                                   | # REQUIRED: acquisition metadata (source, license snapshot, timestamps, checksums, policy label)
│        └─ artifacts/                                      | # Raw captured artifacts (as received; no normalization guarantees)
│           └─ ...                                          | # Files/blobs from source (format varies; may include compressed bundles)
│
├─ processed/                                               | # Publishable, normalized artifacts for each DatasetVersion (immutable once promoted)
│  └─ <dataset_slug>/                                       | # Dataset bucket (stable slug; matches raw/<dataset_slug>/)
│     └─ <dataset_version_id>/                              | # Version snapshot ID (deterministic; stable reference for consumers)
│        ├─ artifacts/                                      | # Materialized outputs for this version (formats per dataset contract)
│        │  └─ <artifact_name>.<ext>                        | # One output artifact (e.g., geoparquet/cog/pmtiles/json)
│        ├─ checksums.json                                  | # REQUIRED: digests for artifacts (integrity + deterministic verification)
│        └─ qa/                                             | # QA evidence for this version
│           └─ validation_report.json                       | # Machine QA report (checks, metrics, pass/fail, inputs/outputs refs)
│
└─ catalog/                                                 | # Catalog triplet (DCAT/STAC/PROV) + receipts for each DatasetVersion
   └─ <dataset_slug>/                                       | # Dataset bucket (must match processed/<dataset_slug>/)
      └─ <dataset_version_id>/                              | # Catalog snapshot for the same DatasetVersion (must match processed version)
         ├─ dcat.jsonld                                     | # DCAT dataset metadata + distribution links (policy-aware)
         ├─ stac/                                           | # STAC catalog for assets/tiles/partitions
         │  ├─ collection.json                              | # STAC Collection for this DatasetVersion
         │  └─ items/                                       | # STAC Items (granular asset descriptors)
         │     └─ <item_id>.json                            | # One STAC Item (links to assets, checksums, and required fields)
         ├─ prov/                                           | # Provenance bundle(s) describing lineage
         │  └─ bundle.jsonld                                | # PROV JSON-LD bundle (agents/activities/entities + links)
         └─ receipts/                                       | # REQUIRED: execution receipts proving gates passed
            └─ run_receipt.json                             | # Run receipt (who/what/when, inputs/outputs, checks, policy decisions)
~~~

---

### 7) Run receipt and promotion manifest requirements

**Run receipts** MUST enumerate:
- inputs and outputs with digests,
- environment capture (container digest, git commit, parameters digest),
- policy decision reference,
- timestamps.

**Promotion manifests** MUST exist for each promoted dataset version and MUST reference:
- `dataset_slug`, `dataset_version_id`, `spec_hash`,
- all artifacts and digests,
- all catalogs and digests,
- QA summary and report digest,
- policy label and decision id,
- approvals when required.

---

### 8) Drift prevention and CI gates (identity/hashing)

- CI MUST recompute `spec_hash` from the canonical spec and compare to the committed/registered `spec_hash`.
- CI MUST verify artifact digests match `checksums.json`, run receipt outputs, and promotion manifest entries.
- Any change to hashing rules or ID construction MUST be recorded by an ADR and introduced via a reversible migration (dual-read / dual-write) where possible.

---

## Decision diagram

~~~mermaid
flowchart LR
  A[Dataset onboarding spec] --> B[RFC8785 canonical JSON]
  B --> C[spec_hash sha256]
  C --> D[dataset_version_id from slice key and spec_hash prefix]
  D --> E[Pipeline run]
  E --> F[Raw inputs with sha256 digests]
  E --> G[Processed artifacts with sha256 digests]
  G --> H[checksums.json]
  E --> I[Run receipt with inputs outputs env policy]
  G --> J[DCAT STAC PROV catalogs]
  I --> J
  H --> K[Promotion manifest]
  J --> K
  K --> L[Governed API and UI evidence]
~~~

---

## Consequences

### Positive
- Deterministic, stable IDs enable caching, safe incremental refresh, and EvidenceRef resolution without guessing.
- Hashes provide a clear integrity boundary:
  - spec changes are visible (`spec_hash` changes),
  - content changes are visible (artifact digests change),
  - promotion is fail-closed when evidence is missing.

### Negative / costs
- Requires canonicalization tooling (RFC 8785) and golden tests.
- Requires operational discipline: never overwrite a promoted dataset version; publish a new version.
- Version construction needs dataset-specific slice-key decisions (monthly vs daily vs timestamp vs inputs digest).

### Security & governance implications
- Content addressing and receipts improve integrity and accountability.
- Hashes are not secrecy: do not treat digests as access control; enforce `policy_label` at the policy boundary.

---

## Alternatives considered

1. **Manual SemVer per dataset**
   - Pros: familiar
   - Cons: not deterministic; easy to drift; weak binding to content/spec.

2. **Version = git commit**
   - Pros: available
   - Cons: ties identity to repo topology; doesn’t represent upstream acquisition bytes; awkward across forks.

3. **Version = UUID/ULID per run**
   - Pros: unique
   - Cons: not predictable; harms caching/citations; doesn’t encode spec/content relationships.

4. **Only content-hash outputs**
   - Pros: purely content-addressed
   - Cons: hides spec changes and policy/validation changes that still matter.

---

## Rollback plan

If this scheme causes incompatibility with existing published dataset versions:

- Do **not** rename existing published `dataset_version_id`s.
- Introduce a **dual-read** resolver that can interpret:
  - legacy version patterns, and
  - the canonical pattern from this ADR.
- Add a governed migration map (dataset_id + old_version_id → new_version_id) only if required.
- Roll forward by publishing new versions under the new scheme; deprecate old scheme via documentation, not rewrites.

---

## Implementation notes (non-normative)

### Suggested helper behaviors
- Use `spec_hash_short = first 8 hex chars` for path friendliness.
- Always store full `spec_hash` in receipts/manifests/catalog metadata.
- Use sorted, explicit field selection when computing any aggregate digest (inputs digest) to avoid hidden nondeterminism.

### Suggested regex patterns
- `dataset_id`: `^[a-z0-9_]+$`
- `spec_hash`: `^sha256:[0-9a-f]{64}$`
- `dataset_version_id` (default): `^[0-9]{4}(-[0-9]{2}(-[0-9]{2})?)?\.[0-9a-f]{8}(\.[0-9a-f]{8})?$`

---

## Verification checklist

Minimum checks that convert “paper contract” → “enforced invariant”:

- [ ] Dataset registry schema requires `dataset_id`, `spec_ref`, `spec_hash`.
- [ ] RFC 8785 canonicalization implementation exists (or approved library) and has tests.
- [ ] CI has a `spec_hash drift` check (recompute and compare).
- [ ] Run receipt schema validation exists and runs in CI.
- [ ] Promotion manifest validation exists and runs in CI.
- [ ] Artifact digest verification exists (checksums.json vs file bytes).
- [ ] DCAT/STAC/PROV profiles require `kfm:dataset_id` and `kfm:dataset_version_id`.
- [ ] Evidence resolver can resolve at least one EvidenceRef end-to-end for a promoted dataset version.

---

## References (directional)

- KFM Definitive Design & Governance Guide (vNext)
- Tooling the KFM pipeline (promotion + receipts)
- Catalog triplet profiles (DCAT/STAC/PROV)
- RFC 8785: JSON Canonicalization Scheme (JCS)

<a href="#top">Back to top</a># ADR 0004: Dataset Identity, Versioning, and Hashing

- **Status:** proposed

Planned ADR placeholder.
