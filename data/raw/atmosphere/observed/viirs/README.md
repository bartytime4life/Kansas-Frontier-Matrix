<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/atmosphere/observed/viirs/readme
name: VIIRS Observed Raw Atmosphere README
path: data/raw/atmosphere/observed/viirs/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <atmosphere-domain-steward>
  - <viirs-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
domain: atmosphere
source_role: observed
source_family: viirs
artifact_family: immutable-viirs-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; review-required; rights-needs-verification; release-blocked
tags:
  - kfm
  - data
  - raw
  - atmosphere
  - observed
  - viirs
  - source-role
  - no-public-path
  - evidence-first
notes:
  - "This README documents the requested VIIRS Atmosphere RAW observed source-family lane."
  - "The target file existed as an empty file before this edit."
  - "Parent `data/raw/atmosphere/observed/README.md` is currently an empty file, so this child file stays source-family-lane bounded."
  - "Payload presence, source descriptors, connector activation, receipts, validators, fixtures, CI enforcement, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# VIIRS Observed RAW Atmosphere Lane

RAW source-family lane for VIIRS observed source capture and source-admission sidecars.

> [!CAUTION]
> `data/raw/atmosphere/observed/viirs/` is a no-public-path RAW source lane. It is not processed truth, catalog truth, proof, receipt authority, registry authority, policy authority, public API/UI material, release authority, or generated-answer authority.

---

## Scope

This directory holds immutable RAW captures and source-admission sidecars for VIIRS material whose source role is `observed`, or whose source-role review is expected to resolve as observed after admission.

The observed object is the source record and its metadata, not a downstream interpretation. Platform identity, time fields, source quality fields, source version, source reference, and digest must stay inspectable.

RAW is for preservation, replay, and audit. It does not decide what a source means, whether rights permit use, whether a record may publish, or whether a downstream claim is true.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/atmosphere/observed/viirs/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `atmosphere` |
| Parent source-role lane | `observed/` |
| Source family | `viirs` |
| Artifact role | RAW source-family lane for VIIRS observed source captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Downstream | `data/work/atmosphere/` or `data/quarantine/atmosphere/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |

---

## Source posture

| Source condition | RAW handling |
|---|---|
| Final source record | May use this lane as observed source capture when source-role support is documented. |
| Provisional source record | Treat as candidate or review-required until lifecycle disposition is clear. |
| Platform-specific record | Preserve platform identity and source time. |
| Aggregate derivative | Split to aggregate governance or quarantine. |
| Interpretation or public-output package | Keep out of RAW or route to the appropriate governed downstream lane. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- VIIRS source-record references or raw payload references;
- platform, source time, retrieval time, dataset version, source quality fields, source reference, attribution, and digest sidecars;
- geometry/source packet references, row counts where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, or public authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Product doctrine | `docs/sources/catalog/` |
| Domain doctrine | `docs/domains/atmosphere/` |
| Connector code or connector decisions | `connectors/` |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Rights, terms, sensitivity, or policy rules | `policy/` |
| Quarantine holds and remediation notes | `data/quarantine/atmosphere/` |
| Normalized working material | `data/work/atmosphere/` |
| Validated processed objects | `data/processed/atmosphere/` |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public artifacts | `data/published/` only after release gates close |
| Modeled, aggregate, candidate, interpretation, or public-output authority | Owning source-role/product lane and downstream governed stages |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/atmosphere/observed/viirs/
├── README.md
├── <source_id_or_product_id>/
│   └── <source_run_id>/
│       ├── source_reference.json
│       ├── viirs_source_ref.json
│       ├── platform_metadata.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Source role, status, rights, provenance, source time, geometry, attribution, citation, digest, schema, or source activation is unresolved. |
| Move to work | SourceDescriptor, rights posture, source role, disposition support, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/atmosphere/observed/viirs/
→ data/processed/atmosphere/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to VIIRS and the Atmosphere lane.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, rights, cadence, citation, platform, status, and hash posture.
- [ ] Confirm candidate, observed, aggregate, modeled, and interpretation outputs are not collapsed into one source role.
- [ ] Confirm platform, source time, retrieval time, dataset version, quality fields, geometry support, and caveats are recorded where material.
- [ ] Confirm rights, endpoint/current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README defines the requested VIIRS Atmosphere observed RAW source-family lane boundary. | **CONFIRMED authored** |
| The target path existed in the live repository as an empty file before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/atmosphere/observed/README.md` is currently an empty file. | **CONFIRMED by GitHub contents API during this edit** |
| VIIRS source-page doctrine says default source_role is observation for the source record, while provisional material may be candidate. | **CONFIRMED by GitHub contents API during this edit** |
| VIIRS source-page doctrine says detection is not confirmation and platform/latency classes require distinct handling. | **CONFIRMED by GitHub contents API during this edit** |
| Actual VIIRS observed RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, public artifact authority, or generated-answer authority. | **DENY** |

---

KFM rule: this directory is a VIIRS observed RAW source-family lane for source capture only. It is not source-family doctrine, source registry authority, rights authority, proof authority, receipt authority, release authority, catalog authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
