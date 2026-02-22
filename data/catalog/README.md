<a id="top"></a>

# data/catalog
Dataset-level metadata (DCAT JSON-LD) for KFM’s **Catalog Triplet** — cross-linked to **STAC** (assets) and **PROV** (lineage) so evidence can be resolved deterministically.

**Status:** vNext / Draft  
**Owners:** Data steward(s) + platform maintainer(s) (assign via `CODEOWNERS`)  
`ZONE: CATALOG/TRIPLET` `SURFACE: DCAT` `FORMAT: JSON-LD` `PROMOTION: FAIL-CLOSED` `LINKCHECK: REQUIRED`

**Quick nav:**  
[Overview](#overview) · [Directory layout](#directory-layout) · [What belongs here](#what-belongs-here) ·
[DCAT profile baseline](#dcat-profile-baseline) · [Cross-link contract](#cross-link-contract) ·
[Validation and promotion gates](#validation-and-promotion-gates) · [Adding a dataset version](#adding-a-dataset-version) ·
[Safety and sensitive location notes](#safety-and-sensitive-location-notes)

---

## Overview

KFM treats catalogs as **contract surfaces**, not “nice-to-have metadata.” The catalog triplet is:

- **DCAT** — dataset-level identity, publisher, license/rights, and distributions
- **STAC** — asset-level inventory + spatiotemporal extents
- **PROV** — lineage: which inputs/tools/params produced which outputs

These are **cross-linked** so an `EvidenceRef` can resolve without guessing.

---

## Directory layout

This folder is the DCAT portion of the triplet. The triplet is typically laid out under `data/` like:

~~~text
data/
  catalog/
    README.md
    dcat/                  # DCAT JSON-LD outputs
  stac/                    # STAC collections + items (asset metadata)
  prov/                    # PROV bundles + run receipts (lineage)
~~~

If your repo structure differs, update this README and the validation/link-check rules so paths stay deterministic.

---

## What belongs here

✅ **DO store here**
- **DCAT JSON-LD** records for promoted dataset versions (Dataset + Distributions).
- Optional small indexes used by tooling (only if they’re derived + reproducible).

❌ **DO NOT store here**
- Raw artifacts, intermediate work products, or processed data files.
- Secrets, signed URLs, or direct object-store links that bypass the governed API boundary.

---

## DCAT profile baseline

This repo uses a **profiled DCAT minimum** so validation is strict and predictable.

### Minimum required fields (dataset record)

At a minimum, each DCAT Dataset record MUST include:

- `dct:title`
- `dct:description`
- `dct:publisher`
- `dct:license` (or `dct:rights`)
- `dcat:theme` (controlled vocabulary)
- `dct:spatial` and `dct:temporal`
- `dcat:distribution` (one per artifact class)
- `prov:wasGeneratedBy` link to the PROV activity/bundle
- `kfm:policy_label`
- `kfm:dataset_id`
- `kfm:dataset_version_id`

### Distribution requirements (practical)

Each `dcat:Distribution` SHOULD:
- Refer to a **content-addressed artifact** (digest-addressed) rather than a mutable filename.
- Declare format/media type.
- Point to an allowed access method (governed API, signed link generated server-side, etc.).

---

## Cross-link contract

Cross-links MUST be explicit and testable (validated in CI):

- DCAT Dataset → Distributions → **artifact digests**
- DCAT Dataset → `prov:wasGeneratedBy` → **PROV bundle/activity**
- STAC Collection → `rel="describedby"` → **DCAT Dataset**
- STAC Item → links to **PROV run receipt/activity** and **DCAT distribution**

### EvidenceRef schemes (minimum)

Evidence references SHOULD use explicit schemes so resolution is bounded and deterministic:

- `dcat://...` → dataset/distribution metadata
- `stac://...` → collection/item/asset metadata
- `prov://...` → lineage (activities/entities/agents; run receipts)
- `doc://...` → governed documentation / story citations
- `graph://...` → entity relations (if enabled)

---

## How this fits the KFM truth path

KFM’s data lifecycle is:

~~~mermaid
flowchart LR
  RAW[RAW<br/>immutable acquisition] --> WORK[WORK or QUARANTINE<br/>normalize + QA]
  WORK --> PROCESSED[PROCESSED<br/>publishable artifacts]
  PROCESSED --> CATALOG[CATALOG triplet<br/>DCAT + STAC + PROV]
  CATALOG --> PUBLISHED[PUBLISHED surfaces<br/>API + UI]
~~~

**Key rule:** A dataset version cannot be served in runtime surfaces until it has **processed artifacts + validated catalogs + run receipts + policy labels**.

---

## Validation and promotion gates

Promotion is **fail-closed**. At minimum, promotion MUST be blocked if any required artifact is missing or invalid.

### Catalog-related gates (summary)

| Gate | What it checks | Why it matters |
|---|---|---|
| Gate A | Stable `dataset_id`, immutable `dataset_version_id`, deterministic `spec_hash` | Reproducibility and auditability |
| Gate B | License/rights explicit; attribution captured; unknown stays quarantined | Prevents unlawful or unsafe release |
| Gate C | `policy_label` assigned; redaction/generalization plan recorded | Prevents sensitive leakage |
| **Gate D** | DCAT/STAC/PROV validate + cross-links resolvable | Enables evidence resolution |
| Gate E | Run receipt exists; checksums for inputs/outputs; environment captured | Makes results reproducible |
| Gate F | Policy tests + contract tests pass; evidence resolves in CI | Ensures enforcement is real |

### Validators and link-checking

CI SHOULD run:
- DCAT validator (profile + JSON-LD validity)
- STAC validator (collection/item correctness)
- PROV validator (bundle structure)
- Catalog link-checker (cross-links + existence checks)

If these tools don’t exist yet in your repo, treat this as the required acceptance criteria for adding them.

---

## Adding a dataset version

Use this checklist when generating/updating DCAT outputs for a dataset version.

### Required checklist

- [ ] `kfm:dataset_id` is stable for the logical dataset.
- [ ] `kfm:dataset_version_id` is immutable for the promoted output set.
- [ ] `kfm:policy_label` is set (and obligations are recorded in PROV where applicable).
- [ ] DCAT Dataset record includes all required minimum fields.
- [ ] Every Distribution points to a content-addressed artifact (digest recorded).
- [ ] `prov:wasGeneratedBy` links to the correct PROV activity/bundle.
- [ ] STAC records link back to DCAT (`rel="describedby"`) and to PROV (run receipt/activity).
- [ ] Validators pass and cross-links resolve in CI.

<details>
<summary>Example: minimal DCAT JSON-LD skeleton (illustrative)</summary>

~~~json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "prov": "http://www.w3.org/ns/prov#",
    "kfm": "https://example.invalid/ns/kfm#"
  },
  "@id": "dcat://kfm/datasets/<dataset_id>/<dataset_version_id>",
  "@type": "dcat:Dataset",
  "kfm:dataset_id": "<dataset_id>",
  "kfm:dataset_version_id": "<dataset_version_id>",
  "kfm:policy_label": "public",
  "dct:title": "…",
  "dct:description": "…",
  "dct:publisher": "…",
  "dct:license": "…",
  "dcat:theme": ["…"],
  "dct:spatial": "…",
  "dct:temporal": "…",
  "prov:wasGeneratedBy": { "@id": "prov://kfm/run/<run_id>" },
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:format": "application/x-parquet",
      "dcat:downloadURL": "kfm+digest://sha256:<artifact_digest>"
    }
  ]
}
~~~

</details>

---

## Safety and sensitive location notes

If a dataset contains **sensitive locations** (e.g., archaeology sites, sensitive species), default posture is **do not publish precise locations**.

Recommended pattern:
- classify as `restricted_sensitive_location`
- produce dual outputs:
  - restricted precise dataset version
  - public generalized dataset version (only if allowed)
- document the generalization method (grid aggregation, dissolve, etc.)
- test to confirm no precise coordinates leak
- ensure UI indicates generalization + reason
- require governance review before release

---

## Related docs and schemas

- Repo structure and data layout: `../../docs/MASTER_GUIDE_v13.md` (if present)
- DCAT / STAC / PROV schemas: `../../schemas/`
- Governance / promotion rules: see the KFM design & governance guide (vNext)

---

## Contributing rules of thumb

- Prefer **generated** catalogs from pipeline code over manual edits.
- If you must edit by hand: keep changes minimal and update the corresponding pipeline/spec so regeneration is stable.
- Never add links that bypass the governed API/policy boundary.

---

[Back to top](#top)
