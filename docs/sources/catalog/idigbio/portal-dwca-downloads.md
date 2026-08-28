<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-idigbio-portal-dwca-downloads
title: iDigBio Portal DwC-A Downloads
type: product-page
version: v0.2
status: draft
owners: <PLACEHOLDER — Docs steward + Source steward for idigbio>
created: 2026-05-20
updated: 2026-05-21
policy_label: public
related:
  - docs/sources/catalog/idigbio/README.md
  - docs/sources/catalog/idigbio/occurrence-search.md
  - docs/sources/catalog/idigbio/media-records.md
  - docs/sources/catalog/idigbio.md
  - docs/sources/catalog/README.md
  - docs/sources/catalog/IDENTITY.md
  - docs/sources/catalog/PROFILES.md
  - docs/sources/catalog/RIGHTS-AND-SENSITIVITY-MAP.md
  - docs/sources/catalog/OPEN-QUESTIONS.md
  - docs/sources/catalog/_template/SOURCE_PRODUCT_TEMPLATE.md
  - docs/sources/catalog/idigbio/_examples/dwca-package-example.json
  - docs/doctrine/directory-rules.md
  - docs/standards/PROV.md
  - docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md
  - docs/domains/fauna/README.md
  - docs/domains/flora/README.md
tags: [kfm, docs, sources, catalog, idigbio, dwca, bulk-download, citable, replay-stable, citation-bound]
notes:
  - "PROPOSED product-page scaffold; sibling-link presence verified in prior Claude Code session, NEEDS VERIFICATION against mounted repo."
  - "v0.2: applied KFM presentation standard; added DwC-A package structure breakdown, Search-API ↔ Download surface contrast, citation-bound replay doctrine (corpus EXTERNAL via citations.txt), publication-class evidence posture parallel to GBIF Download DOI surface, and OPEN-IDB-CONV-01 carry-forward."
[/KFM_META_BLOCK_V2] -->

# 📦 iDigBio Portal DwC-A Downloads

> Bulk **Darwin Core Archive** downloads from the iDigBio portal — the **replay-stable, citation-bound** counterpart to the synchronous Search API; the publication-class evidence path for KFM iDigBio admission.

[![Status: draft](https://img.shields.io/badge/status-draft-blue)](#) [![Type: product-page](https://img.shields.io/badge/type-product--page-informational)](#) [![Family: idigbio](https://img.shields.io/badge/family-idigbio-2e7d32)](./README.md) [![Surface: bulk DwC-A](https://img.shields.io/badge/surface-bulk%20DwC--A-blueviolet)](#3-search-api-vs-portal-dwc-a--surface-contrast) [![Replay: byte-stable snapshot](https://img.shields.io/badge/replay-byte--stable%20snapshot-2e7d32)](#13-replay-and-determinism) [![Citation: citations.txt bound](https://img.shields.io/badge/citation-citations.txt%20bound-success)](#9-rights-citation-and-sensitivity) [![Policy: per-record license](https://img.shields.io/badge/policy-per--record%20license%20required-orange)](#9-rights-citation-and-sensitivity) [![Truth: receipt%E2%89%A0proof%E2%89%A0catalog%E2%89%A0publication](https://img.shields.io/badge/truth-receipt%E2%89%A0proof%E2%89%A0catalog%E2%89%A0publication-lightgrey)](#) [![ADR: pending (OPEN-IDB-CONV-01)](https://img.shields.io/badge/ADR-pending%20(OPEN--IDB--CONV--01)-yellow)](#16-open-questions)

**Status:** PROPOSED — scaffold + v0.2 polish · **Family:** [`idigbio`](./README.md) · **Owners:** `<PLACEHOLDER — Docs steward + Source steward for idigbio>` · **Last reviewed:** 2026-05-21

> [!IMPORTANT]
> **This surface is the publication anchor for iDigBio in KFM.** The bulk DwC-A download is **replay-stable** (frozen snapshot of records matching the query at request time) and arrives with a `citations.txt` file enumerating the contributing recordsets — the two operational properties the synchronous Search API lacks. Where [`occurrence-search.md`](./occurrence-search.md) ABSTAINS at publication, this product is the path that lets the same evidence resolve to ANSWER.

---

## Mini-TOC

- [1. Overview](#1-overview)
- [2. Source authority](#2-source-authority)
- [3. Search API vs Portal DwC-A — surface contrast](#3-search-api-vs-portal-dwc-a--surface-contrast)
- [4. DwC-A package structure](#4-dwc-a-package-structure)
- [5. Catalog profiles used](#5-catalog-profiles-used)
- [6. Collection identity](#6-collection-identity)
- [7. Provenance fields](#7-provenance-fields)
- [8. Temporal handling](#8-temporal-handling)
- [9. Rights, citation, and sensitivity](#9-rights-citation-and-sensitivity)
- [10. Validation and catalog closure](#10-validation-and-catalog-closure)
- [11. Related contracts and schemas](#11-related-contracts-and-schemas)
- [12. Related connectors and pipelines](#12-related-connectors-and-pipelines)
- [13. Lifecycle diagram](#13-lifecycle-diagram)
- [14. Replay and determinism](#14-replay-and-determinism)
- [15. Examples](#15-examples)
- [16. Open questions](#16-open-questions)
- [17. Related docs](#17-related-docs)

---

## 1. Overview

**CONFIRMED (KFM doctrine, C10-06):** iDigBio is part of the Kansas biodiversity stack alongside KU NHM, KANU IPT, KSU KSC, FHSU Sternberg, Symbiota, GBIF, eBird, iNaturalist, NatureServe, and USFWS. The portal's **bulk DwC-A download** is iDigBio's snapshot distribution channel for records matching a portal query — the path that produces a citable, replay-stable evidence artifact.

**EXTERNAL:** iDigBio providers publish to the portal via Darwin Core Archive packages produced by IPT or Symbiota and exposed on an RSS feed; the most current version of IPT is recommended. 

**CONFIRMED corpus thin slice (KFM-P2-PROG-0001):** the canonical KFM biodiversity ETL recipe explicitly composes "GBIF and provider IPT DwC-A endpoints" into the admission path, normalizes Darwin Core terms to EPSG:4326 geometry, deduplicates by `(institutionCode|catalogNumber)` with a rounded-coordinate fallback, applies the license map (`CC0 / CC-BY-4.0 / restricted`), redacts sensitive taxa, and emits Parquet + EvidenceBundle + signed RunReceipt under `data/receipts/`. **The Portal DwC-A surface is the iDigBio instantiation of this recipe.**

**PROPOSED — appropriate use cases for this product:**

| Use case | Posture |
|---|---|
| Canonical iDigBio ingest for releases (the corpus thin-slice path) | **OK** — this is the corpus-recommended admission route. |
| Standing as the source of a PUBLISHED claim | **OK** when paired with EvidenceBundle, license map, sensitivity gate, and the bundle's `citations.txt`. |
| Backing a Citation Validation Report | **OK** — `citations.txt` is the contributing-recordset enumeration. |
| Periodic refresh against a steward-chosen cadence (PROPOSED quarterly) | **OK** — bulk-snapshot model with no-op RunReceipt when content unchanged (KFM-P21-PROG-0048). |
| Real-time / per-call exploration | **DENY** — use [`occurrence-search.md`](./occurrence-search.md) (Search API) instead. |
| Sole evidence for a sensitive-taxon publication | **DENY** — DwC-A does not pre-filter for KFM sensitivity; redaction at WORK is non-negotiable. |
| Replacement for direct IPT pulls from KANU / KSC / KU NHM / Sternberg | **DENY** — institutional IPT remains preferred for in-state Kansas material; DwC-A from iDigBio is the cross-check and coverage fill. |

**NEEDS VERIFICATION (this product instance):** current portal-download endpoint URL, exact request-submission flow (web form vs API), per-query record limit, package format manifest, archive RSS feed URL, and refresh cadence policy choice.

[Back to top](#-idigbio-portal-dwc-a-downloads)

---

## 2. Source authority

| Field | Authoritative home | Status here |
|---|---|---|
| SourceDescriptor (identity, role, endpoints, cadence, terms, **`watcher_type: file`**) | [`data/registry/sources/`](../../../../data/registry/sources/) — schema home `schemas/contracts/v1/source/source-descriptor.schema.json` per **ADR-0001** | **Do not duplicate** here (PROPOSED; NEEDS VERIFICATION) |
| Source role | Source-role registry (PROPOSED, KFM-P20-IDEA-0001). iDigBio DwC-A Download role: **`observed`** (specimen-backed for specimen records) with the snapshot itself recorded as an **administrative** artifact (the citable package). | PROPOSED |
| Watcher classification | Watcher schema type enum — **CONFIRMED includes** `stac, gtfs, tile, file, api`. This product is **`watcher_type: file`** (bulk file/RSS), distinct from the `api` watcher used by `occurrence-search.md`. | PROPOSED instance |
| Rights / license matrix | [`policy/sensitivity/`](../../../../policy/sensitivity/) + license-map JSON. Per-record license carried in the DwC-A record rows. | See §[9](#9-rights-citation-and-sensitivity) |
| Citation custody | **`citations.txt` inside the DwC-A package**, paired with `meta.xml`, `occurrence.csv`, and extension CSVs | See §[4](#4-dwc-a-package-structure) and §[9](#9-rights-citation-and-sensitivity) |
| Taxon backbone | ITIS TSN → GBIF Backbone fallback per **C7-08** (DOI `10.15468/39omei`); pinned in `RunReceipt` | CONFIRMED requirement |
| Parent dossier | [`docs/sources/catalog/idigbio.md`](../idigbio.md) *(flat-dossier path; see OPEN-IDB-CONV-01)* | CONFIRMED authored prior session |

[Back to top](#-idigbio-portal-dwc-a-downloads)

---

## 3. Search API vs Portal DwC-A — surface contrast

> [!NOTE]
> The two iDigBio surfaces are **complementary**, not redundant. The Search API explores; the DwC-A download anchors. This page is the anchor.

| Dimension | [Occurrence Search API](./occurrence-search.md) | **Portal DwC-A Download (this page)** |
|---|---|---|
| **Pattern** | Synchronous HTTP search (paginated) | Asynchronous bulk request → zipped DwC-Archive |
| **Watcher class** | `watcher_type: api` | **`watcher_type: file`** (or `rss`-driven file fetch) |
| **Replay-stability** | **Non-deterministic** — records change between calls | **Stable** — frozen snapshot at request time |
| **Citability** | No DOI minted per call; abstain at publication | **`citations.txt` enumerates contributing recordsets** per query and access date |
| **Suitable as PUBLISHED-class evidence** | **No** — must be paired with a cached fixture or DwC-A snapshot | **Yes** (subject to license + sensitivity gates) |
| **Cadence in KFM (PROPOSED)** | Continuous, polling-style | Quarterly refresh against steward-chosen interval (PROPOSED) |
| **Typical KFM use** | Runtime focus-mode queries, watcher polling, exploratory overlays | Canonical ingest for releases; the corpus thin-slice path |
| **Connector output (PROPOSED)** | `data/raw/<domain>/idigbio/<run_id>/api/` | `data/raw/<domain>/idigbio/<run_id>/dwca/` |
| **Cite-or-abstain default** | ABSTAIN unless paired evidence resolves | ANSWER when EvidenceBundle resolves and gates pass |

> [!TIP]
> **Compose, don't choose.** The strongest KFM pattern uses **both** surfaces: the API for runtime exploration and watcher freshness detection, the DwC-A download for the citable evidence anchor. When the API surfaces a record of interest, the next snapshot DwC-A is the path that lets that record cross the publication threshold.

[Back to top](#-idigbio-portal-dwc-a-downloads)

---

## 4. DwC-A package structure

**EXTERNAL — CONFIRMED via iDigBio Data Ingestion Guidance** Darwin Core Archive packages published through IPT or Symbiota expose a structured directory containing a `meta.xml` schema, a core CSV (typically `occurrence.csv`), and one or more extension CSVs (e.g., Audubon Core for media via the `coreid` linkage). 

**PROPOSED — KFM-relevant package members:**

```text
idigbio-dwca-<query-hash>-<retrieved-at>.zip
├── meta.xml                    # CONFIRMED — DwC-A schema descriptor (which files, which fields)
├── eml.xml                     # Ecological Metadata Language (dataset-level metadata)
├── occurrence.csv              # CONFIRMED — Darwin Core core record file
├── multimedia.csv              # PROPOSED — Audubon Core extension (when media included)
├── measurementorfact.csv       # PROPOSED — measurement / fact extension (when included)
├── identification.csv          # PROPOSED — identification history extension (when included)
└── citations.txt               # CONFIRMED EXTERNAL — contributing recordsets + access date + query
```

| Package file | Authority | Lifecycle role |
|---|---|---|
| `meta.xml` | iDigBio (DwC-A schema descriptor) | Drives column-mapping at WORK |
| `eml.xml` | Provider (dataset metadata) | Carried as DCAT distribution metadata at CATALOG |
| `occurrence.csv` | Provider (DwC fields per row) | Normalized to canonical KFM record at WORK; dedupe key `(institutionCode|catalogNumber)` |
| `multimedia.csv` | Provider (AC fields) | Composes with the [`media-records.md`](./media-records.md) product page lane |
| `measurementorfact.csv` | Provider | Optional; carried where present |
| `identification.csv` | Provider | Optional; supports KFM identification history (Pass-32 expansion direction) |
| **`citations.txt`** | iDigBio (per-query enumeration) | **The citation anchor.** Must be preserved end-to-end in the EvidenceBundle and resolvable from any PUBLISHED claim. |

> [!CAUTION]
> **`citations.txt` is not optional.** A KFM ingest that drops `citations.txt` because "we already have the data" loses the publication-class evidence anchor. The file MUST be preserved at RAW, carried through WORK and PROCESSED, and resolved from the EvidenceBundle at CATALOG. Citation Validation reports cannot pass without it.

[Back to top](#-idigbio-portal-dwc-a-downloads)

---

## 5. Catalog profiles used

**PROPOSED.** A DwC-A download produces a **bundle** that lands in catalog lanes differently from a single API call: the bundle as a whole gets a DCAT distribution record, individual occurrences get STAC Items, and the query-citation linkage uses PROV-O.

| Profile | Lane | Default for Portal DwC-A (PROPOSED) | Notes |
|---|---|---|---|
| **STAC × Darwin Core hybrid** | [`data/catalog/stac/`](../../../../data/catalog/stac/) | **Yes** (per-occurrence Items) | C4-03 hybrid; C4-01 `kfm:provenance` block; `source_surface: "idigbio-dwca"`. |
| **DCAT Distribution** | [`data/catalog/dcat/`](../../../../data/catalog/dcat/) | **Yes** (per-bundle distribution record) | Records the bundle archive URL, retrieval timestamp, `citations.txt` content-address, and DwC-A `meta.xml` schema link. |
| **PROV-O** | [`data/catalog/prov/`](../../../../data/catalog/prov/) | **Yes** | Required — captures query → bundle → records → publication lineage. The bundle is the `prov:Entity`; the download is the `prov:Activity`. |
| **Domain projection** | `data/catalog/domain/fauna/` and/or `data/catalog/domain/flora/` | **Yes (NEEDS VERIFICATION)** | Fauna / Flora projections for steward review and Focus Mode payloads. |

> [!IMPORTANT]
> **DCAT and PROV are mandatory here, not optional.** The `citations.txt` discipline only works if the catalog records the bundle as a first-class artifact (DCAT) and the lineage from query to claim (PROV). Skipping DCAT/PROV for "just STAC" hides the citation anchor.

[Back to top](#-idigbio-portal-dwc-a-downloads)

---

## 6. Collection identity

- **PROPOSED Collection id pattern:** `kfm-<org>-<product>` (corpus expansion direction, C4-02). Illustrative shape: `kfm-idigbio-dwca-kansas`. Not authoritative until [`IDENTITY.md`](../IDENTITY.md) pins.
- **PROPOSED KFM namespace:** `kfm:` — **OPEN-DSC-03** (corpus C4-01 records `kfm:` vs `ks-kfm:` as unresolved).
- **PROPOSED — keep Search-API-derived and DwC-A-derived Items in separate Collections** so trust class (non-deterministic vs replay-stable) and citation discipline (paired-evidence vs citations.txt-bound) stay legible at the Collection level. See **OPEN-IDB-DWCA-04**.
- **CONFIRMED (C7-08):** the GBIF Backbone DOI version used by the canonicalization step MUST be captured in the `RunReceipt`. Backbone drift across snapshots is a build break for any claim that depends on replayable name resolution.

[Back to top](#-idigbio-portal-dwc-a-downloads)

---

## 7. Provenance fields

**CONFIRMED (C4-01):** STAC Items carry an `item.properties.kfm:provenance` block. For the DwC-A surface, the block is **extended (PROPOSED)** with bundle-level discriminators so the citation anchor and replay-stability are inspectable at the record level.

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "properties": {
    "datetime": "<observed/event ISO-8601>",
    "taxon": { /* DwC terms, see media-records.md §3 contrast */ },
    "kfm:provenance": {
      "spec_hash": "sha256:<JCS-canonicalized record hash>",
      "evidence_bundle_ref": "kfm://evidence/<digest>",
      "run_record_ref": "kfm://run/<run-id>",
      "audit_ref": "kfm://audit/<attestation-id>",
      "policy_digest": "sha256:<policy bundle digest>",

      "source_surface": "idigbio-dwca",
      "dwca_bundle_ref": "kfm://catalog/dcat/idigbio-dwca/<bundle-digest>",
      "dwca_bundle_digest": "sha256:<bytes of zip archive>",
      "dwca_query_spec_hash": "sha256:<JCS of normalized portal query>",
      "dwca_retrieved_at": "<RFC 3339 timestamp>",
      "dwca_meta_xml_digest": "sha256:<bytes of meta.xml>",
      "dwca_citations_txt_digest": "sha256:<bytes of citations.txt>",
      "dwca_record_count": 142378,
      "dwca_contributing_recordsets": ["<UUID-1>", "<UUID-2>", "..."],
      "backbone_doi_version": "10.15468/39omei@<snapshot>"
    },
    "redaction_profile": "<public-safe profile id or null>"
  }
}
```

| Field | Required for DwC-A surface? | Source of authority |
|---|---|---|
| `spec_hash`, `evidence_bundle_ref`, `run_record_ref`, `audit_ref`, `policy_digest` | **Yes** (same as all KFM STAC Items) | **CONFIRMED (C4-01)** |
| `source_surface: "idigbio-dwca"` | **Yes** | PROPOSED — disambiguates from the Search API surface. |
| `dwca_bundle_ref` | **Yes** | PROPOSED — points to the bundle's DCAT distribution record. |
| `dwca_bundle_digest` | **Yes** | PROPOSED — content-addresses the zip archive; the replay anchor. |
| `dwca_query_spec_hash` | **Yes** | PROPOSED — JCS over the portal query that produced the bundle. |
| `dwca_retrieved_at` | **Yes** | PROPOSED — the citable access date (part of `citations.txt` semantics). |
| `dwca_meta_xml_digest`, `dwca_citations_txt_digest` | **Yes** | PROPOSED — content-addresses critical package metadata. |
| `dwca_record_count` | **Yes** | PROPOSED — record count from the bundle; gate test against post-normalize count. |
| `dwca_contributing_recordsets` | **Yes** | PROPOSED — list of recordset UUIDs from `citations.txt`; surfaces attribution at the Item level. |
| `backbone_doi_version` | **Yes** | **CONFIRMED requirement (C7-08)** |

[Back to top](#-idigbio-portal-dwc-a-downloads)

---

## 8. Temporal handling

**CONFIRMED doctrine:** source, observed, valid, retrieval, release, and correction times stay **distinct** where material. The DwC-A bundle surface adds one more temporal anchor that occurrence-only surfaces lack: the **bundle retrieval timestamp**, which is the citation-bound moment.

| Time concept | Carrier (PROPOSED) | DwC-A-specific notes |
|---|---|---|
| **source time** | DwC `eventDate` per occurrence row | Original observation/collection event. |
| **observed time** | Source for `HUMAN_OBSERVATION`; specimen-prep-adjusted for `PRESERVED_SPECIMEN` | NEEDS VERIFICATION per basisOfRecord. |
| **valid time** | EvidenceBundle `valid_from` / `valid_to` | Default valid window: until the next scheduled refresh (PROPOSED quarterly). |
| **retrieval time** | `RunReceipt.fetched_at` + `dwca_retrieved_at` | **Citation-bound.** The `citations.txt` file embeds this value; the EvidenceBundle MUST match. |
| **release time** | `ReleaseManifest.released_at` | When the KFM derivative was published. |
| **correction time** | `CorrectionNotice.corrected_at` | When a provider revokes / corrects a recordset; iDigBio's next-snapshot reflects it; rollback required. |

> [!CAUTION]
> **Snapshot drift is real.** Between two DwC-A bundles retrieved at different times, providers may have revoked, added, or revised records — and may have changed licenses. The corresponding KFM releases are **byte-distinct evidence artifacts** even when the surface looks the same. Never silently overwrite one snapshot's EvidenceBundle with another's.

[Back to top](#-idigbio-portal-dwc-a-downloads)

---

## 9. Rights, citation, and sensitivity

### 9.1 License map (per-record, propagated through the bundle)

**CONFIRMED EXTERNAL:** iDigBio's IP Policy enumerates four Creative Commons mechanisms providers may select — CC0, CC BY, CC BY-SA, and CC BY-NC-SA — and applies CC BY as the default when no license is selected.  The DwC-A bundle carries per-record `dwc:license` (often with `dcterms:rightsHolder`); KFM enforces the license at admission, **per record**, not per bundle.

**CONFIRMED corpus thin slice (KFM-P2-PROG-0001):** the license map is fail-closed; admission DENIES records lacking a parseable license value and routes them to QUARANTINE. KFM does **not** apply iDigBio's CC BY default at its own admission gate (iDigBio is fail-open on license; KFM is fail-closed).

| License token (per record) | Disposition at admission (PROPOSED, fail-closed) | Notes |
|---|---|---|
| `CC0` | Public-safe path allowed | Attribution recorded for courtesy. |
| `CC BY 4.0` | Public-safe path allowed | Per-record attribution propagated; `citations.txt` recordset attribution composes with it. |
| `CC BY-SA 4.0` | Public-safe path allowed with derivative-license obligation | Any KFM derivative inherits the share-alike obligation. |
| `CC BY-NC-SA 4.0` | **Quarantine by default** | NonCommercial-use review and tier downgrade required before any public-layer release. See **OPEN-IDB-DWCA-06**. |
| *unrecognized / absent* | Quarantine by default | iDigBio's CC BY default does **not** apply at the KFM admission gate. |

### 9.2 Citation anchor (`citations.txt`)

**CONFIRMED EXTERNAL via prior-turn citation appendix:** every iDigBio portal download bundles a `citations.txt` that enumerates the contributing recordsets, the iDigBio query that produced the selection, the number of records contributed by each recordset, and the access date — intended to ground downstream citations in the originating providers.

**PROPOSED KFM behavior** (consistent with KFM-P2-PROG-0001 license-map-and-attribute requirement):

- the `citations.txt` digest is captured in `kfm:provenance.dwca_citations_txt_digest` at admission;
- the contributing-recordset list is mirrored into `kfm:provenance.dwca_contributing_recordsets`;
- every PUBLISHED claim grounded in this product MUST resolve through its `EvidenceBundle` to a citation that includes (a) the iDigBio query, (b) `dwca_retrieved_at`, (c) the contributing recordset identifier(s) from `citations.txt`, and (d) the per-record provider attribution from DwC fields.

### 9.3 Sensitivity rules

CONFIRMED doctrine (Atlas §24.5.1 sensitivity tier scheme; C10-06 sensitive-taxa rule; KFM-P25-IDEA-0006 sensitive fauna precision degradation):

| Trigger | Disposition | Doctrine source |
|---|---|---|
| Parent record names a NatureServe S1/S2 or KDWP-listed taxon | **T4 deny by default**; generalize coordinates to county/HUC + `RedactionReceipt` to admit at T1 | C10-06 + C6-01 |
| Precise locality on sensitive site (sacred / archaeological / private parcel) | Steward review required; generalization profile required | PROPOSED |
| `CC BY-NC-SA`–licensed records | T2+ at admission regardless of taxon | License-tier gate |
| Aggregate counts derived from the bundle (record counts per recordset) | T0/T1 with `role_aggregation_unit` set | C6 aggregation guard |
| Whole-bundle redistribution (verbatim re-hosting) | **HOLD pending policy** — license-by-license review | See **OPEN-IDB-DWCA-07** |

> [!CAUTION]
> **DwC-A bundles do not pre-filter for KFM sensitivity.** iDigBio does not know KFM's sensitivity rubric. Apply the deny-by-default gate at WORK, on the bundle's records, before any normalization writes to PROCESSED.

[Back to top](#-idigbio-portal-dwc-a-downloads)

---

## 10. Validation and catalog closure

- **CONFIRMED doctrine (Pass-10 / KFM-P1-IDEA-0020):** catalog closure is the final discoverability and accountability gate before public release.
- **PROPOSED DwC-A-specific gate (this product):** an Item with `kfm:provenance.source_surface == "idigbio-dwca"` and a null `dwca_citations_txt_digest` is **denied promotion**. The citation anchor is non-negotiable.
- **PROPOSED DwC-A-specific gate:** post-normalize record count must match `kfm:provenance.dwca_record_count` ± a steward-defined tolerance (PROPOSED 0% — exact match) after dedupe; mismatch holds at CATALOG for review.
- **PROPOSED DwC-A-specific gate:** every record promoted from a DwC-A bundle must trace back via PROV-O to the bundle's DCAT distribution and to the EvidenceBundle's `dwca_bundle_digest`.
- **PROPOSED (KFM-P27-FEAT-0003):** STAC Projection lint as a fail-closed gate.
- **PROPOSED (KFM-P22-PROG-0037):** STAC checksum closure against the `ReleaseManifest` digest, **including the bundle digest** in the chain.
- **PROPOSED (KFM-P27-PROG-0012 / -0013):** `run_catalog_qa.py` + `catalog-qa` GitHub workflow. **NEEDS VERIFICATION** against `directory-rules.md §7.5.a` and OPEN-DR-07.
- **PROPOSED (KFM-P21-PROG-0048):** when a scheduled refresh produces an identical-digest bundle, emit a **no-op `RunReceipt`** — audit continuity without catalog churn.

[Back to top](#-idigbio-portal-dwc-a-downloads)

---

## 11. Related contracts and schemas

- `contracts/domains/fauna/`, `contracts/domains/flora/` — semantic contracts for the per-domain consumers. **NEEDS VERIFICATION.**
- `schemas/contracts/v1/source/` — canonical SourceDescriptor home per **ADR-0001** (PROPOSED; NEEDS VERIFICATION).
- `schemas/contracts/v1/dwca/` — DwC-A bundle contract (PROPOSED). Until pinned, the bundle is treated as a DCAT distribution with content-addressed components.
- `contracts/evidence/` — EvidenceBundle / EvidenceRef contracts (KFM-P26-PROG-0004 / -0005).
- `tools/validators/biodiversity_dwca_validator/` (PROPOSED) — DwC-A schema + license + sensitivity validator referenced by OQ-6 of the parent dossier.

[Back to top](#-idigbio-portal-dwc-a-downloads)

---

## 12. Related connectors and pipelines

- [`connectors/idigbio/`](../../../../connectors/idigbio/) — source-specific fetch and admission per `directory-rules.md §7.3`. **CONFIRMED this session: stub** (NEEDS VERIFICATION). Bulk-download output to `data/raw/<domain>/idigbio/<run_id>/dwca/` (PROPOSED); never writes to processed/catalog/published.
- `pipelines/ingest/`, `pipelines/normalize/`, `pipelines/validate/`, `pipelines/catalog/` — executable pipeline lanes per `directory-rules.md §7.4`.
- `pipeline_specs/fauna/idigbio-dwca.yaml`, `pipeline_specs/flora/idigbio-dwca.yaml` — declarative specs (PROPOSED).
- [`docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md`](../../../runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md) — operational refresh runbook (CONFIRMED authored prior session; mounted-repo presence NEEDS VERIFICATION). The DwC-A refresh cadence flows through this runbook.

[Back to top](#-idigbio-portal-dwc-a-downloads)

---

## 13. Lifecycle diagram

> [!NOTE]
> The diagram shows the **expected lifecycle** of a DwC-A bundle through the KFM trust membrane. It reflects corpus doctrine (KFM-P2-PROG-0001 thin slice, C4-01 `kfm:provenance`, C5-02 default-deny, KFM-P21-PROG-0048 no-op receipt, watcher-as-non-publisher) plus the DwC-A-specific gates introduced above. **Implementation maturity remains UNKNOWN** until `connectors/idigbio/` gains content.

```mermaid
flowchart LR
    SCHED["Scheduled refresh<br/>(quarterly default — PROPOSED)<br/>or RSS-driven trigger"] -->|connectors/idigbio/<br/>(watcher_type: file)| FETCH["HTTPS bulk fetch<br/>iDigBio portal download<br/>(external)"]
    FETCH -->|.zip archive| BC["Bundle capture<br/>+ bundle_digest<br/>+ retrieved_at"]
    BC --> NOOP{"bundle_digest unchanged<br/>since last run?"}
    NOOP -- yes --> NO["No-op RunReceipt<br/>(KFM-P21-PROG-0048)"]
    NOOP -- no --> RAW["data/raw/&lt;domain&gt;/idigbio/&lt;run_id&gt;/dwca/<br/>RAW<br/>(zip + meta.xml + citations.txt preserved)"]
    RAW --> EXT["Extract<br/>+ meta.xml schema parse<br/>+ citations.txt digest"]
    EXT --> CIT{"citations.txt present<br/>and parseable?"}
    CIT -- no --> Q["data/quarantine/<br/>&lt;domain&gt;/<br/>missing-citation-anchor"]
    CIT -- yes --> LIC["Per-record license map<br/>(CC0 / CC BY / CC BY-SA → public-safe;<br/>CC BY-NC-SA / unknown → quarantine)"]
    LIC --> S{"sensitive taxon?<br/>(NatureServe S1/S2,<br/>KDWP T&E)"}
    S -- yes --> SR["Steward review<br/>+ generalization profile<br/>+ RedactionReceipt"]
    SR -->|approved| N["pipelines/normalize<br/>EPSG:4326 + JCS spec_hash<br/>+ dedupe (institutionCode|catalogNumber)"]
    SR -->|denied| Q
    S -- no --> N
    N --> CNT{"record count matches<br/>dwca_record_count?"}
    CNT -- no --> HOLD["HOLD at WORK<br/>steward review required"]
    CNT -- yes --> V["pipelines/validate"]
    V -- fail closed --> Q
    V -- pass --> P["data/processed/&lt;domain&gt;/<br/>PROCESSED"]
    P --> CAT["pipelines/catalog<br/>STAC × DwC + DCAT bundle + PROV lineage<br/>+ source_surface: idigbio-dwca"]
    CAT --> H["data/catalog/{stac,dcat,prov,domain/...}/<br/>CATALOG"]
    H --> EB["EvidenceBundle +<br/>RunReceipt + ProofPack<br/>(citations.txt resolvable)"]
    EB --> J{"PromotionDecision<br/>(gates A–G,<br/>citations.txt + count + license + sensitivity)"}
    J -- deny / hold --> RB["RollbackCard /<br/>steward review"]
    J -- allow --> REL["release/<br/>ReleaseManifest<br/>(bundle_digest in chain)"]
    REL --> PUB["data/published/...<br/>PUBLISHED (public-safe only,<br/>cite-bound via citations.txt)"]

    classDef quar fill:#fde0e0,stroke:#b00020,color:#000;
    classDef sens fill:#fff3e0,stroke:#c25e00,color:#000;
    classDef gate fill:#fff8e1,stroke:#9a6700,color:#000;
    classDef pub fill:#e7f5ee,stroke:#2e7d32,color:#000;
    classDef hold fill:#eef2f7,stroke:#46555f,color:#000;
    class Q,RB quar;
    class S,SR sens;
    class NOOP,CIT,LIC,CNT,V,J gate;
    class REL,PUB pub;
    class NO,HOLD hold;
```

[Back to top](#-idigbio-portal-dwc-a-downloads)

---

## 14. Replay and determinism

> **Evidence basis: §13 identity rule; replay-verification invariant; remote/non-deterministic deps rule (`tests/replay/fixtures/<use_case>/cached_responses/`).**

**CONFIRMED doctrine.** Replay drift is a **build break**.

**The DwC-A surface is the iDigBio replay anchor.** Where [`occurrence-search.md`](./occurrence-search.md) is non-deterministic (API responses drift across calls), this product is **byte-stable by construction**: the bundle is a frozen snapshot, content-addressed by `dwca_bundle_digest`, and reproducible because the bundle itself is the cached response.

| Strategy | When | Status |
|---|---|---|
| **Store the bundle zip as the cached response** under `tests/replay/fixtures/idigbio_dwca/cached_responses/<bundle-digest>.zip` | Default for all pipelines that need to be replay-stable against iDigBio evidence | **CONFIRMED doctrine pattern** / PROPOSED filesystem path |
| **Re-fetch live + diff vs golden** | Forbidden for promotion-bearing pipelines | DENY by default |
| **Replay against a different bundle digest** | A new evidence artifact, not a replay; new EvidenceBundle, new ReleaseManifest, new ProofPack | PROPOSED — handle via snapshot lineage in PROV, not in-place |

> [!TIP]
> **The bundle IS the cached response.** Unlike the Search API surface (which must construct a cached fixture from JSON responses), the DwC-A surface arrives pre-frozen as a single zip archive. The content-address (`dwca_bundle_digest`) is the replay anchor and is the same value that PROV records as the `prov:Entity` for the bundle.

[Back to top](#-idigbio-portal-dwc-a-downloads)

---

## 15. Examples

*Illustrative only — do not treat as authoritative.*

See [`_examples/dwca-package-example.json`](./_examples/dwca-package-example.json) for the minimal DwC-A descriptor + `kfm:provenance` shape *(PROPOSED sibling; NEEDS VERIFICATION)*.

<details>
<summary>📦 PROPOSED normalized portal-query envelope (input to <code>dwca_query_spec_hash</code>)</summary>

```json
{
  "kfm:dwca_query_envelope": {
    "portal_query_url": "<NEEDS VERIFICATION: iDigBio portal download query URL>",
    "submission_method": "form | api",
    "filters": {
      "country": "United States",
      "stateProvince": "Kansas",
      "geopoint": { "type": "exists" },
      "recordset_allowlist": null
    },
    "filter_canonical_order": ["country", "geopoint", "recordset_allowlist", "stateProvince"],
    "submitted_at": "<RFC 3339 timestamp>"
  }
}
```

JCS canonicalization (RFC 8785) over `filters` sorted by `filter_canonical_order` produces `dwca_query_spec_hash`.

</details>

<details>
<summary>🧾 PROPOSED <code>citations.txt</code> shape (illustrative)</summary>

```text
# Citations file
# Generated by iDigBio portal
# Access date: 2026-05-21
# Query: country="United States" AND stateProvince="Kansas" AND geopoint=exists

University of Kansas Biodiversity Institute. Mammalogy Collection.
  records: 12,548
  recordset_uuid: <UUID-1>

Kansas State University. Vertebrate Collection.
  records: 3,407
  recordset_uuid: <UUID-2>

Fort Hays State University. Sternberg Museum.
  records: 8,921
  recordset_uuid: <UUID-3>

...
Total records: 142,378
Total recordsets: 47
```

The content-address of this file (sha256 of bytes) is recorded as `kfm:provenance.dwca_citations_txt_digest` and resolved from every published claim.

</details>

<details>
<summary>📄 STAC × DwC fragment with DwC-A source_surface (illustrative)</summary>

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "kfm-idigbio-dwca-<uuid>",
  "collection": "kfm-idigbio-dwca-kansas",
  "geometry": { "type": "Point", "coordinates": [-98.0, 38.5] },
  "properties": {
    "datetime": "2024-06-15T14:22:00Z",
    "proj:code": "EPSG:4326",
    "taxon": {
      "scientificName": "Sterna forsteri",
      "kbs_id": "176849",
      "basisOfRecord": "PRESERVED_SPECIMEN",
      "institutionCode": "KU",
      "collectionCode": "Ornithology",
      "catalogNumber": "12345",
      "kdwp_status": null,
      "sensitivity_rank": "public"
    },
    "kfm:provenance": {
      "spec_hash": "sha256:abc…",
      "evidence_bundle_ref": "kfm://evidence/sha256:def…",
      "run_record_ref": "kfm://run/run-2026-05-21-001",
      "audit_ref": "kfm://audit/attest-…",
      "policy_digest": "sha256:ghi…",
      "source_surface": "idigbio-dwca",
      "dwca_bundle_ref": "kfm://catalog/dcat/idigbio-dwca/sha256:jkl…",
      "dwca_bundle_digest": "sha256:jkl…",
      "dwca_query_spec_hash": "sha256:mno…",
      "dwca_retrieved_at": "2026-05-21T08:00:00Z",
      "dwca_meta_xml_digest": "sha256:pqr…",
      "dwca_citations_txt_digest": "sha256:stu…",
      "dwca_record_count": 142378,
      "dwca_contributing_recordsets": ["<UUID-1>", "<UUID-2>", "<UUID-3>", "..."],
      "backbone_doi_version": "10.15468/39omei@<snapshot>"
    },
    "redaction_profile": null
  },
  "assets": {
    "data": {
      "href": "../data.parquet",
      "type": "application/vnd.apache.parquet",
      "file:checksum": "sha256:vwx…"
    },
    "dwca_bundle": {
      "href": "../bundle.zip",
      "type": "application/zip",
      "file:checksum": "sha256:jkl…",
      "roles": ["source", "metadata"]
    },
    "citations_txt": {
      "href": "../citations.txt",
      "type": "text/plain",
      "file:checksum": "sha256:stu…",
      "roles": ["metadata", "attribution"]
    }
  },
  "links": [
    { "rel": "cite-as", "href": "kfm://catalog/dcat/idigbio-dwca/sha256:jkl…", "title": "iDigBio Portal DwC-A bundle (cite-as)" },
    { "rel": "derived_from", "href": "kfm://catalog/dcat/idigbio-dwca/sha256:jkl…", "title": "source bundle" },
    { "rel": "self", "href": "./item.json" }
  ]
}
```

</details>

[Back to top](#-idigbio-portal-dwc-a-downloads)

---

## 16. Open questions

| ID | Question | Class | Status |
|---|---|---|---|
| OPEN-IDB-DWCA-01 | Confirm current iDigBio **portal download endpoint URL** and submission flow (web form vs API). | ops | **NEEDS VERIFICATION** |
| OPEN-IDB-DWCA-02 | Confirm the **refresh cadence** policy (PROPOSED quarterly; alternative: RSS-driven trigger on contributing-recordset publication). | ops | **OPEN** |
| OPEN-IDB-DWCA-03 | Confirm the **maximum bundle size** the connector should tolerate before chunking the portal query into multiple sub-bundles. | ops | **NEEDS VERIFICATION** |
| OPEN-IDB-DWCA-04 | Should DwC-A-derived Items share a STAC Collection with Search-API-derived Items, or live in **separate Collections**? Recommendation: **separate** (trust-class legibility). | catalog | **OPEN** |
| OPEN-IDB-DWCA-05 | Confirm whether the **`citations.txt` parser** is part of `tools/validators/biodiversity_dwca_validator/` or a separate `tools/validators/citation_anchor/`. | implementation | **NEEDS VERIFICATION** |
| OPEN-IDB-DWCA-06 | **CC BY-NC-SA admissibility.** Is NonCommercial-licensed iDigBio material admissible to KFM public layers at all? Default: **no**. | rights / policy | **OPEN** (companion to OPEN-IDB-MED-09) |
| OPEN-IDB-DWCA-07 | **Whole-bundle redistribution.** May KFM mirror the verbatim DwC-A zip on KFM-controlled infrastructure, or only host derivative records? | rights / governance | **OPEN — ADR-class** |
| OPEN-IDB-DWCA-08 | **Snapshot lineage in PROV.** Define the PROV-O shape that links a v2 bundle to its v1 predecessor (which records changed, which recordsets were revoked). | catalog | **OPEN** |
| OPEN-IDB-DWCA-09 | **Post-normalize record-count tolerance.** PROPOSED 0% (exact match after dedupe). Confirm or relax with steward sign-off. | implementation | **OPEN** |
| **OPEN-IDB-CONV-01** | **Flat-dossier vs family-folder convention.** Parallel iDigBio dossier sits at [`docs/sources/catalog/idigbio.md`](../idigbio.md); this product page sits in `docs/sources/catalog/idigbio/`. Reconciliation required. | governance / ADR | **OPEN — ADR-class** (companion to OQ-11 in the iDigBio dossier) |
| OPEN-DSC-03 | KFM namespace token (`kfm:` vs `ks-kfm:`) for STAC Collection summaries. | identity | **OPEN** — corpus C4-01 unresolved. |
| OPEN-DSC-* | Lane-wide open items — see [`OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md). | various | various |

[Back to top](#-idigbio-portal-dwc-a-downloads)

---

## 17. Related docs

- [`docs/sources/catalog/idigbio/README.md`](./README.md) — family landing page *(PROPOSED sibling; NEEDS VERIFICATION)*
- [`docs/sources/catalog/idigbio/occurrence-search.md`](./occurrence-search.md) — companion product page for the synchronous Search API surface *(PROPOSED sibling; NEEDS VERIFICATION)*
- [`docs/sources/catalog/idigbio/media-records.md`](./media-records.md) — companion product page for media records *(PROPOSED sibling; NEEDS VERIFICATION)*
- [`docs/sources/catalog/idigbio.md`](../idigbio.md) — **parallel iDigBio source dossier (flat-path convention)**; reconciled by OPEN-IDB-CONV-01
- [`docs/sources/catalog/README.md`](../README.md) — catalog source-pages index
- [`docs/sources/catalog/IDENTITY.md`](../IDENTITY.md) — Collection-id + namespace conventions
- [`docs/sources/catalog/PROFILES.md`](../PROFILES.md) — catalog profile lanes
- [`docs/sources/catalog/RIGHTS-AND-SENSITIVITY-MAP.md`](../RIGHTS-AND-SENSITIVITY-MAP.md) — per-license + per-feature sensitivity map
- [`docs/sources/catalog/OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) — lane-wide `OPEN-DSC-*` register
- [`docs/sources/catalog/_template/SOURCE_PRODUCT_TEMPLATE.md`](../_template/SOURCE_PRODUCT_TEMPLATE.md) — template every product page follows
- [`docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md`](../../../runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md) — operational refresh runbook; DwC-A cadence flows through this
- [`docs/doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) — placement, lifecycle, and naming authority
- [`docs/standards/PROV.md`](../../../standards/PROV.md) — W3C PROV-O profile (filename `PROV.md` vs corpus `PROVENANCE.md` is OPEN-DR-01 in `directory-rules.md §18`)
- [`docs/domains/fauna/README.md`](../../../domains/fauna/README.md), [`docs/domains/flora/README.md`](../../../domains/flora/README.md) — primary downstream consumers
- **External (cited inline):** iDigBio Data Ingestion Guidance, iDigBio IP Policy — see the dossier appendix in [`../idigbio.md`](../idigbio.md) for primary-source URLs.

<details>
<summary>📎 Appendix — corpus citations grounding this product page</summary>

- **C4-01 STAC `kfm:provenance`** (CONFIRMED) — `spec_hash`, `evidence_bundle_ref`, `run_record_ref`, `audit_ref`, `policy_digest`; per-asset `file:checksum`.
- **C4-02 Collection identity** (CONFIRMED expansion direction) — `kfm-<org>-<product>` pattern.
- **C4-03 STAC × Darwin Core hybrid** (CONFIRMED) — DwC terms inside STAC `properties` under `taxon` object.
- **C4-05 DCAT Distribution** (CONFIRMED) — dataset-level metadata for non-spatial / bundle-level data; the home for the DwC-A bundle record.
- **C5-02 Default-deny promotion** (CONFIRMED) — promotion fails closed.
- **C6-01 Sensitivity Rubric 0–5** (CONFIRMED) — six-level rubric.
- **C7-08 GBIF Backbone DOI** `10.15468/39omei` (CONFIRMED) — Backbone version pinned in `RunReceipt`.
- **C10-06 Kansas biodiversity stack** (CONFIRMED) — iDigBio named explicitly.
- **KFM-P2-PROG-0001** (PROPOSED, Pass 32) — "Kansas biodiversity ETL (GBIF + DwC-A) thin-slice recipe" composing GBIF and provider IPT DwC-A endpoints; license map `CC0 / CC-BY-4.0 / restricted`; EPSG:4326 normalization; dedupe by `(institutionCode|catalogNumber)`; EvidenceBundle + signed RunReceipt under `data/receipts/`. **This product is the iDigBio instantiation of the recipe.**
- **KFM-P17-PROG-0010** (PROPOSED) — DwC-A ingest separates raw zip, work extraction, processed observations, audit receipt, policy files, and CI gates by lifecycle stage.
- **KFM-P21-PROG-0048** (PROPOSED) — watcher no-op receipt for audit continuity when no material change observed; applies on identical-digest bundles.
- **KFM-P25-IDEA-0006 / KFM-P25-PROG-0017** (PROPOSED) — sensitive fauna precision degradation; fauna geoprivacy conditional schema.
- **KFM-P26-IDEA-0012** (PROPOSED) — canonical DwC normalizer before dedupe.
- **KFM-P26-PROG-0025** (PROPOSED) — catalog writers emit DCAT, STAC, and PROV entries with dataset DOI, harvest date, dataset version, license, rightsHolder, datasetID, and EvidenceBundle references.
- **KFM-P27-FEAT-0003** (PROPOSED) — STAC Projection lint report.
- **KFM-P22-PROG-0037** (PROPOSED) — STAC checksum closure against the ReleaseManifest digest.
- **`directory-rules.md §7.3`** (CONFIRMED) — connectors emit RAW/quarantine only; never publish.
- **`directory-rules.md §2.4(2)`** (CONFIRMED) — adding/removing canonical roots is ADR-class; whole-bundle mirror treated as ADR-class by analogy.
- **ADR-0001** (PROPOSED) — `schemas/contracts/v1/` schema home.

</details>

---

<sub>**Last reviewed:** 2026-05-21 *(Claude Code product-page polish session; KFM presentation standard v2 applied)* · **Version:** v0.2 (draft) · **Doc ID:** `kfm://doc/docs-sources-catalog-idigbio-portal-dwca-downloads` · [Back to top ↑](#-idigbio-portal-dwc-a-downloads)</sub>
