# KFM Sample Dataset
Tiny, policy-safe fixture dataset + catalogs used to validate the Kansas Frontier Matrix (KFM) end-to-end (promotion → governed API → Map/Story/Focus).

`status: draft` `policy_label: public` `scope: examples` `intent: CI + e2e fixture`

**This folder is a contract.** It defines the *minimum* set of artifacts and linkages needed to prove that:
- versioning is deterministic,
- catalogs are valid and cross-linked,
- evidence resolves (or fails closed) without leaking sensitive details,
- policy gates are enforceable.

## Quick navigation
- [What this fixture is for](#what-this-fixture-is-for)
- [Directory layout](#directory-layout)
- [What done looks like](#what-done-looks-like)
- [Data model](#data-model)
- [Identity, versioning, and checksums](#identity-versioning-and-checksums)
- [Catalog triplet and cross-links](#catalog-triplet-and-cross-links)
- [Evidence and citations](#evidence-and-citations)
- [How to use in local dev and CI](#how-to-use-in-local-dev-and-ci)
- [Safety and governance](#safety-and-governance)
- [Troubleshooting](#troubleshooting)

---

## What this fixture is for

### Primary goals
1. **Deterministic promotion:** prove that the same spec always yields the same `spec_hash` and `dataset_version_id`.
2. **Catalog interoperability:** provide a small but complete DCAT + STAC + PROV “triplet”.
3. **Evidence-led UX:** include at least one resolvable EvidenceRef so the UI can open an evidence drawer for a feature/claim.
4. **Policy enforcement:** ensure “default deny” behavior is testable (especially around evidence + restricted references).

### End-to-end surfaces this fixture should exercise
| Surface | What we validate with this fixture |
|---|---|
| Data zones | Raw → Work/QA → Processed → Catalog triplet → Published surfaces |
| Validators | Schema checks + link checks + deterministic hashing |
| Governed API | Dataset discovery + STAC queries + evidence resolution |
| Map Explorer | Load a layer and inspect a feature’s evidence |
| Story | (Optional) block publishing if any citation fails to resolve |
| Focus | (Optional) cite-or-abstain behavior using the same evidence graph |

### Minimal pipeline shape
~~~mermaid
flowchart LR
  A[Spec and fixture input] --> B[Normalize and QA]
  B --> C[Processed artifacts]
  C --> D[Catalog triplet]
  D --> E[Promotion manifest and run receipt]
  E --> F[Governed API]
  F --> G[Map Story Focus]
~~~

> WARNING  
> This folder should not become a dumping ground. Keep the fixture **small, fast, and safe**. If you need real data, keep it out of `examples/` and follow the governed promotion path.

[Back to top](#kfm-sample-dataset)

---

## Directory layout

### Target layout
This README does **not** assume every file exists yet. It defines what *should* exist for the fixture to be considered “done”.

~~~text
examples/sample_dataset/
  README.md

  spec/
    dataset_spec.json                 # canonical input to spec_hash

  raw/
    acquisition_manifest.json         # where fixture data came from (even if synthetic)
    fixtures/
      upstream.csv                    # tiny fixture input (or geojson, etc.)
    checksums.sha256                  # digests for raw artifacts

  work/
    normalized.parquet                # optional intermediate
    qa_report.json                    # optional but recommended

  processed/
    features.parquet                  # GeoParquet/Parquet feature layer
    tiles/
      features.pmtiles                # optional PMTiles bundle for UI smoke tests
    checksums.sha256                  # digests for processed artifacts

  catalog/
    dcat.jsonld                       # dataset-level metadata
    stac/
      collection.json                 # STAC collection describing assets
      items/
        features.json                 # STAC item (or items) referencing assets + time/space
    prov.jsonld                       # lineage for this dataset_version

  receipts/
    run_receipt.json                  # run_record for pipeline execution
    promotion_manifest.json           # promotion manifest for this dataset_version
~~~

### Required vs optional artifacts
| Path | Required | Purpose |
|---|:---:|---|
| `spec/dataset_spec.json` | ✅ | Canonical input for deterministic `spec_hash` and `dataset_version_id`. |
| `raw/fixtures/*` | ✅ | Minimal fixture input. Keep it tiny. |
| `processed/features.parquet` | ✅ | The processed artifact exercised by validators, APIs, and UI. |
| `catalog/dcat.jsonld` | ✅ | Dataset discovery + rights + distribution metadata. |
| `catalog/stac/collection.json` | ✅ | Spatial/temporal discovery + asset catalog. |
| `catalog/prov.jsonld` | ✅ | Lineage and reproducibility (what generated what). |
| `receipts/run_receipt.json` | ✅ | Audit record for the run (inputs, outputs, digests). |
| `receipts/promotion_manifest.json` | ✅ | Release/promotion summary tying artifacts + catalogs + approvals. |
| `work/qa_report.json` | ◻︎ | Machine-readable QA metrics linked from run receipt. |
| `processed/tiles/*.pmtiles` | ◻︎ | Optional fast UI smoke test layer; keep public-safe. |

[Back to top](#kfm-sample-dataset)

---

## What done looks like

A PR that updates this fixture should be mergeable only if:

- [ ] **Identity & versioning**: `spec_hash` is deterministic and recorded; `dataset_version_id` matches expectations.
- [ ] **Artifacts**: processed artifacts exist and have SHA-256 digests; paths are predictable.
- [ ] **Catalogs**: DCAT/STAC/PROV validate under the KFM profiles.
- [ ] **Cross-links**: links resolve locally (repo context); no dangling hrefs.
- [ ] **Policy**: a `policy_label` is assigned; obligations (if any) are recorded; default-deny behavior is testable.
- [ ] **QA**: a QA report exists or validation results are captured; failures quarantine instead of publishing.
- [ ] **Audit**: a run receipt exists and references inputs/outputs by digest; promotion manifest exists.

[Back to top](#kfm-sample-dataset)

---

## Data model

This fixture is intentionally minimal, but it should still be *representative*.

### Required feature-level fields
If `processed/features.parquet` is a vector layer, include (at minimum):

| Field | Required | Notes |
|---|:---:|---|
| `feature_id` | ✅ | Stable per feature. Used by Map/Story/Focus to reference the same feature over time. |
| `geometry` | ✅ | Must be policy-consistent (generalized if required). |
| `datetime` **or** `start_datetime` + `end_datetime` | ✅ | Enables time filtering and story time windows. |
| `policy_label` | ✅ | Access classification for the feature or row group. |
| `evidence_ref` | ✅ | EvidenceRef used by the evidence resolver to return an EvidenceBundle. |
| `upstream_id` | ◻︎ | Useful for debugging normalization; optional for synthetic fixtures. |
| `title` or `label` | ◻︎ | Human-friendly label for UI. |

### STAC item minimums
For `catalog/stac/items/*.json`, ensure each item has:
- `id`
- `geometry` **or** `bbox` (consistent with policy label)
- `datetime` **or** `start_datetime`/`end_datetime`
- `assets` with `href` + `checksum` + `media_type`
- links to PROV/run receipt and DCAT distribution

[Back to top](#kfm-sample-dataset)

---

## Identity, versioning, and checksums

### Deterministic IDs
This fixture should model KFM’s deterministic versioning rules:

- `spec_hash` is computed from the **canonical** dataset spec (preferred: JSON).
- `dataset_version_id` is derived from `spec_hash` (example format: `YYYY-MM.<first8(spec_hash)>`).

> TIP  
> Treat `spec/dataset_spec.json` as a *build contract* (not a narrative). Small changes should produce a new version, predictably.

### Checksums
- Every artifact referenced by catalogs or receipts should have a SHA-256 digest.
- Keep checksum lists adjacent to the artifacts (e.g., `raw/checksums.sha256`, `processed/checksums.sha256`).

[Back to top](#kfm-sample-dataset)

---

## Catalog triplet and cross-links

KFM relies on a “catalog triplet” pattern:

- **DCAT**: dataset-level metadata (title, description, license, distributions).
- **STAC**: asset-level metadata (spatiotemporal indexing + explicit assets).
- **PROV**: lineage (what activities and inputs produced what artifacts).

### Cross-link checklist
Make navigation deterministic by including explicit links:

- DCAT dataset → distributions → artifact digests
- DCAT dataset → PROV bundle (lineage)
- STAC collection → link `rel="describedby"` → DCAT dataset
- STAC item → link to PROV activity and/or run receipt
- EvidenceRefs resolve into these objects **without guessing**

### Cross-link matrix
| From | To | How |
|---|---|---|
| DCAT dataset | STAC collection | DCAT distribution or `related`/`describedby` link |
| STAC collection | DCAT dataset | `links[].rel = "describedby"` |
| STAC item | Processed artifact | `assets[].href` + `checksum` + `media_type` |
| STAC item | PROV | `links[].rel = "via"` or `derived_from` (choose a stable KFM convention) |
| PROV | Artifacts | `prov:Entity` nodes with digests + paths |
| Run receipt | Everything | digests + IDs for inputs/outputs |

[Back to top](#kfm-sample-dataset)

---

## Evidence and citations

### EvidenceRef principles
- EvidenceRefs must be parseable without network calls.
- Evidence must resolve to an immutable dataset version and an evidence span (not “just a URL”).
- Avoid “free-floating” features with no evidence:
  - If evidence is not available, mark feature as `uncited`
  - Do not allow `uncited` items in Story Nodes until evidence exists

### Recommended EvidenceRef schemes
Use the smallest set that supports your surfaces:

- `dcat://...`
- `stac://...`
- `prov://...`
- `doc://sha256:<digest>#page=<n>&span=<a>:<b>`
- `graph://...` (optional)

### EvidenceBundle expectations
When a feature or claim is clicked, the evidence resolver should be able to return an EvidenceBundle containing:
- bundle digest / ID
- dataset_version_id
- policy decision + obligations applied
- license + attribution
- provenance link (run receipt / PROV)
- artifact links (only if policy allows)
- audit_ref

[Back to top](#kfm-sample-dataset)

---

## How to use in local dev and CI

### Validating the fixture
In CI (and locally), validate at least:
1. JSON schema validation for KFM DCAT/STAC/PROV profiles
2. Link checking: cross-links exist and resolve in repo context
3. Evidence resolver contract tests:
   - “public” evidence resolves to a bundle with allowed artifacts
   - “restricted” evidence returns 403 with no sensitive metadata leakage
4. `spec_hash` stability tests (golden tests)

### Expected governed API behavior
In a KFM-compliant stack, this fixture should be discoverable and queryable via the governed API (example v1 endpoints):

- `GET /api/v1/datasets`
- `GET /api/v1/stac/collections`
- `GET /api/v1/stac/items`
- `POST /api/v1/evidence/resolve`
- `GET/POST /api/v1/story`
- `POST /api/v1/focus/ask`
- `GET /api/v1/lineage/status` (or equivalent status feed)

If tiles are served as PMTiles bundles:
- `GET /assets/pmtiles/<dataset_version_id>/<layer>.pmtiles` (public-safe only, unless your policy layer gates static assets)

> NOTE  
> This README intentionally does **not** prescribe exact CLI commands, because repo tooling varies. The fixture is meant to be compatible with whatever runner/validators your repo provides.

[Back to top](#kfm-sample-dataset)

---

## Safety and governance

This is a fixture dataset. Treat it as production-adjacent because it will be used in CI and demos.

### Hard rules
- Do **not** add PII.
- Do **not** add precise locations for culturally restricted sites, private individuals, or vulnerable infrastructure.
- Do **not** add third-party data unless:
  - license/terms are explicit, and
  - attribution text is present, and
  - redistribution is permitted.

### If you need a “restricted” test case
Use synthetic geometry and synthetic attributes, and ensure:
- policy label is `restricted`
- obligations indicate what is being generalized/suppressed
- evidence resolver returns policy-safe errors and does not leak “ghost metadata”

[Back to top](#kfm-sample-dataset)

---

## Troubleshooting

### Spec hash mismatch
- Ensure `spec/dataset_spec.json` is canonicalized exactly the same way in all environments.
- Confirm no non-deterministic fields (timestamps, absolute paths) are included in the spec hash input.

### Link check failures
- Confirm every `href`/`link` points to an existing file (relative paths recommended for repo-local fixtures).
- Confirm STAC assets include `checksum` and `media_type`.

### Evidence resolve failures
- Confirm EvidenceRef syntax is correct.
- Confirm the resolver can map the reference to:
  - dataset_version_id + artifact digest, or
  - document digest + page/span

### “Restricted” leakage concerns
- Ensure error behavior does not reveal restricted existence by inconsistent 403 vs 404 patterns.
- Ensure evidence bundles never include restricted artifacts for unauthorized roles.

[Back to top](#kfm-sample-dataset)
