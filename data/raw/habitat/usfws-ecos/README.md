<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/habitat/usfws-ecos/readme
title: Habitat USFWS ECOS Raw README
path: data/raw/habitat/usfws-ecos/README.md
type: data-raw-source-family-lane-readme
version: v0.2.0
prior_version: v0.1.0
status: draft
owners:
  - <habitat-domain-steward>
  - <habitat-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-10-11
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
owning_root: data/
responsibility: Preserve the tracked Habitat USFWS ECOS RAW compatibility and reference documentation without treating this lane as a physical source-first capture home or duplicating RAW bytes.
domain: habitat
source_family: usfws-ecos
source_role: regulatory-context
artifact_family: habitat-usfws-ecos-raw-compatibility-reference
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../../fauna/usfws_ecos/README.md
  - ../../README.md
  - ../../../quarantine/habitat/README.md
  - ../../../processed/habitat/README.md
  - ../../../catalog/domain/habitat/README.md
  - ../../../published/layers/habitat/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/domains/habitat/SOURCE_REGISTRY.md
  - ../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../docs/domains/habitat/SOURCES.md
  - ../../../../docs/domains/habitat/POLICY.md
  - ../../../../docs/sources/catalog/usfws_ecos/README.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - habitat
  - usfws
  - ecos
  - regulatory
  - source-capture
  - no-public-path
  - evidence-first
  - compatibility-reference
  - source-first
notes:
  - "This README replaces placeholder content at `data/raw/habitat/usfws-ecos/README.md`."
  - "Parent `data/raw/habitat/README.md` was a greenfield stub when this README was first authored; it now exists as the Habitat RAW compatibility/reference index."
  - "This lane is compatibility/reference documentation only; implementation wiring, capture placement, and payload presence remain unverified."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat USFWS ECOS RAW Lane

Compatibility/reference lane for Habitat-facing USFWS ECOS source documentation and legacy RAW topology; not a physical source-capture home.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Source family: USFWS ECOS" src="https://img.shields.io/badge/source-USFWS%20ECOS-1f6feb">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

> [!CAUTION]
> `data/raw/habitat/usfws-ecos/` is a no-public-path compatibility/reference lane inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this source-named directory is not a default physical capture home and must not receive duplicate RAW payloads. It is not processed truth, catalog truth, proof, receipt authority, registry authority, policy authority, release authority, public UI/API material, model output, or generated-answer authority.

---

## Scope

This directory documents USFWS ECOS material as it bears on Habitat and the legacy Habitat-scoped RAW topology. It may reference one governed source-first capture, but it does not establish where that capture is stored.

KFM treats USFWS ECOS as regulatory context for Habitat. The Habitat docs identify ECOS as a regulatory source family and require role authority, designation type, species reference, product version, service URI, and rights in the SourceDescriptor. The ECOS catalog says the Federal Register rule is the legal source and ECOS is the carrier.

A governed source-first capture records what was captured, where it came from, what role it carried, and which identifiers, times, rights notes, citations, product version, service URI, species reference, hashes, and caveats must travel downstream.

Cross-domain overlap: [`data/raw/fauna/usfws_ecos/`](../../fauna/usfws_ecos/README.md) documents the same upstream source for Fauna; `data/raw/flora/usfws_ecos/` holds only a `.gitkeep` placeholder. All of these lanes must reference the same single source-first capture, never two copies.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/habitat/usfws-ecos/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain lane | `habitat` |
| Source family | `usfws-ecos` |
| Source role | `regulatory`; exact role set by SourceDescriptor |
| Artifact role | Compatibility/reference lane for Habitat-facing USFWS ECOS source documentation and unresolved legacy RAW topology |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Downstream | Governed Habitat WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies |
| Release authority | `release/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when role, rights, product version, service URI, species reference, citation, validation, or release support is insufficient |

---

## Source posture

| Source condition | RAW handling | Boundary |
|---|---|---|
| Capture identity is source-first | Register one `source_id` and preserve one immutable capture identity; references may support Habitat without duplicating RAW bytes. | This lane does not create a second Habitat-scoped copy. |
| Physical placement is held | Do not infer `data/raw/habitat/usfws-ecos/` as the capture home; use only an accepted writer/path contract. | None is established by this README. |
| ECOS service pull | Capture as regulatory context when admitted. | RAW capture is not release state. |
| Product version or service URI | Preserve version, URI, source time, retrieval time, citation, and digest. | Updates must not overwrite prior captures in place. |
| Species reference | Preserve source reference and crosswalk target. | Habitat does not own taxon truth. |
| Framing as modeled output | Quarantine or deny. | ECOS context must not be collapsed with modeled Habitat products. |
| Public derivative proposal | Hold until policy, proof, release, correction, and rollback gates close. | RAW capture is not a public derivative. |

---

## Accepted material

Accepted content is limited to documentation and governed references that do not duplicate source-first captures:

- this tracked README;
- links to canonical SourceDescriptor, admission-ticket, source-admission, rights, sensitivity, and connector authority;
- references to a governed source-first capture or quarantine handoff when an accepted contract defines their shape;
- migration or correction notes that label legacy topology without moving or copying payloads;
- an optional local documentation index only after its schema, producer, owner, and non-authoritative role are accepted; it must not become proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

The governed source-first capture or reference for USFWS ECOS material, not this lane, must carry:

- source-reference manifests;
- ECOS service references, product/version references, species-reference sidecars, or raw payload references;
- role authority, designation type, species reference, product version, service URI, source time, retrieval time, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support Habitat. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
| Source-family doctrine | `docs/sources/catalog/usfws_ecos/` or `docs/domains/habitat/` |
| Connector code or connector decisions | `connectors/` |
| Authoritative SourceDescriptor records | `data/registry/sources/` |
| Rights, terms, review, or release policy | `policy/` and governed review lanes |
| Quarantine notes | `data/quarantine/habitat/` |
| Normalized working material | `data/work/habitat/` |
| Validated Habitat objects | `data/processed/habitat/` |
| Catalog, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| Receipts as authority | `data/receipts/` |
| Release manifests and rollback records | `release/` |
| Public artifacts | `data/published/` only after release gates close |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/habitat/usfws-ecos/
└── README.md
```

This is the confirmed documentation topology, not a storage specification. Do not add a source-run directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

The earlier version of this map sketched `<service_or_run_id>/` folders holding `source_reference.json`, `ecos_service_ref.json`, `product_ref.json`, `species_reference_ref.json`, `checksums.sha256`, and a run `README.md`, plus an optional local index. Treat that layout as a proposed shape for a future accepted source-first home, not this subtree.

Any local documentation index accepted later must remain non-authoritative and RAW-local; it must not become proof, catalog, registry, policy, release, public artifact, or answer authority.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was captured, but no downstream decision has been made. This lane may retain a governed reference only. |
| Quarantine | Source role, rights, product version, service URI, species reference, citation, schema, source activation, or physical placement is unresolved. |
| Return / reject | Admission decision or steward review says the capture must not be retained; correction occurs through the owning source-first or quarantine procedure. |
| Move to work | A governed reference or approved handoff may enter Habitat WORK only when SourceDescriptor, rights posture, source role, source-family identity, citation, hash, and minimal validation support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence. |

---

## Forbidden shortcut

```text
source-first RAW capture (physical path NEEDS VERIFICATION)
→ data/processed/habitat/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm one registered `source_id` and one immutable source-first capture identity; do not create a second Habitat-scoped copy.
- [ ] Treat this README as compatibility/reference documentation only; do not create a child directory under this lane as a payload destination.
- [ ] Confirm SourceDescriptor or admission ticket records role authority, designation type, species reference, product version, service URI, rights, citation, and hash posture.
- [ ] Confirm ECOS material is not collapsed with modeled Habitat products or occurrence evidence.
- [ ] Confirm species reference crosswalks preserve the correct owner lane for taxon truth.
- [ ] Confirm updates are stored as new captures and routed to downstream correction review where needed.
- [ ] Confirm rights, terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/habitat/usfws-ecos/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/habitat/README.md` was a greenfield stub when this README was first authored; it now exists as the Habitat RAW compatibility/reference index. | **CONFIRMED at reconciliation base `main@9e8bf3e6` (2026-10-11)** |
| Habitat docs identify USFWS ECOS as regulatory context and require role authority, designation type, species reference, product version, service URI, and rights. | **CONFIRMED by GitHub contents API during this edit** |
| ECOS catalog docs say the Federal Register rule is the legal source and ECOS is the carrier. | **CONFIRMED by GitHub contents API during this edit** |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| Actual USFWS ECOS RAW payloads exist under this subtree. | **UNKNOWN; none added or moved by this documentation correction.** No payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN |
| `data/raw/fauna/usfws_ecos/` documents the same upstream source for Fauna; both sides must reference one source-first capture, never two copies. | **CONFIRMED README presence at `main@9e8bf3e6`** |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired to an accepted source-first RAW writer for this source family. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../fauna/usfws_ecos/README.md`](../../fauna/usfws_ecos/README.md)
- [`../../README.md`](../../README.md)
- [`../../../quarantine/habitat/README.md`](../../../quarantine/habitat/README.md)
- [`../../../processed/habitat/README.md`](../../../processed/habitat/README.md)
- [`../../../catalog/domain/habitat/README.md`](../../../catalog/domain/habitat/README.md)
- [`../../../published/layers/habitat/README.md`](../../../published/layers/habitat/README.md)
- [`../../../registry/sources/README.md`](../../../registry/sources/README.md)
- [`../../../../docs/domains/habitat/SOURCE_REGISTRY.md`](../../../../docs/domains/habitat/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/habitat/SOURCE_FAMILIES.md`](../../../../docs/domains/habitat/SOURCE_FAMILIES.md)
- [`../../../../docs/domains/habitat/SOURCES.md`](../../../../docs/domains/habitat/SOURCES.md)
- `../../../../docs/domains/habitat/POLICY.md` (not present)
- [`../../../../docs/sources/catalog/usfws_ecos/README.md`](../../../../docs/sources/catalog/usfws_ecos/README.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a Habitat-facing USFWS ECOS compatibility/reference lane. One governed source-first capture may support Habitat without duplicated RAW bytes; this lane does not establish physical placement. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, model-output truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
