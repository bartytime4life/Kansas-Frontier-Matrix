# 🔐 Signatures (PROV Integrity & Authenticity)

![PROV-O](https://img.shields.io/badge/PROV--O-lineage-2ea44f) ![OPA+Conftest](https://img.shields.io/badge/Policy-OPA%20%2B%20Conftest-1f6feb) ![Cosign/Sigstore](https://img.shields.io/badge/Signing-Cosign%20%2F%20Sigstore-f97316) ![Fail-Closed](https://img.shields.io/badge/Gates-Fail--Closed-critical)

> [!IMPORTANT]
> This folder is **tamper-evidence** (integrity + authenticity), not confidentiality.  
> If you need secrecy, use **encryption/access control** _before_ signing.

---

## 🧭 Purpose

This directory stores **cryptographic signature artifacts** that “seal” the provenance bundle for this experiment report.  
The goal is to make your `prov/` outputs:

- ✅ **Verifiable** (who signed it?)
- ✅ **Tamper-evident** (did anything change?)
- ✅ **Promotable** (CI can **fail closed** if signatures are missing/invalid)
- ✅ **Queryable** (signature events can themselves be represented in **PROV-O**)

In the Kansas Frontier Matrix mindset, signatures are part of the **evidence-first** chain: data and outputs aren’t considered “published/promoted” until the provenance and governance checks are satisfied.

---

## ⚡ TL;DR Workflow

1) **Hash** the key provenance files (canonicalized when applicable) 🧾  
2) **Sign** those hashes 🔏  
3) **Verify** in CI (policy gate) 🚦  
4) **Record** the signing event in PROV (optional but recommended) 🧬  
5) **Promote** only if everything passes ✅

---

## 🧩 Where this sits in the report tree

Typical placement inside the example report:

```text
📦 (example_report_tree)/
└─ 🧬 prov/
   ├─ 📄 prov.jsonld                  # provenance bundle (JSON-LD)
   ├─ 🧾 checksums/                   # optional: raw digests (sha256, etc.)
   └─ 🔐 signatures/                  # 👈 you are here
      └─ 📄 README.md
```

> [!TIP]
> Prefer signing **digests/manifests** over signing ad-hoc files individually.  
> It scales better as your experiment grows.

---

## 📦 What belongs in `prov/signatures/`

This is a **template-friendly** directory. Use what matches your signing approach.

| Item | Recommended name(s) | What it’s for |
|---|---|---|
| Signature manifest | `signature-manifest.json` | Single source of truth: what was signed, digests, signer identity, timestamps |
| Signature bundle(s) | `*.sig`, `*.bundle`, `*.att` | Tool output (e.g., Sigstore/Cosign bundle, detached signature, attestation) |
| Public keys (if key-based) | `public-keys/*.pem` / `public-keys/*.pub` | Verification material safe to commit |
| Identity proof (if needed) | `identities/*` | Optional: recorded identities (OIDC subject, CI identity, etc.) |
| Verification logs | `verification/*.json` | Optional: machine logs of verification runs (useful for audits) |

> [!NOTE]
> **Never commit private keys** 🔥  
> Only commit **public keys** and verification artifacts.

---

## 🧾 Signature Manifest (recommended)

A manifest makes signatures **auditable** and **policy-checkable**.

Example structure (adapt as needed):

```json
{
  "schema": "dev_prov.signature_manifest.v1",
  "created_at": "2026-01-22T00:00:00Z",
  "signed_targets": [
    {
      "path": "../prov.jsonld",
      "media_type": "application/ld+json",
      "canonicalization": "RFC8785",
      "digest": {
        "alg": "sha256",
        "value": "<hex>"
      },
      "signature": {
        "tool": "cosign",
        "type": "bundle",
        "path": "./prov.jsonld.bundle"
      },
      "signer": {
        "mode": "keyless-or-keyed",
        "identity": "ci@your-org / oidc-subject / key-id"
      }
    }
  ]
}
```

✅ Benefits:
- One policy can assert: **“Every `prov.jsonld` must have a valid signature entry.”**
- You can diff manifest changes like any other artifact (Git-friendly) 🧠

---

## 🧮 Canonical Hashing (determinism matters)

Different JSON formatting can change bytes, breaking signatures.  
For JSON/JSON-LD, canonicalize first (e.g., **RFC 8785**) so everyone hashes the **same normalized bytes**.

**Rule of thumb:**
- 📄 JSON / JSON-LD → **canonicalize → hash → sign**
- 🗃️ Binary artifacts (GeoTIFF, Parquet, PMTiles, model weights) → **hash bytes → sign digest**

> [!WARNING]
> If you sign a file that later gets “pretty-printed,” line-ending normalized, or re-ordered, verification will fail — even if the meaning is the same.

---

## ✍️ Signing Workflows

### A) CI / Keyless signing (recommended) 🤖✅
Best for “Detect → Validate → Promote” pipelines where CI produces artifacts and must attest to them.

**Conceptual steps:**
- CI generates `prov.jsonld`
- CI computes canonical digest
- CI signs digest (keyless identity, or org key)
- CI verifies before promote

> [!TIP]
> Pair this with **policy-as-code** gates (OPA + Conftest) to enforce “no signature, no merge.”

---

### B) Local / Key-based signing (dev + offline) 🧑‍💻🔏
Useful for offline or air-gapped validation, or when you need long-lived keys.

**Pattern:**
- Put **public keys** in `public-keys/`
- Keep **private keys** in your secrets manager / secure local storage
- Generate signatures and commit them alongside the provenance bundle

---

## ✅ Verification & Policy Gates (fail closed)

Verification should happen in at least two places:

- **Local verify** (before you publish)
- **CI verify** (before you merge/promote)

> [!IMPORTANT]
> Governance gates should be **fail-closed**: missing/invalid signature ⇒ **reject promotion**.

**Policy checks typically enforce:**
- `prov.jsonld` exists ✅
- signature manifest exists ✅
- signatures verify ✅
- provenance is updated when derived outputs change ✅
- no secrets/credentials appear in signed artifacts ✅

---

## 🧬 Modeling the signing event in PROV-O (recommended)

Treat signatures as first-class provenance objects:

- The signed artifact = `prov:Entity`
- The signature file/bundle = `prov:Entity`
- The signing action = `prov:Activity`
- The signer (CI runner, maintainer, bot) = `prov:Agent`

Example (illustrative JSON-LD skeleton):

```json
{
  "@context": "https://www.w3.org/ns/prov.jsonld",
  "entity": {
    "ex:prov_bundle": { "prov:label": "Provenance Bundle", "prov:type": "prov:Entity" },
    "ex:prov_bundle_sig": { "prov:label": "Signature for prov bundle", "prov:type": "prov:Entity" }
  },
  "activity": {
    "ex:signing": {
      "prov:label": "Sign provenance bundle",
      "prov:type": "prov:Activity",
      "prov:startTime": "2026-01-22T00:00:00Z"
    }
  },
  "agent": {
    "ex:ci": { "prov:label": "CI Signer", "prov:type": "prov:Agent" }
  },
  "used": {
    "_:use1": { "prov:activity": "ex:signing", "prov:entity": "ex:prov_bundle", "prov:role": "input" }
  },
  "wasGeneratedBy": {
    "_:gen1": { "prov:entity": "ex:prov_bundle_sig", "prov:activity": "ex:signing" }
  },
  "wasAssociatedWith": {
    "_:assoc1": { "prov:activity": "ex:signing", "prov:agent": "ex:ci" }
  }
}
```

✅ Why do this?
- You can query: “Which signer produced this signature?”  
- You can trace provenance integrity alongside data lineage.

---

## 🧱 OCI Artifact Flows (optional, but powerful) 📦🚀

If you store artifacts in an **OCI registry** (via ORAS) and sign with **Cosign**, signatures may live in the registry as referrers/attachments.

This folder can still be useful as:
- 📌 an **offline export** of signature bundles for audits
- 🧾 a **human-readable manifest** for reviewers
- 🧪 a **portable verification kit** for reproductions

---

## 🔒 Sensitive Data Notes (don’t sign secrets)

Before signing, ensure the signed targets do **not** contain:
- API keys, tokens, credentials
- sensitive coordinates or protected site locations (if governed)
- private identifiers that should not be distributed

> [!TIP]
> If you must prove integrity of sensitive content, sign a **redacted derivative** or a **hashed manifest** instead of the raw dataset.

---

## 🧠 Common Pitfalls & Fixes

- **Pitfall:** Signing JSON before canonicalization  
  ✅ Fix: Canonicalize (RFC8785) then hash.

- **Pitfall:** Recomputing artifacts in a non-deterministic pipeline  
  ✅ Fix: Pin versions, record tool versions, and generate stable run manifests.

- **Pitfall:** Overwriting signatures  
  ✅ Fix: Treat signatures as **append-only**. New artifact version ⇒ new signature.

- **Pitfall:** Mixing “who signed” with “who authored”  
  ✅ Fix: Record both. Author in PROV agent; signer in signing activity agent.

---

## 📚 Glossary

- **Digest / Hash** 🧾: A deterministic fingerprint of content (e.g., SHA-256).
- **Detached signature** 🧷: Signature stored separately from the signed file.
- **Bundle** 🎒: A signature artifact that may include extra verification material (identity, cert chain, timestamps).
- **Attestation** 📜: A signed statement about an artifact (e.g., provenance/SBOM claims).
- **Fail-closed** 🚦: If checks can’t prove compliance, the change is rejected.

---

## ✅ Template TODOs (fill these in)

- [ ] Decide which files are “signature-required” (minimum: `prov.jsonld`)
- [ ] Choose signing mode: keyless CI / keyed signing / both
- [ ] Add CI step: verify signatures before Promote
- [ ] Add OPA/Conftest rule(s): missing/invalid signatures fail the pipeline
- [ ] Record signer identity + tool versions in the manifest
