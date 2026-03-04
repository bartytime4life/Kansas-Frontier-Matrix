<!--
Template: Story Node v3 — Tombstone

- Intended use: copy/paste or include at the top of a Story Node v3 markdown file.
- Do NOT add a KFM MetaBlock here; the parent Story Node markdown file already contains one.
- Keep this section structured and brief. It is a reviewer/UI “facts box”.
-->

## Tombstone

_Key metadata, scope, governance posture, and publish gates for this Story Node._

| Field | Value |
|---|---|
| Story ID | `kfm://story/<uuid>` |
| Version ID | `<vN>` |
| Status | `<draft | pending | published | abstain | withdrawn>` |
| Review state | `<needs_review | in_review | approved | rejected>` |
| Policy label | `<public | restricted | …>` |
| Owners | `<team(s)/name(s)>` |
| Last updated | `<YYYY-MM-DD>` |

### Scope

| Field | Value |
|---|---|
| Geography (human) | `<County / Region / Route / Basin / …>` |
| Geography (bbox) | `<minLon, minLat, maxLon, maxLat>` |
| Time window | `<YYYY-MM-DD> → <YYYY-MM-DD>` |
| Map layers (layer_id → dataset_version_id) | `<layer_id>@<dataset_version_id>, …>` |

> If your story is **sensitive** (restricted sites, culturally sensitive topics, endangered species, etc.),
> **do not** publish precise locations or overly granular time windows. Fail closed and route to governance review.

### EvidenceRefs

> **Publish gate:** every citation must be an **EvidenceRef** and must resolve via `/api/v1/evidence/resolve`.
> Use EvidenceRefs (not raw URLs) everywhere you cite.

- Dataset (DCAT): `dcat://<dataset>@<dataset_version_id>`
- Dataset (STAC): `stac://<collection_or_item>@<dataset_version_id>`
- Provenance (PROV): `prov://run/<run_id>`
- Document: `doc://<doc_id>@<version>`
- Evidence bundle (OCI, if used): `oci:ghcr.io/<org>/kfm/evidence/<bundle>@sha256:<digest>`

### Claim posture inventory

Every *meaningful* claim must be explicitly labeled in the **Claims** section as one of:

- **CONFIRMED** — supported by resolvable evidence
- **PROPOSED** — interpretation/hypothesis; clearly labeled; still requires supporting citations
- **UNKNOWN** — not supported (do not publish as fact)

| Posture | Claim IDs |
|---|---|
| CONFIRMED | `<claim.001, claim.002>` |
| PROPOSED | `<claim.003>` |
| UNKNOWN | `<claim.004>` |

### Sensitivity and redaction

| Field | Value |
|---|---|
| Sensitivity | `<public | restricted | …>` |
| Redaction profile | `<public_default | public_generalized | …>` |
| Redaction receipt | `<audit/redaction_receipt.json>` |

### Publish checklist

- [ ] `review_state` captured (not blank)
- [ ] Every factual claim has ≥1 inline citation: `[CITATION: <ref>]`
- [ ] All citations resolve via `/api/v1/evidence/resolve`
- [ ] Rights/attribution recorded for any embedded media
- [ ] Sensitivity label and redaction profile are consistent; redaction receipt attached if needed
- [ ] If any box unchecked → set `status: abstain` and record missing receipts below

### Abstain / missing receipts

- **abstain_reason**
  - `<claim.002 missing EvidenceBundle>`
  - `<dataset catalog entry missing spec_hash>`
- **missing_receipts**
  - `<evidence/<bundle>/bundle.json>`
  - `<data/catalog/stac/items/...>`
- **next_actions**
  - `<Ingest missing source>`
  - `<Re-run transform and emit spec_hash + run_receipt>`
