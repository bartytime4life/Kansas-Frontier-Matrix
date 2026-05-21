<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-familysearch-historical-record-images
title: FamilySearch Historical Record Images
type: product-page
version: v0.2
status: draft
owners: <PLACEHOLDER — Docs steward + People-Genealogy-DNA-Land domain owner + Source steward for familysearch; assign before review>
created: 2026-05-20
updated: 2026-05-21
policy_label: public
related:
  - docs/sources/catalog/familysearch/README.md
  - docs/sources/catalog/familysearch/family-tree.md
  - docs/sources/catalog/familysearch.md
  - docs/sources/catalog/README.md
  - docs/domains/people-genealogy-dna-land/README.md
  - docs/doctrine/directory-rules.md
  - data/registry/sources/people-genealogy-dna-land/
  - policy/genealogy/publication.rego
  - schemas/contracts/v1/source/source-descriptor.schema.json
tags: [kfm, docs, sources, catalog, familysearch, historical-records, genealogy, dom-people, observation, iiif, c9-02]
notes:
  - "PROPOSED product-page scaffold. Path `docs/sources/catalog/familysearch/historical-record-images.md` is PROPOSED; the `catalog/<family>/<product>.md` nested pattern conflicts with the parent FamilySearch source catalog standard doc at `docs/sources/catalog/familysearch.md` (flat). Inconsistency flagged for ADR (OPEN-PATH-01)."
  - "Doctrinal subtlety: this product is the **corroborating-observation** sibling to Family Tree. Where Family Tree records are `source_role: candidate` and cannot publish until merged + corroborated, Historical Record Images are `source_role: observation` (scoped) — they ARE the corroborating evidence. The candidate→publish gate at Family Tree depends on this product."
  - "Doctrinal subtlety 2 — image vs. index: the raw scanned image is observation evidence; the community-contributed transcription / index may itself be `source_role: candidate` (per the FamilySearch indexing program). Their source roles are tracked separately; the image's observation status does not auto-confer observation status on its index. See [Image vs. index](#image-vs-index)."
  - "Sibling-link placements (`./README.md`, `./family-tree.md`, `../IDENTITY.md`, `../RIGHTS-AND-SENSITIVITY-MAP.md`, `../_examples/`) are PROPOSED only."
[/KFM_META_BLOCK_V2] -->

# 📜 FamilySearch Historical Record Images

> Indexed historical record images (census, vital, church, military, immigration, court) admitted as **scoped observation evidence** — the source-document anchor that backs every claim about a person and event in time and place.

[![Status: PROPOSED](https://img.shields.io/badge/status-PROPOSED--scaffold-orange)](#)
[![Truth: receipt ≠ proof ≠ catalog ≠ publication](https://img.shields.io/badge/truth-receipt%20%E2%89%A0%20proof%20%E2%89%A0%20catalog%20%E2%89%A0%20publication-blue)](../../../doctrine/directory-rules.md)
[![source_role: observation (scoped)](https://img.shields.io/badge/source__role-observation%20(scoped)-success)](#source-role-observation-scoped)
[![Role in stack: corroborating evidence](https://img.shields.io/badge/role-corroborating%20evidence%20for%20Family%20Tree-blueviolet)](./family-tree.md)
[![Domain: DOM-PEOPLE](https://img.shields.io/badge/domain-DOM--PEOPLE-informational)](../../../domains/people-genealogy-dna-land/)
[![Delivery: IIIF + image assets](https://img.shields.io/badge/delivery-IIIF%20%2B%20image%20assets-orange)](#iiif-and-image-asset-handling)
[![Living-person guards: apply](https://img.shields.io/badge/living--person%20guards-apply-critical)](#rights-and-sensitivity)
[![Last reviewed: 2026-05-21](https://img.shields.io/badge/last--reviewed-2026--05--21-success)](#last-reviewed)

**Status:** PROPOSED — scaffold only ·
**Family:** [`familysearch`](./README.md) ·
**Kind:** Source-document evidence (image + indexed transcription) ·
**Domain:** People / Genealogy / DNA / Land (`DOM-PEOPLE`) ·
**Owners:** `<PLACEHOLDER — Docs steward + People-Genealogy-DNA-Land domain owner + Source steward for familysearch>` ·
**Last reviewed:** 2026-05-21

> [!IMPORTANT]
> **Historical Record Images are the observation side of the FamilySearch upstream.** A Family Tree merged person record cannot clear the publication gate without a corroborating `observation`-role binding — and this product is where most of those bindings come from. The doctrinal asymmetry is deliberate: the corpus admits FamilySearch trees only as candidates, but it admits FamilySearch historical record images as scoped observations because they are source-document evidence (with a date, a place, and a captured artifact). This product is doctrinally heavier than Family Tree precisely because it carries that observation weight.

---

## 📑 On this page

- [Overview](#overview)
- [Role in the genealogy stack](#role-in-the-genealogy-stack)
- [Doctrinal anchors](#doctrinal-anchors)
- [Source-role: observation (scoped)](#source-role-observation-scoped)
- [Image vs. index](#image-vs-index)
- [Source authority](#source-authority)
- [Record types and rights variability](#record-types-and-rights-variability)
- [IIIF and image asset handling](#iiif-and-image-asset-handling)
- [Catalog profiles used](#catalog-profiles-used)
- [Collection identity](#collection-identity)
- [Provenance fields (`kfm:provenance`)](#provenance-fields-kfmprovenance)
- [CIDOC-CRM projection](#cidoc-crm-projection)
- [Temporal handling](#temporal-handling)
- [Geometry and projection](#geometry-and-projection)
- [Consent and revocation](#consent-and-revocation)
- [Rights and sensitivity](#rights-and-sensitivity)
- [Validation and catalog closure](#validation-and-catalog-closure)
- [Related contracts and schemas](#related-contracts-and-schemas)
- [Related connectors and pipelines](#related-connectors-and-pipelines)
- [UI affordances](#ui-affordances)
- [Examples](#examples)
- [Open questions](#open-questions)
- [Related docs](#related-docs)

---

## Overview

**CONFIRMED (doctrine, C9-02).** FamilySearch is KFM's primary upstream for live genealogical data, accessed via OAuth2 with consent scopes. Within FamilySearch, **historical record images** include indexed scans of census records, vital records (birth, marriage, death), church records (baptism, marriage, burial), military records, immigration records, and court / probate records — institutional source documents that record specific events at specific dates and places.

**PROPOSED (product page scope).** This page describes how historical record images and their associated indices are admitted (as `observation`-role evidence), how they project into the CIDOC-CRM graph as E31 Documents anchoring E5 Events, how IIIF delivery and image rights are preserved, and how living-person guards still apply even on observation-role records when subjects may be living.

**NEEDS VERIFICATION:** Current FamilySearch historical-record API endpoint URLs and IIIF manifest patterns; per-record-collection license metadata semantics; institutional partnership terms (FamilySearch holds varying agreements with archives); the exact distinction in the API between image-level metadata and index-level metadata.

> [!NOTE]
> This page is the **product-specific briefing** for historical record images and indices. The broader FamilySearch upstream — OAuth2 / GA4GH framing, full receipt envelope, vendor-risk posture — lives in the parent source catalog entry at [`docs/sources/catalog/familysearch.md`](../familysearch.md). **Do not duplicate** that material here; reference it.

---

## Role in the genealogy stack

This product sits across from [Family Tree](./family-tree.md) and the two together form the **hypothesis-and-evidence** spine of the genealogy domain:

| Product | `source_role` | Role in stack | PUBLISHED edge? |
|---|---|---|---|
| [Family Tree](./family-tree.md) | `candidate` | Community-contributed hypothesis | **No** — until `merged` + corroborated by an observation |
| **Historical Record Images** (this page) | `observation` (scoped) | Source-document evidence with date + place | **Yes**, subject to living-person, rights, and consent gates |

> [!IMPORTANT]
> The corpus's evidence-first doctrine routes every publishable claim about a person through an **observation**. Historical Record Images are the most common — and often the only available — observation source for genealogy claims. Without this product, a FamilySearch-derived Family Tree record cannot pass the merge gate to publication. **This is by design**, not a workflow inconvenience.

---

## Doctrinal anchors

| Anchor | Source | Why it applies here |
|---|---|---|
| **C9-02** | FamilySearch API as genealogy upstream | Parent CONFIRMED doctrine (Pass-10); records subset admitted as observation (scoped) |
| **C9-01** | GEDCOM 5.5 / GEDCOM-X | Date qualifier normalization carries to record images too (CONFIRMED) |
| **C8-01** | CIDOC-CRM core classes (E5/E7/E21/E53/E55/E74) | E5 Event anchored by source-document Persons + Places (CONFIRMED) |
| **C8-03** | PROV-O + PAV | Claim-level provenance including OCR/index provenance (CONFIRMED) |
| **C8-04** | Evidence-Bundle JSON-LD | Content-addressed wrapping (CONFIRMED) |
| **C7-09** | USGS GNIS for U.S. place authority | Place anchoring for record-stated places (CONFIRMED) |
| **C9-04** | GA4GH AAI / Passports / DUO / MRCG | Consent and access-control framework (CONFIRMED) |
| **C6-06** | k-anonymity for living-person overlays | Defaults `k=10`, `cell_m=500`, fallback `radius_mask=250m` — applies if a recent record covers a possibly-living subject (CONFIRMED) |
| **C6-07** | Consent tokens | JWT, OAuth introspection, PDP enforcement (CONFIRMED) |
| **C6-08** | Revocation endpoints, embargo, cache invalidation | Render-time enforcement (CONFIRMED) |
| **C5-09** | Tombstones for revocation | Revocation discipline (CONFIRMED) |
| **C10-07** | Kansas archive integration (KSHS, KHRI, KU Spencer, Kansas Memory, LOC IIIF, SNAC/EAC-CPF) | Adjacent archive sources; integration patterns (CONFIRMED) |
| **KFM-P15-PROG-0033** | OCR / image / IIIF source families with rights propagation | Doctrinal anchor for image+OCR+IIIF source families (PROPOSED Pass-23/32) |
| **KFM-P9-PROG-0074** | IIIF rights and georeferencing annotation provenance | Plugin governance + IIIF rights preservation before MapLibre display (PROPOSED) |
| **KFM-P1-IDEA-0033** | Living-person / DNA / genomic restriction posture | Pass-23 carry-forward of C9 sensitivity stance (PROPOSED) |
| **Pass-23 source-role table** | Admin compilation ≠ observation; aggregate ≠ per-place | `observation` is the role that supports per-place truth — this product's grounds for publication (CONFIRMED rules) |
| **DOM-PEOPLE** | Domains Atlas People/Genealogy/DNA/Land | Object families: Person Assertion, NameAssertion |
| **Directory Rules §§3, 4, 7.3, 7.4** | Placement law | Connectors don't publish; schemas under `schemas/contracts/v1/...` |
| **ADR-0001** | Schema home rule | Establishes `schemas/contracts/v1/source/source-descriptor.schema.json` as canonical home |

---

## Source-role: observation (scoped)

**CONFIRMED rule (KFM-P1-PROG-0007 + Pass-23 source-role table).** Historical record images are admitted under `source_role: observation` with explicit scoping — the scope is **what the document actually records**, not what later analysis infers.

| Concern | Posture |
|---|---|
| What the observation **is** | The source document at the time of its creation — names, dates, places, relationships as recorded by the original document |
| What the observation **is not** | An assertion of genealogical truth across time; a substitute for vital-records authority; a deeds/title authority; an authority for living-person identity |
| Scope rule | Each observation MUST carry a `scope_note` describing what the source document covers and what it does not |
| Combination rule | Two observations of the same person event from different documents corroborate each other; one observation is sufficient to clear the merge gate at Family Tree, two strengthens it |

> [!CAUTION]
> **Source-document evidence is not the same as historical truth.** A 1900 census enumerator's spelling of a name is observation evidence of how that name was recorded by that enumerator at that moment — **not** an authoritative spelling. Treat the record as the artifact, not as ground truth, and preserve verbatim strings (C9-06).

---

## Image vs. index

> [!IMPORTANT]
> **The image and the index are doctrinally distinct.** FamilySearch indexing is partly institutional and partly community-contributed; conflating their source roles is a documented failure mode.

| Artifact | Default `source_role` | Why |
|---|---|---|
| **Raw scanned image** (TIFF / JPEG / IIIF tile pyramid) | `observation` (scoped) | Direct capture of a source document |
| **Institutional index** (FamilySearch-curated transcription) | `observation` (scoped, derived) | Institutional transcription; carries QA |
| **Community-contributed index** (volunteer transcription) | `candidate` | Community-authored; subject to the candidate→merge gate |
| **OCR-extracted text** (machine transcription) | `modeled` | Output of an OCR model; requires `role_model_run_ref` + uncertainty fields |
| **Subsequent corrections** (corrections to any of the above) | per-correction descriptor | Tracked via `CorrectionNotice` + supersession |

**Rule:** the observation status of the image does **not** automatically confer observation status on its index. Each surface carries its own role tag, and PROV-O lineage records the relationship between them.

---

## Source authority

The authoritative SourceDescriptor lives in [`data/registry/sources/people-genealogy-dna-land/`](../../../../data/registry/sources/people-genealogy-dna-land/) per **ADR-0001** and Directory Rules §7.4. **Do not duplicate** descriptor fields here.

| Field on the descriptor | Where defined | Why it is **not** restated here |
|---|---|---|
| Identity, role, rights, cadence | SourceDescriptor | Single source of truth |
| `source_role: observation` | `source_role` enum on descriptor | Set at admission per artifact subset |
| `scope_note` | descriptor field | What the document records and does not |
| Per-record-type rights | descriptor + `RightsDecision` | Varies enormously (see [Record types and rights variability](#record-types-and-rights-variability)) |
| Source archive partner | descriptor field | The institution holding the original (FamilySearch is the access provider; the source-of-source matters) |
| Index provenance | `role_model_run_ref` (for OCR) or descriptor field | Tracks who indexed and when |

> [!WARNING]
> **Source-of-source matters for this product.** FamilySearch is the access layer; the underlying source archive (a state vital records office, a county clerk, a church denomination, the National Archives) is the **authority for the record itself**. Both must appear in the EvidenceBundle and in citation text on any public surface.

---

## Record types and rights variability

> [!CAUTION]
> Historical record images are **not a uniform rights category**. Different record types operate under different legal regimes; the policy bundle, not this page, decides what crosses the publication boundary. The table below is **NEEDS VERIFICATION**: per-jurisdiction details must be confirmed against current SourceDescriptors and policy bundles.

| Record type | Typical rights posture (NEEDS VERIFICATION) | Doctrinal note |
|---|---|---|
| **U.S. census** | Federally administered; **release after a defined statutory restriction period** (the corpus does not codify the exact period; verify the current applicable rule from the source archive). Historical census records past the restriction window are typically public-domain. | Recent census records may still cover living people and trigger living-person guards. |
| **Vital records** (birth / marriage / death) | State-administered; restrictions vary by state and by event type (most-recent N years restricted). | The state-of-record is the authority; FamilySearch is the access layer. |
| **Church records** (baptism, marriage, burial) | Institutional / denominational; may carry use-permission terms separate from the digital host. | Some denominations require attribution; some restrict redistribution. |
| **Military records** | Federally administered; service-record restrictions vary by branch, era, and personal-identifier sensitivity. | Recent records typically restricted; older records often public. |
| **Immigration records** (passenger lists, naturalization) | Federally administered; older records typically public; living-individual records restricted. | Sensitive identity-document fields require redaction. |
| **Court / probate / land records** | County-administered; rights vary by jurisdiction; many older records are public. | Adjacent to DOM-PEOPLE land-records subdomain (LandInstrument). |

> [!IMPORTANT]
> KFM **MUST NOT** invent jurisdiction-specific rights claims in this docs page. The policy bundle and the SourceDescriptor (with current rights review) are the only authoritative places for "this record type is currently publishable on these terms." This table is a **navigation aid**, not a rights determination.

---

## IIIF and image asset handling

**CONFIRMED doctrine (KFM-P15-PROG-0033 + KFM-P9-PROG-0074, PROPOSED).** Historical record images are typically delivered via **IIIF Image API** and **IIIF Presentation API** manifests. KFM treats the IIIF manifest as part of the EvidenceBundle, not as ephemeral delivery infrastructure.

| Concern | PROPOSED handling | Status |
|---|---|---|
| **Image storage** | Cloud-Optimized GeoTIFFs (COGs) where georeferenced; original raster preserved under `data/raw/...` | NEEDS VERIFICATION |
| **IIIF manifest** | Captured and stored alongside the image asset; referenced from EvidenceBundle | KFM-P9-PROG-0074 anchor (PROPOSED) |
| **IIIF rights** | The IIIF `rights` field is preserved verbatim and routes into `RightsDecision` review | KFM-P9-PROG-0074 (PROPOSED) |
| **IIIF tile pyramid** | Public delivery only after rights gate; tile-pyramid mirror only when partnership terms allow | NEEDS VERIFICATION |
| **OCR / index extraction** | OCR-extracted text is `source_role: modeled` (see [Image vs. index](#image-vs-index)); preserves model identity, parameters, version pin | Per the C9-01 + KFM-P15-PROG-0033 framing |
| **Allmaps / georeferencing annotations** | Where present, preserved as separate evidence with annotation provenance | KFM-P9-PROG-0074 (PROPOSED) |
| **Per-asset integrity** | `file:checksum` sha256 on every image and manifest | C3-02 (CONFIRMED) |

> [!NOTE]
> Per **KFM-P9-PROG-0074** (PROPOSED): *"KFM historic-map overlays should preserve IIIF rights, georeferencing annotation provenance, and plugin governance before MapLibre display."* The same discipline applies to historical record images: rights and provenance survive the delivery transformation; they do not get dropped when an image becomes a tile.

---

## Catalog profiles used

**PROPOSED — Pass-10 / C4 + C8 profiles.** Historical record images are a more natural fit for STAC than Family Tree records, because each image is an asset with a date + place and a captured artifact. The catalog footprint is therefore broader.

| Profile | Lane (path) | Used by this product? | Notes |
|---|---|---|---|
| **STAC** with `kfm:provenance` | `data/catalog/stac/` | **PROPOSED — Yes (primary)** | Each image/event Item carries date + place + asset; C4-01 / C4-02 |
| **CIDOC-CRM projection** (E31 Document + E5 Event + E21 Person + E53 Place + E13 Attribute Assignment) | `data/catalog/domain/people-genealogy-dna-land/` | **PROPOSED — Yes** | C8-01; the graph-shaped projection of the same content |
| **PROV-O + PAV** lineage | `data/catalog/prov/` | PROPOSED — Yes | C8-03; includes OCR / index provenance |
| **Evidence-Bundle JSON-LD** (content-addressed) | `data/catalog/evidence/` (PROPOSED) | PROPOSED — Yes | C8-04 |
| **DCAT** distribution | `data/catalog/dcat/` | PROPOSED — Yes (collection-level metadata) | C4-05 |
| **Schema.org** web surface | (web layer) | PROPOSED — Yes (Document / Event / Place / Person) | C8-02; `sameAs` to authority IRIs where confidence permits |
| **IIIF Presentation manifest** | preserved alongside image asset under `data/raw/...` + referenced from STAC + EvidenceBundle | PROPOSED — Yes (CONFIRMED delivery pattern per KFM-P9-PROG-0074) |
| **STAC × DwC hybrid** | — | **No** | Biodiversity-only (C4-03); not applicable |

---

## Collection identity

- **PROPOSED Collection id patterns (per record-type Collection):**
  - `kfm-familysearch-records-census-<jurisdiction>-<year>` (per census year × jurisdiction)
  - `kfm-familysearch-records-vital-<jurisdiction>-<type>` (per state × event type)
  - `kfm-familysearch-records-church-<denomination>-<location>` (per denomination × location)
  - …and so on, following the principle that **a Collection is the smallest stable rights+cadence boundary**.
- **PROPOSED namespace:** `kfm:` *(see OPEN-DSC-03; namespace choice between `kfm:` and `ks-kfm:` remains open — Pass-10 C4-01).*
- **Asset roles:** NEEDS VERIFICATION — confirm against `schemas/contracts/v1/source/` and `contracts/domains/people-genealogy-dna-land/`.

> [!TIP]
> A single "all FamilySearch records" Collection would aggregate records with vastly different rights regimes and would be impossible to gate at promotion. **Collection-per-rights-boundary** is the doctrinal default. The exact boundaries are NEEDS VERIFICATION until source-archive partnership terms are recorded in their SourceDescriptors.

---

## Provenance fields (`kfm:provenance`)

Every STAC Item carries the Pass-10 C4-01 `kfm:provenance` block. Specific values for historical record images are **PROPOSED** until mounted-repo verification.

| Field | Resolves to | Required? | Notes for this product |
|---|---|---|---|
| `spec_hash` | sha256 of the canonical record | MUST | Includes image checksum + index payload |
| `evidence_bundle_ref` | `kfm://evidence/<digest>` → EvidenceBundle | MUST | Bundle lists FamilySearch access path + underlying source archive + IIIF manifest |
| `run_record_ref` | `kfm://run/<run-id>` → RunReceipt | MUST | OAuth scope, GA4GH Passport claim, access-token fingerprint |
| `audit_ref` | `kfm://audit/<attestation-id>` | MUST | SLSA / OPA attestation (C5-08) |
| `policy_digest` | sha256 of the policy bundle at promotion | MUST | Includes per-record-type rights rules + living-person guards |
| (per-asset) `file:checksum` | sha256 of asset bytes | MUST | C3-02 — applies to every image, manifest, and index payload |

<details>
<summary><b>Reference: extra historical-record-specific provenance fields (illustrative — not authoritative)</b></summary>

```text
# Inside kfm:provenance or the bound EvidenceBundle:
source_role                    "observation"
scope_note                     "1900 U.S. Federal Census, Riley County, Kansas, ED 12, Sheet 4A"
source_archive                 "U.S. National Archives and Records Administration (NARA)"
access_provider                "FamilySearch International"
record_type                    "census" | "vital_birth" | "vital_marriage" | "vital_death" |
                               "church_baptism" | "church_marriage" | "church_burial" |
                               "military" | "immigration" | "court_probate" | ...
record_date                    ISO 8601 date or interval
record_place_anchor            kfm://place/<gnis-or-tgn-id>
iiif_manifest_uri              <https URI of IIIF Presentation manifest>
iiif_rights                    <verbatim IIIF rights string>
image_asset_href               <image URI>
image_checksum                 sha256:<...>
index_provenance               { source_role, contributor_attribution_ref, ocr_model_ref? }
ocr_model_run_ref              kfm://run/<id>  (when role_model_run_ref applies)
living_person_redaction_ref    kfm://receipt/redaction/<id>  (when applicable)
oauth_scope                    <scope-string>
passport_claim                 <GA4GH Passport claim ref>
access_token_fingerprint       sha256:<...>  (NEVER the token itself)
```

PROPOSED only. Authoritative shape lives in `schemas/contracts/v1/` (path NEEDS VERIFICATION).

</details>

---

## CIDOC-CRM projection

**CONFIRMED doctrine (C8-01).** Historical record images project to the CIDOC-CRM graph through E31 Document (the artifact) + E5 Event (the recorded event) + E21 Person (the subject) + E53 Place (the recorded place), with **E13 Attribute Assignment** carrying every claim-to-evidence binding.

| Element | CIDOC-CRM target | Notes |
|---|---|---|
| The image as artifact | **E31 Document** (or E84 Information Carrier for digital) | Identified by stable image URI; preserves IIIF manifest reference |
| The recorded event (birth, marriage, etc.) | **E5 Event** | Date as ISO 8601 interval per C9-01; place anchored to GNIS/TGN per C7-09 |
| The subject(s) of the event | **E21 Person** | Carries verbatim source-document name in **E82 Actor Appellation** |
| The recorded place | **E53 Place** with anchor → GNIS / TGN | Confidence score on anchoring decision |
| The act of creating the document | **E7 Activity** | Enumerator, recording official, photographer — captured where known |
| Source-document attribution (per claim) | **E13 Attribute Assignment** | The evidence-per-claim hinge; this is what makes the record "observation evidence" |
| Group context (family, household, congregation, unit) | **E74 Group** | Where the record places the subject within a group |

> [!NOTE]
> **Verbatim source-document strings are preserved alongside the projection.** A census record's name as the enumerator wrote it is preserved; the normalized name in the graph is a separate assertion. C9-06 governs verbatim preservation.

---

## Temporal handling

Historical record images bring two layered time dimensions: the time of the **recorded event** and the time of the **document creation** (which may differ — e.g., a marriage license filed days after the wedding).

| Time | Meaning for a historical record image | Required? |
|---|---|---|
| `event_time` / `observed_time` | When the recorded event occurred (per the document) | MUST when applicable — ISO 8601 interval per C9-01 |
| `document_time` | When the document was created or filed | MUST when distinct from `event_time` |
| `source_time` | When FamilySearch's snapshot of the image / index was returned | MUST |
| `valid_time` | Period the claim is asserted to be valid (e.g., a residence span recorded in a census) | MUST when applicable |
| `retrieval_time` | When KFM watcher fetched the record | MUST |
| `release_time` | When KFM published the artifact | MUST at publication |
| `correction_time` | When a record is superseded (e.g., re-indexed; index correction) | MUST when emitted |

> [!CAUTION]
> Census records, vital records, and church records frequently get **re-indexed** as community contributors correct earlier transcriptions. A re-index does not change the image — the image is the observation — but it produces a new index Item with a `supersedes` pointer to the prior index. The image and its evolving index family are tracked as a temporal sequence, not as silent overwrites.

---

## Geometry and projection

**PROPOSED.**

| Concern | PROPOSED handling | Status |
|---|---|---|
| Geometry type | Point on E53 Place anchor after GNIS / TGN resolution; record-place often resolves to a county or town centroid | NEEDS VERIFICATION |
| CRS | EPSG:4326 in catalog; native projection preserved in EvidenceBundle | NEEDS VERIFICATION |
| Place anchoring | GNIS (U.S. preferred — C7-09) or TGN; ambiguous matches route to curator-review queue | CONFIRMED doctrine |
| Generalization | Living-person residences redacted or generalized per C6-06 defaults; long-deceased subjects retain precise place anchor | CONFIRMED rule; thresholds NEEDS VERIFICATION |
| STAC Projection extension | Required on promotion (KFM-P27-FEAT-0003 PROPOSED) | NEEDS VERIFICATION |
| Georeferenced map overlays | Where the record includes a map or plat (e.g., land records), Allmaps annotation provenance is preserved per KFM-P9-PROG-0074 | PROPOSED |

---

## Consent and revocation

**CONFIRMED doctrine (C9-02, C9-04, C5-09, C6-08).** Every fetch operates under an OAuth2 scope plus a GA4GH Passport claim. KFM records the scope, the **access-token fingerprint** (one-way hash; never the token itself), and the Passport claim on every `RawCaptureReceipt`.

| Event | Required action | Owning artifact |
|---|---|---|
| Source archive withdraws a record (e.g., recently-restricted vital record) | Issue signed `Tombstone`; invalidate caches; re-evaluate `EvidenceBundle` resolution | `Tombstone` (signed) |
| FamilySearch terms-of-use change affecting this record class | Re-evaluate gate; potentially HOLD or QUARANTINE pending steward review | `PolicyDecision` |
| Embargo timestamp passes | Re-evaluate gate; deny if `now < embargo_until` regardless of other approvals | `PolicyDecision` |
| Index correction submitted by a contributor | Emit new index Item with `supersedes` pointer; preserve prior index in audit trail | `CorrectionNotice` |
| OCR re-run with a new model version | Emit new OCR Item with `role_model_run_ref` for the new model; supersedes prior OCR | `CorrectionNotice` + ModelRunReceipt |

> [!IMPORTANT]
> **Revocation that does not invalidate caches is incomplete.** This applies to image-derived tiles, OCR-derived text exposed on AI surfaces, and any composite renderings that bundle multiple records. Invalidation hooks MUST be tested before relying on the revocation pathway.

---

## Rights and sensitivity

**NEEDS VERIFICATION.** See [`policy/sensitivity/`](../../../../policy/sensitivity/) and [`RIGHTS-AND-SENSITIVITY-MAP.md`](../RIGHTS-AND-SENSITIVITY-MAP.md). **Do not restate policy here.**

> [!CAUTION]
> Rights for this product fall in **three** distinct lanes, and conflating them is a documented failure mode:
>
> 1. **The underlying source archive** (NARA, a state vital records office, a church denomination) — the original authority over the record.
> 2. **FamilySearch's access agreement** with the source archive — varies per partnership; sometimes more permissive than the source archive's direct posture, sometimes less.
> 3. **KFM's derived rendering** — even when both underlying rights are permissive, KFM-rendered derivations (tiles, OCR extracts, indexed surfaces) carry their own attribution and reuse posture.

| Risk class | Default | Required controls |
|---|---|---|
| **Living persons** in recent records (recent census within the statutory restriction window; recent vital records) | **DENY** public exact / identifying output | privacy review · redaction · aggregate · staged access (C6-06) |
| **Place strings tied to living-person residences** | **DENY** exact public location | geographic generalization receipt |
| **Rights-limited collections** (per source-archive partnership terms) | **DENY** public republication until terms resolved | `RightsDecision` |
| **IIIF tile-pyramid public mirror** | Allowed only when partnership terms permit | KFM-P9-PROG-0074 rights preservation |
| **OCR-extracted text on AI surfaces** | **ABSTAIN** if OCR confidence is below threshold or if record covers living persons | `cite-or-abstain` + AIReceipt |
| **Aggregate cited as a per-place truth** | **DENY** join from aggregate cell to single record | aggregation receipt (Pass-23 source-role table) |

> [!NOTE]
> **CARE applicability** (C15-01) is usually limited for federally-administered records but **can** apply for church records covering Indigenous communities, mission records, boarding-school records, and any record where a community holds authority over disclosure. The curatorial-decision SOP referenced in C15 governs the applicability call.

---

## Validation and catalog closure

| Gate | Source | Status |
|---|---|---|
| **`source_role = observation`** (scoped) at admission | KFM-P1-PROG-0007 | CONFIRMED rule |
| **`scope_note` present** on every observation | Pass-23 source-role table + KFM doctrine | CONFIRMED rule |
| **Image checksum** binds to STAC Item | C3-02 + C5-04 | CONFIRMED doctrine |
| **IIIF rights preservation** through transformation chain | KFM-P9-PROG-0074 | PROPOSED |
| **OCR-as-modeled** discipline (role_model_run_ref present where OCR is used) | KFM-P15-PROG-0033 | PROPOSED |
| **Index-as-candidate** discipline (community-contributed index carries candidate role) | C9-02 + KFM-P1-PROG-0007 | PROPOSED rule |
| **Living-person guard** (k-anonymity or full redaction for any possibly-living subject) | C6-06 + KFM-P1-IDEA-0033 | CONFIRMED |
| **Per-record-type rights review** clean (`RightsDecision: allowed` or `restricted`) | Per-archive partnership terms | NEEDS VERIFICATION per Collection |
| **Catalog closure** before public release | Pass-10 / KFM-P1-IDEA-0020 | CONFIRMED doctrine |
| **STAC Projection lint** | KFM-P27-FEAT-0003 | PROPOSED |
| **STAC checksum closure** against ReleaseManifest digest | KFM-P22-PROG-0037 | PROPOSED |
| **Spec-hash-match** gate | C5-04 | CONFIRMED doctrine |
| **Policy parity** (CI = runtime) | C5-03 | CONFIRMED doctrine |
| **Lineage required** (OpenLineage → receipts; includes OCR + index lineage) | C5-08 | CONFIRMED doctrine |
| **Revocation status** check at render time; tombstone absent | C5-09 + C6-08 | CONFIRMED doctrine |

> [!WARNING]
> **Fail-closed is the default.** If any gate is unresolved, the answer is `DENY` or `ABSTAIN`. A `RuntimeResponseEnvelope` with finite outcome `ABSTAIN` is preferred to a fluent answer that bypasses governance.

---

## Related contracts and schemas

| Concern | PROPOSED home | Status |
|---|---|---|
| SourceDescriptor schema | `schemas/contracts/v1/source/source-descriptor.schema.json` | PROPOSED per ADR-0001; NEEDS VERIFICATION |
| CIDOC-CRM projection schema (E31 Document family) | `schemas/contracts/v1/catalog/cidoc-crm-document.json` (PROPOSED) | NEEDS VERIFICATION |
| IIIF manifest reference schema | `schemas/contracts/v1/iiif/manifest-ref.json` (PROPOSED) | NEEDS VERIFICATION |
| OCR ModelRunReceipt | `schemas/contracts/v1/runtime/model-run-receipt.json` (PROPOSED) | per `ai-build-operating-contract.md` §34 |
| EvidenceBundle / EvidenceRef | `schemas/contracts/v1/evidence/` (KFM-P26-PROG-0004 / 0005) | PROPOSED |
| DecisionEnvelope | `schemas/contracts/v1/runtime/decision_envelope.schema.json` (KFM-P5-PROG-0001) | PROPOSED |
| Domain contracts (DOM-PEOPLE) | `contracts/domains/people-genealogy-dna-land/` | PROPOSED |
| `policy/genealogy/publication.rego` | OPA publication gate for genealogy products | PROPOSED |

> [!NOTE]
> Per Directory Rules §7.4 and ADR-0001, schemas live under `schemas/contracts/v1/...`. **Do not propose a parallel schema home** for record-image-specific shapes. IIIF manifests are preserved as evidence artifacts, not as schema homes.

---

## Related connectors and pipelines

- **Connector:** [`connectors/familysearch/`](../../../../connectors/familysearch/) — OAuth2-gated fetch under per-user scope; image asset + index payload + IIIF manifest captured together.
- **Pipelines:**
  - [`pipelines/ingest/`](../../../../pipelines/ingest/) — RAW capture with full receipt envelope.
  - [`pipelines/normalize/`](../../../../pipelines/normalize/) — IIIF manifest parsing; place anchoring (GNIS/TGN); date normalization; OCR (where applied) under explicit `role_model_run_ref`.
  - [`pipelines/validate/`](../../../../pipelines/validate/) — image checksum, IIIF rights present, scope_note present, living-person guard.
  - [`pipelines/catalog/`](../../../../pipelines/catalog/) — STAC + CIDOC-CRM + DCAT + PROV-O emission.
- **Pipeline spec:** [`pipeline_specs/people-genealogy-dna-land/`](../../../../pipeline_specs/people-genealogy-dna-land/) (PROPOSED).
- **Policy:** [`policy/genealogy/publication.rego`](../../../../policy/genealogy/publication.rego) (PROPOSED).

> [!WARNING]
> Linked paths are PROPOSED placements consistent with the repository structure guide. Mounted-repo evidence has not been inspected in this session; every linked path is NEEDS VERIFICATION.

---

## UI affordances

> [!IMPORTANT]
> A public surface that renders a historical record image without **the image itself viewable through a rights-preserving viewer, plus the verbatim source-document name strings and the scope_note**, has stripped the artifact of what makes it observation evidence. The Evidence Drawer is the affordance that prevents this stripping.

| Affordance | Behavior | Status |
|---|---|---|
| **IIIF viewer integration** | Rights-aware viewer (e.g., Mirador / Universal Viewer) preserving IIIF `rights` and attribution | PROPOSED per KFM-P9-PROG-0074 |
| **Evidence Drawer** | Exposes `source_role: observation`, `scope_note`, source archive, FamilySearch access path, IIIF manifest URI | CONFIRMED affordance class |
| **Verbatim string panel** | Shows original document strings (name, place, date) alongside KFM-normalized values | CONFIRMED rule (C9-06) |
| **Place anchor disclosure** | Shows GNIS / TGN anchor + confidence score; curator-review flag if ambiguous | CONFIRMED rule (C7-09) |
| **Living-person mask** | Default mask for any record whose subject is or might be living; explicit override only via policy + consent | CONFIRMED (C6-06) |
| **Cite-or-abstain on AI surfaces** | AI never summarizes a record without resolving its EvidenceBundle and citing both FamilySearch and the source archive | CONFIRMED doctrine |
| **Image-vs-index toggle** | Where both exist, reader can switch between scanned image and indexed transcription; index role (observation / candidate / modeled) is visible | PROPOSED |

---

## Examples

*Illustrative only — do not treat as authoritative.*

See [`_examples/`](../_examples/) for the minimal STAC Item + `kfm:provenance` + CIDOC-CRM projection + EvidenceBundle shape applied to a historical record image. The example must round-trip through:

1. Spec-hash recomputation (C5-04).
2. Image checksum verification (C3-02).
3. EvidenceBundle resolution including FamilySearch access path + underlying source archive + IIIF manifest.
4. `source_role: observation` + `scope_note` presence check.
5. Index role check (institutional observation vs. community candidate vs. OCR modeled).
6. Living-person guard applied where applicable (C6-06).
7. STAC validator + Projection lint (KFM-P27-FEAT-0003).
8. CIDOC-CRM projection validator (E31 + E5 + E21 + E53 + E13 attribution).
9. Policy-digest match including per-record-type rights + living-person guards.

…before it counts as a valid historical record image Item.

---

## Open questions

- **OPEN-HRI-01** — What is the precise distinction in the FamilySearch API between image-level metadata and index-level metadata? Is a single API call returning both, or are they separate retrievals?
- **OPEN-HRI-02** — Should institutional indexes and community-contributed indexes be exposed in separate Collections, or in a single Collection with role-per-record? Doctrine implies the former; UX may prefer the latter.
- **OPEN-HRI-03** — When does OCR-extracted text get promoted to a public surface (subject to confidence threshold), versus held back as evidence-only?
- **OPEN-HRI-04** — How are corrections to indexes handled across Collection boundaries? When a 1900 census index is re-indexed in 2025, is the prior index retained as a separate Item or merged via supersession?
- **OPEN-HRI-05** — IIIF tile-pyramid hosting: does KFM mirror FamilySearch's IIIF tiles, link out to them, or both depending on partnership terms? KFM-P9-PROG-0074 is the doctrinal anchor but does not codify the choice.
- **OPEN-C9-01** — *(From C9-01.)* When does a non-conforming GEDCOM-X response (where indexes are returned as GEDCOM-X) fail the gate vs. accept with a warning?
- **OPEN-C9-02** — *(From C9-02.)* Deceased-user consent ambiguity — applicable here for living-person records where the subject (not the FamilySearch user) becomes deceased.
- **OPEN-C9-03** — *(From C9-02.)* Retention policy — how long may KFM keep a historical record image in `data/raw/...` after the source archive withdraws it?
- **OPEN-DSC-03** — STAC namespace choice: `kfm:` (global) or `ks-kfm:` (Kansas-scoped)?
- **OPEN-PATH-01** — Confirm `docs/sources/catalog/familysearch/historical-record-images.md` placement against Directory Rules. The nested `<family>/<product>.md` pattern is inconsistent with the parent FamilySearch source catalog standard doc at `docs/sources/catalog/familysearch.md` (flat). File an ADR if the inconsistency persists.

---

## Related docs

- [`docs/sources/catalog/familysearch/README.md`](./README.md) — `familysearch` family landing page (PROPOSED).
- [`docs/sources/catalog/familysearch/family-tree.md`](./family-tree.md) — **Sibling product**: community-contributed tree nodes (`source_role: candidate`; the hypothesis side of merge gates).
- [`docs/sources/catalog/familysearch.md`](../familysearch.md) — **Parent FamilySearch source catalog entry** (standard doc; covers OAuth2, GA4GH overlay, full receipt envelope, retention, vendor risk).
- [`docs/sources/catalog/README.md`](../../README.md) — Sources catalog index (PROPOSED).
- [`docs/sources/catalog/familysearch/IDENTITY.md`](../IDENTITY.md) — Collection-id and namespace conventions (PROPOSED placement).
- [`docs/sources/catalog/familysearch/RIGHTS-AND-SENSITIVITY-MAP.md`](../RIGHTS-AND-SENSITIVITY-MAP.md) — Family-level rights map (PROPOSED placement).
- [`docs/doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) — Authority boundaries and schema-home discipline.
- [`docs/domains/people-genealogy-dna-land/README.md`](../../../domains/people-genealogy-dna-land/README.md) — DOM-PEOPLE domain doctrine.
- [`docs/standards/CIDOC_CRM_PROFILE.md`](../../../standards/CIDOC_CRM_PROFILE.md) — KFM CRM application profile (PROPOSED).
- [`docs/standards/IIIF_PROFILE.md`](../../../standards/IIIF_PROFILE.md) — IIIF integration profile (PROPOSED).
- [`docs/standards/STAC_KFM_PROFILE.md`](../../../standards/STAC_KFM_PROFILE.md) — STAC `kfm:provenance` profile (PROPOSED).
- [`data/registry/sources/people-genealogy-dna-land/`](../../../../data/registry/sources/people-genealogy-dna-land/) — Canonical SourceDescriptor home (ADR-0001).
- [`policy/genealogy/publication.rego`](../../../../policy/genealogy/publication.rego) — OPA publication gate (PROPOSED).
- [`ai-build-operating-contract.md`](../../../../ai-build-operating-contract.md) — §34 RunReceipt / GENERATED_RECEIPT discipline (CONFIRMED).
- [`docs/adr/ADR-0001-schema-home.md`](../../../adr/ADR-0001-schema-home.md) — Schema-home rule.

---

## Last reviewed

**2026-05-21** — Claude product-page polish pass; observation-role framing applied; image-vs-index distinction surfaced; IIIF rights preservation section added; per-record-type rights variability table added; CIDOC-CRM projection section added; corroborating-evidence relationship to Family Tree made explicit. Prior scaffold dated 2026-05-20.

---

<sub>📄 Product page · v0.2 · PROPOSED scaffold · <a href="#-familysearch-historical-record-images">↑ Back to top</a></sub>
