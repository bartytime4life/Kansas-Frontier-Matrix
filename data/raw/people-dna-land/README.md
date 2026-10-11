<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/people-dna-land/readme
title: People DNA Land Raw README
path: data/raw/people-dna-land/README.md
type: data-raw-domain-index-readme
version: v0.2.0
prior_version: v0.1.0
status: draft
owners:
  - <people-dna-land-domain-steward>
  - <data-steward>
  - <rights-reviewer>
  - <privacy-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-10-11
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
owning_root: data/
responsibility: Preserve the tracked People/DNA/Land RAW compatibility and reference index without treating this domain subtree or its land-ownership child as a physical source-first capture home or duplicating RAW bytes.
domain: people-dna-land
artifact_family: people-dna-land-raw-compatibility-reference-index
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; release-blocked
related:
  - land-ownership/README.md
  - ../people/README.md
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
  - compatibility-reference
  - source-first
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/raw/people-dna-land/README.md`."
  - "Confirmed child README lane during this edit: `land-ownership/`."
  - "The `data/raw/people/dna/README.md` file exists as related compatibility context, not as a confirmed child of this directory."
  - "README presence confirms documentation only; it does not prove payloads, descriptors, records, connectors, validators, receipts, review controls, or release readiness."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People/DNA/Land RAW

Compatibility and reference index for legacy People/DNA/Land-scoped RAW documentation; not a physical source-capture home.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: people-dna-land" src="https://img.shields.io/badge/domain-people--dna--land-6f42c1">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

> [!CAUTION]
> `data/raw/people-dna-land/` is a no-public-path compatibility/reference index inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this domain subtree and its `land-ownership/` child are not default physical capture homes and must not receive duplicate RAW payloads. It is not processed truth, catalog truth, proof, receipt authority, source registry authority, rights authority, policy authority, release authority, public API/UI material, graph/vector-index authority, or generated-answer authority.

---

## Scope

This directory indexes tracked People/DNA/Land-facing source documentation and legacy domain-scoped RAW topology. It may reference one governed source-first capture, but it does not establish where that capture is stored.

The sibling [`data/raw/people/`](../people/README.md) compatibility index (and its [`dna/`](../people/dna/README.md) lane) documents the same domain candidate under a legacy segment. Both lanes must reference the same single source-first capture for any shared upstream source, never two copies.

The canonical RAW boundary exists for preservation, replay, and audit. A governed source-first capture records what was admitted, where it came from, what source role it carried, and which identifiers, source times, retrieval times, rights notes, citations, hashes, review notes, and caveats must travel downstream.

RAW does not decide what a person, relationship, genealogy, land instrument, ownership assertion, parcel join, or publication claim means. It does not publish a source or authorize generated answers.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/people-dna-land/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain candidate | `people-dna-land` |
| Artifact role | Compatibility/reference index for People/DNA/Land-facing source documentation and unresolved legacy RAW topology |
| Confirmed child lane | `land-ownership/` |
| Related compatibility lane | `data/raw/people/dna/` |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Downstream | Governed People/DNA/Land WORK (`data/work/people-dna-land/`) or QUARANTINE (`data/quarantine/people-dna-land/`) procedures consume references or approved handoffs, not assumed domain-local copies, after governed triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/sources/`, not this directory |
| Policy authority | `policy/`, not this directory |

---

## Confirmed child lanes

The child lanes below are README paths confirmed by current-session GitHub fetches. Treat them as compatibility/reference documentation or unresolved legacy topology, not source-first capture homes. This table confirms README presence only; it does **not** prove payloads, descriptors, records, connectors, validators, fixtures, receipts, review controls, or release readiness.

| Child lane | Status | Parent boundary |
|---|---|---|
| [`land-ownership/`](land-ownership/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | Land-ownership source documentation is not a capture home,  title opinion, parcel-boundary proof, public artifact authority, or generated-answer authority. |

Related but not a confirmed child of this directory:

| Related path | Status | Boundary |
|---|---|---|
| [`../people/dna/`](../people/dna/README.md) | **RELATED COMPATIBILITY README** | Compatibility/reference lane under `data/raw/people/`; must reference the same single source-first capture as this index for any shared source; do not treat it as proof of a `data/raw/people-dna-land/dna/` child lane. |

---

## RAW source posture

| Rule | Handling |
|---|---|
| Capture identity is source-first | Register one `source_id` and preserve one immutable capture identity; domain references may support People/DNA/Land without duplicating RAW bytes. |
| Physical placement is held | Do not infer `data/raw/people-dna-land/` or a child directory as the capture home. Use only an accepted writer/path contract; none is established by this README. |
| RAW is source capture | Material at the accepted source-first home is admitted/captured for preservation, replay, and audit only; this index holds documentation and governed references, not captures. |
| Source role is preserved | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles must not be flattened. |
| Review gates matter | Downstream use requires governed review, receipts where applicable, correction path, rollback target, and release authority. |
| Public clients never read RAW | Public layers, reports, PMTiles, stories, graph edges, vector indexes, API payloads, and generated answers cannot read this RAW index directly. |

---

## Accepted material

Accepted content is limited to documentation and governed references that do not duplicate source-first captures:

- the tracked README files listed below;
- links to canonical SourceDescriptor, source-admission, rights, sensitivity, and policy authority;
- references to a governed source-first capture or quarantine handoff when an accepted contract defines their shape;
- migration or correction notes that label legacy topology without moving or copying payloads;
- local README documentation that helps a steward understand capture state without becoming proof, catalog, registry, policy, release, public artifact, graph authority, or answer authority.

The governed source-first capture or reference must carry source-reference manifests; raw payload references or access-scoped raw payload pointers; admission-ticket and SourceDescriptor references; and source identity, source family, source role, source time, retrieval time, citation, attribution, rights posture, review notes, digest sidecars, and caveats.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support People/DNA/Land. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
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
└── land-ownership/
    └── README.md
```

This is the confirmed documentation topology, not a storage specification. Do not add a future sublane, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was captured, but no downstream decision has been made. This index may retain a governed reference only. |
| Quarantine | Source role, rights, path authority, storage posture, citation, schema, physical placement, or review state is unresolved. |
| Reject / erase | Rights, retention, or source handling does not allow continued retention; correction or erasure occurs through the owning source-first or quarantine procedure. |
| Move to work | A governed reference or approved handoff may enter People/DNA/Land WORK only when source role, rights posture, citation, hash, storage/access posture, and review support are sufficient. |
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
| This README replaces the greenfield stub at `data/raw/people-dna-land/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Child README lane confirmed during this edit: `land-ownership/`. | **CONFIRMED by GitHub contents API during this edit** |
| `data/raw/people/dna/README.md` exists as related compatibility context, not as a confirmed child of this parent directory. | **CONFIRMED by GitHub contents API during this edit** |
| Child README presence proves payloads, descriptors, records, connectors, validators, fixtures, checks, review controls, or release readiness. | **DENY** |
| Actual People/DNA/Land RAW payloads exist under this subtree. | **UNKNOWN; none added or moved by this documentation correction** — no payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| `data/raw/people/` (with `dna/`) documents the same domain candidate; both lanes must reference one source-first capture, never two copies. | **CONFIRMED sibling README at `main@9e8bf3e6`** |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
| Review controls, validators, fixtures, CI checks, and downstream receipts are wired for this exact parent lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt authority, release authority, catalog authority, registry authority, policy authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`land-ownership/README.md`](land-ownership/README.md)
- [`../people/README.md`](../people/README.md)
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

KFM rule: this directory is a People/DNA/Land-facing compatibility/reference index. One governed source-first capture may support People/DNA/Land without duplicated RAW bytes; this subtree does not establish physical placement. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
