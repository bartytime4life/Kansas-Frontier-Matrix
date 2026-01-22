# 📦 OCI Artifact Distribution — `manifests/` (Example 08)

**Path:** `mcp/dev_prov/examples/08_oci_artifact_distribution/manifests/`  
This folder contains **declarative manifests** that describe *what* gets published to an **OCI registry** (via ORAS-style pushes), *how* it’s **cryptographically verified** (Cosign/Sigstore), and *how* it becomes a **first-class “evidence artifact”** in the Kansas Frontier Matrix (KFM) pipeline (STAC/DCAT/PROV + governed API/UI/Focus Mode).

> 🧭 KFM invariant: **ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**  
> OCI distribution lives at the “**artifact storage + distribution**” boundary and is referenced by the catalogs so downstream layers never consume “mystery bytes.”

---

## 🎯 What these manifests are for

These manifests are the “**contract**” for distributing *data products* and *evidence bundles*:

- **📦 Ship large geospatial artifacts** (e.g., `PMTiles`, `GeoParquet`, `COG`) as **OCI artifacts** (content-addressed, versioned, registry-native).
- **🧾 Attach provenance + SBOM** (and optionally SLSA/in-toto attestations) so consumers can verify:
  - *what produced the artifact*,
  - *which inputs were used*,
  - *which tools/versions ran*, and
  - *that nothing was tampered with*.
- **🗺️ Bridge to KFM catalogs** (STAC/DCAT) and lineage (PROV) so UI + Focus Mode can show “**View Evidence**” and enforce “**no citation → no publish**”.
- **⚖️ Enforce governance** (license, sensitivity classification, FAIR+CARE constraints) with **policy gates** (fail-closed).

---

## 🗂️ What you should see in this folder

> Exact filenames may vary by repo evolution, but the intent stays stable.

```text
manifests/
├─ README.md                          # you are here ✅
├─ oci.distribution.v1.yaml           # “what to push + where + media types”
├─ prov.bundle.jsonld                 # PROV-O lineage (inputs → activities → outputs)
├─ sbom.spdx.json                     # SBOM for the build/toolchain (or pipeline container)
├─ stac.item.json                     # STAC Item referencing the distributed artifact(s)
├─ dcat.dataset.jsonld                # DCAT Dataset entry w/ distribution links
└─ policy.inputs.json                 # optional: inputs for conftest/OPA validation
```

---

## 🧩 The KFM “Evidence Bundle” pattern (what the manifests *represent*)

KFM treats **every published dataset** (including AI/analysis outputs) as an **evidence artifact** that must ship with:

- **STAC** (spatial/temporal metadata and assets),
- **DCAT** (discovery + licensing + distributions), and
- **PROV** (lineage: source → processing → output).

OCI distribution is the **transport/storage layer** for the actual bytes, while STAC/DCAT/PROV are the **boundary artifacts** that downstream layers consume.

```mermaid
flowchart LR
  A[Raw Sources] --> B[ETL + Normalization]
  B --> C[data/processed outputs]
  C --> D[Publish to OCI Registry (ORAS)]
  D --> E[Sign + Attest (Cosign/Sigstore)]
  E --> F[Catalog Boundary Artifacts<br/>STAC + DCAT + PROV]
  F --> G[Neo4j Graph]
  G --> H[API Layer<br/>(contracts + redaction)]
  H --> I[UI + Story Nodes]
  I --> J[Focus Mode<br/>(citations required)]
```

---

## 🧾 Main manifest: `oci.distribution.v1.yaml`

This is the **single source of truth** for “what’s inside the OCI artifact” and “how to verify it”.

### ✅ Minimum expectations

A good distribution manifest should declare:

- **Registry target** (e.g., `ghcr.io`, `registry.example.org`)
- **Repository path** (`org/project` or `org/kfm-data`)
- **Reference strategy**:
  - ✅ pin by **digest** for determinism,
  - tags are allowed but treated as *mutable pointers*.
- **Files + roles + media types** (PMTiles vs GeoParquet vs COG)
- **Checksums + sizes** (content integrity)
- **Governance**:
  - license,
  - sensitivity level (public/sensitive/confidential),
  - any FAIR/CARE or sovereignty constraints.
- **Provenance hooks**:
  - where the PROV bundle lives (as an OCI referrer/attachment or alongside),
  - build/run identifiers.

---

## 🔗 How OCI references should appear in KFM metadata

When STAC/DCAT needs to point at OCI, prefer **digest-pinned** references.

Example (pseudo-field layout; adapt to your repo’s profiles):

```yaml
distribution:
  oci:
    registry: ghcr.io
    repository: bartytime4life/kfm-data/ks-hydrology
    digest: sha256:0123abcd...     # ✅ stable
    tag: v2026.01.22               # optional pointer
    referrers:
      prov:  sha256:aaaa...
      sbom:  sha256:bbbb...
      sig:   sha256:cccc...
```

> 🧠 Why digest pinning matters: it supports deterministic pipelines and repeatable verification (a core KFM invariant).

---

## 🛠️ Typical publish flow (ORAS + Cosign + Catalog update)

> This example is intentionally **provenance-first** and matches KFM’s “fail closed” policy gates.

### 1) Produce artifacts (ETL output)
Examples of artifacts you might publish:

- 🧱 **PMTiles** for fast vector tile serving/offline packs
- 🧊 **GeoParquet** for analytic-friendly vector data
- 🛰️ **COG** (Cloud-Optimized GeoTIFF) for raster layers

### 2) Populate manifests
- Update `oci.distribution.v1.yaml` with files, checksums, media types
- Generate/refresh:
  - `prov.bundle.jsonld`
  - `sbom.spdx.json`
  - `stac.item.json`
  - `dcat.dataset.jsonld`

### 3) Push to OCI (ORAS-style)
Keep refs in code blocks so it’s copy/paste friendly:

```bash
# Example (illustrative)
oras push \
  "$REGISTRY/$REPO:$TAG" \
  ./artifacts/ks.pmtiles:application/vnd.pmtiles \
  ./artifacts/ks.parquet:application/vnd.geo+parquet
```

Capture the **resulting digest** and write it back into:
- `oci.distribution.v1.yaml`
- STAC/DCAT distribution fields
- PROV `Entity` location/identifier

### 4) Sign + attach attestations (Cosign/Sigstore)
```bash
# Sign the OCI artifact by digest (recommended)
cosign sign "$REGISTRY/$REPO@$DIGEST"

# Attach SBOM / PROV as referrers (illustrative)
oras attach \
  "$REGISTRY/$REPO@$DIGEST" \
  --artifact-type application/spdx+json \
  ./manifests/sbom.spdx.json

oras attach \
  "$REGISTRY/$REPO@$DIGEST" \
  --artifact-type application/ld+json \
  ./manifests/prov.bundle.jsonld
```

### 5) Verify before promotion (policy gate)
```bash
cosign verify "$REGISTRY/$REPO@$DIGEST"
# Optional: verify attached attestations (SBOM/PROV) if your policy pack requires it
```

---

## ✅ Validation gates (what should fail the build)

KFM’s governance posture is:

- **No license → no publish**
- **No sensitivity classification → no publish**
- **No STAC/DCAT/PROV completeness → no publish**
- **No provenance/citations (Focus Mode outputs) → refuse/deny**
- **Fail closed**: anything missing blocks promotion

These manifests are designed to be checked by **Conftest/OPA policy packs** during CI and/or by the Watcher → Planner → Executor automation pattern (Planner proposes changes, Executor promotes only with proof/attestations).

---

## ⚖️ Governance & sensitivity (don’t skip this)

KFM explicitly supports **sensitive datasets** (e.g., endangered species habitat, archaeological site locations, PII-adjacent records) by:

- requiring sensitivity tagging,
- supporting **redaction/generalization** (coarsened coordinates, aggregation),
- enforcing access control at API boundaries,
- and codifying FAIR+CARE constraints as automated rules.

**Important:** privacy risk doesn’t stop at raw data. Derived outputs (including ML/data mining outputs) can leak sensitive info. If your artifact is derived from restricted sources, document:
- applied anonymization/aggregation methods,
- thresholds (e.g., k-anonymity / t-closeness style reasoning),
- and any “do-not-query” / “deny export” constraints that the API/UI must enforce.

---

## 🧠 AI & analysis artifacts also use this path

In KFM, AI/analysis outputs are treated like datasets:
- they **must** have STAC/DCAT/PROV,
- they **must** be governed via the API layer (no direct UI-to-graph),
- and Focus Mode requires **citations** and provenance.

OCI distribution makes it practical to ship:
- model outputs,
- derived rasters,
- OCR corpora,
- snapshots used in narratives,
as verifiable, attestable artifacts.

---

## 🌍 Suggested media types (pragmatic defaults)

Use stable, explicit media types so downstream consumers (validators, UI download tooling, offline pack builders) can route correctly.

| Artifact | Suggested mediaType |
|---|---|
| PMTiles | `application/vnd.pmtiles` |
| GeoParquet | `application/vnd.geo+parquet` |
| COG GeoTIFF | `image/tiff` *(optionally annotate “COG” in metadata)* |
| PROV JSON-LD | `application/ld+json` |
| SPDX SBOM | `application/spdx+json` |
| DCAT JSON-LD | `application/ld+json` |
| STAC JSON | `application/json` |

> 🧩 Tip: If you standardize these in policy, you can auto-validate “artifact role ↔ mediaType” mapping.

---

## 🧯 Troubleshooting

- **“It worked by tag yesterday, now it’s different.”**  
  Tags are mutable pointers. Use **digests** for deterministic builds and provenance.

- **“Cosign verify fails in CI.”**  
  Ensure your CI identity/OIDC settings match expected issuer/subject and you’re verifying the right digest.

- **“Policy gate blocks publish for missing metadata.”**  
  That’s expected: add license/sensitivity fields, ensure STAC/DCAT/PROV files exist and cross-link correctly.

- **“UI can’t download the dataset.”**  
  Confirm DCAT distribution links and/or STAC assets reference the OCI digest correctly, and that API download routes enforce classification rules.

---

## 📚 Design sources (project-wide)

<details>
<summary>Open the reference list used to shape this manifest README 🧠</summary>

- KFM architecture + pipeline invariants (ordering, governance gates, W-P-E agents)
- Data intake guide (STAC/DCAT/PROV boundary artifacts + policy pack expectations)
- AI system overview + UI overview (provenance panels, citations, governance ledger)
- Geospatial distribution patterns (PMTiles/GeoParquet/COG + offline packs)
- Data validation + privacy-preserving guidance (quality, leakage risk in derived outputs)
- MCP / documentation-first standards (repeatability, experiment/protocol mindset)

</details>

<!--
FILECITES (do not remove; used for traceability of generated docs):
:contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3}

:contentReference[oaicite:4]{index=4}   (Additional Project Ideas.pdf)
:contentReference[oaicite:5]{index=5}    (Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf)
:contentReference[oaicite:6]{index=6}  (🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf)
:contentReference[oaicite:7]{index=7}   (Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf)
:contentReference[oaicite:8]{index=8}   (Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf)
:contentReference[oaicite:9]{index=9}   (Kansas Frontier Matrix – Comprehensive UI System Overview.pdf)
:contentReference[oaicite:10]{index=10}   (📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf)
:contentReference[oaicite:11]{index=11}   (Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf)

:contentReference[oaicite:12]{index=12}   (AI Concepts & more.pdf — PDF portfolio)
:contentReference[oaicite:13]{index=13}   (Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf — PDF portfolio)
:contentReference[oaicite:14]{index=14}   (Various programming langurages & resources 1.pdf — PDF portfolio)
:contentReference[oaicite:15]{index=15}   (Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf — PDF portfolio)

:contentReference[oaicite:16]{index=16}   (Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf)
:contentReference[oaicite:17]{index=17}   (MARKDOWN_GUIDE_v13.md.gdoc)
:contentReference[oaicite:18]{index=18}   (Scientific Method _ Research _ Master Coder Protocol Documentation.pdf)
:contentReference[oaicite:19]{index=19}    (Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx)
:contentReference[oaicite:20]{index=20}   (KFM python geospatial analysis cookbook pdf)
:contentReference[oaicite:21]{index=21}   (Data Mining Concepts & applictions.pdf)
-->

