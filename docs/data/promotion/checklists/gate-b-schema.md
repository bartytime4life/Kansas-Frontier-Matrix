<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/2a3d9f1b-14cc-4f60-8a32-1a3a3f8bd2a1
title: Gate B — Licensing & Rights Metadata (Schema Checklist)
type: standard
version: v1
status: draft
owners: KFM Maintainers (TODO: set CODEOWNERS team)
created: 2026-03-01
updated: 2026-03-01
policy_label: public
related:
  - docs/data/promotion/README.md (TODO)
  - docs/data/promotion/checklists/ (this directory)
  - docs/data/promotion/checklists/gate-c-sensitivity.md (TODO)
  - docs/data/promotion/checklists/gate-d-catalog-triplet.md (TODO)
tags: [kfm, promotion, gate-b, licensing, rights, governance]
notes:
  - Drafted from KFM vNext governance guidance; verify exact field names against repo schemas before enforcing in CI.
  - This checklist is fail-closed by design: unknown/unclear licensing blocks promotion.
[/KFM_META_BLOCK_V2] -->

# Gate B — Licensing & Rights Metadata (Schema Checklist)

![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Promotion Gate](https://img.shields.io/badge/promotion-gate%20B-blue)
![Domain](https://img.shields.io/badge/domain-licensing%20%26%20rights-orange)
![Policy](https://img.shields.io/badge/policy-public-brightgreen)
![CI](https://img.shields.io/badge/CI-TODO-lightgrey)

**One-line purpose:** Ensure every promoted dataset version has **explicit, enforceable licensing + rights metadata**, plus an immutable snapshot of upstream terms, so KFM can safely publish, export, and cite.

---

## Quick navigation

- [Purpose and scope](#purpose-and-scope)
- [Pass/fail criteria](#passfail-criteria)
- [Required artifacts](#required-artifacts)
- [Schema expectations](#schema-expectations)
- [Checklist](#checklist)
- [CI automation mapping](#ci-automation-mapping)
- [Steward review rubric](#steward-review-rubric)
- [Examples](#examples)
- [FAQ](#faq)

---

## Purpose and scope

**Gate B answers:** “Are we *allowed* to store, distribute, display, export, and publish this dataset version (and any included media) under clearly documented terms?”

This checklist applies to:
- Dataset registry entry (dataset-level license/rights)
- Dataset onboarding spec (upstream terms snapshot reference)
- Catalog surfaces (DCAT + STAC must carry license/rights consistently)
- Runtime obligations (exports and Story publishing must enforce rights)

> **NOTE**: Licensing is not paperwork — it is a policy input that affects what the system is permitted to serve.

### Where this doc fits in the repo

This file lives under:
- `docs/data/promotion/checklists/`

It is used by:
- CI promotion gates (automated checks)
- Human stewards during promotion PR review
- Developers writing ingestion + catalog builders

### Acceptable inputs

- License text and/or SPDX identifier from upstream publisher
- Rights holder identity (publisher/owner)
- Attribution requirements (how to cite)
- Distribution constraints (mirror vs metadata-only reference, no-derivatives, etc.)
- A captured snapshot of upstream terms at acquisition time

### Exclusions

- This checklist is **not legal advice**.
- Do **not** promote datasets where terms are unclear, contradictory, or missing.
- Do **not** “infer” a license from web availability or common practice.

---

## Pass/fail criteria

### PASS when all are true

- License is **explicit** (not “unknown”, not empty).
- Rights holder + attribution requirements are captured for **each distribution** (artifact class).
- Upstream terms are **snapshotted and immutable** (auditable).
- DCAT + STAC metadata includes license/rights consistently and validates under profile.
- Any “metadata-only reference” mode is explicit and enforced (no mirroring when disallowed).

### FAIL (block promotion) if any are true

- License is missing/unknown/unclear.
- Rights holder is missing for a distribution.
- Attribution requirements are missing or contradictory.
- Upstream terms snapshot is missing for the dataset version.
- Catalogs disagree about license/rights (registry ≠ DCAT ≠ STAC).
- Story publishing would include media with unclear rights.

> **WARNING**: Gate B is **fail-closed**. If licensing is unclear, the dataset stays in **QUARANTINE**.

---

## Required artifacts

| Artifact | Purpose | Must be immutable? | Notes |
|---|---|---:|---|
| Upstream terms snapshot | Evidence of licensing at time of acquisition | ✅ | HTML/PDF/text capture + digest |
| Dataset registry entry | Primary license/rights declaration used by KFM | ✅ (by version) | Field names must match repo schema |
| Onboarding spec section for terms | Links dataset version to upstream terms snapshot | ✅ | Include retrieved_at date |
| DCAT dataset record (+ distributions) | Dataset-level metadata: license/rights/distributions | ✅ | “What is this? who published it? what is license?” |
| STAC collection (and items if applicable) | Asset-level metadata including license | ✅ | Must link to DCAT |
| Run receipt / audit record | Captures policy decisions and artifacts used | ✅ append-only | Must include references/digests |

---

## Schema expectations

### 1) Registry expectations (dataset-level)

Minimum concept requirements (verify field names against the repo’s registry schema):
- `dataset_id`
- `publisher`
- `license` and/or `rights`
- attribution/citation instructions (field name TBD)
- upstream acquisition metadata including a `terms_snapshot` reference

### 2) Upstream terms snapshot expectations (RAW)

- Must be captured at acquisition time (not reconstructed later).
- Must be stored with a cryptographic digest.
- Must include a retrieval date/time and source URL (sanitized; no secrets).

### 3) DCAT expectations (dataset + distribution-level)

DCAT must carry:
- dataset license/rights at dataset level, and
- distribution information for each artifact class,
- plus any required attribution / rights notes (shape depends on DCAT profile).

### 4) STAC expectations (collections/items)

STAC must carry:
- `license` in the STAC Collection (at minimum),
- policy label + dataset version identifiers (as required by profile),
- links to the DCAT record (deterministic navigation).

### 5) Runtime enforcement expectations

- **Export functions** must attach attribution + license text automatically.
- **Story publishing** must block if rights are unclear for included media/attachments.
- **Metadata-only reference mode**: catalog is allowed without mirroring when rights disallow distribution.

---

## Checklist

### A. Pre-promotion (pipeline author / integrator)

- [ ] Identify the *authoritative* upstream publisher and canonical terms page/document.
- [ ] Capture and store an upstream **terms snapshot** (raw artifact + digest).
- [ ] Decide: **mirror allowed** vs **metadata-only reference** (document decision in spec).
- [ ] Record license as explicit value (prefer SPDX when applicable) and record rights holder.
- [ ] Record required attribution / citation wording (or pointer to it).

### B. Registry + spec schema checks

- [ ] Registry entry contains license/rights fields (non-empty, non-“unknown”).
- [ ] Registry entry captures publisher/rights holder identity.
- [ ] Onboarding spec contains `terms_snapshot` with `retrieved_at` (or equivalent).
- [ ] Terms snapshot artifact exists and matches referenced digest.

### C. Catalog checks (DCAT + STAC consistency)

- [ ] DCAT dataset record includes `license` or `rights`.
- [ ] DCAT has at least one distribution per artifact class (e.g., GeoParquet, PMTiles, COG).
- [ ] STAC Collection includes `license`.
- [ ] STAC links to DCAT (e.g., `rel="describedby"`).
- [ ] Any distribution-level rights constraints are reflected in runtime behavior (see below).

### D. Runtime enforcement checks (policy + UI/UX)

- [ ] Exports include license + attribution automatically.
- [ ] Story publishing gate blocks if rights unclear for any included media.
- [ ] If metadata-only reference mode is used:
  - [ ] No mirroring occurs (no download URLs to internal storage for disallowed artifacts)
  - [ ] UI indicates “reference-only” and disables export/download as required

### E. Promotion decision (steward sign-off)

- [ ] Steward confirms license/rights are compatible with intended publishing surface(s).
- [ ] Steward confirms attribution text is suitable and present.
- [ ] Steward confirms any restrictions (non-commercial, no-derivatives, embargo, etc.) are encoded as policy obligations (if applicable).
- [ ] Steward confirms Gate B evidence is attached/linked in the promotion PR.

---

## CI automation mapping

> Goal: Gate B should be machine-checkable and block merges on failure.

Recommended CI checks (names illustrative; map to actual workflow/jobs in repo):

1) `registry_schema_validate`
- Validate dataset registry entry schema.
- Assert license/rights required fields present and non-empty.

2) `terms_snapshot_present`
- Verify upstream terms snapshot artifact exists for the dataset version and digest matches.

3) `catalog_profile_validate`
- Validate DCAT profile shape and presence of license/rights fields.
- Validate STAC JSON schema and required `license` field in collection.

4) `license_consistency_check`
- Compare registry license/rights ↔ DCAT ↔ STAC for equality or documented inheritance rules.

5) `story_publish_rights_gate` (if Story Nodes are part of the PR)
- Fail if included media lacks clear rights metadata.

---

## Steward review rubric

Use this rubric during promotion PR review:

- **Clarity:** Are license + rights holder unambiguous?
- **Completeness:** Do we have attribution requirements and (if needed) distribution restrictions?
- **Evidence:** Do we have an immutable upstream terms snapshot?
- **Consistency:** Do registry, DCAT, and STAC agree?
- **Enforcement:** Do export + story publishing behaviors match rights constraints?

If any rubric category fails ⇒ **deny promotion** and send back to QUARANTINE.

---

## Examples

> These examples are illustrative; align field names and exact shapes with repo schemas/contracts.

### Example: onboarding spec terms_snapshot (snippet)

```yaml
upstream:
  cadence: monthly
  terms_snapshot:
    license: public_domain
    retrieved_at: "2026-02-20"
    # artifact_ref: "kfm://artifact/sha256:...."   # TODO: use actual evidence/artifact ref pattern
```

### Example: STAC collection license (snippet)

```json
{
  "type": "Collection",
  "id": "example_dataset_2026-02.abcd1234",
  "license": "public-domain",
  "links": [
    { "rel": "describedby", "href": "dcat://example_dataset@2026-02.abcd1234", "type": "application/ld+json" }
  ]
}
```

### Example: Evidence bundle includes license for UI display (snippet)

```json
{
  "bundle_id": "sha256:bundle...",
  "license": { "spdx": "CC-BY-4.0", "attribution": "Source org" }
}
```

---

## FAQ

### Why capture a terms snapshot instead of just storing a URL?
Because upstream pages change. Gate B requires an auditable, immutable basis for “what the terms were when we acquired/published.”

### What is “metadata-only reference” mode?
Catalog the dataset/version and point to an external distribution without mirroring it internally when rights do not allow redistribution.

### What if the license is missing but the data is publicly downloadable?
Fail closed. Online availability ≠ permission to reuse.

---

<details>
<summary>Appendix: Gate B to other gates (dependency note)</summary>

- Gate B feeds policy enforcement (exports, Story publish, UI badges).
- Gate D (Catalog triplet) depends on Gate B fields being present in DCAT/STAC.
- Gate F (policy tests / contract tests) should include fixtures for “rights unclear ⇒ deny”.

</details>

---

_Back to top:_ [↑](#gate-b--licensing--rights-metadata-schema-checklist)
