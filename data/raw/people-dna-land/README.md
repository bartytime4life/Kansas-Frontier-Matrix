<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/people-dna-land/readme
name: People DNA Land Raw README
path: data/raw/people-dna-land/README.md
type: data-raw-domain-index-readme
version: v0.1.0
status: draft
owners:
  - <people-dna-land-domain-steward>
  - <data-steward>
  - <rights-reviewer>
  - <privacy-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
domain: people-dna-land
artifact_family: immutable-people-dna-land-source-capture-index
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; release-blocked
related:
  - land-ownership/README.md
  - ../people/dna/README.md
  - ../README.md
  - ../../README.md
  - ../../quarantine/people-dna-land/README.md
  - ../../quarantine/people-dna-land/land-ownership/README.md
  - ../../processed/people-dna-land/README.md
  - ../../catalog/domain/people-dna-land/README.md
  - ../../registry/sources/README.md
  - ../../../docs/architecture/directory-rules.md
  - ../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md
  - ../../../docs/domains/people-dna-land/DNA_HANDLING.md
  - ../../../docs/domains/people-dna-land/LAND_OWNERSHIP.md
  - ../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - people-dna-land
  - land-ownership
  - source-capture
  - source-role
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/raw/people-dna-land/README.md`."
  - "Confirmed child README lane during this edit: `land-ownership/`."
  - "The `data/raw/people/dna/README.md` file exists as related compatibility context, not as a confirmed child of this directory."
  - "README presence confirms documentation only; it does not prove payloads, descriptors, records, connectors, validators, receipts, review controls, or release readiness."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People/DNA/Land RAW

Parent RAW lifecycle index for People/DNA/Land source captures and source-admission sidecars.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: people-dna-land" src="https://img.shields.io/badge/domain-people--dna--land-6f42c1">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

> [!CAUTION]
> `data/raw/people-dna-land/` is a no-public-path RAW lifecycle lane. It is not processed truth, catalog truth, proof, receipt authority, source registry authority, rights authority, policy authority, release authority, public API/UI material, graph/vector-index authority, or generated-answer authority.

---

## Scope

This directory indexes immutable RAW source captures and RAW-local sidecars for the People/DNA/Land domain candidate.

RAW exists for preservation, replay, and audit. It records what was admitted, where it came from, what source role it carried, and which identifiers, source times, retrieval times, rights notes, citations, hashes, review notes, and caveats must travel downstream.

RAW does not decide what a person, relationship, genealogy, land instrument, ownership assertion, parcel join, or publication claim means. It does not publish a source or authorize generated answers.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/people-dna-land/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain candidate | `people-dna-land` |
| Artifact role | Parent RAW domain index for source captures and RAW-local sidecars |
| Confirmed child lane | `land-ownership/` |
| Related compatibility lane | `data/raw/people/dna/` |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Downstream | `data/work/people-dna-land/` or `data/quarantine/people-dna-land/` after governed triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/sources/`, not this directory |
| Policy authority | `policy/`, not this directory |

---

## Confirmed child lanes

The child lanes below are README paths confirmed by current-session GitHub fetches. This table confirms README presence only; it does **not** prove payloads, descriptors, records, connectors, validators, fixtures, receipts, review controls, or release readiness.

| Child lane | Status | Parent boundary |
|---|---|---|
| [`land-ownership/`](land-ownership/README.md) | **CONFIRMED README** | Land-ownership RAW source capture is not title opinion, parcel-boundary proof, public artifact authority, or generated-answer authority. |

Related but not a confirmed child of this directory:

| Related path | Status | Boundary |
|---|---|---|
| [`../people/dna/`](../people/dna/README.md) | **RELATED COMPATIBILITY README** | Compatibility RAW lane under `data/raw/people/`; do not treat it as proof of a `data/raw/people-dna-land/dna/` child lane. |

---

## RAW source posture

| Rule | Handling |
|---|---|
| RAW is source capture | Material here is admitted/captured for preservation, replay, and audit only. |
| Source role is preserved | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles must not be flattened. |
| Review gates matter | Downstream use requires governed review, receipts where applicable, correction path, rollback target, and release authority. |
| Public clients never read RAW | Public layers, reports, PMTiles, stories, graph edges, vector indexes, API payloads, and generated answers cannot read this RAW index directly. |

---

## Accepted material

Accepted content is limited to RAW source-capture material and RAW-local sidecars:

- source-reference manifests;
- raw payload references or access-scoped raw payload pointers;
- admission-ticket references and SourceDescriptor references;
- source identity, source family, source role, source time, retrieval time, citation, attribution, rights posture, review notes, digest sidecars, and caveats;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, registry, policy, release, public artifact, graph authority, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| People/DNA/Land doctrine | `docs/domains/people-dna-land/` |
| Source-family doctrine | `docs/domains/people-dna-land/SOURCE_REGISTRY.md` and source catalog docs |
| Authoritative SourceDescriptor records | `data/registry/sources/` |
| Review or release policy | `policy/` and governed policy roots |
| Quarantine holds and remediation notes | `data/quarantine/people-dna-land/` |
| Normalized working material | `data/work/people-dna-land/` after governed triage |
| Validated objects | `data/processed/people-dna-land/` only after gates close |
| Catalog, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| Receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public artifacts or generated answers | `data/published/` only after release gates close; RAW is never public output authority |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/people-dna-land/
├── README.md
├── land-ownership/
│   └── README.md
├── <future-confirmed-sublane>/
│   └── README.md
└── index.local.json
```

`index.local.json` is optional and RAW-local only.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was captured, but no downstream decision has been made. |
| Quarantine | Source role, rights, path authority, storage posture, citation, schema, or review state is unresolved. |
| Reject / erase | Rights, retention, or source handling does not allow continued retention. |
| Move to work | Source role, rights posture, citation, hash, storage/access posture, and review support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence. |

---

## Forbidden shortcut

```text
data/raw/people-dna-land/
→ data/processed/people-dna-land/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/raw/people-dna-land/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Child README lane confirmed during this edit: `land-ownership/`. | **CONFIRMED by GitHub contents API during this edit** |
| `data/raw/people/dna/README.md` exists as related compatibility context, not as a confirmed child of this parent directory. | **CONFIRMED by GitHub contents API during this edit** |
| Child README presence proves payloads, descriptors, records, connectors, validators, fixtures, checks, review controls, or release readiness. | **DENY** |
| Actual People/DNA/Land RAW payloads exist under this subtree. | **UNKNOWN** |
| Review controls, validators, fixtures, CI checks, and downstream receipts are wired for this exact parent lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt authority, release authority, catalog authority, registry authority, policy authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`land-ownership/README.md`](land-ownership/README.md)
- [`../people/dna/README.md`](../people/dna/README.md)
- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../quarantine/people-dna-land/README.md`](../../quarantine/people-dna-land/README.md)
- [`../../quarantine/people-dna-land/land-ownership/README.md`](../../quarantine/people-dna-land/land-ownership/README.md)
- [`../../processed/people-dna-land/README.md`](../../processed/people-dna-land/README.md)
- [`../../catalog/domain/people-dna-land/README.md`](../../catalog/domain/people-dna-land/README.md)
- [`../../registry/sources/README.md`](../../registry/sources/README.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)
- [`../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md`](../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md)
- [`../../../docs/domains/people-dna-land/DNA_HANDLING.md`](../../../docs/domains/people-dna-land/DNA_HANDLING.md)
- [`../../../docs/domains/people-dna-land/LAND_OWNERSHIP.md`](../../../docs/domains/people-dna-land/LAND_OWNERSHIP.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is a People/DNA/Land RAW domain index for source capture only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
