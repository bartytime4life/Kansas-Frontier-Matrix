# 🔐 Checksums — Minimal Triplet Receipts 🧾

![example](https://img.shields.io/badge/example-00__quickstart__minimal__triplet-blue)
![integrity](https://img.shields.io/badge/integrity-SHA--256-informational)
![provenance](https://img.shields.io/badge/provenance-first%20⛓-success)
![policy](https://img.shields.io/badge/gates-fail--closed-critical)

> 📍 **You are here:** `mcp/dev_prov/examples/00_quickstart_minimal_triplet/out/checksums/`  
> ✅ **Goal:** Make every artifact from the quickstart **tamper-evident** and **verifiable** — so the *STAC/DCAT/PROV* “evidence triplet” stays trustworthy end-to-end.

---

## 🧠 Why this folder exists

KFM’s philosophy is **evidence-first + provenance-first**:

- **Raw inputs are immutable evidence** (never edited in-place).  
- Pipelines are meant to be **deterministic**: same inputs + config ⇒ same outputs.  
- Integrity checks (like **SHA-256**) act as a **trust boundary**: if bytes change, the system should notice.  
- Governance gates are designed to **fail closed**: if required integrity/metadata/policy conditions aren’t met, the run should stop.

This folder is the “receipt drawer” for that mindset. 🗃️

---

## 📦 What you’ll typically find here

> Exact filenames can vary by implementation, but the pattern stays the same.

### Common files 🧾
- **`checksums.sha256`**  
  A `sha256sum`-style list: one line per file → `HASH  PATH`
- **`checksums.json`** *(optional)*  
  A structured mapping of `{ path, algorithm, digest, size, mtime?, contentType? }`
- **`run_manifest.json` / `run_manifest.yaml`** *(optional)*  
  A “run ledger” capturing inputs, outputs, tool versions, counts, errors, etc.
- **`attestation.*` / `sbom.*`** *(optional / future)*  
  Supply-chain artifacts (SLSA-style provenance statement, SBOM, signatures)

### Example layout 🗂️
```text
📦 out/
└─ 🔐 checksums/
   ├─ README.md
   ├─ 🧾 checksums.sha256
   ├─ 🧩 checksums.json            (optional)
   └─ 🧪 run_manifest.json         (optional)
```

---

## 🚀 Quick verify (copy/paste)

> ⚠️ **Run the verify command from the directory context expected by the checksum file paths.**  
> If the checksum file contains relative paths, you need to be in the matching folder (or adjust paths).

### 🐧 Linux
```bash
sha256sum -c checksums.sha256
```

### 🍎 macOS
```bash
shasum -a 256 -c checksums.sha256
```

### 🪟 Windows (PowerShell)
**Option A — verify one file quickly**
```powershell
Get-FileHash -Algorithm SHA256 <PATH_TO_FILE>
```

**Option B — verify a `checksums.sha256` file**
```powershell
Get-Content .\checksums.sha256 | ForEach-Object {
  if ($_ -match '^[0-9a-fA-F]{64}\s+(.+)$') {
    $parts = $_ -split '\s+', 2
    $expected = $parts[0].ToLower()
    $path = $parts[1].Trim()
    if (Test-Path $path) {
      $actual = (Get-FileHash -Algorithm SHA256 $path).Hash.ToLower()
      if ($actual -ne $expected) {
        Write-Error "❌ MISMATCH: $path"
      } else {
        Write-Host "✅ OK: $path"
      }
    } else {
      Write-Warning "⚠️ Missing: $path"
    }
  }
}
```

### 🐍 Python (portable)
```python
import hashlib, pathlib

def sha256_file(p: pathlib.Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

# Example usage:
# print(sha256_file(pathlib.Path("some_artifact.json")))
```

---

## 🔗 How checksums fit the “Evidence Triplet” (STAC + DCAT + PROV)

The quickstart produces a minimal “boundary artifacts” set:

- **STAC** 📦 — geospatial catalog view of assets/layers  
- **DCAT** 🗂️ — dataset catalog view (distribution, license, publisher, access)  
- **PROV** ⛓️ — lineage view (inputs → activities → outputs, with agents)

Checksums are the *byte-level anchor* for that system:

- **In PROV:** a checksum can uniquely identify an output entity (“this exact file”)  
- **In DCAT:** a distribution can include a checksum/digest so users verify downloads  
- **In STAC:** assets can carry integrity metadata (via extension/custom fields) so map layers remain verifiable

> 🧩 Practical mental model:  
> **Triplet answers “what is it + where did it come from?”**  
> **Checksums answer “is this the exact same thing?”**

---

## 🧾 Receipts vs. Manifests (and why both matter)

### 1) File receipts (byte-for-byte) 🧾
A `checksums.sha256` file is the simplest, strongest “did the bytes change?” proof.

### 2) Run manifest digests (semantic + reproducible) 🧩
For JSON/YAML manifests, whitespace and key ordering can cause accidental diffs.
A common pattern is:

- **Canonicalize JSON** (e.g., RFC 8785 “JSON Canonicalization Scheme”)  
- Compute digest on canonical bytes  
- Store digest back into the manifest as a self-fingerprint

<details>
<summary>📄 Example (illustrative) run manifest shape</summary>

```json
{
  "run_id": "2026-01-21T12:34:56Z__minimal_triplet",
  "inputs": [{"uri": "...", "sha256": "..." }],
  "outputs": [{"path": "out/triplet/prov.jsonld", "sha256": "..."}],
  "tool_versions": {"python": "3.x", "pipeline": "v0.x"},
  "canonical_digest": "sha256:<computed_over_canonical_json>"
}
```
</details>

---

## 🛡️ Governance + security notes

### ✅ Fail-closed gates
In KFM-style workflows, policy checks should block promotion/merge/deploy if:
- checksums mismatch,
- required metadata is missing (license, source, sensitivity label, etc.),
- provenance artifacts are incomplete (triplet missing),
- or outputs lack required citations (for AI-generated artifacts).

### 🔏 Supply-chain integrity (optional / future path)
A mature version of this pattern can add:
- signed build/run attestations (SLSA-style),
- SBOM attachments,
- signing & verification workflows (e.g., Sigstore-style transparency),
- publishing artifacts with content digests (OCI registry / ORAS-style workflows).

---

## 🧭 What checksums *do not* do (important)

Checksums prove **integrity**, not **privacy**.

- They do **not** prevent sensitive data leakage.
- They do **not** enforce permissions or redaction.
- They do help you prove that a published artifact hasn’t been silently altered.

So: use checksums **alongside** classification rules, FAIR/CARE governance, and access control. 🔐🌿

---

## 🧯 Troubleshooting

### “FAILED” / mismatch
Most common causes:
- the file was regenerated (legit change),
- line endings changed (`CRLF` vs `LF`) for text formats,
- JSON formatting changed (pretty-print, key order),
- compression/container changed (zip/geo-package rebuild),
- paths in `checksums.sha256` are being resolved from the wrong working directory.

✅ Recommended response:
1. Identify what changed.
2. If change is expected, regenerate **triplet + checksums** together.
3. If change is unexpected, treat it as a pipeline integrity failure and investigate.

### Missing files
If `checksums.sha256` references a file that isn’t present:
- you may be verifying from the wrong folder,
- or the out directory is incomplete,
- or the run didn’t finish.

---

## 📚 Design inputs used to shape this README

This README follows the KFM “auditable, provenance-first” approach and pulls patterns from:
- KFM architecture + UI transparency expectations
- data intake integrity gates (SHA-256 receipts)
- evidence manifests + provenance integration
- dev/provenance mapping (CI → PROV)
- supply chain attestation proposals (SLSA/SBOM/signing)
- research reproducibility protocols (include checksums)
- privacy/governance reminders (integrity ≠ privacy)
- reference libraries (AI / data management / geospatial / programming)

<details>
<summary>📖 Full project file list (so this README stays aligned with the whole system)</summary>

- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation
- Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design
- Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖
- Kansas Frontier Matrix – Comprehensive UI System Overview
- 📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide
- 🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals
- Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM)
- Additional Project Ideas
- AI Concepts & more (reference library / portfolio)
- Data Management – Theories / Architectures / Data Science / Bayesian Methods (reference library / portfolio)
- Various programming languages & resources (reference library / portfolio)
- Maps / GoogleMaps / Virtual Worlds / Archaeological / Computer Graphics / Geospatial WebGL (reference library / portfolio)

</details>

---

## ✅ Definition of Done (for this checksums folder)

- [x] Explains what checksums are and why we keep them 🔐  
- [x] Gives copy/paste verification commands for Linux/macOS/Windows 🧪  
- [x] Connects checksums to STAC/DCAT/PROV “evidence triplet” ⛓️  
- [x] Clarifies integrity ≠ privacy (FAIR/CARE still required) 🌿  
- [ ] (Optional) Add `checksums.json` schema and example 🧩  
- [ ] (Optional) Add signing/attestation workflow (cosign/Sigstore/SLSA) 🛡️  


