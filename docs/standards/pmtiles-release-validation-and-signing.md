<!--
KFM Meta Block V2
doc_id: kfm.std.pmtiles.release_validation_signing
title: PMTiles Release Validation and Signing Standard
type: standard
version: v1
status: draft
owners: @bartytime4life
created: 2026-04-16
updated: 2026-04-16
policy_label: public-safe
related:
  - tools/attest/README.md
  - tools/validators/README.md
  - data/receipts/README.md
  - policy/README.md
  - .github/workflows/README.md
tags: [kfm, pmtiles, release, integrity, signing, provenance]
notes: Initial standard for governed PMTiles release artifacts and verification flows.
-->

# PMTiles Release Validation and Signing Standard

> **Purpose**  
> Define the **minimum governed requirements** for producing, validating, signing, and publishing `.pmtiles` artifacts within the Kansas Frontier Matrix (KFM).

---

## 🧭 Quick Navigation

- [Scope](#scope)
- [Release Doctrine Alignment](#release-doctrine-alignment)
- [Artifact Model](#artifact-model)
- [Validation Requirements](#validation-requirements)
- [Signing Requirements](#signing-requirements)
- [CI Workflow Contract](#ci-workflow-contract)
- [Verification & Consumption](#verification--consumption)
- [Failure Modes (Fail-Closed)](#failure-modes-fail-closed)
- [Directory & Output Expectations](#directory--output-expectations)
- [Future Extensions](#future-extensions)

---

## Scope

This standard applies to:

- All `.pmtiles` artifacts produced for:
  - map layers
  - temporal map slices
  - derived geospatial products
- All release-bound tilesets (anything referenced by a Release Manifest)

**Out of scope:**
- Raw ingest formats (MBTiles, GeoJSON, Parquet)
- Non-release staging outputs (`data/work/`)

---

## Release Doctrine Alignment

This standard enforces core KFM doctrine:

| Doctrine Principle | Implementation |
|------------------|----------------|
| Evidence-first | Validation + signature artifacts are required |
| Fail-closed | Invalid or unsigned artifacts must not publish |
| Separation of concerns | Receipts ≠ Proofs ≠ Artifacts |
| Auditability | Every release artifact is verifiable independently |
| Determinism | Releases must be reproducible and content-addressable |

---

## Artifact Model

Each `.pmtiles` release MUST produce:

| Artifact | Description |
|--------|-------------|
| `tiles.pmtiles` | Primary tileset artifact |
| `tiles.pmtiles.sigbundle` | Sigstore bundle (signature + cert + transparency proof) |
| `tiles.pmtiles.digest` (PROPOSED) | Optional SHA256 digest file |
| Receipt entry | Execution + validation record (`data/receipts/`) |
| Proof reference | Linked from Release Manifest |

---

## Validation Requirements

### REQUIRED

All `.pmtiles` files MUST pass:

```
pmtiles verify <file>
```

This validation ensures:

- Archive structure integrity
- Tile directory correctness
- Bounds and zoom metadata consistency
- Tile count coherence

### REQUIRED (KFM augmentation)

Validators SHOULD additionally assert:

- Bounding box matches declared dataset scope (if available)
- Zoom levels fall within contract expectations
- Tile count is within expected range (sanity bound)

> These checks MAY be implemented in `tools/validators/`

---

## Signing Requirements

All release `.pmtiles` artifacts MUST be signed using:

- Keyless Sigstore signing (OIDC-based)
- `cosign sign-blob`

### REQUIRED OUTPUT

```
cosign sign-blob \
  --bundle tiles.pmtiles.sigbundle \
  tiles.pmtiles
```

The `.sigbundle` MUST:

- Contain certificate + signature
- Be verifiable offline
- Be published alongside the artifact

---

## CI Workflow Contract

A compliant workflow MUST:

1. Build `.pmtiles`
2. Validate with `pmtiles verify`
3. Fail immediately on validation error
4. Sign artifact using cosign
5. Publish:
   - `.pmtiles`
   - `.sigbundle`
6. Attach outputs to a GitHub Release

---

### Reference Workflow

```yaml
name: pmtiles-release

on:
  push:
    tags: ['v*']

permissions:
  contents: write
  id-token: write

jobs:
  release:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Install pmtiles CLI
        run: |
          curl -L https://github.com/protomaps/go-pmtiles/releases/latest/download/pmtiles-linux-amd64 \
            -o /usr/local/bin/pmtiles
          chmod +x /usr/local/bin/pmtiles

      - name: Build tiles
        run: |
          # project-specific build step
          test -f dist/tiles.pmtiles

      - name: Validate archive
        run: pmtiles verify dist/tiles.pmtiles

      - name: Install cosign
        uses: sigstore/cosign-installer@v3

      - name: Sign artifact
        run: |
          cosign sign-blob --yes \
            --bundle dist/tiles.pmtiles.sigbundle \
            dist/tiles.pmtiles

      - name: Publish release
        uses: softprops/action-gh-release@v2
        with:
          files: |
            dist/tiles.pmtiles
            dist/tiles.pmtiles.sigbundle
```

---

## Verification & Consumption

Consumers (runtime, reviewers, auditors) MUST be able to:

### Verify integrity

```
pmtiles verify tiles.pmtiles
```

### Verify signature

```
cosign verify-blob \
  --bundle tiles.pmtiles.sigbundle \
  tiles.pmtiles
```

### Expected outcomes

| Result | Meaning |
|------|--------|
| PASS | Artifact trusted |
| FAIL | Artifact MUST NOT be used |
| ERROR | Treat as DENY |

---

## Failure Modes (Fail-Closed)

| Failure | Required Behavior |
|--------|------------------|
| `pmtiles verify` fails | STOP pipeline |
| cosign signing fails | STOP pipeline |
| missing `.sigbundle` | DO NOT publish |
| verification fails downstream | ABSTAIN or DENY |

---

## Directory & Output Expectations

**Build output:**

```
dist/
  tiles.pmtiles
  tiles.pmtiles.sigbundle
```

**Receipts:**

```
data/receipts/<run-id>/
  pmtiles-verify.json
  signing.json
```

**Release:**

- Attached GitHub assets
- Referenced in Release Manifest

---

## Integration Points

| Lane | Role |
|-----|------|
| `tools/validators/` | PMTiles validation augmentation |
| `tools/attest/` | Signature + bundle verification helpers |
| `data/receipts/` | Execution memory |
| `policy/` | Trust enforcement (deny unsigned artifacts) |
| `tests/e2e/runtime_proof/` | Downstream trust validation |

---

## Future Extensions

**PROPOSED**

- Embed PMTiles metadata into Release Manifest
- Attach STAC Item linkage for tilesets
- Digest pinning in manifests (`sha256`)
- Cross-check tile bounds against catalog geometry
- Transparency log index capture in proof packs

---

## Summary

This standard ensures:

- Every `.pmtiles` artifact is **structurally valid**
- Every release artifact is **cryptographically verifiable**
- Every publication is **auditable and reproducible**
- The system remains **fail-closed and evidence-first**

---

> **KFM Position**  
> A map is not trusted because it renders correctly.  
> A map is trusted because it is **provably correct, verifiably signed, and auditably released.**
