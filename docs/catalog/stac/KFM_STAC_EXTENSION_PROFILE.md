<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-NEEDS-UUID
title: KFM STAC Extension Profile
type: standard
version: v1
status: draft
owners: TODO
created: TODO
updated: 2026-04-27
policy_label: public
related: [
  docs/adr/ADR-PROV-STAC-DCAT-CATALOG-MAPPING.md,
  docs/catalog/dcat/KFM_DCAT_EXPORT_PROFILE.md,
  contracts/v1/catalog/stac/kfm_stac_item.schema.json,
  contracts/v1/provenance/kfm_prov_sidecar.schema.json,
  contracts/v1/release/kfm_release_manifest.schema.json,
  tools/validators/catalog/validate_stac_item.py,
  policy/catalog/stac/stac_item_gate.rego,
  tests/fixtures/catalog/stac/valid/minimal.item.json,
  tests/fixtures/catalog/stac/invalid/missing_evidence_ref.item.json,
  tests/fixtures/catalog/stac/invalid/restricted_policy_label.item.json,
  tests/fixtures/catalog/stac/invalid/missing_provenance_asset.item.json
]
tags: [kfm, stac, catalog, provenance, evidence, receipts, release-manifest, governance]
notes: [Defines KFM-specific STAC fields and links for public-safe catalog artifacts. doc_id, owners, created date, and final path need repository verification.]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KFM STAC Extension Profile

KFM-specific STAC fields for evidence-bound, provenance-linked, public-safe catalog exports.

<p align="center">
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Policy: public" src="https://img.shields.io/badge/policy-public-brightgreen">
  <img alt="Catalog: STAC" src="https://img.shields.io/badge/catalog-STAC-blue">
  <img alt="Repo verification needed" src="https://img.shields.io/badge/repo-NEEDS_VERIFICATION-orange">
</p>

---

## Impact block

| Field | Value |
| --- | --- |
| **Status** | `draft` |
| **Target path** | `docs/catalog/stac/KFM_STAC_EXTENSION_PROFILE.md` |
| **Owners** | `TODO` |
| **Policy label** | `public` |
| **Primary schema** | `contracts/v1/catalog/stac/kfm_stac_item.schema.json` |
| **Validator** | `tools/validators/catalog/validate_stac_item.py` |
| **Policy gate** | `policy/catalog/stac/stac_item_gate.rego` |

> [!IMPORTANT]
> STAC is a discovery layer. It is **not** the source of truth. Public STAC records must resolve to EvidenceBundle, provenance, policy, release, and correction state before they support consequential UI or Focus Mode behavior.

---

## Quick jump

- [Purpose](#purpose)
- [Repo fit](#repo-fit)
- [Scope](#scope)
- [Required KFM properties](#required-kfm-properties)
- [Allowed public values](#allowed-public-values)
- [Required processing properties](#required-processing-properties)
- [Required links](#required-links)
- [Required assets](#required-assets)
- [Minimal STAC Item example](#minimal-stac-item-example)
- [Publication rules](#publication-rules)
- [Evidence Drawer impact](#evidence-drawer-impact)
- [Focus Mode rules](#focus-mode-rules)
- [Validation checklist](#validation-checklist)
- [Open verification items](#open-verification-items)

---

## Purpose

This profile defines how KFM publishes STAC Items and Collections without losing:

- deterministic identity
- EvidenceBundle lineage
- run receipts
- redaction receipts
- AI receipts
- attestation links
- rights and sensitivity posture
- release-manifest closure

A STAC record may make an artifact discoverable. It must never become the proof that the artifact is publishable.

[Back to top](#top)

---

## Repo fit

| Surface | Proposed path | Role |
| --- | --- | --- |
| STAC profile doc | `docs/catalog/stac/KFM_STAC_EXTENSION_PROFILE.md` | Human-readable STAC publication profile. |
| STAC schema | `contracts/v1/catalog/stac/kfm_stac_item.schema.json` | Machine-readable shape for KFM STAC Items. |
| STAC validator | `tools/validators/catalog/validate_stac_item.py` | Enforces schema and KFM publication rules. |
| STAC policy | `policy/catalog/stac/stac_item_gate.rego` | Denies unsafe public catalog records. |
| Valid fixture | `tests/fixtures/catalog/stac/valid/minimal.item.json` | Positive-path public-safe example. |
| Invalid fixtures | `tests/fixtures/catalog/stac/invalid/*.item.json` | Negative-path gates for missing evidence, restricted policy, and missing provenance asset. |

> [!NOTE]
> Paths are **PROPOSED** until confirmed in a mounted repository checkout.

[Back to top](#top)

---

## Scope

### In scope

- Public-safe STAC Items and Collections.
- KFM `kfm:*` extension fields required for governance.
- Links to EvidenceBundle, PROV sidecar, and ReleaseManifest.
- Asset requirements for data and provenance.
- Publication denial rules for missing evidence, missing provenance, restricted policy labels, or restricted/internal references.

### Exclusions

- RAW, WORK, QUARANTINE, or candidate-only material.
- Restricted coordinates in public STAC geometry, properties, links, or assets.
- Direct model output or AI-generated prose as source truth.
- Treating STAC as a replacement for EvidenceBundle, ReleaseManifest, review record, or policy decision.

[Back to top](#top)

---

## Required KFM properties

| Property | Required | Type | Description |
| --- | --- | --- | --- |
| `kfm:spec_hash` | yes | string | Canonical deterministic artifact/spec identity. |
| `kfm:content_spec_hash` | recommended | string | Content-level deterministic identity when distinct from `spec_hash`. |
| `kfm:geometry_hash` | conditional | string | Required when geometry identity matters. |
| `kfm:evidence_ref` | yes | string | Reference to the governing EvidenceBundle. |
| `kfm:run_receipt_url` | yes | string | URL or repo path to the run/provenance record. |
| `kfm:release_manifest_ref` | yes | string | ReleaseManifest reference. |
| `kfm:policy_label` | yes | string | Public policy posture. |
| `kfm:review_state` | yes | string | Review state at publication. |
| `kfm:source_role` | yes | string | Role of the underlying source. |
| `kfm:sensitivity` | recommended | string | Must be `public` when present in public STAC. |
| `kfm:source_descriptor_ref` | recommended | string | SourceDescriptor reference. |
| `kfm:redaction_receipt_url` | conditional | string | Required when geometry or fields were transformed. |
| `kfm:ai_receipt_url` | conditional | string | Required when AI contributed interpretation. |
| `kfm:attestation_url` | conditional | string | Required when release policy requires attestation. |
| `kfm:correction_ref` | conditional | string | Required when corrected, superseded, or withdrawn state exists. |

[Back to top](#top)

---

## Allowed public values

For public STAC publication:

```text
kfm:policy_label = public
kfm:sensitivity  = public
```

Allowed review states:

```text
reviewed
published
```

The following values **MUST NOT** appear in a published public STAC record:

```text
TODO
unknown
UNKNOWN
NEEDS-VERIFICATION
restricted
deny
```

[Back to top](#top)

---

## Required processing properties

| Property | Required | Description |
| --- | --- | --- |
| `processing:software` | yes | Pipeline or tool name. |
| `processing:version` | yes | Pipeline or tool version. |
| `processing:datetime` | yes | Run timestamp in date-time format. |
| `datetime` | recommended | STAC temporal timestamp where applicable. |
| `start_datetime` | conditional | Required for interval assets when `datetime` is not sufficient. |
| `end_datetime` | conditional | Required for interval assets when `datetime` is not sufficient. |

[Back to top](#top)

---

## Required links

| `rel` | Required | Target |
| --- | --- | --- |
| `provenance` | yes | PROV JSON-LD sidecar. |
| `evidence` | yes | EvidenceBundle. |
| `release-manifest` | yes | ReleaseManifest. |
| `attestation` | conditional | DSSE/Cosign or other attestation bundle. |
| `redaction-receipt` | conditional | Redaction or geoprivacy transform receipt. |
| `ai-receipt` | conditional | AI interpretive receipt. |
| `correction` | conditional | Correction notice. |
| `supersedes` | conditional | Prior released object. |

[Back to top](#top)

---

## Required assets

At minimum, a published STAC Item SHOULD contain both `data` and `provenance` assets:

```json
{
  "assets": {
    "data": {
      "href": "https://example.invalid/artifact.ext",
      "type": "application/octet-stream",
      "roles": ["data"]
    },
    "provenance": {
      "href": "https://example.invalid/artifact.prov.jsonld",
      "type": "application/ld+json",
      "roles": ["metadata", "provenance"]
    }
  }
}
```

> [!IMPORTANT]
> A `links[rel=provenance]` entry is not enough by itself when KFM requires materialized provenance for Evidence Drawer, offline validation, or release closure. The `assets.provenance` entry must also exist.

When attestation is required:

```json
{
  "assets": {
    "attestation": {
      "href": "https://example.invalid/artifact.bundle.json",
      "type": "application/json",
      "roles": ["metadata", "attestation"]
    }
  }
}
```

[Back to top](#top)

---

## Minimal STAC Item example

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "kfm-item-minimal-fixture",
  "collection": "kfm-collection-minimal-fixture",
  "bbox": [-102.051744, 36.993016, -94.588413, 40.003162],
  "geometry": null,
  "properties": {
    "datetime": "2026-04-27T00:00:00Z",
    "kfm:spec_hash": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "kfm:content_spec_hash": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "kfm:evidence_ref": "kfm://evidence/minimal-fixture",
    "kfm:run_receipt_url": "https://example.invalid/artifact.prov.jsonld",
    "kfm:release_manifest_ref": "kfm://release/minimal-fixture",
    "kfm:policy_label": "public",
    "kfm:review_state": "reviewed",
    "kfm:source_role": "authoritative_source",
    "kfm:sensitivity": "public",
    "kfm:source_descriptor_ref": "kfm://source/minimal-fixture",
    "processing:software": "kfm-pipeline",
    "processing:version": "v1",
    "processing:datetime": "2026-04-27T00:00:00Z"
  },
  "links": [
    {
      "rel": "provenance",
      "href": "https://example.invalid/artifact.prov.jsonld",
      "type": "application/ld+json",
      "title": "KFM PROV sidecar"
    },
    {
      "rel": "evidence",
      "href": "https://example.invalid/evidence.json",
      "type": "application/json",
      "title": "KFM EvidenceBundle"
    },
    {
      "rel": "release-manifest",
      "href": "https://example.invalid/release-manifest.json",
      "type": "application/json",
      "title": "KFM ReleaseManifest"
    }
  ],
  "assets": {
    "data": {
      "href": "https://example.invalid/artifact.ext",
      "type": "application/octet-stream",
      "title": "Minimal fixture artifact",
      "roles": ["data"],
      "kfm:spec_hash": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "kfm:provenance_ref": "https://example.invalid/artifact.prov.jsonld"
    },
    "provenance": {
      "href": "https://example.invalid/artifact.prov.jsonld",
      "type": "application/ld+json",
      "title": "KFM PROV sidecar",
      "roles": ["metadata", "provenance"],
      "kfm:provenance_ref": "https://example.invalid/artifact.prov.jsonld"
    }
  }
}
```

[Back to top](#top)

---

## Publication rules

A STAC Item MUST NOT publish when:

- `kfm:policy_label` is not `public`
- `kfm:sensitivity` is present and not `public`
- `kfm:review_state` is not `reviewed` or `published`
- `kfm:spec_hash` is missing or malformed
- `kfm:evidence_ref` is missing
- `kfm:run_receipt_url` is missing
- `kfm:release_manifest_ref` is missing
- `links[rel=provenance]` is missing
- `links[rel=evidence]` is missing
- `links[rel=release-manifest]` is missing
- `assets.data` is missing
- `assets.provenance` is missing
- redaction was performed but no redaction receipt is linked
- AI interpretation was used but no AI receipt is linked
- attestation is declared but no attestation link exists
- source rights are unknown
- public record references RAW / WORK / QUARANTINE material
- exact sensitive geometry or restricted fields appear in public output

[Back to top](#top)

---

## Evidence Drawer impact

Public UI may derive Evidence Drawer metadata from STAC only when all linked governance records resolve.

| UI field | Source |
| --- | --- |
| Evidence reference | `properties.kfm:evidence_ref` |
| Spec hash | `properties.kfm:spec_hash` |
| Review state | `properties.kfm:review_state` |
| Source role | `properties.kfm:source_role` |
| Provenance | `links[rel=provenance]` and `assets.provenance` |
| Release manifest | `links[rel=release-manifest]` |
| Redaction receipt | `links[rel=redaction-receipt]` |
| Correction notice | `links[rel=correction]` |

[Back to top](#top)

---

## Focus Mode rules

Focus Mode MUST only consume STAC records that are:

- public-safe
- released or reviewed for release
- evidence-bound
- provenance-linked
- release-manifest-linked
- policy-allowed

Missing evidence produces:

```text
ABSTAIN
```

Policy denial produces:

```text
DENY
```

Validation/runtime failure produces:

```text
ERROR
```

[Back to top](#top)

---

## Validation checklist

- [ ] STAC JSON parses.
- [ ] Required `kfm:*` fields exist.
- [ ] `kfm:spec_hash` matches `sha256:<64 hex>`.
- [ ] `kfm:policy_label` is `public`.
- [ ] `kfm:sensitivity` is `public` when present.
- [ ] `kfm:review_state` is `reviewed` or `published`.
- [ ] Evidence reference exists.
- [ ] Provenance link exists.
- [ ] Provenance asset exists.
- [ ] ReleaseManifest reference exists.
- [ ] Data asset exists.
- [ ] Redaction receipt exists when needed.
- [ ] AI receipt exists when needed.
- [ ] Attestation exists when required.
- [ ] No restricted geometry leak.
- [ ] No RAW / WORK / QUARANTINE references.

[Back to top](#top)

---

## Open verification items

| Item | Status | Needed action |
| --- | --- | --- |
| `doc_id` | NEEDS VERIFICATION | Replace placeholder with registry-approved ID. |
| Owners | NEEDS VERIFICATION | Confirm owning team or maintainers. |
| Created date | NEEDS VERIFICATION | Confirm from repository history. |
| Target path | PROPOSED | Confirm final docs location. |
| Schema path | PROPOSED | Confirm contract/schema home. |
| STAC extension URI | NEEDS VERIFICATION | Decide official URI if publishing as formal STAC extension. |
| Link relation names | PROPOSED | Confirm `provenance`, `evidence`, and `release-manifest` conventions. |
| Public sensitivity vocabulary | NEEDS VERIFICATION | Align with KFM policy registry. |

[Back to top](#top)
