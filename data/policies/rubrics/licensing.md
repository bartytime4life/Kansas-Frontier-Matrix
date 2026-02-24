<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/3d3b7b9d-2b55-4a48-88e5-27c3f7a9b2e1
title: data/policies/rubrics/licensing.md
type: standard
version: v1
status: draft
owners: Governance + Data Stewardship + Legal (as applicable)
created: 2026-02-24
updated: 2026-02-24
policy_label: restricted
related:
  - configs/contracts/schemas/catalogs/
  - configs/contracts/policy/
tags: [kfm, policy, rubric, licensing, rights, spdx, governance]
notes:
  - Normative rubric for classifying and enforcing licensing + rights for KFM artifacts.
  - Default-deny when license/rights-holder are missing, unclear, or conflicting.
[/KFM_META_BLOCK_V2] -->

# Licensing & Rights Rubric
One-line purpose: **Classify and enforce license + rights posture for all KFM artifacts** (data, derived products, media, code, docs) across the lifecycle and all distribution surfaces.

![status](https://img.shields.io/badge/status-draft-yellow)
![policy](https://img.shields.io/badge/policy_label-restricted-orange)
![enforcement](https://img.shields.io/badge/enforcement-fail--closed-red)
![spdx](https://img.shields.io/badge/license-using%20SPDX-blue)

> ⚠️ Not legal advice. This is an engineering + governance rubric for enforcement. Escalate edge cases to an appropriate reviewer.

---

## Where this fits in the repo
This file lives under `data/policies/rubrics/` and defines **the operational decision rules** that:
- drive **promotion gates** (Raw → Work/Quarantine → Processed → Published),
- drive **publish/export/runtime behavior** (API, tiles, downloads, Story/Map embeds),
- define what metadata is **required** for redistribution.

---

## Quick navigation
- [Non-negotiables](#non-negotiables)
- [Required metadata](#required-metadata)
- [License classes](#license-classes)
- [Decision flow](#decision-flow)
- [Lifecycle gates](#lifecycle-gates)
- [Attribution & notices](#attribution--notices)
- [Special cases](#special-cases)
- [Templates](#templates)
- [Definition of Done](#definition-of-done)

---

## Non-negotiables
1) **Online availability ≠ permission to reuse.**  
2) **No promotion to Published without license + rights-holder.**  
3) If rights are insufficient/unclear, **metadata-only reference mode** is allowed (catalog and cite, but do not mirror bytes or redistribute).  
4) **Exports must automatically carry attribution + license/notice material.**  
5) Story/Map publishing is blocked if **citations/rights are incomplete** for included media/assets.  
6) Licensing is an **input to policy** (access control + redaction + distribution behavior).  
7) **When in doubt: deny.** Use class **L5** and route to review.

---

## Required metadata
### Minimum required fields (per distributable artifact)
Every artifact that can be distributed (downloaded, exported, embedded, served by API) MUST carry:

| Field | Required | Notes |
|---|---:|---|
| `license.spdx` | ✅ | SPDX identifier or SPDX expression (use `LicenseRef-*` only when unavoidable) |
| `rights_holder` | ✅ | Person/org/government/entity holding rights |
| `source` | ✅ | Source URL/DOI/contract id, plus citation pointer |
| `attribution` | ✅ | Human-readable attribution statement |
| `restrictions` | ✅ | Any constraints (SA/NC/ND/contract-only/field-of-use/etc.) |
| `redistribution_allowed` | ✅ | Derived boolean (true/false) |
| `derivatives_allowed` | ✅ | Derived boolean (true/false) |
| `notes` | ✅ | Clarifications, carve-outs, third-party exclusions |

### Where these fields must appear
Licensing signals MUST be consistent across:
- **Catalogs** (DCAT distributions + STAC collections/items as applicable)
- **Manifests / receipts** (run manifests, publish manifests, export manifests)
- **Packaging** (NOTICE/ATTRIBUTION bundle for any export)

> ✅ Conflict rule: If licensing signals disagree across surfaces, classify as **L5** and deny publish until resolved.

---

## License classes
> Default: If uncertain, missing, or conflicting → **L5**.

| Class | Name | Typical identifiers | Publish allowed | Operational obligations |
|---:|---|---|---|---|
| L0 | Public domain / dedication | `CC0-1.0`, `PDDL-1.0` | ✅ Yes | Attribution recommended; verify no embedded third-party exclusions |
| L1 | Permissive / attribution | `MIT`, `BSD-3-Clause`, `Apache-2.0`, `CC-BY-4.0`, `ODC-By-1.0` | ✅ Yes | Must satisfy attribution + notices; include “changes made” when required |
| L2 | Reciprocal / share-alike | `GPL-3.0-only`, `AGPL-3.0-only`, `LGPL-3.0-only`, `CC-BY-SA-4.0`, `ODbL-1.0` | ⚠️ Conditional | Requires compatibility review; publishing may impose SA obligations on downstream |
| L3 | Restricted commons | `CC-BY-NC-*`, `CC-BY-ND-*`, `CC-BY-NC-ND-*` | ❌ Default | Generally blocks KFM “Published” distribution; allow only if an explicit policy exception exists |
| L4 | Proprietary / contract-only / no redistribution | “All rights reserved”, ToS-only, partner delivery with redistribution prohibition | ❌ No | Metadata-only reference unless a contract explicitly permits redistribution |
| L5 | Unknown / missing / conflicting | `NOASSERTION`, empty, contradictory | ❌ No | Quarantine + metadata-only reference; requires remediation |

---

## Decision flow
Use this flow for every new source, every derived product, and every publish/export job.

    [1] Do we have verifiable license text or authoritative license statement?
         - No  -> Class L5 (deny publish; metadata-only reference)
         - Yes -> continue

    [2] Can we encode it as SPDX id or SPDX expression?
         - No  -> Use LicenseRef-* + attach license text + flag for review
         - Yes -> continue

    [3] Do we have a named rights holder?
         - No  -> Class L5
         - Yes -> continue

    [4] Any restrictions (SA/NC/ND/field-of-use/contract-only)?
         - Yes -> Class L2/L3/L4 per restriction + review outcome required
         - No  -> Class L0/L1

    [5] Publish decision:
         - L0/L1 -> allow publish with automatic attribution/notices
         - L2     -> allow only if obligations are enforceable + distribution is compatible
         - L3/L4/L5 -> deny publish; metadata-only reference (unless explicit exception)

---

## Lifecycle gates
### Intake gate (before mirroring bytes)
- If **L4/L5**, prefer **pointer only** (no mirroring) unless a contract explicitly allows mirroring.
- If **L0–L3**, mirroring is allowed only when attribution/notices can be emitted.

### Promotion gate: Raw/Work → Processed
Promotion requires:
- License classified (L0–L4) AND
- Rights holder recorded AND
- Restrictions recorded AND
- Derived booleans computed (`redistribution_allowed`, `derivatives_allowed`) AND
- Attribution statement defined

### Publishing gate: Processed → Published
Publishing is blocked if:
- Any included artifact is **L3/L4/L5**
- Any required attribution cannot be emitted automatically
- Any share-alike obligations cannot be satisfied by the intended distribution
- Any story/media rights are incomplete

---

## Attribution & notices
### Required behaviors
All exports (files, bundles, tilesets, reports) MUST include:
- License identifier(s) or expression(s)
- Attribution statement(s)
- License URL or embedded license text (when required)
- “Changes made” statement when applicable
- “Third-party exclusions” note when applicable

### Recommended attribution format (TASL-style)
- **Title** (if known)
- **Author/Publisher**
- **Source** (URL/DOI)
- **License** (SPDX + link or embedded text)

---

## Special cases
### Open access with third-party exclusions
Some open access works include third-party materials that are excluded unless explicitly stated.
Rule: Track license at the **asset level** when third-party materials may be excluded; do not assume umbrella coverage.

### Mixed-license composites
If derived products combine multiple sources:
- Derived distribution must comply with the most restrictive applicable obligations.
- If obligations are incompatible or unclear → **L5** until resolved.

### Website Terms of Service / API ToS
If acquisition is governed by ToS (not a license grant):
- Treat as **L4** unless explicit redistribution permission exists.
- Prefer metadata-only reference and store citation + access path.

### Dual licensing / license expressions
Use SPDX expressions when source is explicitly multi-licensed (e.g., `MIT OR Apache-2.0`).

---

## Templates
### A) Catalog record snippet (YAML-like)
    license:
      spdx: "CC-BY-4.0"
      text_ref: "evidence://license/cc-by-4.0.txt"   # optional if required
    rights_holder: "Example Org"
    source: "doi:10.xxxx/xxxxx"
    attribution: "Example Org (2024). Example Dataset. DOI:10.xxxx/xxxxx. Licensed CC-BY-4.0."
    restrictions:
      sharealike: false
      noncommercial: false
      noderivatives: false
      contract_only: false
      field_of_use: null
    redistribution_allowed: true
    derivatives_allowed: true
    notes:
      - "Verify embedded media credit lines for exclusions."

### B) Export NOTICE stub
    NOTICES
    =======
    This export includes materials under the following licenses:
    - CC-BY-4.0 — Example Org (2024). Example Dataset. DOI:10.xxxx/xxxxx.

    Attribution:
    Example Org (2024). Example Dataset. DOI:10.xxxx/xxxxx. Licensed CC-BY-4.0.

    Changes:
    Derived product generated by KFM pipelines. See provenance record for transforms.

### C) Metadata-only reference mode
    distribution_mode: "metadata-only"
    mirror_bytes: false
    external_reference: "https://source.example.org/dataset/123"
    publish_allowed: false
    reason: "License/rights do not permit redistribution"

---

## Definition of Done
### Intake DoD
- [ ] Source captured (URL/DOI/contract id)
- [ ] License statement captured (text/link) and normalized to SPDX where possible
- [ ] Rights holder identified
- [ ] Restrictions recorded (SA/NC/ND/contract-only/field-of-use)
- [ ] Asset-level license tracked for embedded third-party content (if applicable)

### Promotion DoD (Raw/Work → Processed)
- [ ] Class assigned (L0–L5)
- [ ] Derived booleans computed and stored
- [ ] Attribution string validated
- [ ] If L2/L3/L4: review outcome recorded + policy exception (if any) documented

### Publish DoD (Processed → Published)
- [ ] No L5 included
- [ ] No L3/L4 included (unless explicit exception)
- [ ] Export packaging emits attribution + notices automatically
- [ ] Story/Map assets have complete citations + rights
