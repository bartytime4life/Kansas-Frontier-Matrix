<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/ba77f63c-7663-4431-9049-95386f4377ad
title: tools/hash — Deterministic hashing utilities
type: standard
version: v1
status: draft
owners: KFM Engineering (TBD)
created: 2026-02-22
updated: 2026-02-22
policy_label: public
related:
  - tools/hash
tags: [kfm, tooling, hashing, provenance]
notes:
  - Contract + operator notes for deterministic spec_hash and artifact digests.
[/KFM_META_BLOCK_V2] -->

# tools/hash
Deterministic hashing + canonicalization helpers used for **spec_hash**, **artifact digests**, and promotion/evidence workflows.

**Status:** draft • **Owners:** KFM Engineering (TBD)

![status](https://img.shields.io/badge/status-draft-yellow)
![policy](https://img.shields.io/badge/policy-public-brightgreen)
![hash](https://img.shields.io/badge/hash-sha256-blue)
![canonical-json](https://img.shields.io/badge/canonical_json-RFC_8785_JCS-blueviolet)

---

## Navigation
- [What this is](#what-this-is)
- [Why it exists in KFM](#why-it-exists-in-kfm)
- [Core terms](#core-terms)
- [Hashing contract](#hashing-contract)
- [CLI contract](#cli-contract)
- [Canonicalization rules](#canonicalization-rules)
- [Promotion + catalog integration](#promotion--catalog-integration)
- [Test fixtures](#test-fixtures)
- [Security and governance notes](#security-and-governance-notes)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## What this is
`tools/hash` is intended to host a small utility (library + CLI) that produces **stable hashes** for:

1. **Dataset specifications** → `spec_hash` (deterministic version identity)
2. **Artifacts** (files/bundles) → `sha256:<hex>` digests used in run receipts, promotion manifests, and catalogs

This README is intentionally written as a **contract**: if the implementation changes languages or packaging, the outputs and invariants must remain stable.

<a id="back-to-top"></a>

---

## Why it exists in KFM
KFM’s governance loop depends on predictable identity and evidence integrity:

```mermaid
flowchart TD
  A[Dataset spec JSON] -->|RFC 8785 canonicalize| B[spec_hash = sha256(canonical spec)]
  C[Raw inputs] -->|sha256(bytes)| D[raw artifact digests]
  E[Transforms] -->|sha256(bytes)| F[processed artifact digests]
  B --> G[run_receipt]
  D --> G
  F --> G
  G --> H[promotion_manifest]
  H --> I[DCAT / STAC / PROV records]
  I --> J[Evidence drawer + Focus Mode]
```

The evidence UX expects to surface "artifact links and checksums" alongside provenance and policy labels, so hashing is a first-class contract surface.

The practical outcome: **hashes are not “nice metadata”** — they are the glue that makes promotion fail-closed, makes provenance verifiable, and enables caching/immutability semantics.

---

## Core terms
- **Digest**: `sha256:<hex>` over bytes of an artifact (file/bundle). The algorithm name is part of the ID to support future migration.
- **spec_hash**: `sha256` over a *canonicalized* dataset specification (canonical JSON, RFC 8785 / JCS).
- **Hash drift**: the same semantic object yields different hashes because of unstable formatting, ordering, floating precision, timestamps, randomness, or toolchain variation.

---

## Hashing contract

### ✅ Confirmed invariants (must not change)
- `sha256` is the mandatory algorithm for artifacts and bundles.
- `sha256` is also the algorithm for `spec_hash`.
- Hash IDs must be algorithm-qualified: `sha256:<hex>`.
- Never hash “pretty printed” JSON. Hash canonicalized JSON only.

### Required outputs
All functions/commands MUST be able to return digests in these forms:

| Kind | Output example | Intended use |
|---|---|---|
| Artifact digest | `sha256:2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae` | Files/bundles in receipts/manifests/catalogs |
| spec_hash | `sha256:abcd1234...` | DatasetVersion identity derived from dataset spec |
| Canonical JSON | RFC 8785 canonical string/bytes | Stored next to `spec_hash` to prevent drift |

### MUST: store canonical inputs next to computed hashes
To prevent “hash drift” and simplify audits:

- Store the **canonical dataset spec** used for hashing next to the computed `spec_hash`.
- Unit test that re-hashing that stored canonical spec yields the same `spec_hash`.
- Treat `spec_hash` changes as **breaking** and require human review.
- Never compute `spec_hash` from values dependent on clocks, randomness, or nondeterministic ordering.

---

## CLI contract
> The repository may choose any implementation language. The contract below defines **behavior**, not a specific binary name.

### Proposed commands
These commands are **PROPOSED** (not confirmed in repo), but recommended so CI/pipelines have a stable, testable interface.

| Command | Input | Output |
|---|---|---|
| `kfm-hash file <path>` | file path | prints `sha256:<hex>` |
| `kfm-hash spec <spec.json>` | JSON spec file | prints `sha256:<hex>` (`spec_hash`) |
| `kfm-hash canon-json <in.json>` | JSON file/stdin | writes canonical JSON (RFC 8785) |
| `kfm-hash stac <item_or_collection.json>` | STAC JSON | canonicalizes and returns `sha256:<hex>` of canonical bytes |
| `kfm-hash bundle <dir>` | directory | deterministic bundle manifest + digest (see below) |

### Bundle hashing (recommended pattern)
If hashing a directory/bundle is required, do **not** hash the filesystem traversal order.

Recommended approach:
1. Create a manifest of `relative_path → sha256(file bytes)` with **stable sorting**.
2. Canonicalize the manifest (RFC 8785 if JSON).
3. Compute bundle digest as `sha256(canonical manifest bytes)`.

This yields deterministic “bundle identity” while still letting auditors inspect per-file digests.

---

## Canonicalization rules

### JSON canonicalization
For anything that impacts identity (specs, configs, manifests):

- Use **RFC 8785 / JSON Canonicalization Scheme (JCS)**.
- Do not rely on language runtime dict ordering.
- Ensure numbers are normalized per RFC 8785 rules.

### STAC JSON
Deterministic packaging guidance that affects hashing/signing:

- Canonicalize STAC JSON (sorted keys) before hashing/signing.
- Normalize numeric precision and geometry before hashing (stable rounding, snap-to-grid, force2D where appropriate).

### Raster/vector determinism (when hashing outputs)
Hashing only means something if the underlying outputs are deterministic. If a pipeline writes outputs that depend on:
- unpinned tool versions,
- “auto” chunking/tiling,
- post-write mutation,
then hashes will drift even when the tool is correct.

**Minimum packaging checklist (recommended):**
- Pin tool versions (e.g., GDAL/PROJ and relevant Python libs).
- Fix tiling/chunks and compressor settings (avoid “auto”).
- Avoid post-writes to COGs / in-place updates.
- Canonicalize metadata before hashing/signing.

---

## Promotion + catalog integration

### Where the digests go
This tool is expected to supply digests for these governed artifacts:

- `run_receipt` (inputs, outputs, environment digests)
- `promotion_manifest` (spec_hash + artifact digests + catalog digests)
- STAC Items/Collections (asset checksums/digests)
- PROV bundles (artifact entities reference digests)
- DCAT distributions (distribution → artifact digest)

### Fail-closed expectations
Promotion MUST be blocked if:
- Any required artifact digest is missing or malformed
- `spec_hash` cannot be reproduced from the stored canonical spec
- Hashing is performed on non-canonical JSON inputs

---

## Test fixtures
This folder SHOULD include fixtures that make hash behavior “locked”:

- `fixtures/specs/*.json` with expected `spec_hash`
- `fixtures/json/*.json` with expected canonical output bytes
- `fixtures/files/*` with expected `sha256`
- a cross-platform “golden test” that recomputes all expected hashes and fails on drift

Suggested CI checks:
- recompute `spec_hash` for each fixture spec and assert equality
- recompute canonical JSON and assert byte-for-byte match
- recompute file digests in streaming mode

---

## Security and governance notes
- Hashes are integrity signals, not access control. Apply policy decisions before exposing any artifact URIs.
- Receipts/manifests may leak sensitive information (paths, URLs, parameters). Treat them as governed artifacts and redact where required.
- If the environment can influence output bytes (locale, float formatting, timezone), pin or normalize it in CI and pipelines.

---

## Troubleshooting

### “spec_hash changed but the spec is the same”
Most common causes:
- hashing non-canonical JSON
- adding/removing insignificant whitespace
- nondeterministic key ordering (runtime dict ordering, YAML loader ordering)
- numeric formatting differences across platforms

Fix:
- re-run `canon-json`, store the canonical spec, and compute `spec_hash` over canonical bytes.

### “same dataset run produced different artifact digests”
Most common causes:
- toolchain drift (different GDAL versions, different compressor defaults)
- nondeterministic chunking/tiling
- post-write updates

Fix:
- pin versions + determinism settings, then recompute.

---

## Contributing
- Any change that alters hash outputs requires:
  - updating/adding fixtures, and
  - explaining why drift is acceptable (ideally via an ADR).
- Prefer additive changes (new subcommands, new output modes) over changing existing outputs.
- Keep dependencies minimal; the hashing implementation should be able to run in CI and in constrained pipeline containers.

---

<details>
<summary><strong>Suggested folder layout (PROPOSED)</strong></summary>

```text
tools/hash/
├─ README.md                  # this file
├─ fixtures/                  # golden inputs + expected hashes
│  ├─ specs/
│  ├─ json/
│  └─ files/
├─ src/                       # implementation (language-dependent)
└─ tests/                     # unit tests for canonicalization + hashing
```

</details>

---

**Back to top:** [↑](#back-to-top)
