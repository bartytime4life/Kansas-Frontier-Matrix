# 🧪 08 — OCI Artifact Distribution Scripts 📦🔐  
**Location:** `mcp/dev_prov/examples/08_oci_artifact_distribution/scripts/README.md`

![OCI](https://img.shields.io/badge/OCI-artifacts-1f6feb?logo=docker&logoColor=white)
![ORAS](https://img.shields.io/badge/ORAS-push%2Fpull-6f42c1)
![Cosign](https://img.shields.io/badge/Cosign-signed-2ea44f)
![Provenance](https://img.shields.io/badge/PROV-JSON--LD-7f3fbf)
![Evidence-first](https://img.shields.io/badge/KFM-evidence--first-orange)

> [!NOTE]
> This example is aligned with KFM’s **evidence-first publishing** stance (no “mystery layers”), where everything distributed is meant to stay **traceable + verifiable** end-to-end. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

---

## 🎯 What this scripts folder is for

These scripts demonstrate a **provenance-first artifact distribution** pattern:

- ✅ Package KFM deliverables (ex: **PMTiles**, **GeoParquet**, **COG**) as OCI artifacts  
- ✅ Push/pull via **ORAS** into an OCI registry  
- ✅ Sign + attach provenance (and optionally SBOM) via **Cosign** using OCI **referrers**  
- ✅ Write back immutable distribution metadata into STAC/DCAT (via `distribution.oci` + `provenance_ref`)  
- ✅ Enforce “fail closed” governance checks before promotion

This matches the broader KFM pipeline discipline where you don’t skip stages (Raw → Work → Processed → Catalog → Graph → AI).:contentReference[oaicite:2]{index=2}

---

## 🗂️ Folder map (typical)

> Script names can vary by repo iteration — what matters is the **responsibility** of each step.

```text
📁 scripts/
├─ 🧰 00_check_prereqs.sh           # tools, env vars, registry auth
├─ 📦 10_oras_push.sh               # ORAS push → OCI registry
├─ 🔐 20_cosign_sign.sh             # sign artifact digest/tag
├─ 🧾 30_cosign_attest.sh           # attach PROV JSON-LD (+ SBOM) as referrers
├─ 🗂️ 40_patch_catalogs.sh          # write distribution.oci + provenance_ref into STAC/DCAT
├─ ✅ 50_verify.sh                  # verify signatures/attestations + pull by digest
└─ 📄 README.md                     # 👈 you are here
```

---

## ⚙️ Prerequisites

### 🧩 Required
- `oras` (OCI artifact push/pull)  
- `cosign` (signing + attestations)  
- Registry access (ex: GHCR, ECR, GCR, Harbor)

ORAS + Cosign are explicitly the intended toolchain for this pattern.:contentReference[oaicite:3]{index=3}

### 🧰 Helpful (optional)
- `jq` / `yq` (catalog patching)
- `conftest` (OPA policy checks)

---

## 🚀 Quickstart (happy path)

### 1) Set environment variables
```bash
export OCI_REGISTRY="ghcr.io"
export OCI_REPOSITORY="myorg/kfm/surficial"
export OCI_TAG="20260111"
export OCI_REF="${OCI_REGISTRY}/${OCI_REPOSITORY}:${OCI_TAG}"

# Optional: a run id for audit logging
export RUN_ID="$(date +%Y%m%dT%H%M%SZ)"
```

### 2) Push artifacts to OCI (ORAS)
Example shows **PMTiles + GeoParquet** (a KFM “dual-format” performance pattern).:contentReference[oaicite:4]{index=4}

```bash
oras push "$OCI_REF" \
  ./surficial_geology.pmtiles:application/vnd.pmtiles \
  ./surficial_geology.parquet:application/vnd.geo+parquet
```

This exact pattern (custom media types for PMTiles/GeoParquet) is called out in the project docs.:contentReference[oaicite:5]{index=5}

> [!TIP]
> Prefer recording the resulting **sha256 digest** and treating it as the *canonical identity* of the release. (Tags are convenience; digests are truth.):contentReference[oaicite:6]{index=6}

### 3) Sign the artifact (Cosign)
```bash
cosign sign --yes "$OCI_REF"
```

Cosign keyless signing (OIDC flow) is part of the intended approach for modern provenance workflows.:contentReference[oaicite:7]{index=7}

### 4) Attach provenance (and SBOM) as OCI referrers
Attach a **PROV JSON-LD** predicate (and optionally SBOM) as referrers so provenance “travels with” the artifact digest.:contentReference[oaicite:8]{index=8}

```bash
# PROV JSON-LD (predicate)
cosign attest --yes \
  --type "application/vnd.kfm.prov+jsonld" \
  --predicate "./prov.jsonld" \
  "$OCI_REF"

# (optional) SBOM
cosign attest --yes \
  --type "application/spdx+json" \
  --predicate "./sbom.spdx.json" \
  "$OCI_REF"
```

### 5) Patch catalogs with OCI distribution metadata
Your STAC/DCAT record should gain a `distribution.oci` entry with registry/repo/tag/digest + the file list and media types.:contentReference[oaicite:9]{index=9}

You also add a `provenance_ref` that points at the artifact’s **referrer records** (signatures, SBOMs, attestations).:contentReference[oaicite:10]{index=10}

### 6) Verify + pull by digest (recommended)
```bash
cosign verify "$OCI_REF"

# Recommended: pull by digest (example placeholder)
# oras pull "oci://${OCI_REGISTRY}/${OCI_REPOSITORY}@sha256:<DIGEST>" -o ./out
```

---

## 🧾 How the catalogs are supposed to look

### A) `distribution.oci` (DCAT/STAC extension concept)
Here’s an example structure mirroring the documented fields (registry, repository, tag, digest, files+mediaType).:contentReference[oaicite:11]{index=11}

```yaml
distribution:
  oci:
    registry: ghcr.io
    repository: myorg/kfm/surficial
    tag: "20260111"
    digest: "sha256:…"
    files:
      - name: "surficial_geology.pmtiles"
        mediaType: "application/vnd.pmtiles"
      - name: "surficial_geology.parquet"
        mediaType: "application/vnd.geo+parquet"
```

### B) `provenance_ref` and STAC `href: oci://…`
The provenance pointer is expected to be an OCI-style reference, and STAC assets can also use `oci://…` hrefs for immutable content addressing.:contentReference[oaicite:12]{index=12}

```yaml
provenance_ref: "oci://ghcr.io/myorg/kfm/surficial@sha256:…"
assets:
  pmtiles:
    href: "oci://ghcr.io/myorg/kfm/surficial@sha256:…"
    type: "application/vnd.pmtiles"
```

> [!IMPORTANT]
> KFM’s STAC guidance explicitly encourages linking Items to provenance via **custom fields or links** (e.g., `assets.provenance` linking to PROV JSON).:contentReference[oaicite:13]{index=13}

---

## 🧬 Where this fits in the KFM lifecycle

### 🔁 Pipeline alignment
KFM emphasizes a strict stage order (no skipping):  
**Raw → Work → Processed → Catalog → Graph → AI**:contentReference[oaicite:14]{index=14}

This example primarily lives at the **Processed → Catalog** boundary:
- The “payload” is processed deliverables (GeoParquet, PMTiles, COG, etc.):contentReference[oaicite:15]{index=15}
- The “contract” is the evidence triplet that must exist before publishing.

### 🧾 Evidence triplet (why catalogs must be updated)
KFM’s catalogs (DCAT + STAC + PROV) are the required **“evidence triplet”** and are version-controlled for auditability; this is described as **evidence-first publishing**.:contentReference[oaicite:16]{index=16}

---

## 🛡️ Policy gates (fail closed ✅🚫)

A key theme is governance that **fails closed** when provenance/signatures are missing.:contentReference[oaicite:17]{index=17}

Typical checks you’ll want in scripts/CI:
- ✅ artifact has a stable digest recorded (no floating-only tags)
- ✅ signature exists and verifies
- ✅ provenance attestation exists (PROV JSON-LD)
- ✅ metadata required for promotion exists (license, sensitivity classification, etc.)

KFM’s intake design also includes sensitivity-aware controls where the most restrictive classification propagates through derived data and affects UI/API behaviors.:contentReference[oaicite:18]{index=18}:contentReference[oaicite:19]{index=19}

---

## 🧾 Audit trail artifact (run manifest)

The docs propose writing a run manifest under `data/audits/<run_id>/run_manifest.json`, including a canonical digest for deterministic verification.:contentReference[oaicite:20]{index=20}

Recommended pattern for these scripts:
- Create a per-run manifest (inputs, outputs, hashes, tool versions)
- Canonicalize JSON and store a canonical digest
- Attach/record those references in provenance and/or registry referrers

---

## 🧠 Why this matters to UI + “Focus Mode” 🤖🧭

- KFM’s UI goal is that every visualization remains traceable to sources (“the map behind the map”).:contentReference[oaicite:21]{index=21}
- KFM’s AI “Focus Mode” is designed to **cite sources** and refuse to fabricate when it cannot ground an answer in data.:contentReference[oaicite:22]{index=22}

✅ OCI digest pinning + signed provenance makes that possible at scale.

---

## 🌿 Ethics + sensitive content distribution

KFM explicitly explores **differential access** and cultural protocol-informed restrictions (tiered access, tagging, obfuscation for sensitive locations).:contentReference[oaicite:23]{index=23}:contentReference[oaicite:24]{index=24}

When using OCI registries:
- Prefer **private registries** for sensitive layers
- Keep provenance/signatures intact while limiting who can pull the artifact
- Ensure catalog entries respect “restricted” semantics (don’t leak hrefs publicly)

The OCI approach is also explicitly framed with FAIR+CARE considerations and permission controls (private repos/registries).:contentReference[oaicite:25]{index=25}

---

## 🧯 Troubleshooting

- **ORAS push fails** → check registry login + repo permissions  
- **Cosign verify fails** → confirm you’re verifying the same digest/tag you signed  
- **Catalog patch looks right but UI doesn’t change** → remember: UI typically reads from **catalog+graph**, not raw artifacts; ensure graph ingestion / index refresh is part of your flow.:contentReference[oaicite:26]{index=26}
- **Missing provenance** → treat as a release blocker; this project explicitly supports “fail closed” policy gates.:contentReference[oaicite:27]{index=27}

---

## 📚 Source docs (project files used)

### Core KFM design docs
- 📦 **Additional Project Ideas** :contentReference[oaicite:28]{index=28}  
- 🧾 **KFM Data Intake — Technical & Design Guide** :contentReference[oaicite:29]{index=29}  
- 🧭 **KFM AI System Overview** :contentReference[oaicite:30]{index=30}  
- 🖥️ **KFM UI System Overview** :contentReference[oaicite:31]{index=31}  
- 🧱 **KFM Comprehensive Architecture, Features, and Design** :contentReference[oaicite:32]{index=32}  
- 🧰 **KFM Comprehensive Technical Documentation** :contentReference[oaicite:33]{index=33}  
- 🌟 **Latest Ideas & Future Proposals** :contentReference[oaicite:34]{index=34}  
- 💡 **Innovative Concepts to Evolve KFM** :contentReference[oaicite:35]{index=35}  

### MCP / repo structure reference
- 🗺️ **Kansas-Frontier-Matrix — Open-Source Geospatial Historical Mapping Hub Design** :contentReference[oaicite:36]{index=36}  
  (Includes `mcp/` as a documentation-heavy home for experiments + SOPs + reproducibility patterns.):contentReference[oaicite:37]{index=37}

### Knowledge library (PDF portfolios)
Some references are bundled as **PDF portfolios** that are best opened in Acrobat/Reader X+:
- 📚 Various programming languages & resources 1 :contentReference[oaicite:38]{index=38} :contentReference[oaicite:39]{index=39}
- 🧠 AI Concepts & more :contentReference[oaicite:40]{index=40} :contentReference[oaicite:41]{index=41}

### Legacy filecite markers (requested for cross-linking)
- 💡 Innovative Concepts (legacy cite) :contentReference[oaicite:42]{index=42}
- 🧾 Document Refinement Request (legacy cite) :contentReference[oaicite:43]{index=43}
- 📚 Data Intake (legacy cite) :contentReference[oaicite:44]{index=44}

