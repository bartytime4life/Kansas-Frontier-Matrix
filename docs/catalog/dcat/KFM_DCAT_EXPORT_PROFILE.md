<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-NEEDS-UUID
title: KFM DCAT Export Profile
type: standard
version: v1
status: draft
owners: TODO
created: TODO
updated: 2026-04-27
policy_label: public
related: [
  docs/adr/ADR-PROV-STAC-DCAT-CATALOG-MAPPING.md,
  docs/catalog/stac/KFM_STAC_EXTENSION_PROFILE.md,
  contracts/v1/catalog/dcat/kfm_dcat_dataset.schema.json,
  contracts/v1/provenance/kfm_prov_sidecar.schema.json,
  contracts/v1/release/kfm_release_manifest.schema.json,
  tools/validators/catalog/validate_dcat_dataset.py,
  policy/catalog/dcat/dcat_dataset_gate.rego,
  tests/fixtures/catalog/dcat/valid/minimal.dataset.jsonld,
  tests/fixtures/catalog/dcat/invalid/restricted_access.dataset.jsonld,
  tests/fixtures/catalog/dcat/invalid/missing_provenance.dataset.jsonld
]
tags: [kfm, dcat, catalog, provenance, rights, access-rights, evidence, release-manifest, governance]
notes: [Defines KFM DCAT export rules for public-safe dataset discovery and rights propagation. doc_id, owners, created date, and final path need repository verification.]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KFM DCAT Export Profile

Public-safe DCAT export rules for KFM datasets, distributions, rights, provenance, release closure, and access posture.

<p align="center">
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Policy: public" src="https://img.shields.io/badge/policy-public-brightgreen">
  <img alt="Catalog: DCAT" src="https://img.shields.io/badge/catalog-DCAT-blue">
  <img alt="Repo verification needed" src="https://img.shields.io/badge/repo-NEEDS_VERIFICATION-orange">
</p>

---

## Impact block

| Field | Value |
| --- | --- |
| **Status** | `draft` |
| **Target path** | `docs/catalog/dcat/KFM_DCAT_EXPORT_PROFILE.md` |
| **Owners** | `TODO` |
| **Policy label** | `public` |
| **Primary schema** | `contracts/v1/catalog/dcat/kfm_dcat_dataset.schema.json` |
| **Validator** | `tools/validators/catalog/validate_dcat_dataset.py` |
| **Policy gate** | `policy/catalog/dcat/dcat_dataset_gate.rego` |
| **Truth posture** | CONFIRMED source-draft doctrine / PROPOSED validation contract / UNKNOWN mounted-repo enforcement |

> [!IMPORTANT]
> DCAT is a **public discovery/export layer**. It is not the KFM source of truth, not a substitute for STAC asset records, not a substitute for PROV lineage, and not an authorization bypass.

---

## Quick jump

- [Scope](#scope)
- [Repo fit](#repo-fit)
- [Export flow](#export-flow)
- [Core mapping](#core-mapping)
- [Field requirements](#field-requirements)
- [Allowed public values](#allowed-public-values)
- [Rules](#rules)
- [Examples](#examples)
- [Validation checklist](#validation-checklist)
- [Open verification items](#open-verification-items)

---

## Scope

This profile defines how KFM exports public catalog records into **DCAT-compatible JSON-LD** without losing:

- license posture
- access-rights posture
- provenance links
- `EvidenceBundle` lineage
- ReleaseManifest closure
- correction and supersession lineage
- sensitivity and geoprivacy constraints

A DCAT record is valid only when it describes **public-safe released or release-candidate scope** and traces back to governed KFM evidence.

### Exclusions

Do not export DCAT records that contain or point to:

- `RAW`, `WORK`, or `QUARANTINE` material
- restricted, denied, unknown, or TODO access posture
- unresolved rights or license terms
- exact sensitive geometry without a required redaction receipt
- unpublished candidate data presented as released truth
- direct model output without evidence and AI receipt linkage
- any distribution endpoint that is not public-safe

[Back to top](#top)

---

## Repo fit

| Concern | Expected KFM surface | Role |
| --- | --- | --- |
| This profile | `docs/catalog/dcat/KFM_DCAT_EXPORT_PROFILE.md` | Human-readable normative export rules. |
| STAC profile | `docs/catalog/stac/KFM_STAC_EXTENSION_PROFILE.md` | Spatial/temporal asset and item discovery companion. |
| PROV sidecar schema | `contracts/v1/provenance/kfm_prov_sidecar.schema.json` | Machine-readable provenance validation target. |
| DCAT schema | `contracts/v1/catalog/dcat/kfm_dcat_dataset.schema.json` | Machine-readable DCAT export contract. |
| DCAT validator | `tools/validators/catalog/validate_dcat_dataset.py` | Enforces schema and public-safe catalog rules. |
| DCAT policy gate | `policy/catalog/dcat/dcat_dataset_gate.rego` | Fails closed on unsafe export posture. |
| Release closure | `contracts/v1/release/kfm_release_manifest.schema.json` | Binds DCAT to artifact, evidence, PROV, STAC, and release state. |

> [!NOTE]
> Path placement and validator entrypoints are **NEEDS VERIFICATION** until checked against the mounted repository branch.

### Accepted inputs

A DCAT export may be emitted from records that have:

- resolved `EvidenceBundle`
- resolved ReleaseManifest reference
- resolved provenance sidecar
- known license and rights posture
- public-safe access posture
- review state sufficient for public discovery
- public-safe distribution targets

[Back to top](#top)

---

## Export flow

```mermaid
flowchart TD
    A[RAW] --> B[WORK / QUARANTINE]
    B --> C[PROCESSED]
    C --> D[EvidenceBundle]
    C --> E[STAC companion]
    C --> F[PROV sidecar]
    D --> G[ReleaseManifest]
    E --> H[Catalog closure check]
    F --> H
    G --> H
    H --> I{Policy + rights + sensitivity}
    I -- public-safe --> J[DCAT Dataset / Distribution]
    I -- unresolved / restricted --> K[ABSTAIN or DENY]
    J --> L[Governed public discovery]
```

The flow is intentionally asymmetric: DCAT receives released evidence and catalog closure; it does not create them.

[Back to top](#top)

---

## Core mapping

| KFM object or concept | DCAT / DCT carrier | Requirement |
| --- | --- | --- |
| Published dataset | `dcat:Dataset` | Required. |
| Public artifact or service | `dcat:Distribution` / `dcat:DataService` where applicable | At least one public-safe distribution is required. |
| License | `dct:license` | Required; must not be `TODO` or unknown. |
| Access posture | `dct:accessRights` | Required; must be `public`. |
| Evidence reference | `dct:source` and/or `kfm:evidence_ref` | Required through KFM extension field. |
| Provenance sidecar | `dct:provenance` | Required and resolvable. |
| Release manifest | `kfm:release_manifest_ref` | Required. |
| Correction lineage | `dct:isReplacedBy` / `dct:replaces` | Required when superseded or replacing another record. |
| AI interpretation receipt | `kfm:ai_receipt_ref` | Conditional; required when AI contributed interpretation. |
| Redaction receipt | `kfm:redaction_receipt_ref` | Conditional; required after geoprivacy or sensitivity transform. |

[Back to top](#top)

---

## Field requirements

### Required dataset fields

| Field | Required | Description | Export check |
| --- | --- | --- | --- |
| `@context` | yes | JSON-LD context containing `dcat`, `dct`, and `kfm`. | Must parse as JSON-LD context. |
| `@type` | yes | Must be `dcat:Dataset`. | Exact value required. |
| `dct:title` | yes | Human-readable dataset title. | Must be non-empty. |
| `dct:identifier` | yes | Stable KFM dataset identifier. | Must be non-empty. |
| `dct:license` | yes | License URI. | Must be known and non-blocked. |
| `dct:accessRights` | yes | Access-rights value. | Must be `public`. |
| `dct:provenance` | yes | PROV sidecar reference. | Must resolve and validate. |
| `dcat:distribution` | yes | Public-safe distribution list. | Must contain at least one distribution. |

### Required KFM extension fields

| Field | Required | Description | Export check |
| --- | --- | --- | --- |
| `kfm:spec_hash` | yes | Deterministic identity / export-spec hash. | Must match `sha256:<64 hex>`. |
| `kfm:evidence_ref` | yes | `EvidenceBundle` reference. | Must resolve before public export. |
| `kfm:run_receipt_ref` | recommended | Run receipt reference. | Required when release policy requires run closure. |
| `kfm:release_manifest_ref` | yes | ReleaseManifest reference. | Must resolve before public export. |
| `kfm:policy_label` | yes | Publication policy label. | Must be `public`. |
| `kfm:review_state` | yes | Review state at export. | Must be `reviewed` or `published`. |
| `kfm:source_role` | yes | Source role used for the exported claim or dataset. | Must not be unknown where source authority matters. |
| `kfm:sensitivity` | recommended | Sensitivity posture. | Must be `public` when present. |
| `kfm:redaction_receipt_ref` | conditional | Required after geoprivacy or sensitivity transform. | Must resolve when transform occurred. |
| `kfm:ai_receipt_ref` | conditional | Required when AI contributed interpretation. | Must resolve when AI contributed text or interpretation. |

### Required distribution fields

| Field | Required | Description | Export check |
| --- | --- | --- | --- |
| `@type` | yes | Must be `dcat:Distribution`. | Exact value required. |
| `dcat:accessURL` | yes | Public-safe artifact URL, landing page, service endpoint, or mediated access point. | Must not point to RAW, WORK, QUARANTINE, restricted stores, or internal-only paths. |
| `dcat:downloadURL` | conditional | Direct downloadable artifact URL. | Use only when the target is actually downloadable. |
| `dct:license` | yes | Distribution license URI. | Must match dataset license unless reviewed exception is modeled. |
| `dcat:mediaType` | recommended | Media type for the distribution. | Prefer when known. |
| `dct:format` | recommended | Format label or URI. | Use when helpful for discovery. |
| `dct:conformsTo` | recommended | STAC / schema / profile reference. | Recommended for validator and consumer clarity. |

> [!TIP]
> Use `dcat:downloadURL` for a direct file download. Use `dcat:accessURL` for a landing page, service, API endpoint, viewer, or mediated access surface.

[Back to top](#top)

---

## Allowed public values

`kfm:policy_label` **MUST** be:

```text
public
```

`dct:accessRights` **MUST** be:

```text
public
```

Allowed review states:

```text
reviewed
published
```

The following values **MUST NOT** appear in a published DCAT export:

```text
restricted
deny
TODO
todo
unknown
UNKNOWN
NEEDS-VERIFICATION
```

A record with a public `kfm:policy_label` but restricted or unknown `dct:accessRights` is invalid.

[Back to top](#top)

---

## Rules

### Rights rules

DCAT export **MUST fail closed** when:

- `dct:license` is missing
- `dct:license` is `TODO`, unknown, restricted, denied, or empty
- rights are unknown
- access posture is missing
- access posture conflicts with public export
- a distribution license conflicts with the dataset license without a modeled reviewed exception
- a distribution URL points to material whose release rights are not public-safe

### Sensitivity rules

DCAT export **MUST fail closed** when:

- `dct:accessRights` is missing
- `dct:accessRights` is `restricted`, `deny`, `unknown`, or `TODO`
- public distribution points to restricted material
- precise sensitive geometry is exposed
- a required redaction receipt is missing
- a public record would reveal steward-controlled, culturally sensitive, living-person, DNA, protected-species, archaeological, critical-infrastructure, or other sensitive detail without policy clearance

### Provenance rules

DCAT export **MUST** include a resolvable provenance pointer:

```json
{
  "dct:provenance": "https://catalog.example.invalid/prov/artifact.prov.jsonld"
}
```

The referenced provenance sidecar must validate against:

```text
contracts/v1/provenance/kfm_prov_sidecar.schema.json
```

### Catalog closure rules

A DCAT export is valid only when all of the following resolve or are explicitly marked not applicable by policy:

- `EvidenceBundle`
- ReleaseManifest
- provenance sidecar
- public artifact or mediated access surface
- rights and license posture
- sensitivity/public-safety posture
- STAC companion record where spatial/temporal asset discovery exists
- correction lineage when superseded, withdrawn, or replacing another record

### STAC / DCAT / PROV cross-link rules

| Link direction | Preferred carrier | Requirement |
| --- | --- | --- |
| DCAT → STAC | `dct:relation` or `dct:conformsTo` | Include when a STAC collection/item is the asset companion. |
| DCAT → PROV | `dct:provenance` | Required for lineage. |
| DCAT → ReleaseManifest | `kfm:release_manifest_ref` and/or `dct:relation` | Required for release closure. |
| STAC → DCAT | STAC `links[]` with `rel: describedby` | Recommended for companion navigability. |
| PROV → DCAT/STAC | PROV entity/activity references | Recommended for replayable closure. |

### Correction lineage rules

When a dataset supersedes another dataset, include only the applicable direction:

```json
{
  "dct:replaces": "kfm://dataset/previous"
}
```

or:

```json
{
  "dct:isReplacedBy": "kfm://dataset/newer"
}
```

Do not erase old outward discovery records merely because a newer release exists. Mark the old record’s status and link it forward.

### Public UI and runtime rules

The public UI may use DCAT records for discovery, but **MUST NOT** treat DCAT as source truth.

For claim-level answers, UI and runtime systems must resolve:

```text
DCAT → STAC → EvidenceBundle → receipts/proofs
```

Missing evidence produces:

```text
ABSTAIN
```

Policy denial produces:

```text
DENY
```

[Back to top](#top)

---

## Examples

### Minimal public-safe DCAT example

```json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "kfm": "https://kfm.local/ns#",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@type": "dcat:Dataset",
  "dct:title": "KFM Minimal Public Dataset Fixture",
  "dct:description": "Valid minimal DCAT dataset for CI validation.",
  "dct:identifier": "kfm://dataset/minimal-fixture",
  "dct:license": "https://spdx.org/licenses/CC-BY-4.0.html",
  "dct:accessRights": "public",
  "dct:provenance": "https://example.invalid/artifact.prov.jsonld",
  "dct:issued": "2026-04-27T00:00:00Z",
  "dct:modified": "2026-04-27T00:00:00Z",
  "kfm:spec_hash": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "kfm:evidence_ref": "kfm://evidence/minimal-fixture",
  "kfm:run_receipt_ref": "kfm://receipt/run/minimal-fixture",
  "kfm:release_manifest_ref": "kfm://release/minimal-fixture",
  "kfm:policy_label": "public",
  "kfm:review_state": "reviewed",
  "kfm:source_role": "authoritative_source",
  "kfm:sensitivity": "public",
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dcat:accessURL": "https://example.invalid/artifact.ext",
      "dct:license": "https://spdx.org/licenses/CC-BY-4.0.html",
      "dct:format": "application/octet-stream",
      "dct:conformsTo": "docs/catalog/stac/KFM_STAC_EXTENSION_PROFILE.md"
    }
  ]
}
```

### Common invalid patterns

| Anti-pattern | Why it fails |
| --- | --- |
| `kfm:policy_label: restricted` | Published DCAT export is public-only. |
| Missing `dct:license` | Rights posture cannot be reviewed or discovered safely. |
| `dct:accessRights: unknown` | KFM must fail closed when access posture is unresolved. |
| Distribution points to `RAW` / `WORK` / `QUARANTINE` | Public discovery would bypass the governed lifecycle. |
| AI-written description without `kfm:ai_receipt_ref` | Generated interpretation would be detached from audit evidence. |
| Precise sensitive geometry without `kfm:redaction_receipt_ref` | Public release would lack transform proof. |
| Superseded record with no correction lineage | Discovery would erase replacement history. |
| Distribution license differs from dataset license | Rights posture is inconsistent without an explicit reviewed exception. |

[Back to top](#top)

---

## Validation checklist

Before publishing a DCAT export, verify:

- [ ] JSON parses.
- [ ] JSON-LD context includes expected prefixes.
- [ ] `@type` is `dcat:Dataset`.
- [ ] `dct:identifier` exists.
- [ ] `dct:title` exists.
- [ ] `dct:license` exists and is not `TODO` or unknown.
- [ ] `dct:accessRights` is `public`.
- [ ] `dct:provenance` resolves.
- [ ] PROV sidecar validates against `contracts/v1/provenance/kfm_prov_sidecar.schema.json`.
- [ ] `kfm:spec_hash` is valid.
- [ ] `kfm:evidence_ref` resolves.
- [ ] `kfm:release_manifest_ref` resolves.
- [ ] `kfm:policy_label` is `public`.
- [ ] `kfm:review_state` is `reviewed` or `published`.
- [ ] `kfm:sensitivity` is `public` when present.
- [ ] At least one distribution exists.
- [ ] All distribution URLs are public-safe.
- [ ] No `RAW`, `WORK`, or `QUARANTINE` references appear in outward records.
- [ ] Distribution license matches dataset license unless reviewed exception is modeled.
- [ ] Redaction receipt exists when sensitivity transform occurred.
- [ ] AI receipt exists when AI contributed interpretation.
- [ ] STAC / DCAT / PROV / release links agree on stable identifiers.
- [ ] Correction lineage is present when superseded, withdrawn, or replacing another record.

### Definition of done

A DCAT export profile change is ready for review when it is:

- evidence-grounded
- public-safe
- release-linked
- link-resolvable
- rights-explicit
- sensitivity-aware
- correction-preserving
- honest about remaining **UNKNOWN** or **NEEDS VERIFICATION** items

[Back to top](#top)

---

## Open verification items

<details>
<summary><strong>Items to verify before claiming enforcement</strong></summary>

- Final `doc_id`, `owners`, and `created` metadata values.
- Whether `contracts/v1/catalog/dcat/kfm_dcat_dataset.schema.json` is the exact current mounted schema path.
- Whether `contracts/v1/provenance/kfm_prov_sidecar.schema.json` is the exact current mounted provenance schema path.
- Exact controlled enum or URI set for `dct:accessRights`.
- Exact current validator entrypoint for DCAT JSON-LD.
- Whether `data/catalog/dcat/` or another path is the active emitted payload home on the target branch.
- Whether catalog closure is represented by `CatalogMatrix`, `ReleaseManifest`, proof pack, or another current contract name.
- Whether external public namespace for `kfm:` should remain `https://kfm.local/ns#` or be replaced before public release.

</details>

[Back to top](#top)
