# 🧾 KFM Evidence Bundle — `sha256:<digest>`

> **Directory:** `data/bundles/sha256/<digest>/`  
> **Canonical bundle address:** `sha256:<digest>` (this folder name)  
> **Intended resolver:** `GET /bundles/<digest>` (governed API) *(see “Resolver contract”)*

> [!IMPORTANT]
> **Immutable, digest-addressed. Do not edit in place.**  
> If anything in this bundle changes, the **digest changes** → create a **new** folder under `data/bundles/sha256/`.

---

## What this is

This folder is a **digest-addressed Evidence Bundle**: a self-describing snapshot of **what was published** (or proposed for publish), plus the **evidence needed to trust it** (catalogs, provenance, receipts, checksums, and—when available—signatures/attestations/SBOM).

KFM uses evidence bundles to:

- **Pin references** (stable, content-addressed identifiers rather than mutable tags).
- **Support “cite-or-abstain”** UX and audits (every surfaced claim must resolve back to evidence).
- **Enable reproducibility** and “what changed” review (receipts + manifests + diffs).

---

## Bundle card

| Field | Value (fill in / generated) | Where to find it |
|---|---|---|
| Bundle digest | `sha256:<digest>` | Folder name + `bundle.config.json` |
| Artifact type | `<media-type>` | `bundle.config.json` |
| Dataset ID(s) | `<kfm.dataset…>` | `catalog/dcat/*` and/or `catalog/stac/*` |
| Run ID | `<prov:kfm.run.…>` | `evidence/run_receipt.json` |
| `spec_hash` | `<sha256(JCS(spec))>` | `evidence/run_manifest.json` |
| Lane | `quarantine \| staging \| prod` | `evidence/run_manifest.json` |
| Sensitivity | `public \| internal \| restricted` | `evidence/run_manifest.json` / policy labels |
| Rights / license | `<SPDX or “various”>` | `catalog/dcat/*` + policy labels |
| Generated at | `<ISO-8601 UTC>` | `evidence/run_receipt.json` |

> [!NOTE]
> If you’re reviewing this in a PR: treat the bundle card values as *derived from the evidence files*, not manually curated.

---

## Directory layout

> [!TIP]
> The exact filenames may evolve, but the **invariants** must hold: (a) digest-addressed folder, (b) machine-readable bundle index, (c) checksums, (d) cross-linked catalogs, (e) receipts/provenance.

```text
data/bundles/sha256/<digest>/
├── README.md
├── bundle.config.json              # bundle index (file list + digests + media types)
├── checksums.sha256                # sha256 checksums for files in this folder (fail-closed)
│
├── catalog/                        # discovery + citation anchors (cross-linked)
│   ├── stac/                       # STAC Items/Collections/Catalog (JSON)
│   ├── dcat/                       # DCAT Dataset/Distributions (JSON/JSON-LD)
│   └── prov/                       # PROV bundle(s) (JSON-LD / PROV-N export)
│
├── evidence/                       # “why trust this” artifacts
│   ├── run_manifest.json           # canonical run manifest (policy + spec identity)
│   ├── run_receipt.json            # typed receipt for the run (PASS or FAIL)
│   ├── validation_report.json      # schema/geo validation outputs
│   ├── sbom.*.json                 # SPDX or CycloneDX (optional but recommended)
│   └── attestations/               # signatures/attestations (optional; required in higher lanes)
│       ├── slsa.att.json           # in-toto/SLSA provenance attestation (if mirrored locally)
│       └── cosign.bundle           # signature bundle / verification material (if mirrored)
│
└── payload/                        # optional: actual data artifacts (may be external)
    ├── *.parquet                   # GeoParquet (if bundled)
    ├── *.tif                       # COG (if bundled)
    ├── *.pmtiles                   # PMTiles (if bundled)
    └── ...                         # PDFs/media (if bundled)
```

---

## Bundle contract

### Required invariants (fail closed)

- **Digest addressing**
  - Folder name MUST equal the canonical digest: `sha256:<digest>`.

- **Machine-readable index**
  - `bundle.config.json` MUST exist and MUST enumerate:
    - relative paths
    - media types
    - file digests
    - sizes (recommended)

- **Checksums**
  - `checksums.sha256` MUST exist and MUST verify cleanly.

- **Cross-linked catalogs**
  - STAC/DCAT/PROV MUST link to each other **and** point back to this bundle digest (directly or via a known bundle URI scheme).

- **Receipts and provenance**
  - A typed receipt and a provenance bundle MUST exist for the run (PASS **and** FAIL runs should still emit provenance/receipts).

> [!WARNING]
> If any invariant fails, downstream consumers MUST treat this bundle as **untrusted** and UIs should show an explicit “why not trusted” state.

---

## Bundle pieces and suggested media types

These are the canonical “pieces” KFM expects an OCI Evidence Bundle to contain (whether the payload is fully local or referenced externally):

| Artifact piece | Suggested media type | Typical location |
|---|---|---|
| Bundle config | `application/vnd.kfm.stac-bundle+json` | `bundle.config.json` |
| STAC Catalog/Collection/Item | `application/vnd.stac.catalog+json` / `application/vnd.stac.collection+json` / `application/geo+json` | `catalog/stac/` |
| SBOM | `application/spdx+json` *(or CycloneDX JSON)* | `evidence/sbom.*.json` |
| Run receipt | `application/vnd.kfm.run-receipt+json` | `evidence/run_receipt.json` |
| Attestation | `application/vnd.in-toto.attestation` | `evidence/attestations/` |
| GeoParquet | `application/x-parquet` | `payload/*.parquet` |
| COG | `image/tiff` | `payload/*.tif` |

> [!NOTE]
> KFM may keep large payloads in an object store and only include **descriptors + checksums** here. Either approach is acceptable as long as the resolver can fetch by digest and the catalogs point to the right artifacts.

---

## Local verification

### 1) Verify file integrity (required)

```bash
cd data/bundles/sha256/<digest>
sha256sum --check checksums.sha256
```

### 2) Validate catalogs (recommended)

```bash
# STAC (example — adjust command/tooling to repo standard)
stac-validator catalog/stac/**/collection.json

# PROV (example — depends on your PROV tooling)
provconvert -infile catalog/prov/**/*.provn -validator
```

### 3) Policy gates (recommended, fail-closed in CI)

```bash
# Example shape; policy pack location may differ
conftest test evidence/run_receipt.json --policy policy/opa
conftest test evidence/run_manifest.json --policy policy/opa
```

### 4) Signature / attestation verification (lane-dependent)

If this bundle is mirrored from an OCI registry, verify at the registry subject digest (preferred). If your workflow stores attestations locally, verify them according to repo tooling.

---

## Resolver contract

This bundle is meant to be accessed through the **governed API** (trust membrane). The bounded resolver should:

- Resolve **bundle metadata** by digest (e.g., `GET /bundles/<digest>`).
- Return enough information for clients to fetch:
  - catalogs (STAC/DCAT/PROV)
  - receipts/attestations/SBOM
  - payload (or payload descriptors)
- Support citation resolution with a strict UX contract:
  - “From any claim → evidence drawer” must be achievable with **minimal hops** (target: ≤2 calls per citation reference).

> [!IMPORTANT]
> Frontends and external clients MUST NOT access databases or object stores directly; all access goes through the governed API + policy boundary.

---

## Governance and sensitivity notes

- **Rights metadata is not optional.** If rights/licensing fields are missing or contradictory, promotion should be blocked.
- **Sensitive location data must be handled explicitly.** If this bundle includes restricted archaeological or culturally sensitive material, the public lane MUST require redaction/generalization and human review.
- Receipts/logs must avoid leaking sensitive fields; redact where required.

---

## How to update / regenerate

1. Re-run the pipeline (deterministic packaging rules apply).
2. Emit catalogs + receipts + provenance.
3. Create a **new** digest folder under `data/bundles/sha256/`.
4. Update any catalog pointers that referenced the old digest.
5. Open PR with the new bundle + validation evidence.

> [!TIP]
> Keep changes reviewable: include a “what changed” diff artifact when possible (row counts, schema diffs, etc.), and link it from the receipt.
