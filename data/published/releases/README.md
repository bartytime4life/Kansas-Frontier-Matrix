<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/00000000-0000-0000-0000-000000000000
title: data/published/releases/README.md
type: standard
version: v1
status: draft
owners: kfm-core
created: 2026-02-24
updated: 2026-02-24
policy_label: public
related:
  - data/published/README.md
  - data/audit/ledger/README.md
  - data/catalog/prov/runs/README.md
  - data/policies/decisions/README.md
tags: [kfm, published, releases, provenance, supply-chain]
notes:
  - This folder is the stable, *consumer-facing* release surface for the Published zone.
  - Everything here is immutable once published (append-only).
[/KFM_META_BLOCK_V2] -->

# data/published/releases
**Purpose:** Immutable, consumer-facing release records for *Published* artifacts (datasets, catalogs, tiles, bundles).

![Status](https://img.shields.io/badge/status-draft-yellow)
![Zone](https://img.shields.io/badge/zone-published-blue)
![Immutability](https://img.shields.io/badge/immutability-append--only-brightgreen)
![Policy](https://img.shields.io/badge/policy-public-informational)
<!-- TODO: Replace placeholder badges with real CI/release badges once paths are known -->

## Quick navigation
- [What belongs here](#what-belongs-here)
- [Directory layout](#directory-layout)
- [Release record contract](#release-record-contract)
- [How to add a new release](#how-to-add-a-new-release)
- [Verification](#verification)
- [Retention and immutability rules](#retention-and-immutability-rules)
- [FAQ](#faq)

---

## Where this fits in the repo
This directory is the **Published → Releases** surface: the stable “what shipped” ledger for downstream consumers (UI, APIs, external users, mirrors). Releases should only reference artifacts that have passed promotion gates into Published.

> **Rule:** clients/consumers should *prefer releases* over loose Published outputs when they need reproducibility, rollbacks, or formal citation.

---

## What belongs here
A **release** is a named, immutable snapshot of one or more Published outputs.

Examples:
- A set of `DatasetVersion`s promoted to Published and bundled for consumption.
- A catalog refresh (e.g., STAC/DCAT) that points at the same immutable dataset versions.
- A tile/derivative build (e.g., vector tiles) tied to specific dataset inputs and policy decisions.

### Acceptable inputs
- Release directories that contain:
  - a **human-readable** `RELEASE_NOTES.md`
  - a **machine-readable** release manifest (see contract below)
  - checksums + integrity metadata
  - provenance pointers (inputs, transforms, tool versions)
  - policy decisions/obligations that affect what is exposed

### Exclusions
Do **not** put these here:
- Raw or Work/Quarantine artifacts (those belong in their zone directories).
- Ad-hoc intermediate build files.
- Anything mutable or “latest/rolling” without a pinned identity.
- Secrets, credentials, or private keys (ever).

---

## Directory layout

```text
data/published/releases/
├─ README.md
├─ index.json                         # OPTIONAL: release index for fast lookup (append-only updates)
├─ vYYYY.MM.DD/                       # RECOMMENDED: date-based releases (e.g., v2026.02.24)
│  ├─ RELEASE_NOTES.md
│  ├─ release_manifest.json           # REQUIRED (see contract)
│  ├─ checksums.sha256                # REQUIRED (or equivalent)
│  ├─ signatures/                     # OPTIONAL but recommended
│  │  ├─ release_manifest.sig
│  │  └─ checksums.sig
│  ├─ sbom/                           # OPTIONAL but recommended
│  │  ├─ sbom.spdx.json
│  │  └─ sbom.cyclonedx.json
│  ├─ evidence/                       # OPTIONAL: digest-addressed evidence bundle references
│  │  └─ evidence_bundle.ref.json
│  └─ pointers/                       # OPTIONAL: convenience pointers to other registries/catalogs
│     ├─ datasets.json                # list of DatasetVersion refs
│     ├─ catalogs.json                # STAC/DCAT refs
│     └─ tiles.json                   # tile build refs
└─ vMAJOR.MINOR.PATCH/                # OPTIONAL: semantic version releases (e.g., v1.4.0)
   └─ (same contents as above)
```

> **Naming convention:** choose **one** primary convention (date-based or semver) and keep it consistent. Date-based is simplest for data drops; semver is best when you treat KFM as a product release train.

---

## Release record contract

### Required files
| File | Why it exists | Hard requirement |
|---|---|---|
| `RELEASE_NOTES.md` | Human narrative: what changed, why, impact | MUST |
| `release_manifest.json` | Machine contract: what shipped + provenance/policy links | MUST |
| `checksums.sha256` | Integrity for all files in the release directory | MUST |

### Recommended files (strongly)
| File/Folder | Why it exists |
|---|---|
| `signatures/` | Detached signatures for manifest + checksums (tamper-evidence) |
| `sbom/` | Supply-chain transparency for build tools/containers/libs used in release |
| `evidence/` | Evidence bundle pointers for cite-or-abstain UX and audits |
| `pointers/` | Convenience lists for downstream consumers |

---

## release_manifest.json schema (minimum)
This is a suggested *minimum* shape to keep releases consistent and verifiable:

```json
{
  "release_id": "kfm-release:v2026.02.24",
  "created_utc": "2026-02-24T17:05:00Z",
  "created_by": "ci@kfm",
  "policy_label": "public",
  "source_repo": {
    "repo": "TODO",
    "ref": "TODO-commit-sha"
  },
  "inputs": {
    "dataset_versions": [
      { "dataset_id": "kfm.dataset:usgs_nwis", "version_id": "sha256:..." }
    ],
    "catalogs": [
      { "kind": "stac", "ref": "kfm://..." },
      { "kind": "dcat", "ref": "kfm://..." }
    ]
  },
  "outputs": {
    "published_artifacts": [
      { "type": "dataset_bundle", "ref": "kfm://...", "sha256": "..." }
    ]
  },
  "provenance": {
    "run_refs": ["kfm://prov/run/..."],
    "receipts": ["kfm://audit/receipt/..."]
  },
  "policy": {
    "decisions": ["kfm://policy/decision/..."],
    "obligations": ["kfm://policy/obligation/..."],
    "redactions": ["kfm://policy/redaction_plan/..."]
  },
  "verification": {
    "checksums_file": "checksums.sha256",
    "signatures": [
      { "file": "signatures/release_manifest.sig", "for": "release_manifest.json" }
    ]
  },
  "notes": "Short free-text note about the release intent."
}
```

> Keep the manifest **boring and stable**: additive changes are okay; breaking changes require a version bump of the manifest schema.

---

## How to add a new release

### Definition of Done
- [ ] All referenced inputs are **Published** (not Raw/Work/Quarantine).
- [ ] `release_manifest.json` created and validated (JSON well-formed, required fields present).
- [ ] `RELEASE_NOTES.md` includes: summary, motivation, breaking changes, migration notes, known issues.
- [ ] `checksums.sha256` generated for every file in the release directory.
- [ ] (Recommended) signatures produced for manifest + checksums.
- [ ] (Recommended) SBOM artifacts attached if builds/containers were involved.
- [ ] Release directory is treated as **immutable** after merge/publish.

### Suggested release notes template
```markdown
# Release v2026.02.24

## Summary
- What shipped (1–5 bullets)

## Why
- Motivation / user need / issue refs

## What changed
- Added:
- Updated:
- Deprecated/Removed:

## Impact
- Who is affected and how (API/UI/tiles/catalog)

## Verification
- How to verify checksums/signatures
- Key run/provenance references

## Known issues
- Known limitations + workarounds

## Links
- DatasetVersions:
- Catalogs:
- Policy decisions:
```

---

## Verification

### Verify checksums
```bash
# run from within the release directory
sha256sum -c checksums.sha256
```

### Verify signatures (example)
```bash
# tooling depends on what you standardize on (cosign/gpg/sigstore/etc.)
# TODO: document the exact command once the signing tool is chosen.
```

---

## Retention and immutability rules
- **Append-only:** releases are never modified in place.
- **No overwrites:** if something is wrong, publish a new release and mark the old one deprecated in its notes.
- **Deterministic IDs:** prefer content-addressed identifiers where practical (e.g., `sha256:` refs).
- **No “latest” pointer inside this directory** unless it is generated and *owned* by a governed process (and still should not break reproducibility).

---

## FAQ

**Why releases instead of “just use Published”?**  
Published is the zone; releases are the **named snapshots** that downstream users can cite, mirror, diff, and roll back to.

**Can a release include multiple datasets?**  
Yes—treat a release as a bundle of *versioned* dataset outputs plus the catalogs/policy/provenance that explain them.

**What if a release contains sensitive-location data?**  
Then the release must carry the correct `policy_label` and include the policy decisions and redaction/generalization obligations that justify what is exposed. If uncertain: default-deny and publish a generalized release.

---

_Back to top: [Quick navigation](#quick-navigation)_
