# People Published Layers

Released public-safe layer-artifact placeholder for the requested `people/` lane.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Placement: needs verification" src="https://img.shields.io/badge/placement-NEEDS%20VERIFICATION-orange">
  <img alt="Lifecycle: published" src="https://img.shields.io/badge/lifecycle-published-success">
  <img alt="Policy: restricted review" src="https://img.shields.io/badge/policy-restricted--review-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Purpose](#purpose) · [Repo fit](#repo-fit) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> **NEEDS VERIFICATION:** this requested path uses `people/`. Current repo-facing evidence uses `people-dna-land/` as the nearest confirmed related published-layer lane. Treat this file as a restricted-review placeholder until a directory-rule decision, ADR, or migration note confirms whether this path is canonical or compatibility-only.

## Purpose

This directory may hold only released public-safe layer artifacts and direct sidecars after the normal KFM publication gates have passed.

This file does not make the path canonical. It records the requested path and keeps the lane bounded until a directory-rule decision, ADR, or migration note confirms the correct long-term home.

## Repo fit

| Field | Value |
|---|---|
| Path | `data/published/layers/people/` |
| Responsibility root | `data/` |
| Lifecycle phase | `published/` |
| Placement status | **NEEDS VERIFICATION** |
| Nearest confirmed related lane | `data/published/layers/people-dna-land/` |
| Known child placeholder | `data/published/layers/people/dna/` |

## Inputs

Accepted content is limited to:

- released public-safe layer artifacts;
- release-linked layer sidecars;
- field allowlists and digests;
- release-local notes;
- generated pointers derived from release state.

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Source, work, quarantine, processed, and catalog material | Their lifecycle homes |
| Proof bundles | `data/proofs/` |
| Receipts | `data/receipts/` |
| Registry records | `data/registry/` |
| Release decisions | `release/` |
| Direct model-generated claims | Governed answer/provenance paths only |

## Directory map

```text
data/published/layers/people/
├── README.md
└── dna/
    └── README.md
```

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
