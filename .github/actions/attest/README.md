<div align="center">

# 🧾 `.github/actions/attest` — Build Attestations

**Cryptographic “receipts” for what we build** 🧬  
So KFM artifacts (containers, zips, bundles) stay **traceable, auditable, and provenance-first**.

<p>
  <img alt="Type" src="https://img.shields.io/badge/GitHub%20Action-Composite-informational?style=for-the-badge&logo=githubactions">
  <img alt="Security" src="https://img.shields.io/badge/Supply%20Chain-Attestation-blue?style=for-the-badge&logo=shield">
  <img alt="Policy" src="https://img.shields.io/badge/Governance-Fail%20Closed-critical?style=for-the-badge&logo=checkmarx">
</p>

</div>

---

## 🎯 Purpose

This action creates and uploads **build attestations** for KFM outputs—most commonly:

- 🐳 **Container images** (by **digest**)
- 📦 **Release artifacts** (e.g., `.zip`, `.tar.gz`, dataset bundles)
- 🧩 **Build metadata** that ties artifacts back to the workflow run

In KFM terms: this is one of the “trust rails” that keeps the system **provenance-first** and **auditable**—so the repo doesn’t become a black box over time. 🧭

> [!IMPORTANT]
> Attestations are **not** a replacement for KFM dataset provenance (`data/provenance`, STAC/DCAT).  
> They are the *software supply-chain* side of the story.

---

## ✅ What this action does

- 🔐 Uses GitHub OIDC (recommended) to generate a **signed build attestation**
- 🧾 Records *what* was built and *from where* (commit + workflow run)
- 📌 Targets a build **subject** (file or image digest)
- ☁️ Uploads the attestation so it can be verified later (release/package provenance)

> [!NOTE]
> Exact behavior depends on this folder’s `action.yml` implementation.  
> This README documents the **intended contract**. If you change the contract, update this file in the same PR. ✅

---

## 🧠 Why KFM cares

KFM is designed as a pipeline → catalog → database → API → UI system where trust comes from traceability.  
Build attestations extend that philosophy to **binaries and containers**—so deployments can answer:

- “Which commit produced this image?”
- “Was it built by our CI or by someone’s laptop?”
- “What workflow and runner built it?”

This supports KFM’s governance posture (deny-by-default / “fail closed” when provenance is uncertain). 🛡️

---

## 🔐 Required workflow permissions

Most attestation flows require these permissions in the calling workflow:

```yaml
permissions:
  contents: read
  id-token: write        # OIDC signing
  attestations: write    # upload attestations (GitHub attestation store)
```

> [!TIP]
> Keep permissions scoped to the job that needs them (least privilege). 🔒

---

## 🧩 Inputs

Inputs vary by implementation, but the action is expected to support **at least one subject type**:

### Common subject options

| Input | Required | Example | Notes |
|------|----------|---------|------|
| `subject-path` | Sometimes | `dist/kfm-web.zip` | Attest a file produced in the workflow. |
| `subject-name` | Sometimes | `ghcr.io/<owner>/kfm-api` | Logical name (useful for images). |
| `subject-digest` | Sometimes | `sha256:...` | **Preferred for containers**. Avoid tags. |
| `predicate-type` | Optional | `slsa` / `provenance` | If supported; default should be sane. |
| `extra-metadata-path` | Optional | `.build/build-info.json` | If supported; pairs well with `build-info/`. |

> [!IMPORTANT]
> If you’re attesting a container, **attest the digest** (`sha256:...`), not a tag like `:latest`. Tags move; digests don’t. 📌

---

## 📤 Outputs

If your implementation exposes outputs, the typical ones are:

| Output | Example | Meaning |
|--------|---------|---------|
| `attestation-id` | `1234567890` | Identifier for the attestation record. |
| `attestation-url` | *(url)* | Link to where it can be inspected/verified. |

---

## 🚀 Usage examples

### 1) 🐳 Attest a container image (recommended)

```yaml
jobs:
  build_api:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      id-token: write
      attestations: write

    steps:
      - uses: actions/checkout@v4

      # Build & push image (your repo likely uses .github/actions/docker-build)
      - name: Build image
        uses: ./.github/actions/docker-build
        id: build
        with:
          image: ghcr.io/${{ github.repository }}/kfm-api
          tags: latest

      - name: Attest build (image digest)
        uses: ./.github/actions/attest
        with:
          subject-name: ghcr.io/${{ github.repository }}/kfm-api
          subject-digest: ${{ steps.build.outputs.digest }}
```

### 2) 📦 Attest a release artifact (zip/tar)

```yaml
- name: Build web bundle
  run: |
    npm ci
    npm run build
    tar -czf dist/kfm-web.tar.gz build/

- name: Attest build (file)
  uses: ./.github/actions/attest
  with:
    subject-path: dist/kfm-web.tar.gz
```

### 3) 🧬 Pair with SBOM + provenance guard

A solid KFM supply-chain chain-of-custody usually looks like:

1) 🧱 `setup-kfm/` (tooling + deps)  
2) 🐳 `docker-build/` (or build step)  
3) 🧾 `sbom/` (generate SBOM)  
4) 🧾 `attest/` (attest build output)  
5) 🛡️ `provenance-guard/` + `policy-gate/` (enforce governance)

---

## 🧯 Troubleshooting

### “Permission denied / OIDC token not available”
- Ensure the job has:
  - `permissions: id-token: write`
  - `permissions: attestations: write`
- Some events/fork PR contexts restrict OIDC usage. Consider running attestation only on trusted branches.

### “Attestation created but can’t be verified”
- Verify you’re attesting the **final artifact** (post-signing, post-compression).
- For containers: attest the **digest** emitted by the push step, not a tag.

### “Attestation step runs before artifact exists”
- Put `attest` **after** the build step that generates the file/image digest.
- Prefer passing values via `id: build` step outputs.

---

## 🛡️ Security notes

- ✅ Attestations strengthen integrity, but they do **not** prove the artifact is safe—only where it came from.
- 🚫 Do not embed secrets in build metadata. Treat “provenance” as public.
- 🧪 If the build is non-deterministic, attestations still help, but reproducibility becomes harder—aim for deterministic builds where feasible.

---

## 🔗 Related actions

- 🧾 **SBOM generation** → [`../sbom/`](../sbom/)
- 🧱 **Build metadata** → [`../build-info/`](../build-info/)
- 🛡️ **Policy enforcement** → [`../policy-gate/`](../policy-gate/) and [`../governance-scan/`](../governance-scan/)
- 🧾 **PR provenance checks** → [`../pr-provenance/`](../pr-provenance/) and [`../provenance-guard/`](../provenance-guard/)

---

## 🧷 Maintainer notes

If you modify this action:

- Update this README ✅  
- Keep the contract “fail closed” (missing subject/digest should error) 🛑  
- Prefer digest-based subjects (immutability) 📌

---

## 📚 References

[^kfm_blueprint]: *Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint* (project library). Emphasizes provenance-first design, governance, and traceable outputs.