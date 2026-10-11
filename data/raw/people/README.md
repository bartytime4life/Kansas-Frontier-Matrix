<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/people/readme
title: People Raw Compatibility README
path: data/raw/people/README.md
type: data-raw-domain-index-readme
secondary_type: compatibility-lane-readme
version: v0.2.0
prior_version: v0.1.0
status: draft
owners:
  - <people-dna-land-domain-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-10-11
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
owning_root: data/
responsibility: Preserve the tracked People RAW compatibility and reference documentation without treating this subtree or its dna/ child as a physical source-first capture home or duplicating RAW bytes.
requested_path_segment: people
canonical_domain_candidate: people-dna-land
artifact_family: people-raw-compatibility-reference-index
sensitivity_posture: restricted-review; no-public-path; release-blocked
related:
  - dna/README.md
  - ../README.md
  - ../../README.md
  - ../people-dna-land/README.md
  - ../people-dna-land/land-ownership/README.md
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
  - compatibility-reference
  - source-first
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/raw/people/README.md`."
  - "Confirmed child README lane during this edit: `dna/`."
  - "The requested `people` path is documented as a compatibility RAW index, not a canonical domain authority root."
  - "README presence confirms documentation only; it does not prove payloads, records, automation, validators, receipts, review controls, or release readiness."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People RAW Compatibility Index

Compatibility and reference index for legacy People-facing RAW documentation associated with the People/DNA/Land domain candidate; not a physical source-capture home.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Segment: compatibility" src="https://img.shields.io/badge/segment-compatibility-orange">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

> [!CAUTION]
> `data/raw/people/` is a no-public-path compatibility/reference index inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this subtree and its `dna/` child are not default physical capture homes and must not receive duplicate RAW payloads. It is not canonical domain authority, processed truth, catalog truth, proof, receipt authority, policy authority, release authority, public UI/API material, graph/vector-index authority, or generated-answer authority.

---

## Canonical path warning

Directory Rules state that file placement encodes ownership, governance, and lifecycle, and topic alone does not justify a root folder. Visible People/DNA/Land doctrine uses `people-dna-land` as the current domain candidate, while this requested path uses `people`.

Treat this path as a compatibility/reference index unless an accepted ADR or migration note explicitly authorizes `people` as a canonical lifecycle path. Even then, accepted Directory Rules rule `DIR-SOURCE-001` keeps capture identity source-first; a domain path name does not establish physical RAW placement.

---

## Scope

This directory indexes tracked People-facing documentation and legacy domain-scoped RAW topology only when the repository intentionally preserves the `people` path as a compatibility bridge. It may reference one governed source-first capture, but it does not establish where that capture is stored.

The sibling [`data/raw/people-dna-land/`](../people-dna-land/README.md) index (and its [`land-ownership/`](../people-dna-land/land-ownership/README.md) lane) documents the same People/DNA/Land domain candidate. Both lanes must reference the same single source-first capture for any shared upstream source, never two copies.

Confirmed child README lane:

| Child lane | Status | Boundary |
|---|---|---|
| [`dna/`](dna/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | Restricted DNA compatibility/reference lane under deny-by-default handling; not a capture home. It cannot become public artifact or generated-answer authority by itself. |

A governed source-first capture records capture context and review caveats for downstream governed handling. RAW does not prove identity, relationship, publication readiness, or answer readiness.

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
| Artifact role | Compatibility/reference index for People-facing documentation and unresolved legacy RAW topology |
| Confirmed child lane | `dna/` |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Downstream | Governed People/DNA/Land WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies, only after governed triage and path review |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/sources/`, not this directory |

---

## RAW source posture

| Rule | Handling |
|---|---|
| Capture identity is source-first | Register one `source_id` and preserve one immutable capture identity; domain references may support People/DNA/Land without duplicating RAW bytes. |
| Physical placement is held | Do not infer `data/raw/people/` or `dna/` as the capture home. Use only an accepted writer/path contract; none is established by this README. |
| Compatibility path is not authority | `data/raw/people/` does not create a new canonical People authority root. |
| RAW is source capture | Material at the accepted source-first home is admitted/captured for preservation, replay, and audit only; this index holds documentation and governed references, not captures. |
| Public clients never read RAW | Public layers, reports, PMTiles, stories, graph edges, vector indexes, API payloads, and generated answers cannot read this RAW index directly. |
| Release requires gates | Publication requires governed downstream review and release authority. |

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support People/DNA/Land. Exact physical placement and legacy migration remain **HOLD**.

---

## Directory map

```text
data/raw/people/
├── README.md
└── dna/
    └── README.md
```

This is the confirmed documentation topology, not a storage specification. Do not add a future compatibility lane, payload, or local index (such as the previously sketched optional RAW-local index file) here until an accepted source-first placement or compatibility decision defines its role.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was captured, but no downstream decision has been made. This index may retain a governed reference only. |
| Quarantine | Rights, source role, path authority, storage posture, physical placement, or review state is unresolved. |
| Move to work | A governed reference or approved handoff may enter People/DNA/Land WORK only when source role, access posture, citation, hash, and review support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence. |

---

## Forbidden shortcut

```text
source-first RAW capture (physical path NEEDS VERIFICATION)
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
| Actual People RAW payloads exist under this subtree. | **UNKNOWN; none added or moved by this documentation correction** — no payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| `data/raw/people-dna-land/` documents the same domain candidate; both lanes must reference the one source-first capture of each shared upstream source, never two copies. | **CONFIRMED sibling README at `main@9e8bf3e6`** |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
| This README is canonical domain authority, proof, receipt authority, release authority, catalog authority, registry authority, policy authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`dna/README.md`](dna/README.md)
- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../people-dna-land/README.md`](../people-dna-land/README.md)
- [`../people-dna-land/land-ownership/README.md`](../people-dna-land/land-ownership/README.md)
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

KFM rule: this directory is a People-facing compatibility/reference index. One governed source-first capture may support People/DNA/Land without duplicated RAW bytes; this subtree does not establish physical placement. It is not canonical domain authority, source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
