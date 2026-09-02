<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/habitat/gap-landfire/readme
name: Habitat GAP LANDFIRE Raw README
path: data/raw/habitat/gap-landfire/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <habitat-domain-steward>
  - <habitat-source-steward>
  - <gap-landfire-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <sensitivity-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
domain: habitat
source_family: gap-landfire
source_role: modeled
artifact_family: immutable-habitat-gap-landfire-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; modeled-not-observed; modelrun-and-uncertainty-required; sensitive-joins-fail-closed; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../quarantine/habitat/README.md
  - ../../../processed/habitat/README.md
  - ../../../catalog/domain/habitat/README.md
  - ../../../published/layers/habitat/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/domains/habitat/SOURCE_REGISTRY.md
  - ../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../docs/domains/habitat/SOURCES.md
  - ../../../../docs/domains/habitat/SENSITIVITY.md
  - ../../../../docs/domains/habitat/POLICY.md
  - ../../../../docs/domains/habitat/REASON_CODES.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - habitat
  - gap
  - landfire
  - ecological-systems
  - vegetation
  - land-cover
  - modeled
  - modelrun-required
  - uncertainty-surface
  - sensitive-join
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the placeholder content at `data/raw/habitat/gap-landfire/README.md`."
  - "Parent `data/raw/habitat/README.md` is currently a greenfield stub, so this child file stays source-family-lane bounded."
  - "GAP/LANDFIRE material is treated conservatively as modeled Habitat source capture by default; any per-product role split must be pinned in SourceDescriptor records."
  - "The Habitat registry currently shows role-label divergence for LANDFIRE/GAP; this README records that tension and fails closed to SourceDescriptor review."
  - "Payload presence, SourceDescriptor records, connector activation, ModelRunReceipts, UncertaintySurfaces, validators, fixtures, CI enforcement, sensitivity controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat GAP / LANDFIRE RAW Lane

RAW source-family lane for immutable GAP and LANDFIRE source captures, model-release references, ecological-system / vegetation classification support, and source-admission sidecars in the Habitat domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Source family: GAP / LANDFIRE" src="https://img.shields.io/badge/source-GAP%20%2F%20LANDFIRE-1f6feb">
  <img alt="Role: modeled" src="https://img.shields.io/badge/role-modeled-7048e8">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [GAP / LANDFIRE source posture](#gap--landfire-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/habitat/gap-landfire/` is a no-public-path RAW source-family lane. It is not processed Habitat truth, catalog truth, proof, receipt authority, source registry authority, rights authority, sensitivity policy authority, regulatory authority, observed occurrence authority, public API/UI material, release authority, or generated-answer authority.

---

## Scope

This directory holds immutable RAW captures and source-admission sidecars for GAP and LANDFIRE material admitted to the Habitat lane.

KFM treats GAP/LANDFIRE material conservatively as modeled vegetation, land-cover, ecological-system, fuels, disturbance, and habitat-representation source capture by default. It may support Habitat modeling and ecological-system context after governed normalization, but it is not observed occurrence evidence, not a regulatory designation, not critical habitat, and not public release authority merely because it was captured.

RAW exists for preservation, replay, and audit. It records what was admitted, where it came from, which product/vintage/model release was used, what source role it carried, and which identifiers, times, rights, citations, classification vocabulary, raster/vector form, model basis, uncertainty support, hashes, sensitivity flags, and caveats must travel with it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/habitat/gap-landfire/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `habitat` |
| Source family | `gap-landfire` |
| Source role | `modeled` by default; exact per-product role set by SourceDescriptor |
| Artifact role | RAW source-family lane for GAP/LANDFIRE captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/habitat/` or `data/quarantine/habitat/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, product/vintage identity, model basis, uncertainty support, classification vocabulary, sensitive-join risk, citation, validation, correction, rollback, or release support is insufficient |

---

## GAP / LANDFIRE source posture

| Source condition | RAW handling | Boundary |
|---|---|---|
| GAP ecological-system or habitat-representation product | Capture as modeled Habitat source material when admitted. | Modeled output; not observed occurrence evidence, not regulatory designation, and not public release truth. |
| LANDFIRE vegetation, fuels, disturbance, or condition product | Capture as modeled or per-product role-reviewed source material. | Role must be pinned in SourceDescriptor; do not infer observed status from source family name alone. |
| Ecological-system / USNVC classification | Preserve native classification, version, product form, and citation. | Crosswalks are advisory and must not replace native classification. |
| Model release or new vintage | Require model/run identity, version, source vintage, and uncertainty support before downstream use. | New release is not an in-place overwrite and may require a new ModelRunReceipt. |
| Framing as regulatory or observed fact | Route to quarantine or denial. | Modeled-as-regulatory and modeled-as-observed collapses fail closed. |
| Join to occurrence or rare-species data | Route through sensitivity review before downstream use. | Sensitive joins fail closed; no exact occurrence-linked public product from RAW. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- GAP or LANDFIRE dataset references, service references, model-release references, download references, raster/vector payload references, or restricted raw payload references;
- product identifiers, product family, source version/vintage, ecological-system or USNVC classification references, raster/vector form, source time, retrieval time, model/run reference where available, uncertainty reference where available, geometry/support notes, citation, attribution, rights posture, sensitivity hints, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts or tile/scene counts where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| GAP/LANDFIRE source-family doctrine | `docs/sources/catalog/` or `docs/domains/habitat/` |
| Habitat domain doctrine | `docs/domains/habitat/` |
| Connector code or connector decisions | `connectors/` |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Rights, terms, sensitivity, geoprivacy, redaction, or release policy | `policy/` and governed review lanes |
| Quarantine holds and remediation notes | `data/quarantine/habitat/` |
| Normalized working material | `data/work/habitat/` |
| Validated Habitat objects | `data/processed/habitat/` |
| ModelRunReceipt, UncertaintySurface receipt, ValidationReport, or RedactionReceipt as authority | `data/receipts/` or proof lanes, not RAW |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Observed occurrence truth, regulatory designation truth, critical-habitat truth, suitability truth, taxonomic truth, or public answer authority | Owning governed downstream/policy/proof/release lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/habitat/gap-landfire/
├── README.md
├── gap/
│   └── <release_or_run_id>/
│       ├── source_reference.json
│       ├── product_ref.json
│       ├── classification_ref.json
│       ├── model_run_ref.json
│       ├── uncertainty_ref.json
│       ├── checksums.sha256
│       └── README.md
├── landfire/
│   └── <release_or_run_id>/
│       ├── source_reference.json
│       ├── product_ref.json
│       ├── classification_ref.json
│       ├── model_run_ref.json
│       ├── uncertainty_ref.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, model authority, regulatory authority, occurrence authority, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Source role, rights, product/vintage identity, model basis, uncertainty support, classification vocabulary, attribution, citation, digest, schema, or source activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, source-family/product identity, citation, hash, model/run identity, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, ModelRunReceipt, uncertainty support, redaction/generalization receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/habitat/gap-landfire/
→ data/processed/habitat/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Habitat lane and the GAP/LANDFIRE source family.
- [ ] Confirm whether the captured material is GAP, LANDFIRE, or a mixed package.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, product/surface identity, rights, cadence, citation, sensitivity posture, and hash posture.
- [ ] Confirm source role is pinned by SourceDescriptor, especially where registry and dossier role labels diverge.
- [ ] Confirm product version/vintage, raster/vector form, ecological-system or USNVC classification, model basis, and uncertainty support are recorded before downstream use.
- [ ] Confirm native classification is preserved before any advisory crosswalk.
- [ ] Confirm GAP/LANDFIRE material is not being treated as observed occurrence truth, regulatory designation truth, critical-habitat truth, or public-release authority.
- [ ] Confirm sensitive joins to Fauna/Flora occurrence, rare-species, or steward-controlled records fail closed until policy review, geoprivacy transform, and receipts exist.
- [ ] Confirm rights, endpoint/current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/habitat/gap-landfire/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/habitat/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat source-family doctrine identifies GAP/LANDFIRE as modeled vegetation, land-cover, and ecological-system products requiring model identity and uncertainty support. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat source-registry doctrine lists GAP as modeled and LANDFIRE as observed/modeled, with role-label divergence to be resolved by SourceDescriptor. | **CONFIRMED by GitHub contents API during this edit** |
| Actual GAP/LANDFIRE RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, ModelRunReceipts, UncertaintySurfaces, validators, fixtures, CI checks, sensitivity controls, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, regulatory authority, observed occurrence authority, model-run authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../quarantine/habitat/README.md`](../../../quarantine/habitat/README.md)
- [`../../../processed/habitat/README.md`](../../../processed/habitat/README.md)
- [`../../../catalog/domain/habitat/README.md`](../../../catalog/domain/habitat/README.md)
- [`../../../published/layers/habitat/README.md`](../../../published/layers/habitat/README.md)
- [`../../../registry/sources/README.md`](../../../registry/sources/README.md)
- [`../../../../docs/domains/habitat/SOURCE_REGISTRY.md`](../../../../docs/domains/habitat/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/habitat/SOURCE_FAMILIES.md`](../../../../docs/domains/habitat/SOURCE_FAMILIES.md)
- [`../../../../docs/domains/habitat/SOURCES.md`](../../../../docs/domains/habitat/SOURCES.md)
- [`../../../../docs/domains/habitat/SENSITIVITY.md`](../../../../docs/domains/habitat/SENSITIVITY.md)
- [`../../../../docs/domains/habitat/POLICY.md`](../../../../docs/domains/habitat/POLICY.md)
- [`../../../../docs/domains/habitat/REASON_CODES.md`](../../../../docs/domains/habitat/REASON_CODES.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a Habitat GAP/LANDFIRE RAW source-family lane for source capture only. It is not source-family doctrine, source registry authority, rights authority, sensitivity policy authority, proof authority, receipt authority, release authority, catalog authority, regulatory authority, observed occurrence authority, model-run authority, habitat-suitability truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
