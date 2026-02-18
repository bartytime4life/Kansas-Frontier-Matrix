# SHA-256 Evidence Bundles (KFM)

![Governed](https://img.shields.io/badge/Governed-yes-2ea44f)
![Evidence-first](https://img.shields.io/badge/Evidence--first-yes-blue)
![Immutable](https://img.shields.io/badge/Immutability-write--once-important)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-aligned-informational)

This directory is a **content-addressed** bundle store: **each bundle is keyed by its SHA-256 digest** and treated as **immutable evidence**.

It exists to support KFM’s “Truth Path” and governed distribution model:

- pipelines produce validated artifacts (STAC/DCAT/PROV + data assets)
- bundles package or reference those artifacts
- catalogs and APIs refer to bundles **by digest**, enabling verification and auditable resolution

> [!IMPORTANT]
> In production, external clients should **not** read this folder directly. They resolve evidence via the **governed API boundary** (trust membrane). This folder is an internal store/cache/fixture location.

---

## What belongs here

Bundles that represent **auditable, promotion-ready evidence**:

- dataset payloads (e.g., GeoParquet/COG/PMTiles) **and/or** pointers to object-store locations
- STAC objects (Collections/Items) describing spatial-temporal assets
- DCAT dataset/distributions capturing rights, access, and attribution
- PROV bundles / run receipts / validation reports
- optional supply-chain evidence (SBOMs, signatures, attestations)

> [!NOTE]
> “Bundle” in KFM can be implemented as an OCI artifact + referrers (recommended upstream), with a filesystem mirror here for local dev, CI fixtures, offline testing, and deterministic resolution experiments.

---

## Non-negotiable rules ✅

| Rule | What it means | Why it exists |
|---|---|---|
| **Digest is the address** | The bundle ID is `sha256:<64-hex>` and MUST match content | Enables unambiguous verification and auditability |
| **Write-once** | Never mutate a bundle “in place” | Any mutation breaks digest integrity |
| **Pin digests, not tags** | Catalogs/receipts refer to `@sha256:<digest>` (not floating tags) | Prevents ambiguity + supply-chain downgrade |
| **Fail-closed** | If required evidence is missing or invalid → treat as NOT promotable | Preserves trust and blocks unsafe publication |
| **Governance travels with the bundle** | License + sensitivity/CARE constraints must be present and consistent | Policy enforcement requires portable metadata |

---

## Directory layout

Recommended (MVP) layout:

```text
data/
  bundles/
    sha256/
      README.md
      <DIGEST>/                      # 64-hex (lowercase recommended)
        bundle.json                  # bundle descriptor (manifest/index)
        artifacts/                   # optional extracted children
          stac/                      # optional STAC objects (collection/item/catalog)
          dcat/                      # optional DCAT dataset/distribution JSON
          prov/                      # optional PROV bundle(s)
          receipts/                  # optional run_receipt / run_manifest / validation outputs
        checks/                      # optional validation summaries / QA logs
        signatures/                  # optional signatures / attestations (if mirrored)
```

**Scaling option (fan-out):** for very large stores, you MAY shard by the first 2 hex chars:

```text
data/bundles/sha256/ab/<DIGEST>/...
```

> [!WARNING]
> Large binaries (multi-GB rasters, big parquet) should generally live in an object store or OCI registry.
> If you place them here, prefer this directory to be **gitignored** and treated as a cache.

---

## `bundle.json` descriptor

This repository does not (yet) confirm a final bundle schema, so `bundle.json` below is a **recommended minimal contract** for local use.

```json
{
  "schema": "io.kfm.bundle.v0",
  "bundle_digest": "sha256:<64-hex>",
  "created_at": "RFC3339",
  "subject": {
    "type": "kfm:dataset_version",
    "digest": "sha256:<digest-of-subject-if-applicable>",
    "dataset_id": "kfm.dataset.<domain>.<name>",
    "version": "vYYYY.MM"
  },
  "catalogs": {
    "stac": ["artifacts/stac/collection.json", "artifacts/stac/items/<id>.json"],
    "dcat": ["artifacts/dcat/dataset.json"],
    "prov": ["artifacts/prov/bundle.jsonld"]
  },
  "receipts": ["artifacts/receipts/run_receipt.json"],
  "rights": {
    "license": "SPDX-or-text",
    "attribution": "string",
    "redistribution": "allowed|restricted|unknown"
  },
  "sensitivity": {
    "class": "public|restricted|sensitive",
    "notes": "string"
  },
  "checks": {
    "stac": "ok|fail",
    "dcat": "ok|fail",
    "prov": "ok|fail",
    "policy": "ok|fail"
  }
}
```

---

## How bundles are produced (conceptual flow)

```mermaid
flowchart LR
  A[Ingest raw sources] --> B[Validate + normalize]
  B --> C[Processed artifacts + checksums]
  C --> D[Emit catalogs: STAC/DCAT/PROV]
  D --> E[Assemble Evidence Bundle]
  E --> F[(data/bundles/sha256/<digest>)]
  E --> G[Governed API: GET /bundles/{digest}]
  G --> H[Map UI / Focus Mode / Story Nodes]
```

---

## Governance & sensitivity handling

> [!CAUTION]
> Bundles can include sensitive location data (e.g., protected heritage sites, private landholder details).
> If sensitivity triggers fire:
>
> - **generalize geometry** (e.g., larger grid/region)
> - **redact sensitive attributes**
> - require **human approval** before promotion/publishing
> - ensure catalogs and receipts reflect the redaction decision

---

## Validation gates for anything stored here

A bundle is “eligible” for this store when it has, at minimum:

- deterministic checksums for promoted artifacts
- catalogs are present and linkable (DCAT always; STAC/PROV as applicable)
- schema validation passes (geo + temporal sanity)
- license + attribution captured and propagated
- provenance completeness (PROV chain + run metadata)
- policy checks pass (fail-closed)

### Bundle DoD checklist (copy/paste)

- [ ] `bundle.json` present and references required children
- [ ] license + attribution present and consistent with catalogs
- [ ] sensitivity classification present
- [ ] `checks.*` are present and none are `fail`
- [ ] STAC validates
- [ ] DCAT validates
- [ ] PROV validates (PASS and FAIL provenance policy satisfied)
- [ ] digest recorded in catalogs (digest-pinned reference)

---

## FAQ

<details>
<summary><strong>Why SHA-256?</strong></summary>

SHA-256 enables stable, verifiable, content-addressed references. This supports “pin by digest” distribution, provenance integrity, and reproducible audits.
</details>

<details>
<summary><strong>How are bundles resolved in the product?</strong></summary>

Via governed APIs (trust membrane). A resolver endpoint (e.g., <code>GET /bundles/{digest}</code>) returns bundle metadata and/or links to child artifacts.
</details>

<details>
<summary><strong>Can I update a bundle?</strong></summary>

No. Create a new bundle (new digest) and update catalogs to point to the new digest.
</details>

---

## Related (typical) KFM directories

These are typically produced alongside bundles and referenced by them:

```text
data/
  raw/                # acquired source payloads + capture metadata
  processed/          # validated outputs (immutable/versioned)
  catalog/
    dcat/             # dataset + distribution records
    stac/             # collections/items/assets
  prov/
    run_receipts/     # per-run receipts/manifests
    datasets/         # lineage bundles
```

> Keep the linkage tight: promoted artifacts ↔ exactly one run receipt ↔ discoverable from catalogs.
