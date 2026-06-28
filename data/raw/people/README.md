<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/people/readme
name: People Raw Compatibility README
path: data/raw/people/README.md
type: data-raw-domain-index-readme; compatibility-lane-readme
version: v0.1.0
status: draft
owners:
  - <people-dna-land-domain-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
requested_path_segment: people
canonical_domain_candidate: people-dna-land
artifact_family: people-raw-compatibility-source-capture-index
sensitivity_posture: restricted-review; no-public-path; release-blocked
related:
  - dna/README.md
  - ../README.md
  - ../../README.md
  - ../../quarantine/people/README.md
  - ../../quarantine/people/dna/README.md
  - ../../quarantine/people-dna-land/README.md
  - ../../processed/people-dna-land/README.md
  - ../../registry/sources/README.md
  - ../../../docs/architecture/directory-rules.md
  - ../../../docs/domains/people-dna-land/DNA_HANDLING.md
  - ../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md
  - ../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - people
  - people-dna-land
  - compatibility-path
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/raw/people/README.md`."
  - "Confirmed child README lane during this edit: `dna/`."
  - "The requested `people` path is documented as a compatibility RAW index, not a canonical domain authority root."
  - "README presence confirms documentation only; it does not prove payloads, records, automation, validators, receipts, review controls, or release readiness."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People RAW Compatibility Index

Compatibility RAW lifecycle index for People-related source captures associated with the People/DNA/Land domain candidate.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Segment: compatibility" src="https://img.shields.io/badge/segment-compatibility-orange">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

> [!CAUTION]
> `data/raw/people/` is a compatibility RAW index. It is not canonical domain authority, processed truth, catalog truth, proof, receipt authority, policy authority, release authority, public UI/API material, graph/vector-index authority, or generated-answer authority.

---

## Canonical path warning

Directory Rules state that file placement encodes ownership, governance, and lifecycle, and topic alone does not justify a root folder. Visible People/DNA/Land doctrine uses `people-dna-land` as the current domain candidate, while this requested path uses `people`.

Treat this path as a compatibility RAW index unless an accepted ADR or migration note explicitly authorizes `people` as a canonical lifecycle path.

---

## Scope

This directory indexes People-related RAW source-capture material only when the repository intentionally preserves the `people` path as a compatibility bridge.

Confirmed child README lane:

| Child lane | Status | Boundary |
|---|---|---|
| [`dna/`](dna/README.md) | **CONFIRMED README** | Restricted source-capture lane. It cannot become public artifact or generated-answer authority by itself. |

RAW records capture context and review caveats for downstream governed handling. RAW does not prove identity, relationship, publication readiness, or answer readiness.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/people/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Requested segment | `people` |
| Canonical domain candidate | `people-dna-land` |
| Lane type | Compatibility parent RAW index |
| Confirmed child lane | `dna/` |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Downstream | Work or quarantine only after governed triage and path review |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/sources/`, not this directory |

---

## RAW source posture

| Rule | Handling |
|---|---|
| Compatibility path is not authority | `data/raw/people/` does not create a new canonical People authority root. |
| RAW is source capture | Material here is admitted/captured for preservation, replay, and audit only. |
| Public clients never read RAW | Public layers, reports, PMTiles, stories, graph edges, vector indexes, API payloads, and generated answers cannot read this RAW index directly. |
| Release requires gates | Publication requires governed downstream review and release authority. |

---

## Directory map

```text
data/raw/people/
├── README.md
├── dna/
│   └── README.md
├── <future-compatibility-lane>/
│   └── README.md
└── index.local.json
```

`index.local.json` is optional and RAW-local only.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was captured, but no downstream decision has been made. |
| Quarantine | Rights, source role, path authority, storage posture, or review state is unresolved. |
| Move to work | Source role, access posture, citation, hash, and review support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence. |

---

## Forbidden shortcut

```text
data/raw/people/
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
| This README replaces placeholder content at `data/raw/people/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Child README lane confirmed during this edit: `dna/`. | **CONFIRMED by GitHub contents API during this edit** |
| Child README presence proves payloads, records, automation, validators, fixtures, checks, review controls, or release readiness. | **DENY** |
| Directory Rules say placement encodes ownership, governance, and lifecycle; topic alone does not justify a root folder. | **CONFIRMED by GitHub contents API during this edit** |
| Actual People RAW payloads exist under this subtree. | **UNKNOWN** |
| This README is canonical domain authority, proof, receipt authority, release authority, catalog authority, registry authority, policy authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`dna/README.md`](dna/README.md)
- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../quarantine/people/README.md`](../../quarantine/people/README.md)
- [`../../quarantine/people/dna/README.md`](../../quarantine/people/dna/README.md)
- [`../../quarantine/people-dna-land/README.md`](../../quarantine/people-dna-land/README.md)
- [`../../processed/people-dna-land/README.md`](../../processed/people-dna-land/README.md)
- [`../../registry/sources/README.md`](../../registry/sources/README.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)
- [`../../../docs/domains/people-dna-land/DNA_HANDLING.md`](../../../docs/domains/people-dna-land/DNA_HANDLING.md)
- [`../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md`](../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is a People compatibility RAW index for source capture only. It is not canonical domain authority, source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
