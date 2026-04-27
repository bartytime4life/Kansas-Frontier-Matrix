<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: DCAT Catalog Documentation
type: standard
version: v1
status: draft
owners: NEEDS-VERIFICATION
created: 2026-04-27
updated: 2026-04-27
policy_label: NEEDS-VERIFICATION
related: [../README.md, ../../README.md, ../../standards/KFM_DCAT_PROFILE.md, ../../../data/catalog/dcat/README.md, ../../../data/catalog/stac/README.md, ../../../data/catalog/prov/README.md]
tags: [kfm, catalog, dcat, metadata, catalog-closure]
notes: [Target path is docs/catalog/dcat/README.md. Owner, policy label, doc_id, parent links, sibling links, and active-branch file inventory require checkout verification before publication.]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# DCAT Catalog Documentation

Documentation guide for KFM’s DCAT-facing catalog lane: dataset and distribution discovery without treating catalog metadata as canonical truth.

> [!IMPORTANT]
> **Status:** experimental  
> **Owners:** `NEEDS-VERIFICATION`  
> **Path:** `docs/catalog/dcat/README.md`  
> **Repo fit:** documentation surface for the DCAT side of KFM catalog closure; expected downstream data lane is [`../../../data/catalog/dcat/README.md`](../../../data/catalog/dcat/README.md), with sibling discovery and lineage surfaces in [`../../../data/catalog/stac/README.md`](../../../data/catalog/stac/README.md) and [`../../../data/catalog/prov/README.md`](../../../data/catalog/prov/README.md).  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Reference tables](#reference-tables) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

![status](https://img.shields.io/badge/status-experimental-orange)
![doc](https://img.shields.io/badge/doc-standard%20README--like-blue)
![catalog](https://img.shields.io/badge/catalog-DCAT%20%2B%20STAC%20%2B%20PROV-0A7BBB)
![truth](https://img.shields.io/badge/truth-evidence--bounded-6A5ACD)
![policy](https://img.shields.io/badge/policy-fail--closed-lightgrey)
![owner](https://img.shields.io/badge/owner-NEEDS--VERIFICATION-red)

> [!NOTE]
> This README is intentionally **documentation-facing**. DCAT JSON-LD payloads, if present, belong under the data catalog lane, not under this docs path.

> [!CAUTION]
> Use **profile fit** language by default. Do not claim DCAT conformance, emitted catalog coverage, validator enforcement, or release-gate adoption unless the active checkout contains reviewable records, fixtures, validators, and promotion evidence.

---

## Scope

`docs/catalog/dcat/` explains how KFM should document and review the **DCAT side of catalog closure**.

In KFM terms, DCAT is the outward-facing dataset and distribution discovery vocabulary. It helps people and systems understand what a released or release-candidate dataset is, how it can be accessed, what rights posture applies, and how it relates to sibling catalog and provenance surfaces.

This documentation lane exists so maintainers can keep DCAT practice:

- downstream of `PROCESSED`,
- tied to `ReleaseManifest`, `ProofPack`, and `CatalogMatrix` expectations,
- cross-linked with STAC and PROV instead of competing with them,
- explicit about rights, access, temporal scope, and public-safe spatial scope,
- and honest about what is **CONFIRMED**, **PROPOSED**, **UNKNOWN**, or **NEEDS VERIFICATION**.

### What this README is for

Use this file to answer four questions quickly:

1. What does KFM mean by DCAT in the catalog-closure layer?
2. What belongs in this documentation lane versus the data catalog lane?
3. What must be checked before a DCAT record can support public discovery?
4. How should DCAT stay aligned with STAC, PROV, release state, policy state, and correction lineage?

[Back to top](#top)

---

## Repo fit

### Path and adjacency

| Relationship | Surface | Status | Why it matters |
| --- | --- | --- | --- |
| This documentation lane | `docs/catalog/dcat/README.md` | **PROPOSED / target file** | Explains DCAT operating posture, field expectations, review checks, and documentation boundaries. |
| Parent catalog docs | [`../README.md`](../README.md) | **NEEDS VERIFICATION** | Should define the wider catalog documentation boundary. |
| Docs root | [`../../README.md`](../../README.md) | **NEEDS VERIFICATION** | Should define broader documentation conventions and navigation. |
| KFM DCAT profile | [`../../standards/KFM_DCAT_PROFILE.md`](../../standards/KFM_DCAT_PROFILE.md) | **NEEDS VERIFICATION** | Expected profile authority for field-level and conformance language. |
| DCAT data lane | [`../../../data/catalog/dcat/README.md`](../../../data/catalog/dcat/README.md) | **NEEDS VERIFICATION in active checkout** | Expected home for emitted dataset/distribution records, not this docs lane. |
| STAC sibling | [`../../../data/catalog/stac/README.md`](../../../data/catalog/stac/README.md) | **NEEDS VERIFICATION in active checkout** | Asset, item, collection, and spatiotemporal discovery should remain distinct from DCAT. |
| PROV sibling | [`../../../data/catalog/prov/README.md`](../../../data/catalog/prov/README.md) | **NEEDS VERIFICATION in active checkout** | Lineage, activity, and agent traceability should remain distinct from DCAT. |
| Data lifecycle | [`../../../data/README.md`](../../../data/README.md) | **NEEDS VERIFICATION** | Should preserve the `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED` boundary. |
| Contract / schema authority | [`../../../contracts/README.md`](../../../contracts/README.md), [`../../../schemas/README.md`](../../../schemas/README.md) | **NEEDS VERIFICATION** | DCAT documentation may reference declared shapes but must not silently define machine-contract authority. |
| Policy authority | [`../../../policy/README.md`](../../../policy/README.md) | **NEEDS VERIFICATION** | Rights, sensitivity, and publication denial rules belong in policy, even when DCAT exposes their consequences. |
| Catalog helper / tests | [`../../../tools/catalog/README.md`](../../../tools/catalog/README.md), [`../../../tests/catalog/README.md`](../../../tests/catalog/README.md) | **NEEDS VERIFICATION** | Helpers and tests should prove cross-link behavior rather than letting README prose stand in for validation. |

### Operating boundary

DCAT in KFM should describe **released or release-candidate discovery scope**. It should not become:

- the canonical payload store,
- a source registry,
- a policy engine,
- a proof pack,
- a runtime API envelope,
- an AI evidence bundle,
- or a workaround for release review.

> [!TIP]
> Keep the KFM trust split visible:
>
> **catalog metadata ≠ canonical payload ≠ proof ≠ policy ≠ publication**

[Back to top](#top)

---

## Accepted inputs

The following belong in `docs/catalog/dcat/` when they remain documentation, guidance, examples, or review scaffolding.

| Accepted input | Belongs here when… | Status |
| --- | --- | --- |
| `README.md` orientation | it explains the lane, boundaries, links, review checks, and uncertainty clearly | **CONFIRMED for this output** |
| DCAT profile guidance | it summarizes or links to the project’s DCAT profile without replacing the profile | **PROPOSED / NEEDS VERIFICATION** |
| Field mapping notes | they explain how KFM release, rights, provenance, access, and correction concepts map into DCAT-facing records | **PROPOSED** |
| Review checklists | they help reviewers verify release linkage, rights posture, access posture, spatial/temporal scope, and sibling catalog closure | **PROPOSED** |
| Illustrative JSON-LD snippets | they are labeled as examples or pseudocode and do not claim emitted fixture status | **PROPOSED** |
| Crosswalk tables | they clarify relationships among DCAT, STAC, PROV, `ReleaseManifest`, `CatalogMatrix`, and `EvidenceBundle` | **PROPOSED** |
| Open verification notes | they identify what must be checked in the active branch before publication claims are made | **CONFIRMED documentation pattern** |

### What “accepted” means in KFM terms

Accepted documentation here should make discovery safer and easier to review. It should never downgrade proof, policy, provenance, or release state into prose-only advice.

[Back to top](#top)

---

## Exclusions

| Not here | Goes instead | Why |
| --- | --- | --- |
| Actual DCAT JSON-LD dataset/distribution records | `data/catalog/dcat/` | This docs lane explains; the data lane emits and stores catalog records. |
| STAC Catalogs, Collections, or Items | `data/catalog/stac/` | STAC remains the asset and spatiotemporal discovery carrier. |
| PROV bundles | `data/catalog/prov/` | PROV remains the lineage/activity/agent carrier. |
| Raw acquisitions or source-native dumps | `data/raw/` | Discovery is not intake. |
| Intermediate transforms, scratch QA, or unresolved candidates | `data/work/` or `data/quarantine/` | Validation and experimentation are not publication. |
| Canonical processed payloads | `data/processed/` | DCAT describes discoverable scope; it does not replace the payload. |
| Public publication packages | `data/published/` | Publication is governed state, not just catalog presence. |
| Run receipts and process memory | `data/receipts/` | Receipts may be linked but are not DCAT records. |
| Release proofs, attestations, and proof packs | `data/proofs/` | Proof artifacts remain first-class and reviewable. |
| Policy rules or reason registries | `policy/` | Policy should be executable and independently reviewable. |
| JSON Schema / OpenAPI / machine contracts | `contracts/` or `schemas/` | Documentation can reference contracts but must not become the contract authority. |
| Runtime API envelopes, Evidence Drawer payloads, or Focus Mode answers | governed API / app surfaces | Runtime trust objects are not catalog metadata. |
| AI summaries or generated prose | governed AI surfaces with EvidenceBundle references | AI is interpretive only and must not become source truth. |

> [!WARNING]
> If a proposed DCAT record would expose unresolved rights, unreleased scope, exact-location-sensitive detail, or an access point that is not public-safe, it should fail closed and stay out of public discovery.

[Back to top](#top)

---

## Directory tree

### Target documentation shape

```text
docs/
└── catalog/
    └── dcat/
        └── README.md
```

### Expected adjacent catalog-data shape

```text
data/
└── catalog/
    ├── README.md
    ├── dcat/
    │   └── README.md
    ├── stac/
    │   └── README.md
    └── prov/
        └── README.md
```

### Possible payload-bearing shape

```text
data/
└── catalog/
    └── dcat/
        ├── README.md
        └── datasets/
            └── <dataset>__<version>.jsonld
```

> [!NOTE]
> The payload-bearing shape is **PROPOSED** until verified in the active branch. Do not create it merely because this README names it.

[Back to top](#top)

---

## Quickstart

Run these checks before revising this file or adding DCAT-related catalog records.

### 1. Verify the active checkout

```bash
pwd
git status --short
git branch --show-current || true
git ls-files 'docs/catalog/**' 'data/catalog/**' 'docs/standards/**' | sort
```

### 2. Inspect nearby documentation and data lanes

```bash
sed -n '1,220p' docs/catalog/README.md 2>/dev/null || true
sed -n '1,260p' docs/standards/KFM_DCAT_PROFILE.md 2>/dev/null || true

sed -n '1,220p' data/README.md 2>/dev/null || true
sed -n '1,220p' data/catalog/README.md 2>/dev/null || true
sed -n '1,220p' data/catalog/dcat/README.md 2>/dev/null || true
sed -n '1,220p' data/catalog/stac/README.md 2>/dev/null || true
sed -n '1,220p' data/catalog/prov/README.md 2>/dev/null || true
```

### 3. Search before inventing names

```bash
rg -n "DCAT|dcat:Dataset|dcat:Distribution|CatalogMatrix|CatalogClosure|ReleaseManifest|ProofPack|EvidenceBundle|PROV|STAC" \
  docs data contracts schemas policy tools scripts tests .github 2>/dev/null || true
```

### 4. Confirm validator and fixture reality

```bash
find tools scripts tests contracts schemas -maxdepth 4 -type f 2>/dev/null | sort
rg -n "validate.*dcat|dcat.*validate|catalog.*crosslink|CatalogMatrix|catalog closure" \
  tools scripts tests contracts schemas .github 2>/dev/null || true
```

### 5. Add examples only as examples

```bash
# Example only: verify active branch conventions before creating payload files.
mkdir -p data/catalog/dcat/datasets
$EDITOR data/catalog/dcat/datasets/<dataset>__<version>.jsonld
```

> [!TIP]
> The safest first DCAT change is usually **docs + profile + fixtures + tests**, not a standalone JSON-LD record with no release, proof, or cross-link evidence.

[Back to top](#top)

---

## Usage

### How DCAT should behave in KFM

DCAT-facing material should remain:

- **discovery-oriented**, not payload-heavy,
- **release-linked**, not free-floating,
- **profile-aware**, not ad hoc,
- **rights-visible**, not silent on access posture,
- **public-safe**, not accidentally precise or sensitive,
- **cross-linked**, not isolated from STAC and PROV,
- and **correction-friendly**, not lineage-erasing.

### Profile-aligned example shape

The following is an **illustrative JSON-LD sketch**, not proof of an emitted fixture.

```jsonc
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "spdx": "http://spdx.org/rdf/terms#",
    "time": "http://www.w3.org/2006/time#"
  },
  "@type": "dcat:Dataset",
  "dct:identifier": "TODO(stable-dataset-id)",
  "dct:title": "TODO(human-readable title)",
  "dct:description": "TODO(release-linked description)",
  "dct:license": { "@id": "TODO(resolvable-license-iri)" },
  "dct:rights": "TODO(rights/access posture)",
  "dct:spatial": {
    "@type": "dct:Location",
    "dcat:bbox": "TODO(public-safe bbox or profile-approved geometry)"
  },
  "dct:temporal": {
    "@type": "dct:PeriodOfTime",
    "time:hasBeginning": {
      "@type": "time:Instant",
      "time:inXSDDateTime": "TODO(ISO-8601 start)"
    },
    "time:hasEnd": {
      "@type": "time:Instant",
      "time:inXSDDateTime": "TODO(ISO-8601 end)"
    }
  },
  "dct:conformsTo": [
    { "@id": "https://www.w3.org/TR/vocab-dcat-3/" },
    { "@id": "TODO(kfm-dcat-profile-ref)" }
  ],
  "dct:relation": [
    { "@id": "TODO(release-manifest-ref)" },
    { "@id": "TODO(stac-record-ref)" },
    { "@id": "TODO(prov-bundle-ref)" },
    { "@id": "TODO(catalog-matrix-ref)" }
  ],
  "dct:provenance": { "@id": "TODO(prov-bundle-ref)" },
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:identifier": "TODO(distribution-id)",
      "dct:title": "TODO(distribution title)",
      "dcat:mediaType": "TODO(media type)",
      "dcat:downloadURL": { "@id": "TODO(actual-downloadable-artifact-url)" },
      "spdx:checksum": {
        "@type": "spdx:Checksum",
        "spdx:algorithm": "spdx:checksumAlgorithm_sha256",
        "spdx:checksumValue": "TODO(sha256 digest)"
      }
    }
  ]
}
```

Use `dcat:downloadURL` only for an actual downloadable artifact. Use `dcat:accessURL` when the outward object is a service, viewer, or mediated access point.

[Back to top](#top)

---

## Diagram

```mermaid
flowchart TD
    A[RAW] --> B[WORK / QUARANTINE]
    B --> C[PROCESSED]
    C --> D[DatasetVersion]
    D --> E[ReleaseManifest]
    D --> F[EvidenceBundle]
    D --> G[ProofPack]
    E --> H[CatalogMatrix / catalog closure]
    F --> H
    G --> H

    H --> I[data/catalog/dcat/]
    H --> J[data/catalog/stac/]
    H --> K[data/catalog/prov/]

    L[docs/catalog/dcat/] --> I
    L --> M[KFM DCAT profile]
    L --> N[review checklist]

    I --> O[Dataset / distribution discovery]
    J --> P[Asset / time discovery]
    K --> Q[Lineage / activity / agent traceability]

    O --> R[Governed public discovery]
    P --> R
    Q --> R

    R --> S[Governed API / UI / Evidence Drawer]
    S --> T[ANSWER / ABSTAIN / DENY / ERROR]

    classDef lifecycle fill:#eef6ff,stroke:#4a74a8,stroke-width:1.5px,color:#1f2d3d;
    classDef proof fill:#fff7e6,stroke:#c9871a,stroke-width:1.5px,color:#5c3b00;
    classDef doc fill:#f4f0ff,stroke:#6f42c1,stroke-width:1.5px,color:#2d124f;
    classDef catalog fill:#eef9ef,stroke:#3d8b50,stroke-width:1.5px,color:#183d23;
    class A,B,C,D lifecycle;
    class E,F,G,H proof;
    class L,M,N doc;
    class I,J,K,O,P,Q,R catalog;
```

[Back to top](#top)

---

## Reference tables

### DCAT in the catalog triplet

| Surface | Primary job | KFM expectation |
| --- | --- | --- |
| DCAT | Dataset, distribution, access, rights, and catalog interoperability | Present or planned for outward dataset/distribution discovery. |
| STAC | Spatiotemporal asset, item, collection, and asset-link discovery | Used where item/asset/time discovery is the stronger carrier. |
| PROV | Lineage, activity, agent, derivation, and provenance interchange | Present or resolvable for release-bearing artifacts. |
| KFM governance objects | Policy, review, release, proof, runtime, correction, and rollback | Must remain first-class; DCAT may link to them but must not absorb them. |

### Minimum dataset / distribution expectations

| Concern | DCAT-facing carrier | KFM consequence |
| --- | --- | --- |
| Stable dataset identity | `dct:identifier`, title, description | Identity drift breaks discovery, lineage, and correction. |
| Release linkage | `dct:relation` or profile-defined relation fields | Public discovery must not outrun release state. |
| Profile reference | `dct:conformsTo` | Validators and reviewers need explicit profile pins. |
| Rights posture | `dct:license`, `dct:rights`, `dct:accessRights` | Unknown or restricted rights should block public discovery. |
| Public-safe spatial scope | `dct:spatial`, profile-approved geometry/bounds | Discovery should communicate scope without leaking unsafe precision. |
| Time basis | `dct:temporal`, profile-approved temporal fields | KFM is time-aware; catalog records should not hide observation, validity, or publication time. |
| Distribution class | `dcat:distribution` | Different artifact classes should not be flattened into one ambiguous distribution. |
| Download vs access | `dcat:downloadURL` / `dcat:accessURL` | URL type must match the actual outward surface. |
| Provenance continuation | `dct:provenance` and sibling PROV links | Discovery should continue into lineage instead of stopping at a catalog title. |
| Correction visibility | relation to correction/supersession/withdrawal records | Public discovery must preserve visible change lineage. |

### Avoid patterns

| Avoid | Why |
| --- | --- |
| Treating DCAT as canonical truth | KFM keeps catalog metadata downstream of evidence, proof, policy, and release state. |
| Claiming conformance because DCAT is a good fit | KFM separates profile fit from implemented, validated adoption. |
| Publishing discovery before rights/review closure | Fail-closed publication posture must remain real. |
| Letting DCAT, STAC, and PROV disagree on identifiers or release scope | Catalog closure stops being trustworthy when the triplet drifts. |
| Minting ad hoc extension terms in README prose | Extension drift becomes catalog drift. |
| Hiding services behind `downloadURL` | Consumers need to know whether a distribution is a downloadable artifact or mediated access point. |

[Back to top](#top)

---

## Task list / definition of done

Use this checklist for changes to this documentation lane or the downstream DCAT data lane.

- [ ] Active checkout confirms whether `docs/catalog/dcat/README.md` exists or is new.
- [ ] KFM Meta Block V2 remains present and synchronized with the visible title.
- [ ] Owner, policy label, created date, and related links have been verified or explicitly left as placeholders.
- [ ] This documentation lane remains separate from `data/catalog/dcat/`.
- [ ] Any example is labeled as illustrative unless emitted fixture evidence exists.
- [ ] Any referenced profile path is checked in and linked correctly from this file.
- [ ] Any new DCAT record links to release state or release-candidate state.
- [ ] STAC, DCAT, PROV, `ReleaseManifest`, and `CatalogMatrix` identifiers are aligned where catalog closure is claimed.
- [ ] Rights, access, sensitivity, and public-safe spatial scope are visible.
- [ ] `downloadURL` and `accessURL` are used according to actual distribution type.
- [ ] Correction, supersession, withdrawal, or rollback references are visible when relevant.
- [ ] Validator, fixture, and CI claims are grounded in active-branch files.
- [ ] No README prose claims public release, publication, conformance, or enforcement without proof.
- [ ] Rollback path is documented for any public-facing catalog change.

[Back to top](#top)

---

## FAQ

### Is this the home for DCAT JSON-LD files?

No. This is the documentation guide at `docs/catalog/dcat/`. DCAT JSON-LD payloads should live in the data catalog lane, expected as `data/catalog/dcat/` unless the active repo proves a different convention.

### Does a DCAT record make a dataset published?

No. Publication is a governed state transition. A DCAT record may participate in discovery after release gates pass, but it does not replace release approval, proof objects, policy decisions, or rollback records.

### Can DCAT replace STAC or PROV?

No. KFM uses the catalog triplet because each standard carries a different burden: DCAT for dataset/distribution discovery, STAC for spatiotemporal asset discovery, and PROV for lineage and activity traceability.

### Can Focus Mode answer from DCAT alone?

No. Focus Mode must resolve admissible evidence through governed backend flow. DCAT can help point to released scope, but `EvidenceBundle` and policy state outrank catalog prose.

### What should happen when rights or sensitivity are unclear?

The record should stay out of public discovery or be redacted/generalized until rights, review, and sensitivity posture are resolved.

[Back to top](#top)

---

## Appendix

<details>
<summary><strong>Evidence markers used in this README</strong></summary>

| Marker | Meaning |
| --- | --- |
| **CONFIRMED** | Verified from active checkout, supplied project source, visible generated artifact, or direct command evidence. |
| **INFERRED** | Strongly suggested by project doctrine or adjacent docs, but not proven as current implementation. |
| **PROPOSED** | Recommended target behavior or structure that still needs implementation evidence. |
| **UNKNOWN** | Not verified strongly enough to claim. |
| **NEEDS VERIFICATION** | Specific branch, owner, path, policy, tool, validator, rights, or runtime detail that should be checked before merge. |

</details>

<details>
<summary><strong>Review prompts for maintainers</strong></summary>

- Does this README describe the active branch, or only the desired design?
- Are DCAT examples clearly labeled as examples unless fixtures exist?
- Are rights, access posture, and public-safe geometry visible?
- Are STAC and PROV cross-links present where catalog closure is claimed?
- Are `ReleaseManifest`, `ProofPack`, `EvidenceBundle`, and `CatalogMatrix` still first-class?
- Are policy and validation claims backed by files, tests, or workflow evidence?
- Would a public user understand whether a URL is a direct download, a service, or a mediated access point?
- Is correction lineage visible if a release was replaced, withdrawn, or superseded?

</details>

<details>
<summary><strong>External standard anchors</strong></summary>

- [W3C DCAT Version 3][w3c-dcat-v3]
- [OGC STAC Community Standard 1.1][ogc-stac]
- [W3C PROV-O][w3c-prov-o]

These anchors support vocabulary alignment only. KFM publication readiness still depends on KFM evidence, policy, review, release, proof, and catalog-closure gates.

</details>

[w3c-dcat-v3]: https://www.w3.org/TR/vocab-dcat-3/
[ogc-stac]: https://docs.ogc.org/cs/25-004/25-004.html
[w3c-prov-o]: https://www.w3.org/TR/prov-o/
