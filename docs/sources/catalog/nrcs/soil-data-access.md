<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-nrcs-soil-data-access
title: NRCS Soil Data Access (SDA)
type: product-page
version: v0.2
status: draft
owners: <PLACEHOLDER — Docs steward + Source steward for `nrcs`>
created: 2026-05-20
updated: 2026-05-22
policy_label: public
related:
  - docs/sources/catalog/nrcs/README.md
  - docs/sources/catalog/README.md
  - docs/sources/catalog/IDENTITY.md
  - docs/sources/catalog/RIGHTS-AND-SENSITIVITY-MAP.md
  - docs/doctrine/directory-rules.md
  - data/registry/sources/
  - policy/sensitivity/
tags: [kfm, docs, sources, catalog, nrcs, soil, sda, ssurgo]
notes:
  - "PROPOSED product-page scaffold; sibling-link presence verified in a Claude Code session, not in a mounted repo."
  - "Path `docs/sources/catalog/nrcs/SOIL-DATA-ACCESS.md` is PROPOSED; Directory Rules treat `docs/sources/` as a documentation lane and `data/registry/sources/` as the authoritative source-descriptor home."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NRCS Soil Data Access (SDA)

> Product page for the **USDA NRCS Soil Data Access** programmatic surface — the SQL / REST query API over the **SSURGO / STATSGO2** Soil Data Mart. This page is a **reader-oriented orientation** to the product; it does **not** replace the authoritative `SourceDescriptor` in `data/registry/sources/`.

![status: draft](https://img.shields.io/badge/status-draft-lightgrey)
![truth: scaffold](https://img.shields.io/badge/truth-PROPOSED%20scaffold-orange)
![family: nrcs](https://img.shields.io/badge/family-nrcs-blue)
![domain: soil](https://img.shields.io/badge/domain-soil-8B4513)
![sensitivity: T0](https://img.shields.io/badge/sensitivity-T0%20open-brightgreen)
![rights: NEEDS VERIFICATION](https://img.shields.io/badge/rights-NEEDS%20VERIFICATION-yellow)
<!-- TODO: replace placeholder badges with generated trust / gate / freshness / source-role badges per KFM-P3-FEAT-0005 once badge generator lands. -->

**Status:** PROPOSED — scaffold only ·
**Family:** [`nrcs`](./README.md) ·
**Domain segment:** `soil` (per Directory Rules §4 Step 3) ·
**Owners:** *PLACEHOLDER — Docs steward + Source steward for `nrcs`* ·
**Last reviewed:** 2026-05-22

---

## Mini-TOC

1. [Scope](#1-scope)
2. [Repo fit](#2-repo-fit)
3. [Source authority — single source of truth](#3-source-authority--single-source-of-truth)
4. [Pipeline shape (diagram)](#4-pipeline-shape-diagram)
5. [Source role, freshness, and watcher cadence](#5-source-role-freshness-and-watcher-cadence)
6. [Catalog profiles used (STAC · DCAT · PROV-O)](#6-catalog-profiles-used-stac--dcat--prov-o)
7. [Collection identity](#7-collection-identity)
8. [Provenance fields](#8-provenance-fields)
9. [Temporal handling](#9-temporal-handling)
10. [Geometry and projection](#10-geometry-and-projection)
11. [Rights and sensitivity](#11-rights-and-sensitivity)
12. [Validation and catalog closure](#12-validation-and-catalog-closure)
13. [Related contracts and schemas](#13-related-contracts-and-schemas)
14. [Related connectors and pipelines](#14-related-connectors-and-pipelines)
15. [Illustrative examples](#15-illustrative-examples)
16. [Open questions](#16-open-questions)
17. [Related docs](#17-related-docs)

---

## 1. Scope

> [!NOTE]
> This product page is a **PROPOSED** scaffold. Cadence, geographic coverage, current endpoint URL, rights status, and license terms for the live SDA surface are **NEEDS VERIFICATION** until checked against the operating `SourceDescriptor` and live publisher behavior.

NRCS **Soil Data Access (SDA)** is the USDA NRCS programmatic surface over the **Soil Data Mart**, which serves **SSURGO** (county-scale soil survey) and **STATSGO2** (generalized national) attribute and tabular content. KFM treats SDA as one of several NRCS soil products tracked under the `nrcs` source family — alongside SSURGO/gSSURGO bulk downloads, gNATSGO, and the **NRCS SCAN** soil-climate network. <sup>CONFIRMED source-family membership per `[DOM-SOIL]` / `[DOM-AG]` in the KFM Domains v1.1 + Pass 23/32 Consolidated Atlas; specific endpoint behavior NEEDS VERIFICATION.</sup>

[↑ Back to top](#top)

---

## 2. Repo fit

**Proposed home:** `docs/sources/catalog/nrcs/SOIL-DATA-ACCESS.md` — a **PROPOSED** documentation lane.

> [!IMPORTANT]
> Per **Directory Rules** §4 Steps 1–5, the *human-facing description* of this product belongs under `docs/`; the *machine-actionable `SourceDescriptor`* belongs under `data/registry/sources/`; the *connector* belongs under `connectors/`; the *pipeline logic* belongs under `pipelines/`. **Do not duplicate descriptor fields here.** When the descriptor and this page disagree, the descriptor wins and this page MUST be updated. <sup>CONFIRMED doctrine per `docs/doctrine/directory-rules.md` §4, §5, §7.</sup>

| Upstream / authority | This page | Downstream consumers |
|---|---|---|
| `data/registry/sources/` — authoritative `SourceDescriptor` (CONFIRMED rule / PROPOSED path) | `docs/sources/catalog/nrcs/SOIL-DATA-ACCESS.md` — reader-oriented product page | `connectors/nrcs/`, `pipelines/ingest/`, `pipelines/catalog/`, `data/catalog/{stac,dcat,prov}/` (PROPOSED paths) |

**What belongs on this page**

- Plain-English explanation of *what* SDA is and *what role* it plays in KFM.
- Cross-references to the authoritative descriptor, the catalog profiles, identity rules, and rights map.
- Open questions, watcher cadence, materiality triggers, and known caveats.

**What does NOT belong here**

- Machine-checkable `SourceDescriptor` fields (live under `data/registry/sources/`).
- Schema / contract definitions (live under `schemas/contracts/v1/source/` per ADR-0001).
- Policy allow/deny rules (live under `policy/`).
- Connector secrets, endpoint credentials, or pipeline configuration.

[↑ Back to top](#top)

---

## 3. Source authority — single source of truth

See [`data/registry/sources/`](../../../../data/registry/sources/) for the authoritative `SourceDescriptor` (PROPOSED path per Directory Rules §3 / §4). The descriptor records identity, source role, rights posture, update cadence, authority scope, and verification obligations. <sup>CONFIRMED doctrine; specific file presence is NEEDS VERIFICATION pending mounted-repo evidence.</sup>

> [!CAUTION]
> **Do not** copy descriptor fields into this product page. Duplication creates a **parallel-authority anti-pattern** (Directory Rules §13). If you need a field here for narrative clarity, **link to the descriptor** and paraphrase — do not mirror the field verbatim. <sup>CONFIRMED anti-pattern per Directory Rules §13.</sup>

[↑ Back to top](#top)

---

## 4. Pipeline shape (diagram)

The shape below describes the **PROPOSED** lifecycle for an SDA-derived product from admission to publication. It reflects the KFM lifecycle invariant `RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED` (CONFIRMED doctrine); concrete file homes, route names, and CI behavior are PROPOSED.

```mermaid
flowchart LR
    A[USDA NRCS<br/>Soil Data Access<br/>SDA endpoint]:::ext
    A -->|HEAD / ETag / Last-Modified<br/><i>conditional polling</i>| W[Watcher<br/>connectors/nrcs/<br/><b>PROPOSED</b>]
    W -->|EventRunReceipt + delta_manifest| RAW[(data/raw/soil/<br/><b>PROPOSED</b>)]
    RAW -->|extract · normalize| WORK[(data/work/soil/<br/><b>PROPOSED</b>)]
    WORK -->|validate · join MUKEY| PROC[(data/processed/soil/<br/><b>PROPOSED</b>)]
    PROC -->|STAC + DCAT + PROV-O| CAT[(data/catalog/stac · dcat · prov/<br/><b>PROPOSED</b>)]
    CAT -->|PromotionDecision + ReleaseManifest| PUB[(data/published/layers/soil/<br/><b>PROPOSED</b>)]
    PUB --> API[apps/governed-api/<br/><i>trust membrane</i>]:::api
    API --> Client[Public client]

    classDef ext fill:#fef3c7,stroke:#92400e,stroke-width:1px
    classDef api fill:#dbeafe,stroke:#1e40af,stroke-width:1.5px
```

> [!NOTE]
> The diagram is **illustrative**. It maps to canonical responsibility roots (Directory Rules §5) and the KFM lifecycle law, but each concrete path is PROPOSED until verified against mounted-repo evidence. <sup>NEEDS VERIFICATION per the Working Method §4.</sup>

[↑ Back to top](#top)

---

## 5. Source role, freshness, and watcher cadence

| Field | Value | Status | Basis |
|---|---|---|---|
| Source family | `nrcs` (USDA NRCS) | CONFIRMED | `[DOM-SOIL]`, `[DOM-AG]` Atlas v1.1 |
| Primary `source_role` | **`authority`** (NRCS is the authoritative publisher of SSURGO/STATSGO2) | PROPOSED | Atlas role enum: `authority / observation / context / model` |
| Allowed secondary roles | `observation` (pedon descriptions); `context` (gridded derivatives); `model` (SoilGrids-style derivatives are out-of-scope here) | PROPOSED | Atlas source-role anti-collapse register §24.1 |
| Rights status | NEEDS VERIFICATION against live publisher terms | NEEDS VERIFICATION | Atlas `[DOM-SOIL]`: "rights and current terms NEEDS VERIFICATION; sensitive joins fail closed" |
| Default sensitivity tier | **T0 — Open** (public-safe with no required transforms) | PROPOSED | Per `kfm_unified_doctrine_synthesis.md` §16: "Soil — SSURGO / gNATSGO public layers — T0" |
| Watcher cadence (metadata) | **Weekly** HEAD / ETag check | PROPOSED | `KFM-P2-PROG-0003`, `KFM-P21-PROG-0001`, `KFM-P29-PROG-0005` |
| Watcher cadence (full refresh) | **Annual**, aligned to the NRCS **Oct 1** SSURGO cycle | PROPOSED | `KFM-P2-PROG-0003` |
| HTTP validators | Persist `ETag` + `Last-Modified`; use `If-None-Match` / `If-Modified-Since` | PROPOSED | `KFM-P21-PROG-0017`, `KFM-P23-PROG-0033`, Pass-10 `C3-01` |
| Materiality triggers | Source version change · centroid shift · polygon area delta · numeric median change | PROPOSED | `ML-063-014` (MapLibre Master v2.1) |

> [!TIP]
> All KFM remote-data watchers are **conditional pollers** by default. A blind refetch without HEAD/ETag/Last-Modified preflight is a documented anti-pattern. <sup>CONFIRMED doctrine per `KFM-P21-IDEA-0005`.</sup>

[↑ Back to top](#top)

---

## 6. Catalog profiles used (STAC · DCAT · PROV-O)

KFM threads three catalog profiles through every promoted dataset family: **STAC** for spatiotemporal assets, **DCAT** for dataset-level metadata, and **PROV-O** for lineage. **Catalog closure** across all three is a promotion gate, not a discovery feature. <sup>CONFIRMED doctrine per `kfm_unified_doctrine_synthesis.md` and Pass-10 `C4-01`..`C4-05`, `KFM-P26-IDEA-0007`.</sup>

| Profile | Lane (PROPOSED path) | Used by this product? | Reference |
|---|---|---|---|
| **STAC 1.1** | `data/catalog/stac/` | PROPOSED — Yes (per-source Collection) | Pass-10 `C4-01` / `C4-02`; `KFM-P31-PROG-0004` |
| **DCAT** | `data/catalog/dcat/` | PROPOSED — Yes (tabular SDA query outputs) | Pass-10 `C4-05`; `KFM-P32-IDEA-0005` |
| **PROV-O / PROV-JSON-LD** | `data/catalog/prov/` | PROPOSED — Yes (lineage to RunReceipt) | Pass-10 `C8-03`; `KFM-P10-PROG-0003` |
| **Domain projection** | `data/catalog/domain/soil/` | PROPOSED — Yes (soil-domain view) | Directory Rules §4 Step 3 |

> [!IMPORTANT]
> Asset roles, media types, and STAC extension set are **NEEDS VERIFICATION** — confirm against `schemas/contracts/v1/source/` and the resolved STAC profile pinning in `docs/standards/STAC.md` (or equivalent). <sup>PROPOSED per `KFM-P31-PROG-0004`.</sup>

[↑ Back to top](#top)

---

## 7. Collection identity

| Field | PROPOSED value | Status | Reference |
|---|---|---|---|
| Collection id pattern | `kfm-nrcs-sda` (per `kfm-<org>-<product>` convention) | PROPOSED | Pass-10 `C4-02` Expansion |
| Provenance namespace | `kfm:` *(vs. `ks-kfm:` — see Open Questions)* | PROPOSED — UNRESOLVED | Pass-10 `C4-01` "Tensions"; original scaffold notes `OPEN-DSC-03` (NEEDS VERIFICATION of that ID) |
| Asset roles | `data`, `metadata`, `thumbnail`, `evidence`, `proof` (illustrative) | NEEDS VERIFICATION | confirm against `schemas/contracts/v1/source/` |
| Identity rule | `source id + object role + temporal scope + normalized digest` (PROPOSED deterministic basis) | PROPOSED | Atlas v1.1 §E (SoilMapUnit, SoilComponent) |

> [!NOTE]
> Collection ids are the **stable handle** that Items reference. Renaming a Collection breaks links throughout the catalog. <sup>CONFIRMED design caution per Pass-10 `C4-02`.</sup> Pin the id at admission; route renames through ADR + supersession, not silent edits.

See [`IDENTITY.md`](../IDENTITY.md) for the cross-product identity contract (PROPOSED sibling; NEEDS VERIFICATION of file presence).

[↑ Back to top](#top)

---

## 8. Provenance fields

Each STAC Item carries a `properties.kfm:provenance` block. Per-asset integrity is recorded via `file:checksum`. <sup>CONFIRMED schema shape per Pass-10 `C4-01`.</sup>

| Field | Type | Resolves to | Status |
|---|---|---|---|
| `spec_hash` | `sha256` of canonical (JCS) record | content-addressed identity | CONFIRMED field per `C4-01` / PROPOSED implementation |
| `evidence_bundle_ref` | `kfm://evidence/<digest>` | `EvidenceBundle` (JSON-LD) | CONFIRMED field per `C4-01` |
| `run_record_ref` | `kfm://run/<run-id>` | `RunReceipt` | CONFIRMED field per `C4-01` |
| `audit_ref` | `kfm://audit/<attestation-id>` | SLSA / OPA attestation | CONFIRMED field per `C4-01` |
| `policy_digest` | `sha256` of the policy bundle used at promotion | `PolicyDecision` lineage | CONFIRMED field per `C4-01` |
| *(per-asset)* `file:checksum` | per-file integrity hash | STAC `file` extension | CONFIRMED field per `C4-01` |

**KFM-namespaced STAC extension fields** (also carried, per `KFM-P3-IDEA-0004`):

- `kfm:run_receipt_ref` — link to the receipt that produced the artifact.
- `kfm:proof_ref` — link to the DSSE proof when one exists.
- `kfm:trust_class` — one of `receipt`, `proof`, `catalog`, `publication`.
- `kfm:source_role` — the source role declared at ingestion (see §5 above).

<sup>CONFIRMED documentation pattern per `KFM-P3-IDEA-0004`; specific extension registration is PROPOSED.</sup>

[↑ Back to top](#top)

---

## 9. Temporal handling

KFM keeps **source**, **observed**, **valid**, **retrieval**, **release**, and **correction** times distinct where material — a `SoilTimeCaveat` is required on any product where the reader could otherwise conflate them. <sup>CONFIRMED doctrine per Atlas `[DOM-SOIL]` §E.</sup>

| Time class | Meaning for SDA | Status |
|---|---|---|
| Source time | NRCS publication/version date for the SSURGO snapshot | NEEDS VERIFICATION per product |
| Observed time | Date the underlying pedon/observation was recorded (where present) | NEEDS VERIFICATION per product |
| Valid time | Period the soil map unit description is asserted to apply | PROPOSED (often unbounded) |
| Retrieval time | When KFM fetched the snapshot | CONFIRMED requirement |
| Release time | When KFM promoted the derived product | CONFIRMED requirement |
| Correction time | When a `CorrectionNotice` was issued (if any) | CONFIRMED requirement |

> [!WARNING]
> Soil maps are **revised on cadence**. Historical readers must see the slice they are reading, **not** a silently refreshed current. A `SoilTimeCaveat` and an explicit `CorrectionNotice` path are required when sources are revised. <sup>PROPOSED per the SSURGO/gNATSGO yearly-diff capability card.</sup>

[↑ Back to top](#top)

---

## 10. Geometry and projection

PROPOSED — confirm CRS, generalization rules, and scale support against `data/catalog/` artifacts and the resolved STAC Projection extension profile.

- **Resolution caveat:** SSURGO is the high-resolution county product; gNATSGO is the gridded national-scale derivative. **Cross-product joins MUST NOT silently resample**; the resolution and resampling method MUST be tagged on every derived value. <sup>CONFIRMED design caution per Pass-10 `C10-01`.</sup>
- **Materiality gates** apply to centroid drift, polygon-area delta, and numeric-median delta (see §5).

<sup>NEEDS VERIFICATION of concrete CRS, scale-band, and generalization-receipt fields.</sup>

[↑ Back to top](#top)

---

## 11. Rights and sensitivity

> [!CAUTION]
> **Do not restate policy here.** Policy lives under `policy/`. This page **links** to the policy surface; it does **not** define rules. Defining rules in `docs/` is a documented anti-pattern (Directory Rules §13: *Documentation as truth*).

- **Default sensitivity tier:** **T0 — Open** for public SSURGO / gNATSGO layers. <sup>PROPOSED per sensitivity matrix in `kfm_unified_doctrine_synthesis.md` §16.</sup>
- **Fail-closed posture:** sensitive joins (e.g., private-farm operator × parcel joins for agricultural use) **deny** by default. <sup>CONFIRMED doctrine per Atlas `[DOM-AG]` §I.</sup>
- **Rights status:** **NEEDS VERIFICATION** against live publisher terms. The `SourceDescriptor` is the authoritative location for the rights field.

See [`policy/sensitivity/`](../../../../policy/sensitivity/) and [`RIGHTS-AND-SENSITIVITY-MAP.md`](../RIGHTS-AND-SENSITIVITY-MAP.md) (PROPOSED siblings; NEEDS VERIFICATION of presence).

[↑ Back to top](#top)

---

## 12. Validation and catalog closure

| Check | Status | Reference |
|---|---|---|
| Catalog closure across STAC + DCAT + PROV before public release | PROPOSED — required | `KFM-P26-IDEA-0007`; Pass-10 `C5-01..C5-04` Gate Matrix |
| STAC Projection extension lint | PROPOSED | `KFM-P27-FEAT-0003` (NEEDS VERIFICATION of card ID) |
| STAC checksum closure against `ReleaseManifest` digest | PROPOSED | `KFM-P22-PROG-0037` (NEEDS VERIFICATION of card ID) |
| Spec-hash-match gate (`spec_hash` recomputation) | PROPOSED | Pass-10 `C5-04` |
| Default-deny promotion | PROPOSED — required | Pass-10 `C5-02` |
| OpenLineage required | PROPOSED — required | Pass-10 `C5-08` |

> [!IMPORTANT]
> **Promotion is a governed state transition, not a file move.** No `PUBLISHED` state without `PromotionDecision`, `EvidenceBundle`, `PolicyDecision`, and `ReleaseManifest` closure. <sup>CONFIRMED doctrine per `directory-rules.md` §0 and the doctrine synthesis.</sup>

[↑ Back to top](#top)

---

## 13. Related contracts and schemas

| Artifact | PROPOSED home | Status |
|---|---|---|
| `SourceDescriptor` (semantic contract) | `contracts/source/` | NEEDS VERIFICATION |
| `SourceDescriptor` schema (machine shape) | `schemas/contracts/v1/source/source-descriptor.json` | PROPOSED — canonical home per **ADR-0001** |
| `EvidenceBundle` schema | `schemas/contracts/v1/evidence/evidence_bundle.schema.json` | PROPOSED per `KFM-P26-PROG-0004` |
| `EvidenceRef` schema | `schemas/contracts/v1/evidence/evidence_ref.schema.json` | PROPOSED per `KFM-P26-PROG-0005` |
| KFM-STAC profile contract | `schemas/contracts/v1/catalog/stac/` | PROPOSED per `KFM-P31-PROG-0004` |

<sup>All paths PROPOSED until verified against mounted-repo evidence per Directory Rules §0 and §4 Step 4.</sup>

[↑ Back to top](#top)

---

## 14. Related connectors and pipelines

| Surface | PROPOSED path | Status |
|---|---|---|
| Connector (source-specific fetcher) | `connectors/nrcs/` | PROPOSED |
| Ingest pipeline | `pipelines/ingest/` | PROPOSED |
| Normalize pipeline | `pipelines/normalize/` | PROPOSED |
| Validate pipeline | `pipelines/validate/` | PROPOSED |
| Catalog pipeline | `pipelines/catalog/` | PROPOSED |
| Declarative pipeline spec | `pipeline_specs/soil/` | PROPOSED |
| Soil watcher (canonical entry) | `tools/ingest/watchers/http_stac_watcher.py` *(illustrative)* | PROPOSED per Pass-10 `C3-01` expansion |

[↑ Back to top](#top)

---

## 15. Illustrative examples

> [!NOTE]
> Examples below are **illustrative**. They are not authoritative fixtures and MUST NOT be treated as proof of implementation. The canonical example sibling is [`docs/sources/catalog/_examples/stac-item-example.json`](../_examples/stac-item-example.json) (PROPOSED; NEEDS VERIFICATION of file presence).

<details>
<summary><strong>Minimal STAC Item shape with <code>kfm:provenance</code></strong> · click to expand</summary>

```json
{
  "type": "Feature",
  "stac_version": "1.1.0",
  "id": "kfm-nrcs-sda-<county-fips>-<vintage>-<digest>",
  "collection": "kfm-nrcs-sda",
  "properties": {
    "datetime": "<retrieval_time>",
    "kfm:provenance": {
      "spec_hash": "sha256:<...>",
      "evidence_bundle_ref": "kfm://evidence/<digest>",
      "run_record_ref": "kfm://run/<run-id>",
      "audit_ref": "kfm://audit/<attestation-id>",
      "policy_digest": "sha256:<...>"
    },
    "kfm:run_receipt_ref": "kfm://run/<run-id>",
    "kfm:proof_ref": "kfm://proof/<dsse-id>",
    "kfm:trust_class": "publication",
    "kfm:source_role": "authority"
  },
  "assets": {
    "data": {
      "href": "<...>",
      "type": "application/geo+json",
      "roles": ["data"],
      "file:checksum": "<multihash>"
    }
  },
  "links": [
    { "rel": "collection",  "href": "../collection.json" },
    { "rel": "attestation", "href": "kfm://evidence/<digest>" }
  ]
}
```

<sup>Shape is illustrative; field set follows Pass-10 `C4-01` and `KFM-P3-IDEA-0004`. The `rel: "attestation"` link is PROPOSED per `KFM-P7-PROG-0001` and not a registered STAC link relation.</sup>

</details>

<details>
<summary><strong>Watcher cadence — conditional GET sketch</strong> · click to expand</summary>

```text
# PROPOSED watcher contract (illustrative pseudocode)
# Reference: KFM-P21-PROG-0001, KFM-P2-PROG-0003, Pass-10 C3-01

HEAD <sda_endpoint_or_snapshot_uri>
  If-None-Match: "<stored_etag>"
  If-Modified-Since: "<stored_last_modified>"

if status == 304:
    emit EventRunReceipt { result: "no_change", validators_checked: ["etag","last_modified"] }
elif status == 200:
    GET <sda_endpoint_or_snapshot_uri>
    compute spec_hash(canonical(payload))
    if spec_hash == prior_spec_hash:
        emit EventRunReceipt { result: "byte_change_no_content_change" }
    else:
        emit EventRunReceipt { result: "change_detected",
                               delta_manifest: <uri>,
                               new_etag: "<...>",
                               new_last_modified: "<...>" }
```

<sup>Pseudocode; not a runnable recipe. Real implementation lives in `connectors/nrcs/` and `tools/ingest/watchers/` (PROPOSED).</sup>

</details>

[↑ Back to top](#top)

---

## 16. Open questions

- **OPEN — `nrcs:` vs `ks-kfm:` provenance namespace.** Pass-10 `C4-01` flags this as unresolved; pinning is needed before SDA Collection promotion. *(Original scaffold referenced `OPEN-DSC-03` — that ID is NEEDS VERIFICATION; the underlying question is CONFIRMED open per Pass-10.)*
- **OPEN — Current SDA endpoint URL and authentication posture.** NEEDS VERIFICATION against live publisher behavior.
- **OPEN — Cadence on the SDA SQL surface specifically.** Per `KFM-P21-PROG-0001`, the watcher SHOULD compare ETag, Last-Modified, **product version**, AND **SDA micro-snapshots** — micro-snapshot cadence is not documented in current project knowledge.
- **OPEN — Rights status and CARE applicability.** Confirm against live publisher terms.
- **OPEN — Sharing posture for SDA outputs.** Whether this product warrants its own STAC Collection or shares one with sibling NRCS products (SSURGO bulk, gSSURGO, gNATSGO).
- **OPEN — Resolution-tagging convention.** Per `KFM-P10-PROG-0007` and Pass-10 `C10-01`, every derived value MUST be tagged with its source resolution and resampling method; whether to expose those tags in STAC `properties` or in a sidecar is unresolved.
- **OPEN — Verification placeholders.** Several card IDs referenced above (`KFM-P1-IDEA-0020`, `KFM-P22-PROG-0037`, `KFM-P27-FEAT-0003`) are recorded but NEEDS VERIFICATION against the live Idea Index Master.

[↑ Back to top](#top)

---

## 17. Related docs

- [`./README.md`](./README.md) — `nrcs` family README *(sibling)*
- [`../README.md`](../README.md) — `docs/sources/catalog/README.md` parent
- [`../IDENTITY.md`](../IDENTITY.md) — catalog-wide identity contract *(PROPOSED)*
- [`../RIGHTS-AND-SENSITIVITY-MAP.md`](../RIGHTS-AND-SENSITIVITY-MAP.md) — catalog-wide rights map *(PROPOSED)*
- [`../_examples/stac-item-example.json`](../_examples/stac-item-example.json) — canonical STAC + `kfm:provenance` example *(PROPOSED)*
- [`../../../doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) — Directory Rules v1.2
- [`../../../standards/STAC.md`](../../../standards/STAC.md) — KFM-STAC profile *(NEEDS VERIFICATION of path)*
- [`../../../standards/PROV.md`](../../../standards/PROV.md) — KFM provenance profile *(NEEDS VERIFICATION of path; PROV.md vs PROVENANCE.md naming under ADR review per Directory Rules §13.5 v1.1)*
- [`../../../adr/ADR-0001-schema-home.md`](../../../adr/ADR-0001-schema-home.md) — schema-home ADR *(NEEDS VERIFICATION of path)*

> [!NOTE]
> All sibling paths in this section are **PROPOSED** until verified against mounted-repo evidence. Anchor breakage risk is **moderate** if `docs/sources/catalog/` is restructured by ADR before this draft is published.

---

**Last reviewed:** 2026-05-22 *(Claude Code product-page revision session; full-polish pass against KFM doctrine and Atlas v1.1 + Pass 23/32).*

[↑ Back to top](#top)
