# People Published Layers

Status: draft.

Path: `data/published/layers/people/`

This requested path is documented as a restricted-review placeholder.

Current placement status: **NEEDS VERIFICATION**.

Nearest confirmed related lane: `data/published/layers/people-dna-land/`.

Known child placeholder: `data/published/layers/people/dna/`.

## Purpose

This directory may hold only released public-safe layer artifacts and direct sidecars after the normal KFM publication gates have passed.

This file does not make the path canonical. It records the requested path and keeps the lane bounded until a directory-rule decision, ADR, or migration note confirms the correct long-term home.

## Authority boundary

| Authority | Home |
|---|---|
| Release decisions | `release/` |
| Proof bundles | `data/proofs/` |
| Receipts | `data/receipts/` |
| Registry records | `data/registry/` |
| Source, work, quarantine, processed, and catalog material | Their lifecycle homes, not this directory |

## Public access rule

Public clients must use governed APIs and release-resolved artifacts. They must not read RAW, WORK, QUARANTINE, PROCESSED, catalog, source, or model-runtime outputs directly.

## Required checks before use

- [ ] Confirm whether this path is canonical or compatibility-only.
- [ ] Confirm relationship to `data/published/layers/people-dna-land/`.
- [ ] Confirm the release manifest.
- [ ] Confirm proof and receipt closure.
- [ ] Confirm registry entry.
- [ ] Confirm field allowlist and digest.
- [ ] Confirm rollback target.
- [ ] Confirm governed API access path.

## Status notes

| Claim | Status |
|---|---|
| This README defines the requested path boundary. | **CONFIRMED authored** |
| The target path exists in the live repository. | **CONFIRMED by GitHub contents API during this edit** |
| This path is canonical. | **NEEDS VERIFICATION** |
| `dna/README.md` exists as a child placeholder. | **CONFIRMED by recent GitHub edit in this session** |
| Released artifacts exist here. | **UNKNOWN** |
| Validators are wired in CI. | **NEEDS VERIFICATION** |

## Related files

- `data/published/layers/people-dna-land/README.md`
- `data/published/layers/people-dna-land/land-ownership/README.md`
- `data/published/layers/people/dna/README.md`
- `docs/doctrine/directory-rules.md`
- `docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md`
- `release/manifests/README.md`

---

KFM rule: this directory is an artifact lane only. It is not source authority, proof authority, release authority, registry authority, or AI truth.
