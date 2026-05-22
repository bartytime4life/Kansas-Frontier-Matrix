<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-kansas-ku-herbarium
title: KU R. L. McGregor Herbarium (KANU) — Source Catalog Entry
type: standard
subtype: source-catalog-entry
version: v0.2
status: draft
owners: <PLACEHOLDER — Docs steward + Source steward for kansas + Flora domain steward>
created: 2026-05-21
updated: 2026-05-21
policy_label: public
related:
  - docs/sources/catalog/kansas/README.md
  - docs/sources/catalog/kansas/kbs.md
  - docs/sources/catalog/kansas/ksu-special-collections.md
  - docs/sources/catalog/kansas/ksu-research-extension.md
  - docs/sources/catalog/kansas/ku-nhm.md
  - docs/sources/catalog/kansas/fhsu-sternberg.md
  - docs/sources/catalog/kansas/kdwp.md
  - docs/sources/catalog/kansas/khri.md
  - docs/sources/catalog/kansas/kansas-mesonet.md
  - docs/sources/catalog/kansas/kansas-state-archives.md
  - docs/sources/catalog/kansas/kansas-memory.md
  - docs/sources/catalog/README.md
  - docs/sources/catalog/IDENTITY.md
  - docs/sources/catalog/PROFILES.md
  - docs/sources/catalog/RIGHTS-AND-SENSITIVITY-MAP.md
  - docs/sources/catalog/OPEN-QUESTIONS.md
  - docs/sources/catalog/_template/SOURCE_PRODUCT_TEMPLATE.md
  - docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/truth-posture.md
  - docs/domains/flora/README.md
  - docs/domains/fauna/README.md
  - docs/standards/SENSITIVITY_RUBRIC.md
  - docs/registers/AUTHORITY_LADDER.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - docs/adr/ADR-0001-schema-home.md
  - schemas/contracts/v1/source/source_descriptor.schema.json
  - connectors/kansas/ku-herbarium/
  - data/registry/sources/
  - policy/sensitivity/
  - policy/rights/
  - tools/validators/flora_dwca_validator/
tags: [kfm, sources, catalog, kansas, ku, kanu, mcgregor-herbarium, flora, biodiversity, dwc-a, ipt, c7-10, kfm-p2-idea-0019, kfm-p2-prog-0002]
notes:
  - >-
    v0.2 promotes the v0.1 scaffold (PROPOSED schematic stub with placeholder
    body and `Yes / No (NEEDS VERIFICATION)` cells) into a full per-surface
    product-page brief aligned with the v0.2 catalog convention.
  - >-
    Structural reframing (NEW in v0.2) — umbrella-vs-surface model: this page
    is framed as the **KU McGregor Herbarium (KANU) per-surface product page**
    parented under the **Kansas Biological Survey (KBS) umbrella** at
    [`./kbs.md`](./kbs.md) (v0.2 in this conversation series). The DOM-FLORA
    source-family row "Kansas Biological Survey / KU herbarium surfaces"
    groups these together; the kbs.md v0.2 page treated them as
    two-surfaces-two-source-roles (NHI = authority; KANU = observed). v0.2 of
    this page makes the per-surface relationship explicit, parallel to the
    KSHS umbrella pattern (kansas-state-archives.md → kansas-memory.md +
    khri.md).
  - >-
    **Connector path correction in v0.2 — OPEN-KUHERB-01.** v0.1 used
    `connectors/ku_herbarium/` (top-level, snake_case, outside §7.3 family
    lane). v0.2 corrects to `connectors/kansas/ku-herbarium/` (nested under
    canonical §7.3 family + kebab-case). Same pattern as the other path
    corrections in this v0.2 series (Kansas Mesonet OPEN-MESO-01, KBS
    OPEN-KBS-01, KCC OPEN-KCC-01, KDOT OPEN-KDOT-01).
  - >-
    Atlas card lineage CONFIRMED: `KFM-P2-IDEA-0019` (CONFIRMED, Pass 32 — "the
    University of Kansas Herbarium (KANU)" named explicitly as one of four
    Kansas-specific biodiversity authorities; USDA PLANTS as plant-name
    authority; per-source watchers); `KFM-P2-PROG-0002` (active, Pass 32 —
    Kansas flora watcher; the **operationally definitive card for KANU**
    naming "the KU R.L. McGregor Herbarium (KANU) IPT" with full pipeline
    detail: DwC-A archives, specimen-backed primacy, restricted-taxa
    quarantine, cross-source dedupe via institutionCode + catalogNumber +
    eventDate, lifecycle placement, promotion gates A through G);
    DOM-FLORA §D source-family row "Kansas Biological Survey / KU herbarium
    surfaces"; `C7-10` (Kansas-First Domain Authorities — KBS NHI named);
    `C10-06` (Biodiversity Stack — KU NHM at ~454k specimens cited; KANU not
    specimen-counted in C10-06 but covered in the flora-focused
    KFM-P2-IDEA-0019); `KFM-P24-IDEA-0002` + `KFM-P24-PROG-0013` (sensitive
    species deny-by-default + OPA ABSTAIN/DENY); `KFM-P13-PROG-0018`
    (deterministic grid generalization); `C7-07` ITIS, `C7-08` GBIF Backbone
    DOI `10.15468/39omei`, `C7-09` GNIS, `C7-01` Wikidata for crosswalks.
  - >-
    `connectors/kansas/` lane is CONFIRMED (at commit
    `b6a27916bbb9e07cbf3752870c867476e1e094e7`) per Directory Rules v1.2 §7.3.
[/KFM_META_BLOCK_V2] -->

# KU R. L. McGregor Herbarium (KANU) — Source Catalog Entry

> **Per-surface product page** for the **University of Kansas R. L. McGregor Herbarium (KANU)** — KFM's primary in-state vascular-plant specimen authority per CONFIRMED `KFM-P2-IDEA-0019`: *"Kansas-specific biodiversity authorities supplement GBIF: the **University of Kansas Herbarium (KANU)**, Kansas State University herbarium and biocollections (KSC), iDigBio for digitized natural-history collections, and **USDA PLANTS for authoritative plant nomenclature and distribution**."* Parented under the **Kansas Biological Survey (KBS) umbrella brief** at [`./kbs.md`](./kbs.md) (v0.2) per the DOM-FLORA §D grouping "Kansas Biological Survey / KU herbarium surfaces."

[![Status: draft](https://img.shields.io/badge/status-draft-yellow)](#)
[![doc-version](https://img.shields.io/badge/doc--version-v0.2-blue)](#)
[![family](https://img.shields.io/badge/family-kansas%20%C2%A77.3%20canonical-success)](#)
[![surface-of](https://img.shields.io/badge/surface%20of-kbs.md%20(KBS%20umbrella)-7e57c2)](./kbs.md)
[![authority](https://img.shields.io/badge/C7--10-Kansas--first%20cluster%20(via%20KBS)-7e57c2)](#)
[![DOM-FLORA](https://img.shields.io/badge/DOM--FLORA-%C2%A7D%20"KBS%20%2F%20KU%20herbarium"-success)](#)
[![Source role](https://img.shields.io/badge/source--role-observed%20(specimen--backed)-blue)](#5-source-roles)
[![Restricted taxa](https://img.shields.io/badge/restricted%20taxa-quarantine%20%2F%20redact%20(KFM--P2--PROG--0002)-red)](#)
[![USDA PLANTS](https://img.shields.io/badge/plant%20names-USDA%20PLANTS%20(KFM--P2--IDEA--0019)-success)](#)
[![Rights](https://img.shields.io/badge/rights-NEEDS%20VERIFICATION-orange)](#)
[![DwC-A](https://img.shields.io/badge/format-Darwin%20Core%20Archive%20via%20IPT-informational)](#)
[![last-updated](https://img.shields.io/badge/last--updated-2026--05--21-informational)](#)

**Status:** `draft` (v0.2) &nbsp;·&nbsp; **Family:** [`kansas`](./README.md) &nbsp;·&nbsp; **Parent umbrella:** [`./kbs.md`](./kbs.md) (v0.2) &nbsp;·&nbsp; **Owners:** `<TODO — docs steward + source steward + flora domain steward>` &nbsp;·&nbsp; **Last reviewed:** 2026-05-21

---

## Quick jump

- [1. Scope](#1-scope) · [2. Status and source basis](#2-status-and-source-basis) · [3. Repo fit](#3-repo-fit) · [4. Inputs accepted](#4-inputs-accepted)
- [5. Source roles](#5-source-roles) · [6. Sensitivity and publication posture](#6-sensitivity-and-publication-posture) · [7. Pipeline diagram](#7-pipeline-diagram)
- [8. Cadence and freshness](#8-cadence-and-freshness) · [9. Rights and access](#9-rights-and-access) · [10. Authority anchoring](#10-authority-anchoring-and-crosswalks)
- [11. Pre-admission checklist](#11-pre-admission-checklist) · [12. Open verification](#12-open-verification-items) · [13. FAQ](#13-faq) · [14. Related docs](#14-related-docs)
- [Appendix A — Descriptor field placeholders](#appendix-a--descriptor-field-placeholders) · [Appendix B — Atlas idea-card lineage](#appendix-b--atlas-idea-card-lineage) · [Appendix C — Change log](#appendix-c--change-log)

---

## 1. Scope

> [!NOTE]
> **v0.1 → v0.2 promotion.** This page was authored in v0.1 as a thin PROPOSED scaffold (placeholder body, `Yes / No (NEEDS VERIFICATION)` cells, no operational detail beyond the Pass-10 C4-01 provenance fields). v0.2 promotes it into a full per-surface product-page brief consistent with sibling v0.2 product pages (`kansas-mesonet.md`, `kbs.md`, `kdwp.md`, `khri.md`, `ksgs.md`, etc.) authored earlier in this conversation series.

> [!IMPORTANT]
> **Path migration (connector — OPEN-KUHERB-01).** v0.1 used `connectors/ku_herbarium/` — top-level, snake_case, **OUTSIDE** the canonical `connectors/kansas/` §7.3 family lane. v0.2 corrects to `connectors/kansas/ku-herbarium/` (nested under canonical §7.3 + kebab-case). This is the same path-correction pattern as sibling v0.2 revisions (Kansas Mesonet OPEN-MESO-01, KBS OPEN-KBS-01, KCC OPEN-KCC-01, KDOT OPEN-KDOT-01). v0.2 of this doc preserves the v0.1 reference verbatim in §3 with the correction surfaced as OPEN-KUHERB-01.

> [!IMPORTANT]
> **Structural framing (new in v0.2) — umbrella-vs-surface.** This dossier is the **per-surface product page** for KU McGregor Herbarium (KANU). The **KBS umbrella brief** at [`./kbs.md`](./kbs.md) (v0.2) sets the shared institutional posture across KBS surfaces (KBS NHI + KU McGregor Herbarium / KANU). The two layers coexist:
> - **Umbrella brief** (`kbs.md` v0.2) — KBS institutional posture; two-surfaces-two-source-roles framing (NHI = authority; KANU = observed); restricted-taxa quarantine doctrine; three-way ranking disagreement policy.
> - **Per-surface page** (THIS DOC) — KANU-specific admission posture: IPT endpoint, DwC-A archive shape, specimen-backed observation primacy, USDA PLANTS anchoring, cross-source dedupe rule.
>
> Where this page states posture, it **inherits** from `kbs.md` v0.2 unless explicitly overridden. This is the same pattern as KSHS → kansas-state-archives.md (umbrella) → kansas-memory.md + khri.md (per-surface).

**This dossier** describes the KU R. L. McGregor Herbarium (KANU) as a KFM source: what role it plays in the KFM source ladder, what claims it can support (and which it cannot), the rights / sensitivity / access posture admission must respect, and the lifecycle gates a KANU-derived record passes before it touches a public surface.

**What this dossier is not.** It is not a `SourceDescriptor` instance, a connector, a policy bundle, a route, or a release manifest. Each of those has its own canonical home.

[Back to top](#ku-r-l-mcgregor-herbarium-kanu--source-catalog-entry)

---

## 2. Status and source basis

| Claim | Label | Basis |
|---|---|---|
| KANU is the primary KU vascular-plant specimen herbarium. | **CONFIRMED doctrine** | `KFM-P2-IDEA-0019` (CONFIRMED, Pass 32) — "the **University of Kansas Herbarium (KANU)**" named as one of four Kansas-specific biodiversity authorities supplementing GBIF; "KANU and KSC are the primary in-state herbaria." |
| KANU material is admitted via DwC-A archives from the KANU IPT. | **CONFIRMED operational doctrine** | `KFM-P2-PROG-0002` (active, Pass 32) — "A flora-specific watcher pulling **DwC-A archives from the KU R.L. McGregor Herbarium (KANU) IPT**." |
| KANU sits in the Kansas-first biodiversity authority cluster via the KBS umbrella. | **CONFIRMED doctrine** | DOM-FLORA §D source-family row "**Kansas Biological Survey / KU herbarium surfaces**" groups these together. `C7-10` names "KBS Natural Heritage Inventory" and "KU Biodiversity Institute" as Kansas-first authorities (CONFIRMED Pass-10). |
| Specimen-backed observations are preferred over crowd-sourced observations. | **CONFIRMED doctrine** | `KFM-P2-PROG-0002` — "specimen-backed observations are preferred over crowd observations." |
| USDA PLANTS is the canonical plant-name authority. | **CONFIRMED doctrine** | `KFM-P2-IDEA-0019` — "USDA PLANTS for authoritative plant nomenclature and distribution"; tension: "Nomenclature divergence between sources is real; the corpus directs that **USDA PLANTS be the authority for plant names**, with documented exceptions." |
| Restricted-taxa records (NatureServe, listed species) must be quarantined or redacted before any aggregate is published. | **CONFIRMED doctrine** | `KFM-P2-PROG-0002` — "restricted taxa (NatureServe, listed species) are **quarantined or redacted** before any aggregate is published." Cross-references `KFM-P24-IDEA-0002` deny-by-default + `KFM-P24-PROG-0013` OPA ABSTAIN/DENY. |
| Cross-source dedupe uses `institutionCode + catalogNumber + eventDate`. | **CONFIRMED operational rule** | `KFM-P2-PROG-0002` — "Cross-source dedupe uses institutionCode + catalogNumber + eventDate." |
| Validation rejects DwC-A archives missing required fields. | **CONFIRMED operational rule** | `KFM-P2-PROG-0002` — "Validation rejects archives that lack scientificName, decimalLatitude/Longitude, eventDate, license, rightsHolder, or datasetID." |
| Detection uses ETag / Last-Modified on the IPT. | **CONFIRMED operational rule** | `KFM-P2-PROG-0002` — "Detection uses ETag / Last-Modified for IPT." |
| Lifecycle placement: `data/raw/flora/<source>/...`. | **CONFIRMED operational rule** | `KFM-P2-PROG-0002` — "Lifecycle placement: data/raw/flora/<source>/<timestamp>/, data/work/flora/<run_id>/, data/processed/flora/<spec_hash>/, data/catalog/dcat|stac|prov/flora/, data/receipts/flora/." |
| Promotion gates A–G must all pass. | **CONFIRMED operational rule** | `KFM-P2-PROG-0002` — "Promotion gates A through G must all pass: schema valid, license compliant, provenance complete, spatial integrity verified, temporal consistency, deduplication across sources, Evidence Drawer renders correctly." |
| `connectors/kansas/` family lane CONFIRMED. | **CONFIRMED** | Directory Rules v1.2 §7.3 at commit `b6a27916bbb9e07cbf3752870c867476e1e094e7`. |
| KANU per-institution adapter currently exists at `connectors/kansas/ku-herbarium/`. | **PROPOSED / NEEDS VERIFICATION** | v0.1 used incorrect path `connectors/ku_herbarium/`; v0.2 corrects per OPEN-KUHERB-01; mounted-repo verification remains. |
| Specific KANU IPT endpoint URL, cadence, license terms. | **NEEDS VERIFICATION** | Not pinned by corpus; must be captured in the `SourceDescriptor` at admission. |

[Back to top](#ku-r-l-mcgregor-herbarium-kanu--source-catalog-entry)

---

## 3. Repo fit

> [!NOTE]
> Per Directory Rules v1.2 §6.1, `docs/sources/` is the doctrinal home for source-descriptor standards and source families. v0.2 adopts `docs/sources/catalog/<family>/<product>.md` as the catalog convention. **`connectors/kansas/` is CONFIRMED (at commit `b6a27916...`)** as one of the nine canonical connector families per Directory Rules v1.2 §7.3, so `docs/sources/catalog/kansas/` is the explanatory companion.

This document is **explanation**. It does not store machine-readable descriptors, define object meaning, validate shape, or make admit/deny decisions. Those live in their canonical homes:

| Concern | Canonical home (v0.2 path) | What lives there |
|---|---|---|
| Human-readable catalog entry (this file) | `docs/sources/catalog/kansas/ku-herbarium.md` | This document. |
| Source-descriptor standard | `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` (PROPOSED — referenced in plans, NEEDS VERIFICATION in repo) | Field-by-field doctrine for `SourceDescriptor`. |
| Machine-readable descriptor record | `data/registry/sources/kansas/ku-herbarium/source_descriptor.yaml` (PROPOSED) | Per-product `SourceDescriptor`. |
| Schema (shape) | `schemas/contracts/v1/source/source_descriptor.schema.json` (default per ADR-0001) | JSON Schema for `SourceDescriptor`. |
| Object-family meaning | `contracts/source/` (semantic Markdown) | What a `SourceDescriptor` means and invariants it carries. |
| Admit / restrict / deny policy | `policy/<domain>/` and `policy/sensitivity/` | OPA / policy bundle entries (rights, sensitivity, source-role, restricted-taxa gates). |
| Connector (fetch + admission) | `connectors/kansas/ku-herbarium/` — **family lane CONFIRMED at commit `b6a27916...`**; per-institution adapter PROPOSED. **v0.1 used `connectors/ku_herbarium/` (incorrect); see OPEN-KUHERB-01.** | Source-specific fetcher; output → `data/raw/flora/ku-herbarium/<run_id>/`. |
| Pipelines (executable) | `pipelines/ingest/`, `pipelines/normalize/`, `pipelines/validate/`, `pipelines/catalog/`, `pipelines/publish/` with `pipeline_specs/flora/` declarative companion | Promotion gates A–G per `KFM-P2-PROG-0002`. |
| Flora domain doc | `docs/domains/flora/` | Where flora object families are owned. |
| Sensitivity policy parameters | `policy/sensitivity/` | C6 rubric + restricted-taxa rules per `KFM-P2-PROG-0002` and `KFM-P24-PROG-0013`. |
| DwC-A validator | `tools/validators/flora_dwca_validator/` (PROPOSED per `KFM-P2-PROG-0002`) | Validates schema, required fields, license/rightsHolder/datasetID end-to-end. |
| Parent umbrella brief | [`./kbs.md`](./kbs.md) v0.2 | KBS-umbrella institutional posture (NHI authority + KANU observed). |

[Back to top](#ku-r-l-mcgregor-herbarium-kanu--source-catalog-entry)

---

## 4. Inputs accepted

The following classes of KANU-derived material are **in scope** for admission, subject to source-role tagging, rights resolution, sensitivity classification, and the standard receipt envelope.

- **Specimen records (DwC-A occurrence cores)** — vouchered plant specimens with `scientificName`, `decimalLatitude`/`decimalLongitude`, `eventDate`, `license`, `rightsHolder`, `datasetID`, `institutionCode`, `catalogNumber`, `basisOfRecord`. Treated as **`observed`** material per `KFM-P2-PROG-0002`; the specimen IS the evidence.
- **Specimen multimedia extensions** — herbarium-sheet images, label transcriptions, voucher data. Treated as `observed` evidence with parent-record provenance preserved.
- **Type specimens and historical collections** — taxonomic types and pre-statehood / early-statehood plant collections. Treated as `observed` (high evidentiary value); often citation-rich.
- **Range / distribution polygons derived from KANU specimen aggregations** — typically `aggregate` or `modeled` depending on construction; never collapsed into per-place truth without `AggregationReceipt` per Atlas §24.2.1.
- **Taxonomic determinations as recorded** — KANU determinations stand as the issuing-institution position for the named specimen, anchored to ITIS TSN (`C7-07`) or GBIF Backbone DOI `10.15468/39omei` (`C7-08`) for federation, with USDA PLANTS as the canonical plant-name authority per `KFM-P2-IDEA-0019`.

Every admitted KANU record carries: source identity, source role, rights posture, sensitivity rank, retrieval metadata, content checksum, `institutionCode` + `catalogNumber` + `eventDate` (the cross-source dedupe key per `KFM-P2-PROG-0002`), and a citation back to KANU. Records lacking any of these MUST go to `data/quarantine/`.

[Back to top](#ku-r-l-mcgregor-herbarium-kanu--source-catalog-entry)

---

## 5. Source roles

The source-role taxonomy is **doctrine**, not stylistic preference (Atlas §24.1.3, CONFIRMED Pass-23/32). Each KANU admission picks exactly one role; corrections produce a *new* descriptor and a `CorrectionNotice`, never an in-place edit.

| Role | Used for KANU when… | Example |
|---|---|---|
| `observed` | KANU staff or contributors collected, mounted, and curated the specimen. **This is the dominant role for KANU**. | A vouchered specimen of *Asclepias meadii* collected in Riley County, 1928-06-14, with herbarium-sheet image. |
| `aggregate` | KANU publishes a county-level or region-level rollup. | A county-by-county specimen count published as a checklist summary. |
| `modeled` | KANU publishes a modeled range/distribution surface. | A predicted-range raster derived from specimen aggregations. |
| `administrative` | KANU material is a curatorial / accession compilation. | An accession index or curatorial-history compilation. |
| `candidate` | A pre-validation DwC-A pull staged before merge. | Pre-admission staging while validators run. |

> [!IMPORTANT]
> **KANU is `observed`, not `authority`, in the source-role enum.** Compare KBS NHI ([`./kbs.md`](./kbs.md) v0.2), which IS `authority` for Kansas natural-community classifications and sensitivity rankings. The KBS umbrella's two-surfaces-two-source-roles framing names **NHI = authority** and **KANU = observed**. This distinction is operationally critical: a KANU specimen anchors a place-time-taxon claim (observation); it does not issue a sensitivity ranking or natural-community classification (authority).

> [!NOTE]
> **`regulatory` is NOT a KANU role.** Kansas regulatory authority for listed-species status is KDWP per `KFM-P19-IDEA-0005` (see [`./kdwp.md`](./kdwp.md) v0.2). Conflating a KANU specimen of a listed taxon with the *regulatory listing* of that taxon is a source-role anti-collapse violation per Atlas §24.1.3.

> [!CAUTION]
> **Specimen-backed primacy** (CONFIRMED, `KFM-P2-PROG-0002`): when a KANU specimen and an iNaturalist crowd observation describe the same occurrence, **the specimen is preferred**. This is not a tie-breaker for cosmetic preference — it is the corpus rule. AI surfaces and Evidence Drawer renderers MUST surface the specimen citation, not the crowd observation, when both are present. See [`./kbs.md`](./kbs.md) v0.2 OPEN-KBS-04 for the parallel three-way (KANU vs KBS NHI vs NatureServe) ranking question.

[Back to top](#ku-r-l-mcgregor-herbarium-kanu--source-catalog-entry)

---

## 6. Sensitivity and publication posture

> [!IMPORTANT]
> **Restricted-taxa quarantine rule** (CONFIRMED, `KFM-P2-PROG-0002`): *"restricted taxa (NatureServe, listed species) are **quarantined or redacted before any aggregate is published**."* This is operationally specific — it applies BEFORE aggregation, not after. A KANU DwC-A archive containing rare-plant records routes those records to `data/quarantine/` for steward review before any county-level or region-level aggregate can be published. Cross-references `KFM-P24-IDEA-0002` deny-by-default and `KFM-P24-PROG-0013` OPA ABSTAIN/DENY.

| Sensitivity class | Why KANU material engages it | Default outcome | `C6-01` rank guideline | Required controls |
|---|---|---|---|---|
| **Rare-plant exact locations** | KANU specimens of NatureServe-ranked or KDWP-listed taxa carry locality detail that can identify populations. | DENY public exact location per `KFM-P2-PROG-0002` + `KFM-P24-IDEA-0002`. | rank 3+ (S3); rank 4+ for S1/S2 per `C10-06` parallel | Geoprivacy transform per `KFM-P13-PROG-0018`; default profile `profile:sinc-obscure-10km` at rank 3; steward review; `RedactionReceipt` per Atlas §24.2.1. |
| **Type specimen locations** | Type specimens carry high taxonomic and locality value; population identification risk varies. | Case-by-case review; default RESTRICT for sensitive taxa. | rank 2–4 per taxon | Steward review at admission. |
| **Sacred / culturally sensitive places** | Some traditional-use plant records may overlap culturally sensitive areas. | DENY until consultation. | rank 4–5; `kfm:care` (`C15-02`) + OPA default-deny on CARE-tagged (`C15-03`). | Consultation record; coordinate with archaeology lane. |
| **Private landowner-sensitive data** | Some specimens collected on private land carry locality detail that identifies parcels/owners. | DENY exact / public if private or rights unclear. | rank 3+ | Aggregation; permissions; policy review. |
| **Source-rights-limited records** | KANU DwC-A archives carry per-record `license` and `rightsHolder` fields — these MUST be honored end-to-end. | DENY public release until terms respected per record. | rights gate (not rank) | `KFM-P2-PROG-0002`: "Normalization produces a canonical KFM record carrying license, rightsHolder, and datasetID end-to-end." |

> [!WARNING]
> **License + `rightsHolder` + `datasetID` end-to-end preservation** (CONFIRMED, `KFM-P2-PROG-0002`). KANU DwC-A archives carry per-record license assertions, rightsHolder identification, and `datasetID`. KFM normalization MUST preserve these three fields end-to-end on the canonical record — they are not metadata decoration, they are the operational basis for rights enforcement. Validation that rejects DwC-A records missing `license`, `rightsHolder`, or `datasetID` is mandatory.

> [!TIP]
> **T0–T4 vs `C6-01` 0–5 reconciliation** (same OPEN as sibling KHRI v0.2 OQ-KHRI-14, KSU R&E v0.2 OQ-KSURE-16). The Domains Atlas v1.1 §24.1 uses a T0–T4 scheme; Pass-10 `C6-01` uses a 0–5 scheme. The two schemes have not yet been reconciled by ADR. This page uses `C6-01` rank guidelines; future ADR resolution will harmonize both.

[Back to top](#ku-r-l-mcgregor-herbarium-kanu--source-catalog-entry)

---

## 7. Pipeline diagram

```mermaid
flowchart LR
  subgraph KANU_Universe["KANU universe (external to KFM)"]
    IPT[KANU IPT<br/>DwC-A archives<br/>specimen-backed observed]
    USDA[USDA PLANTS<br/>plant-name authority<br/>KFM-P2-IDEA-0019]
    GBIF[GBIF<br/>coverage + validation]
    iDIG[iDigBio<br/>coverage + validation]
  end

  subgraph KFM["KFM governance lanes"]
    DESC[SourceDescriptor<br/>data/registry/sources/kansas/ku-herbarium/]
    ACT{SourceActivation<br/>Decision}
    CONN[Connector<br/>connectors/kansas/ku-herbarium/<br/>CONFIRMED family lane<br/>adapter PROPOSED]
    VAL[DwC-A validator<br/>tools/validators/flora_dwca_validator/]
    RAW[(data/raw/flora/ku-herbarium/&lt;timestamp&gt;/)]
    QUAR[(data/quarantine/<br/>restricted taxa /<br/>missing required fields)]
    WORK[(data/work/flora/&lt;run_id&gt;/)]
    PROC[(data/processed/flora/&lt;spec_hash&gt;/)]
    CAT[(data/catalog/<br/>dcat | stac | prov / flora/)]
    PUB[(data/published/<br/>public-safe only)]
    POL[/policy/sensitivity/<br/>restricted-taxa rule<br/>KFM-P2-PROG-0002<br/>+ KFM-P13-PROG-0018/]
    REL[release/manifests/<br/>ReleaseManifest]
  end

  IPT --> DESC
  USDA -. plant-name authority .-> DESC
  GBIF -. coverage + dedupe .-> WORK
  iDIG -. coverage + dedupe .-> WORK
  DESC --> ACT
  ACT -->|allowed / restricted| CONN
  ACT -->|denied / needs-review| QUAR
  CONN --> VAL
  VAL -->|valid DwC-A| RAW
  VAL -. missing required fields .-> QUAR
  RAW --> WORK
  WORK -. restricted taxa<br/>quarantine before aggregate .-> QUAR
  WORK --> PROC
  PROC --> CAT
  CAT --> REL
  REL --> PUB
  POL -. restricted-taxa rule .-> WORK
  POL -. redaction profile .-> CAT
  POL -. redaction profile .-> PUB

  classDef confirmed fill:#d5e8d4,stroke:#82b366;
  classDef proposed stroke-dasharray: 4 3;
  classDef quarantine fill:#fff4e0,stroke:#d4882b;
  class CONN confirmed;
  class DESC,ACT,VAL,RAW,WORK,PROC,CAT,PUB,POL,REL proposed;
  class QUAR quarantine;
```

> [!NOTE]
> Lifecycle placement (`data/raw/flora/<source>/<timestamp>/`, `data/work/flora/<run_id>/`, `data/processed/flora/<spec_hash>/`, `data/catalog/dcat|stac|prov/flora/`, `data/receipts/flora/`) is CONFIRMED operational doctrine per `KFM-P2-PROG-0002`. The `restricted-taxa quarantine before aggregate` edge from WORK → QUARANTINE is the operationally specific rule: NOT a generic deny — a pre-aggregate guard that protects rare-plant locality data even when the dataset overall is admissible.

[Back to top](#ku-r-l-mcgregor-herbarium-kanu--source-catalog-entry)

---

## 8. Cadence and freshness

| Concern | Value | Status |
|---|---|---|
| Detection signal | ETag / Last-Modified on the KANU IPT | **CONFIRMED operational rule** per `KFM-P2-PROG-0002` |
| Cadence | Per-IPT; KANU IPT update frequency varies by curatorial activity | **NEEDS VERIFICATION** |
| Cross-source coverage check | GBIF modified-since query | **CONFIRMED operational rule** per `KFM-P2-PROG-0002` |
| Taxonomy refresh | USDA PLANTS version timestamps | **CONFIRMED operational rule** per `KFM-P2-PROG-0002` |
| Cross-source dedupe | `institutionCode + catalogNumber + eventDate` | **CONFIRMED operational rule** per `KFM-P2-PROG-0002` |
| Snapshot vs incremental | Open question — `KFM-P2-PROG-0002` open question: "What is the right cadence per source (incremental modified-since vs frozen GBIF download)?" | **OPEN** |

> [!TIP]
> `KFM-P2-IDEA-0019` raises a parallel open question — "Should KFM produce a unified Kansas-flora dataset that merges KANU, KSC, iDigBio, and GBIF into a single artifact, or maintain separate per-source artifacts? Probably both: separate for fidelity, merged for convenience." The KFM-internal answer is **both** — preserve per-source artifacts (KANU stays distinct from KSC stays distinct from GBIF) AND offer merged convenience views with full lineage. See OPEN-KUHERB-09.

[Back to top](#ku-r-l-mcgregor-herbarium-kanu--source-catalog-entry)

---

## 9. Rights and access

| Posture dimension | Value | Status | Notes |
|---|---|---|---|
| Rights / terms of use | Per-record via DwC-A `license` field | **CONFIRMED operational mechanism** | `KFM-P2-PROG-0002`: "Validation rejects archives that lack… license, rightsHolder, or datasetID." End-to-end preservation mandatory. |
| Specific KANU institutional license terms | Per current KANU IPT | **NEEDS VERIFICATION** | DOM-FLORA: "rights and current terms NEEDS VERIFICATION; sensitive joins fail closed." |
| Attribution requirement | Per `rightsHolder` field + institutional citation | **CONFIRMED operational mechanism** | `rightsHolder` preserved end-to-end. |
| Redistribution | DwC-A `license` may include Creative Commons (CC0, CC-BY, CC-BY-NC) or institutional terms | **NEEDS VERIFICATION per record** | Per-record evaluation at validation. |
| Access method | DwC-A archives via KANU IPT (GBIF Integrated Publishing Toolkit) | **CONFIRMED operational mechanism** | `KFM-P2-PROG-0002`. |
| KANU IPT endpoint URL | Per current KANU configuration | **NEEDS VERIFICATION** | Not pinned by corpus. |
| Cadence | Per KANU curatorial activity | **NEEDS VERIFICATION** | See §8. |
| Stewardship contact | KANU staff | **NEEDS VERIFICATION** | Source-steward role mediates at admission. |
| Persistent identifiers | `institutionCode + catalogNumber` per specimen; `datasetID` per archive | **CONFIRMED operational mechanism** | `KFM-P2-PROG-0002` cross-source dedupe key. |
| Live connector in mounted repo | UNKNOWN | **UNKNOWN** | Family lane `connectors/kansas/` CONFIRMED at commit; per-institution adapter `connectors/kansas/ku-herbarium/` PROPOSED per OPEN-KUHERB-01. |

> [!CAUTION]
> **Unknown rights fail closed** per `C5-02`. Until a `SourceDescriptor` and `SourceActivationDecision` exist for KANU, any harvested KANU material stays in `data/raw/flora/ku-herbarium/` or `data/quarantine/`. The `flora_dwca_validator` per `KFM-P2-PROG-0002` will reject archives missing `license` / `rightsHolder` / `datasetID` — this enforces the rights gate at validation time.

[Back to top](#ku-r-l-mcgregor-herbarium-kanu--source-catalog-entry)

---

## 10. Authority anchoring and crosswalks

KANU records anchor to the relevant *external* authority for the entity type, with the KANU specimen identifier (`institutionCode + catalogNumber`) stored in parallel per `C7-10` parallel-anchor rule — never instead.

| Entity in KANU material | Required external anchor | KANU identifier role | Notes |
|---|---|---|---|
| Plant taxon (name) | **USDA PLANTS (primary per `KFM-P2-IDEA-0019`)**; ITIS TSN (`C7-07` secondary); GBIF Backbone DOI `10.15468/39omei` (`C7-08` federation) | Stored alongside as KANU determination of record. | Per `KFM-P2-IDEA-0019` tension: "USDA PLANTS be the authority for plant names, with documented exceptions." When KANU determination disagrees with USDA PLANTS, the disagreement is recorded — not silently resolved. See OPEN-KUHERB-05. |
| Specimen | `institutionCode + catalogNumber` per DwC-A | KANU specimen-record identifier | Cross-source dedupe key per `KFM-P2-PROG-0002`. |
| Collection event | `eventID` + `eventDate` per DwC-A | Per-event identifier | Part of cross-source dedupe key. |
| Locality / place | USGS GNIS (primary, `C7-09`); Wikidata QID (`C7-01` crosswalk substrate) | KANU locality string preserved | `C7-09` mandates GNIS anchoring for in-scope places. |
| Collector / determiner (persons) | LCNAF (`C7-02`); VIAF (`C7-03`); Wikidata QID (`C7-01`) | KANU agent identifier preserved | Person names tied to historic specimens require name-authority anchoring. |
| Dataset | `datasetID` per DwC-A | KANU dataset identifier | End-to-end preservation per `KFM-P2-PROG-0002`. |

> [!NOTE]
> Per project doctrine, **the USDA PLANTS name is the authority for plant nomenclature** (`KFM-P2-IDEA-0019`), and **the Wikidata QID is a routing anchor, not a truth source** (`C7-01`). The upstream authority IRI (USDA PLANTS, ITIS, GBIF Backbone, GNIS, LCNAF/VIAF) remains the citation target for substantive claims.

[Back to top](#ku-r-l-mcgregor-herbarium-kanu--source-catalog-entry)

---

## 11. Pre-admission checklist

The following items SHOULD be satisfied before any KANU dataset is admitted past `data/raw/`. These are the gates a green-field admission would pass through per `KFM-P2-PROG-0002` (gates A–G).

- [ ] **`SourceDescriptor` drafted** for KANU. Fields populated: identity, source role (`observed`), rights posture, access method (IPT DwC-A), cadence, steward contact, sensitivity class, freshness expectation, attribution, public-release class, parent-umbrella reference to `./kbs.md` v0.2.
- [ ] **Rights confirmation** recorded — DwC-A `license` field semantics confirmed per record; KANU institutional terms confirmed at descriptor level.
- [ ] **Source-role assignment** justified — `observed` is the primary role per `KFM-P2-PROG-0002`; sub-products (aggregates, range polygons) get their own descriptors with different roles.
- [ ] **DwC-A validator wired** — `tools/validators/flora_dwca_validator/` per `KFM-P2-PROG-0002`; rejects archives missing `scientificName`, `decimalLatitude`/`decimalLongitude`, `eventDate`, `license`, `rightsHolder`, or `datasetID`.
- [ ] **Restricted-taxa quarantine rule wired** — automated quarantine of NatureServe-ranked / KDWP-listed taxa BEFORE aggregation per `KFM-P2-PROG-0002`.
- [ ] **Anchoring strategy declared** — USDA PLANTS (primary plant-name authority per `KFM-P2-IDEA-0019`); ITIS TSN / GBIF Backbone for federation; GNIS for locality; LCNAF/VIAF/Wikidata for persons.
- [ ] **`SourceActivationDecision`** issued: `allowed | restricted | denied | needs-review`. Connector remains inactive until this exists per `C5-02`.
- [ ] **Fixtures** — valid + invalid DwC-A fixtures under `fixtures/flora/ku-herbarium/`.
- [ ] **Policy gates** — admit / restrict / deny / abstain rules covering source-role, sensitivity (including restricted-taxa rule), and rights per `KFM-P24-PROG-0013`.
- [ ] **Receipt envelope** — admission emits `RawCaptureReceipt`; promotion emits `TransformReceipt`, `ValidationReport`, `EvidenceRef`, `RedactionReceipt` where applicable per Atlas §24.2.1.
- [ ] **Cross-source dedupe rule** — `institutionCode + catalogNumber + eventDate` per `KFM-P2-PROG-0002`; coordinated with GBIF and iDigBio coverage pulls.
- [ ] **Promotion gates A–G** wired per `KFM-P2-PROG-0002`: schema valid, license compliant, provenance complete, spatial integrity verified, temporal consistency, deduplication across sources, Evidence Drawer renders correctly.
- [ ] **Rollback target** declared before any `PUBLISHED` transition.

[Back to top](#ku-r-l-mcgregor-herbarium-kanu--source-catalog-entry)

---

## 12. Open verification items

| # | Item | Owner (PROPOSED) | Why it matters |
|---|---|---|---|
| **OPEN-KUHERB-01** (PATH CORRECTION) | Connector path corrected from v0.1's `connectors/ku_herbarium/` (top-level, snake_case, outside §7.3) to v0.2's `connectors/kansas/ku-herbarium/` (nested under §7.3 family lane, kebab-case). Mounted-repo verification required. | Pipeline owner | Family-lane integrity per Directory Rules §7.3. |
| **OPEN-KUHERB-02** (UMBRELLA) | Confirm umbrella relationship to [`./kbs.md`](./kbs.md) v0.2 — this page is positioned as a per-surface page under the KBS umbrella per DOM-FLORA §D grouping "Kansas Biological Survey / KU herbarium surfaces" and the two-surfaces-two-source-roles framing in kbs.md v0.2 (NHI = authority; KANU = observed). | Docs steward + flora domain steward | Avoids parallel-authority drift. |
| **OPEN-KUHERB-03** | Confirm current KANU IPT endpoint URL and authentication posture. | Source steward | Drives connector implementation. |
| **OPEN-KUHERB-04** | Confirm KANU institutional license terms and DwC-A per-record license posture (CC0 / CC-BY / CC-BY-NC / restricted). | Source steward | Rights gate at validation per `KFM-P2-PROG-0002`. |
| **OPEN-KUHERB-05** | Three-way plant-name disagreement policy: when KANU determination, USDA PLANTS, and GBIF Backbone disagree on a taxon, what is the operational citation strategy? `KFM-P2-IDEA-0019` directs "USDA PLANTS be the authority for plant names, with documented exceptions" — the exception mechanism needs operational definition. | Flora domain steward | Plant-name authority discipline. |
| **OPEN-KUHERB-06** | Specimen-vs-crowd ranking when KANU and iNaturalist describe the same occurrence: `KFM-P2-PROG-0002` directs "specimen-backed observations are preferred over crowd observations" — confirm Evidence Drawer + AI surface enforcement. | Flora domain steward + UI steward | Specimen-backed primacy enforcement. |
| **OPEN-KUHERB-07** | Cross-source dedupe rule `institutionCode + catalogNumber + eventDate` — confirm field-level semantics across KANU, KSC, GBIF, iDigBio (different aggregators may carry different `institutionCode` casing or `catalogNumber` formats). | Flora domain steward | Dedupe correctness. |
| **OPEN-KUHERB-08** | Confirm sibling product pages exist under `docs/sources/catalog/kansas/`: `kbs.md` (umbrella; v0.2 in this series — CONFIRMED), `ku-nhm.md` (KU Biodiversity Institute Natural History Museum), `fhsu-sternberg.md`, `kdwp.md`, etc. | Docs steward | Cross-reference integrity. |
| **OPEN-KUHERB-09** | Decide unified-Kansas-flora-dataset vs separate per-source artifacts policy per `KFM-P2-IDEA-0019` open question: "Should KFM produce a unified Kansas-flora dataset that merges KANU, KSC, iDigBio, and GBIF into a single artifact, or maintain separate per-source artifacts? Probably both." | Flora domain steward | Catalog architecture. |
| **OPEN-KUHERB-10** | Confirm T0–T4 (Atlas v1.1) vs `C6-01` 0–5 sensitivity tier-scheme reconciliation (same OPEN as KHRI v0.2 OQ-KHRI-14, KSU R&E v0.2 OQ-KSURE-16, KBS v0.2 cross-reference). | Sensitivity steward | Sensitivity rubric harmonization. |
| **OPEN-KUHERB-11** | Confirm KU McGregor Herbarium administrative home — KFM-P2-IDEA-0019 names KANU separately from C7-10's "KU Biodiversity Institute"; DOM-FLORA groups it with KBS. Real-world: McGregor Herbarium is administratively under Kansas Biological Survey at KU. The kbs.md v0.2 umbrella framing is correct; mounted-repo verification of this organizational claim remains. | Docs steward | Umbrella-vs-surface correctness. |
| **OPEN-KUHERB-12** | Confirm corpus card-ID stability for `KFM-P2-IDEA-0019`, `KFM-P2-PROG-0002`, `KFM-P24-IDEA-0002`, `KFM-P24-PROG-0013`. | Docs steward | Card stability. |

[Back to top](#ku-r-l-mcgregor-herbarium-kanu--source-catalog-entry)

---

## 13. FAQ

<details>
<summary><strong>How does this page relate to <code>kbs.md</code> v0.2?</strong></summary>

This page is the **per-surface product page** for KU McGregor Herbarium (KANU); [`./kbs.md`](./kbs.md) v0.2 is the **KBS-umbrella brief**. The umbrella sets shared KBS institutional posture (rights floor, sensitivity register, restricted-taxa quarantine doctrine, two-surfaces-two-source-roles framing — NHI = authority, KANU = observed). This page sets the KANU-surface-specific admission posture (IPT endpoint, DwC-A archive shape, USDA PLANTS anchoring, specimen-backed primacy). Both layers exist by design; the umbrella does not substitute for this page and this page does not substitute for the umbrella.

</details>

<details>
<summary><strong>Why is KANU treated as <code>observed</code> rather than <code>authority</code>?</strong></summary>

Because KANU specimens are *evidence of occurrence* — a place-time-taxon observation backed by a physical voucher. KANU does not issue taxonomic determinations as authoritative legal status, sensitivity rankings, or natural-community classifications; those are authority-class products. The companion in the KBS umbrella, KBS Natural Heritage Inventory (NHI), IS `authority` for Kansas natural-community classifications and sensitivity rankings. The umbrella's two-surfaces-two-source-roles framing surfaces this in [`./kbs.md`](./kbs.md) v0.2.

</details>

<details>
<summary><strong>Why does USDA PLANTS outrank KANU determinations for plant names?</strong></summary>

Because `KFM-P2-IDEA-0019` (CONFIRMED, Pass 32) directs it: "USDA PLANTS for authoritative plant nomenclature and distribution"; tension paragraph: "Nomenclature divergence between sources is real; the corpus directs that USDA PLANTS be the authority for plant names, with documented exceptions." The KANU determination is preserved as the issuing-institution position for the named specimen, but the KFM plant-name slot is filled by the USDA PLANTS resolution. When the two disagree, the disagreement is recorded — not silently picked. See OPEN-KUHERB-05.

</details>

<details>
<summary><strong>What happens if a KANU DwC-A archive contains a rare-plant record?</strong></summary>

The record routes to `data/quarantine/` per the restricted-taxa rule in `KFM-P2-PROG-0002`: "restricted taxa (NatureServe, listed species) are quarantined or redacted before any aggregate is published." This is a PRE-AGGREGATE guard — the dataset as a whole may still admit, but the specific rare-plant records are removed from the aggregation pathway. Public release of generalized derivatives (e.g., 10 km obscured locality via `profile:sinc-obscure-10km` per `C6-02`) is possible only after geoprivacy transform per `KFM-P13-PROG-0018`, `RedactionReceipt` recording, and steward review.

</details>

<details>
<summary><strong>How does KANU dedupe against KSC, GBIF, and iDigBio?</strong></summary>

Per `KFM-P2-PROG-0002`: cross-source dedupe key is `institutionCode + catalogNumber + eventDate`. A KANU specimen with `institutionCode=KANU`, `catalogNumber=N12345`, `eventDate=1928-06-14` is the same specimen whether harvested from the KANU IPT, GBIF, or iDigBio — the three pulls reconcile to one canonical record with three lineage entries. KANU is preferred per specimen-backed primacy when source disagreement exists. See OPEN-KUHERB-07.

</details>

<details>
<summary><strong>What happens if a KANU DwC-A record is missing <code>license</code> or <code>rightsHolder</code>?</strong></summary>

It is rejected at validation per `KFM-P2-PROG-0002`: "Validation rejects archives that lack scientificName, decimalLatitude/Longitude, eventDate, license, rightsHolder, or datasetID." The rejection routes the record to `data/quarantine/` with the missing-field reason in the receipt. The `flora_dwca_validator` enforces this at the gate.

</details>

<details>
<summary><strong>Why is the connector path correction in v0.2 necessary?</strong></summary>

Because v0.1 placed the connector at `connectors/ku_herbarium/` (top-level, snake_case) — outside the canonical `connectors/kansas/` §7.3 family lane (CONFIRMED at commit `b6a27916...` per Directory Rules v1.2). v0.2 corrects to `connectors/kansas/ku-herbarium/` (nested under canonical §7.3 + kebab-case). This is the same path-correction pattern applied to the four other v0.1 scaffolds in this conversation series with incorrect top-level placements: Kansas Mesonet (OPEN-MESO-01), KBS (OPEN-KBS-01), KCC (OPEN-KCC-01), KDOT (OPEN-KDOT-01). See OPEN-KUHERB-01.

</details>

[Back to top](#ku-r-l-mcgregor-herbarium-kanu--source-catalog-entry)

---

## 14. Related docs

> [!NOTE]
> Targets below reflect the v0.2 catalog reorganization (`docs/sources/catalog/<family>/<product>.md`, kebab-case slugs, nested under §7.3 family folders). Sibling product pages PROPOSED until verified in the mounted repo. Adjust paths via a `DRIFT_REGISTER` entry rather than silently divergent siblings.

- [`./README.md`](./README.md) — `docs/sources/catalog/kansas/` family README v0.2 (lists this brief; confirms `connectors/kansas/` as §7.3 canonical at commit `b6a27916...`)
- [`./kbs.md`](./kbs.md) — **KBS-umbrella brief (v0.2)** — this dossier's parent; KBS NHI authority + KU McGregor Herbarium (KANU) observed
- [`./ku-nhm.md`](./ku-nhm.md) — sibling Kansas-first biodiversity authority per `C7-10` (KU Biodiversity Institute / Natural History Museum, ~454k specimens per `C10-06`)
- [`./fhsu-sternberg.md`](./fhsu-sternberg.md) — sibling in-state biodiversity collection
- [`./ksu-special-collections.md`](./ksu-special-collections.md) — sibling K-State collections (PROPOSED; not the same institution but related Kansas land-grant)
- [`./ksu-research-extension.md`](./ksu-research-extension.md) — sibling K-State umbrella covering variety trials (cf. flora context via `KFM-P2-PROG-0002`)
- [`./kdwp.md`](./kdwp.md) — sibling Kansas-first authority per `C7-10` (regulatory listings for rare-plant context per `KFM-P19-IDEA-0005`)
- [`./khri.md`](./khri.md) — sibling Kansas-first authority per `C7-10`
- [`./kansas-mesonet.md`](./kansas-mesonet.md) — sibling per-surface page (atmosphere / soil)
- [`./kansas-state-archives.md`](./kansas-state-archives.md) — sibling Kansas-first umbrella (KSHS — parallel umbrella pattern model)
- [`./kansas-memory.md`](./kansas-memory.md) — sibling per-surface page (parallel umbrella pattern)
- [`../README.md`](../README.md) — `docs/sources/catalog/` index (TODO: create or verify)
- [`../IDENTITY.md`](../IDENTITY.md) — Collection-id and namespace conventions
- [`../PROFILES.md`](../PROFILES.md) — catalog-profile selection guidance
- [`../RIGHTS-AND-SENSITIVITY-MAP.md`](../RIGHTS-AND-SENSITIVITY-MAP.md) — lane-wide rights/sensitivity matrix
- [`../OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) — lane-wide `OPEN-DSC-*` items
- [`../../SOURCE_DESCRIPTOR_STANDARD.md`](../../SOURCE_DESCRIPTOR_STANDARD.md) — source-descriptor field standard *(PROPOSED — referenced in plans; NEEDS VERIFICATION in repo)*
- [`../../../doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) — placement law (§6.1, §7.3, §7.4, §9.1, §11)
- [`../../../doctrine/lifecycle-law.md`](../../../doctrine/lifecycle-law.md) — RAW → PUBLISHED governance
- [`../../../doctrine/truth-posture.md`](../../../doctrine/truth-posture.md) — cite-or-abstain
- [`../../../domains/flora/README.md`](../../../domains/flora/README.md) — primary receiving domain
- [`../../../domains/fauna/README.md`](../../../domains/fauna/README.md) — secondary cross-cutting (specimen-based occurrence pattern transferable per `KFM-P2-PROG-0002` "doctrine likely transferable to fauna and other biodiversity domains")
- [`../../../standards/SENSITIVITY_RUBRIC.md`](../../../standards/SENSITIVITY_RUBRIC.md) — `C6-01` 0–5 rubric (PROPOSED in corpus)
- [`../../../registers/AUTHORITY_LADDER.md`](../../../registers/AUTHORITY_LADDER.md) — authority order
- [`../../../registers/DRIFT_REGISTER.md`](../../../registers/DRIFT_REGISTER.md) — drift filing
- [`../../../adr/ADR-0001-schema-home.md`](../../../adr/ADR-0001-schema-home.md) — schema-home convention
- Pass-10 Idea Index — **`C7-10`** Kansas-First Domain Authorities (CONFIRMED — KBS NHI + KU Biodiversity Institute named); **`C10-06`** Biodiversity Stack (CONFIRMED — KU NHM ~454k specimens cited); **`C5-02`** default-deny promotion (CONFIRMED); **`C6-01`/`C6-02`** sensitivity rubric + named profiles (CONFIRMED); **`C7-01`** Wikidata; **`C7-02`** LCNAF; **`C7-07`** ITIS TSN; **`C7-08`** GBIF Backbone DOI `10.15468/39omei`; **`C7-09`** GNIS; **`C4-01`** STAC `kfm:provenance` (CONFIRMED)
- Pass-23/32 Consolidated Atlas — **`KFM-P2-IDEA-0019`** KANU + KSC + iDigBio + USDA PLANTS biodiversity authorities (CONFIRMED, Pass 32); **`KFM-P2-PROG-0002`** Kansas flora watcher / KANU IPT pipeline (active, Pass 32); **`KFM-P24-IDEA-0002`** + **`KFM-P24-PROG-0013`** sensitive deny-by-default + OPA ABSTAIN/DENY (active); **`KFM-P13-PROG-0018`** sensitive grid generalization (active); **`KFM-P19-IDEA-0005`** KDWP regulatory (referenced for contrast); **DOM-FLORA §D** "Kansas Biological Survey / KU herbarium surfaces" (CONFIRMED listing); Atlas §24.1.2 + §24.1.3 + §24.2.1 + §24.8 (CONFIRMED)

[Back to top](#ku-r-l-mcgregor-herbarium-kanu--source-catalog-entry)

---

## Appendix A — Descriptor field placeholders

<details>
<summary><strong>Illustrative SourceDescriptor skeleton for KU McGregor Herbarium (KANU)</strong></summary>

> [!NOTE]
> The field surface below is **PROPOSED and illustrative**, drawn from the descriptor surface sketched in the Domains Culmination Atlas + sibling v0.2 descriptor sketches (`kbs.md`, `kansas-state-archives.md`, `kdwp.md`). Authoritative shape lives in `schemas/contracts/v1/source/source_descriptor.schema.json` per ADR-0001 (NEEDS VERIFICATION in repo). Do not treat this appendix as a contract.

```yaml
# PROPOSED illustrative skeleton — NOT a contract.
id: TODO/source/ku-herbarium-v<version>
source_id: ku-herbarium
source_family: kansas                           # v0.2 catalog folder; CONFIRMED §7.3 family at commit b6a27916...
source_family_enum: other                       # closed enum per KFM-P3-PROG-0001
biodiversity_subfamily: kbs-umbrella            # internal KBS sub-grouping per DOM-FLORA §D
name: KU R. L. McGregor Herbarium (KANU)
publisher: Kansas Biological Survey, University of Kansas
program: KU R. L. McGregor Herbarium
umbrella_family_ref: kbs                        # PROPOSED v0.2: KBS-umbrella brief per ./kbs.md
source_role: observed                           # primary; KFM-P2-PROG-0002 specimen-backed primacy
role_authority: KU R. L. McGregor Herbarium (KANU)
kansas_first_cluster: C7-10                     # via KBS umbrella; KFM-P2-IDEA-0019 names KANU separately
parallel_anchor_rule: C7-10                     # store KANU IRI alongside federal/international anchor
biodiversity_stack_member: C10-06               # CONFIRMED stack membership (KU NHM separately named at ~454k)
flora_authority: KFM-P2-IDEA-0019               # CONFIRMED card citing KANU
operational_watcher: KFM-P2-PROG-0002           # CONFIRMED card with operational detail
access:
  method: ipt-dwca                              # Integrated Publishing Toolkit + Darwin Core Archive
  endpoint_url: TODO                            # NEEDS VERIFICATION (per OPEN-KUHERB-03)
  auth: TODO                                    # public DwC-A typical; verify
detection:
  signal: ETag / Last-Modified                  # per KFM-P2-PROG-0002
  fallback: modified-since query on GBIF coverage pull
rights:
  per_record_license_field: license             # DwC-A required field per KFM-P2-PROG-0002
  per_record_rightsholder_field: rightsHolder   # DwC-A required field per KFM-P2-PROG-0002
  dataset_id_field: datasetID                   # DwC-A required field per KFM-P2-PROG-0002
  institutional_terms_url: TODO                 # NEEDS VERIFICATION (per OPEN-KUHERB-04)
  posture_if_unknown: deny                       # per C5-02
cadence:
  expected: per-curatorial-activity              # NEEDS VERIFICATION
  observed: TODO
sensitivity:
  rubric_atlas_v1_1: T0-T4                       # PROPOSED scheme
  rubric_pass10: C6-01                            # 0-5 cross-reference
  default_tier: mixed                            # see §6 per record class
  restricted_taxa_rule: quarantine-before-aggregate  # CONFIRMED per KFM-P2-PROG-0002
  rare_plant_default_rank: 3                     # ≈ C6-01 rank 3 (S3); 4+ for S1/S2 per C10-06 parallel
  default_redaction_profile: profile:sinc-obscure-10km
validation:
  validator: tools/validators/flora_dwca_validator
  required_fields:                               # per KFM-P2-PROG-0002
    - scientificName
    - decimalLatitude
    - decimalLongitude
    - eventDate
    - license
    - rightsHolder
    - datasetID
anchoring:
  taxon_authority_primary: USDA PLANTS           # per KFM-P2-IDEA-0019
  taxon_authority_secondary: ITIS TSN            # C7-07
  taxon_authority_federation: GBIF Backbone DOI 10.15468/39omei  # C7-08
  place_authority: USGS GNIS                     # C7-09
  person_authority: LCNAF (C7-02) / VIAF (C7-03) / Wikidata (C7-01)
dedupe:
  cross_source_key: institutionCode + catalogNumber + eventDate  # per KFM-P2-PROG-0002
  cross_source_partners: [kanu, ksc, gbif, idigbio]
lifecycle_placement:                              # CONFIRMED per KFM-P2-PROG-0002
  raw: data/raw/flora/ku-herbarium/<timestamp>/
  work: data/work/flora/<run_id>/
  processed: data/processed/flora/<spec_hash>/
  catalog: data/catalog/dcat|stac|prov/flora/
  receipts: data/receipts/flora/
promotion_gates:                                  # per KFM-P2-PROG-0002
  - A_schema_valid
  - B_license_compliant
  - C_provenance_complete
  - D_spatial_integrity_verified
  - E_temporal_consistency
  - F_deduplication_across_sources
  - G_evidence_drawer_renders
public_release_class: restricted-by-default       # per KFM-P24-IDEA-0002
care_review_required: true                        # per C15-02 / C15-03 for culturally sensitive plant records
status:
  activation_decision: needs-review               # allowed | restricted | denied | needs-review
  fixtures_present: false
  validators_present: false
  policy_gates_present: false
```

</details>

[Back to top](#ku-r-l-mcgregor-herbarium-kanu--source-catalog-entry)

---

## Appendix B — Atlas idea-card lineage

For traceability into the KFM Idea Index spine, this brief draws on the following atlas cards.

<details>
<summary>Click to expand — idea-card lineage</summary>

| Stable ID | Title | Status (atlas) | Relevance to this brief |
|---|---|---|---|
| `KFM-P2-IDEA-0019` | KANU, KSC, iDigBio, USDA PLANTS as Kansas-specific biodiversity authorities | CONFIRMED, Pass 32 | **Central card for KANU.** Names "the University of Kansas Herbarium (KANU)" explicitly as one of four Kansas-specific biodiversity authorities supplementing GBIF; "KANU and KSC are the primary in-state herbaria"; per-source watchers with own license/cadence; USDA PLANTS as authoritative plant nomenclature; nomenclature-divergence tension noted. |
| `KFM-P2-PROG-0002` | Kansas flora watcher (`kansas_flora_watch`) blueprint | active, Pass 32 | **Operationally definitive card for KANU.** "A flora-specific watcher pulling DwC-A archives from the KU R.L. McGregor Herbarium (KANU) IPT and the Kansas State University Herbarium (KSC) IPT, with GBIF and iDigBio as coverage and validation sources and USDA PLANTS as the taxonomy + state-presence baseline; specimen-backed observations are preferred over crowd observations; restricted taxa (NatureServe, listed species) are quarantined or redacted before any aggregate is published." Pipeline detail: ETag/Last-Modified detection; required DwC-A fields; cross-source dedupe key `institutionCode + catalogNumber + eventDate`; lifecycle placement; promotion gates A–G. |
| DOM-FLORA §D source families | "Kansas Biological Survey / KU herbarium surfaces" | CONFIRMED listing | Groups KBS and KU herbarium as a single source-family row; basis for the kbs.md v0.2 umbrella framing. |
| `C7-10` | Kansas-First Domain Authorities | CONFIRMED (Pass-10) | Names "KBS Natural Heritage Inventory" and "KU Biodiversity Institute" as Kansas-first authorities. Parallel-anchor rule. KANU sits in the Kansas-first cluster via the KBS umbrella per DOM-FLORA grouping. |
| `C10-06` | Biodiversity Stack | CONFIRMED (Pass-10) | "The Kansas biodiversity stack consists of… the KU Biodiversity Institute Natural History Museum collections (approximately 454,000 specimens cited in the corpus), and the Sternberg Museum at FHSU." KU NHM is in the stack at 454k specimens; KANU is the herbarium surface (different from KU NHM museum specimens) named in `KFM-P2-IDEA-0019` for flora context. |
| `KFM-P24-IDEA-0002` | Sensitive species deny-by-default posture | active, Pass 32 | Anchors the operational deny-by-default for rare-plant records in KANU DwC-A archives. |
| `KFM-P24-PROG-0013` | Sensitive taxa redaction policy | active, Pass 32 | OPA ABSTAIN/DENY unless redaction satisfied — applies to KANU rare-plant locality data. |
| `KFM-P13-PROG-0018` | Sensitive species grid generalization policy | active, Pass 32, EXPANDED | "Deterministic grid snapping, representative point plus uncertainty, or withholding tiers while preserving precise private coordinates and rule-version provenance" — operational doctrine for KANU rare-plant geometry. |
| `KFM-P19-IDEA-0005` | KDWP listing canonical regulatory context | active, Pass 32 | **Referenced for contrast.** KDWP is `regulatory` for Kansas-listed plants; KANU is `observed` — different roles, complementary citations. |
| `C6-01` | Sensitivity rubric 0–5 | CONFIRMED (Pass-10) | Rank guidelines column in §6 sensitivity-class table. |
| `C6-02` | Named redaction profiles | CONFIRMED (Pass-10) | `profile:sinc-obscure-10km` for rank-3 default; `profile:point_10km_hex_seeded_v1` for grid generalization. |
| `C6-04` | Grid generalization (H3 r7+ public floor) | CONFIRMED (Pass-10) | Sensitive-geometry floor. |
| `C5-02` | Default-deny promotion | CONFIRMED (Pass-10) | Anchors deny-by-default rights posture; "unknown rights fail closed." |
| `C5-04` | Spec-hash-match gate | CONFIRMED (Pass-10) | Promotion gate. |
| `C5-08` | Lineage required | CONFIRMED (Pass-10) | OpenLineage trail back to receipts per Atlas §24.2.1. |
| `C7-01` | Wikidata as universal crosswalk substrate | CONFIRMED (Pass-10) | Routing anchor for KANU specimens; not truth source. |
| `C7-02` | LCNAF | CONFIRMED (Pass-10) | Name authority for collectors / determiners. |
| `C7-03` | VIAF | CONFIRMED (Pass-10) | Person authority federation. |
| `C7-07` | ITIS TSN | CONFIRMED (Pass-10) | Primary taxonomic anchor for federation. |
| `C7-08` | GBIF Backbone DOI `10.15468/39omei` | CONFIRMED (Pass-10) | Taxonomy federation anchor. |
| `C7-09` | USGS GNIS | CONFIRMED (Pass-10) | Place anchor for KANU localities. |
| `C15-02` / `C15-03` | `kfm:care` extension + OPA default-deny on CARE-tagged | CONFIRMED (Pass-10) | Sovereignty review for culturally sensitive plant records. |
| `C4-01` | STAC `kfm:provenance` namespace | CONFIRMED (Pass-10) | Provenance block shape inherited by KANU catalog rows. |
| `C4-02` | STAC Collection (`kfm-<org>-<product>`) | CONFIRMED (Pass-10) | Collection-id convention: `kfm-kanu-specimens` PROPOSED. |
| `C4-05` | DCAT distribution | CONFIRMED (Pass-10) | Applicable to KANU DwC-A distributions. |
| Atlas §24.1.2 | Anti-collapse failure modes | CONFIRMED (Pass-23/32) | "Modeled product labeled as observed" → DENY; "Aggregate cited as a per-place truth" → DENY at trust membrane. |
| Atlas §24.1.3 | Source-role enum (Master Source-Role Anti-Collapse Register) | CONFIRMED (Pass-23/32) | `observed | regulatory | modeled | aggregate | administrative | candidate | synthetic`; KANU primary role `observed`. |
| Atlas §24.2.1 | Master receipt catalog | CONFIRMED (Pass-23/32) | `SourceDescriptor`, `RawCaptureReceipt`, `TransformReceipt`, `ValidationReport`, `RedactionReceipt`, `AggregationReceipt`. |
| Atlas §24.8 | Time discipline | CONFIRMED (Pass-23/32) | source / observed / valid / retrieval / release / correction times preserved separately. |

</details>

[Back to top](#ku-r-l-mcgregor-herbarium-kanu--source-catalog-entry)

---

## Appendix C — Change log

| Date | Author | Change | Reviewed by |
|---|---|---|---|
| 2026-05-21 | `<docs-steward — TODO>` | Initial v0.1 PROPOSED scaffold: title, overview placeholder, source-authority pointer, catalog-profiles table with `Yes / No (NEEDS VERIFICATION)` cells, collection identity, Pass-10 C4-01 provenance fields, temporal/geometry/rights placeholders, validation pointers, related-contracts/connectors/pipelines pointers, examples pointer, open-questions list (3 generic items), last-reviewed footer. Path: `docs/sources/catalog/kansas/ku-herbarium.md` (already in v0.2 catalog convention). Connector path `connectors/ku_herbarium/` — INCORRECT placement (top-level, snake_case, outside §7.3 family lane). | `<TODO — initial scaffold only>` |
| 2026-05-21 | `<docs-steward — TODO>` | **v0.2 revision (same-day promotion).** Promotes v0.1 PROPOSED scaffold to full per-surface product-page brief consistent with sibling v0.2 product pages in this conversation series. **Structural reframings:** (a) **Umbrella-vs-surface model** — frames this page as per-surface product page parented under [`./kbs.md`](./kbs.md) v0.2 KBS-umbrella brief, per DOM-FLORA §D grouping "Kansas Biological Survey / KU herbarium surfaces" and the kbs.md v0.2 two-surfaces-two-source-roles framing (NHI = authority; KANU = observed). Mirrors the KSHS umbrella pattern. Surfaced as IMPORTANT callout in §1 and OPEN-KUHERB-02. (b) **Connector path correction OPEN-KUHERB-01** — v0.1's `connectors/ku_herbarium/` (top-level, snake_case, outside §7.3) corrected to `connectors/kansas/ku-herbarium/` (nested under canonical §7.3 family + kebab-case). Same pattern as Mesonet OPEN-MESO-01, KBS OPEN-KBS-01, KCC OPEN-KCC-01, KDOT OPEN-KDOT-01. Surfaced as IMPORTANT callout in §1. **Substantive doctrinal additions:** (c) explicit citation to **`KFM-P2-IDEA-0019`** (CONFIRMED Pass 32 — KANU named as one of four Kansas-specific biodiversity authorities; USDA PLANTS as plant-name authority; nomenclature-divergence tension) — central card for this brief; v0.1 did not cite this. (d) explicit citation to **`KFM-P2-PROG-0002`** (active Pass 32 — Kansas flora watcher with KANU IPT operational detail) — operationally definitive card; v0.1 did not cite this. The card provides: DwC-A archive shape, ETag/Last-Modified detection, required field list (scientificName, decimalLatitude/Longitude, eventDate, license, rightsHolder, datasetID), cross-source dedupe key (institutionCode + catalogNumber + eventDate), lifecycle placement, promotion gates A–G, specimen-backed-primacy rule, restricted-taxa quarantine rule. (e) Explicit citations to `C7-10`, `C10-06`, `C7-01`, `C7-02`, `C7-03`, `C7-07`, `C7-08`, `C7-09`, `KFM-P24-IDEA-0002`, `KFM-P24-PROG-0013`, `KFM-P13-PROG-0018`, `KFM-P19-IDEA-0005` (for contrast), `C5-02`, `C6-01`, `C6-02`, `C6-04`, `C15-02`, `C15-03`, `C4-01`, `C4-02`, `C4-05`, Atlas §24.1.2 + §24.1.3 + §24.2.1 + §24.8. (f) Upgraded `connectors/kansas/` family lane to **CONFIRMED at commit `b6a27916...`** per Directory Rules v1.2 §7.3. (g) Added §1 IMPORTANT callout: connector path correction OPEN-KUHERB-01. (h) Added §5 IMPORTANT callout: KANU is `observed`, not `authority` (contrasted with KBS NHI's `authority` role). (i) Added §5 NOTE callout: `regulatory` is NOT a KANU role (cross-referenced to KDWP per `KFM-P19-IDEA-0005`). (j) Added §5 CAUTION callout: specimen-backed primacy per `KFM-P2-PROG-0002`. (k) Added §6 IMPORTANT callout: restricted-taxa quarantine-before-aggregate rule per `KFM-P2-PROG-0002`. (l) Added §6 WARNING callout: license + rightsHolder + datasetID end-to-end preservation per `KFM-P2-PROG-0002`. (m) Added §6 TIP callout: T0–T4 vs `C6-01` 0–5 reconciliation. (n) Built full §7 Mermaid lifecycle diagram showing KANU IPT → DwC-A validator → RAW → restricted-taxa quarantine → WORK → CATALOG → PUBLISHED with USDA PLANTS as plant-name authority and GBIF/iDigBio as coverage partners. (o) Built §8 cadence table with CONFIRMED operational rules per `KFM-P2-PROG-0002`. (p) Built §9 rights table with end-to-end DwC-A license/rightsHolder/datasetID preservation. (q) Built §10 authority anchoring table with USDA PLANTS as primary plant-name authority + ITIS/GBIF/GNIS/LCNAF/VIAF/Wikidata crosswalks. (r) Built §11 pre-admission checklist with 13 items including DwC-A validator + restricted-taxa quarantine rule + promotion gates A–G. (s) Built §12 open verification table with twelve items (OPEN-KUHERB-01 through OPEN-KUHERB-12). (t) Built §13 FAQ with seven Q&A entries including umbrella relationship, `observed` vs `authority`, USDA PLANTS outranking, restricted-taxa handling, cross-source dedupe, missing license/rightsHolder handling, connector-path-correction rationale. (u) Built §14 related-docs with eleven sibling product pages under `kansas/` + corpus-card reference group. (v) Built Appendix A descriptor sketch with KANU-specific fields: `source_family: kansas`, `umbrella_family_ref: kbs`, `flora_authority: KFM-P2-IDEA-0019`, `operational_watcher: KFM-P2-PROG-0002`, `validation.required_fields` per `KFM-P2-PROG-0002`, `dedupe.cross_source_key`, `lifecycle_placement` per `KFM-P2-PROG-0002`, `promotion_gates` A–G. (w) Built Appendix B atlas idea-card lineage with 25 cards. (x) Built Appendix C change log (this entry). (y) Updated meta block to v0.2 with full related-docs list (28 entries) and 5-paragraph notes block. (z) Updated badges: added doc-version, family, surface-of, C7-10, DOM-FLORA, source-role, restricted-taxa, USDA-PLANTS, DwC-A, last-updated. | `<flora-domain-steward — TODO>` |

[Back to top](#ku-r-l-mcgregor-herbarium-kanu--source-catalog-entry)

---

<sub>**Last updated:** 2026-05-21 · **Status:** `draft` (v0.2) · **Brief class:** per-surface product page parented under [`./kbs.md`](./kbs.md) v0.2 (KBS umbrella) · **Owners:** _TODO — docs steward + source steward + flora domain steward_</sub>

<sub>**Family lane:** `connectors/kansas/` — CONFIRMED §7.3 at commit `b6a27916bbb9e07cbf3752870c867476e1e094e7`. **Per-institution adapter:** `connectors/kansas/ku-herbarium/` — PROPOSED per OPEN-KUHERB-01 (v0.1's `connectors/ku_herbarium/` corrected to v0.2's nested kebab-case path).</sub>

<sub>**Authority of this brief:** per-surface product page; cites authority, does not own it. The `SourceDescriptor` for KU McGregor Herbarium (KANU) is the source of truth for rights, sensitivity, cadence, citation. The flora watcher pipeline shape lives in `KFM-P2-PROG-0002` (active, Pass 32).</sub>

<sub>**Plant-name authority:** USDA PLANTS per `KFM-P2-IDEA-0019` (CONFIRMED). KANU determinations are preserved as issuing-institution position; USDA PLANTS fills the KFM plant-name slot. Disagreements are recorded, not silently resolved (OPEN-KUHERB-05).</sub>

<sub>**Restricted-taxa rule:** NatureServe-ranked / KDWP-listed taxa records are quarantined or redacted BEFORE any aggregate is published per `KFM-P2-PROG-0002`. Per-record license/rightsHolder/datasetID end-to-end preservation enforced at validation per the same card.</sub>

<sub>**Related doctrine:** [`../../../doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) · [`../../../doctrine/lifecycle-law.md`](../../../doctrine/lifecycle-law.md) · [`../../../doctrine/truth-posture.md`](../../../doctrine/truth-posture.md) · [`../../../registers/AUTHORITY_LADDER.md`](../../../registers/AUTHORITY_LADDER.md)</sub>

<sub>[↑ Back to top](#ku-r-l-mcgregor-herbarium-kanu--source-catalog-entry)</sub>
