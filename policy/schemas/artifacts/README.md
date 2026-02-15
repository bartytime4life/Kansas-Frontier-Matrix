<!--
path: policy/schemas/artifacts/README.md
governance: governed_artifact
-->

# KFM Policy + Schema Artifacts (Governed)

**Status:** 🛡️ Governed · 🔒 Fail‑Closed · 🧾 Provenance‑First · ✅ CI‑Gated

This directory contains **versioned, machine-verifiable artifacts** that enforce KFM’s governance contract:
OPA/Rego policy bundles + JSON Schemas + checksums/signatures + test vectors.

If you are looking for the *source* Rego or the *source* schema definitions, they are **upstream of this folder**
(implementation-specific). This folder is the **build output / release payload** that CI and runtime deployments
should consume.

---

## Why this exists

KFM’s credibility depends on *enforceable* invariants:

- **Fail closed (default deny):** missing inputs, missing policy data, missing metadata ⇒ **deny**.
- **Cite-or-abstain:** Focus Mode responses are allowed only when citations exist and sensitivity is OK.
- **Promotion gates:** datasets/citations are not publishable unless required evidence artifacts validate.
- **Auditability:** decisions must be attributable to a specific **policy+schema artifact digest**.

This folder is the “trust anchor” for policy + schema enforcement because it is:
- **immutable-by-convention**, and
- **checksum/signed**, so CI/runtime can verify exactly what was enforced.

---

## What belongs here

### ✅ Included (expected)

- **OPA bundles** (compiled policy payloads)
- **JSON Schema bundles** (contracts used by validators, policy input/output, receipts)
- **Checksums** (`sha256`) for every bundle and manifest file
- **Signatures / attestations** (when enabled) for supply-chain verification
- **Test vectors** used in CI to prove “deny-by-default” and “cite-or-abstain” behaviors
- **Artifact manifest** that ties everything together (digests, versions, toolchain, source commit)

### 🚫 Not included (belongs elsewhere)

- Raw/processed datasets, STAC/DCAT/PROV catalogs (typically under `data/` or `releases/`)
- Application code (API/UI/pipelines)
- Secrets (keys, tokens, creds)

---

## Directory layout

> The names below are the **recommended** stable contract for this directory.  
> Keep it boring: deterministic paths enable deterministic CI and reproducible builds.

```text
policy/schemas/artifacts/
├─ README.md
├─ manifest/
│  ├─ artifact_manifest.v1.json
│  └─ artifact_manifest.v1.json.sha256
├─ bundles/
│  ├─ opa/
│  │  ├─ kfm-policy.bundle.tar.gz
│  │  └─ kfm-policy.bundle.tar.gz.sha256
│  └─ schemas/
│     ├─ kfm-schemas.bundle.tar.gz
│     └─ kfm-schemas.bundle.tar.gz.sha256
├─ signatures/                       # optional (recommended for releases)
│  ├─ kfm-policy.bundle.cosign.sig
│  ├─ kfm-policy.bundle.cosign.bundle
│  ├─ kfm-schemas.bundle.cosign.sig
│  └─ kfm-schemas.bundle.cosign.bundle
└─ test-vectors/
   ├─ focus_answer/
   │  ├─ allow.minimal.json
   │  ├─ deny.no_citations.json
   │  └─ deny.sensitivity_not_ok.json
   └─ policy_input/
      ├─ allow.public_dataset.json
      └─ deny.restricted_dataset_public_actor.json
```

---

## Artifact inventory (what CI/runtime consumes)

| Artifact | Path | Purpose | Must be immutable |
|---|---|---:|:---:|
| Artifact manifest | `manifest/artifact_manifest.v1.json` | Single source of truth: what was built, from what, with which digests | ✅ |
| OPA policy bundle | `bundles/opa/kfm-policy.bundle.tar.gz` | Runtime + CI policy evaluation (default deny) | ✅ |
| Schema bundle | `bundles/schemas/kfm-schemas.bundle.tar.gz` | Contract enforcement (validators, policy I/O, receipts, audit records) | ✅ |
| Checksums | `*.sha256` | Deterministic verification without network access | ✅ |
| Signatures (optional) | `signatures/*.cosign.*` | Supply-chain attestation for releases | ✅ |
| Test vectors | `test-vectors/**` | CI regression: prove deny-by-default + cite-or-abstain | ✅ |

---

## The “Promotion / Answer” contract this folder supports

### Focus Mode: cite-or-abstain (minimum contract)

**A FocusAnswer is only allowed when:**
- it contains **citations**, and
- it passes **sensitivity checks**, and
- it includes an **audit_ref** (so the response is traceable).

If evidence is insufficient, the system must **abstain** (return a structured refusal and still include `audit_ref`).

### Dataset access: default deny (minimum contract)

**A dataset is only accessible when:**
- it is `public`, OR
- the actor has an elevated role (e.g., `reviewer`/`admin`) consistent with policy rules.

> NOTE  
> Exact role names and sensitivity vocabulary must be treated as a controlled vocabulary and enforced consistently.

---

## Artifact manifest (required)

This manifest ties digests + versions together for auditability.

```json
{
  "manifest_version": "v1",
  "created_at": "YYYY-MM-DDTHH:MM:SSZ",

  "source": {
    "repo": "kfm-repo",
    "git_sha": "<commit>",
    "build_id": "<ci-run-id>"
  },

  "bundles": {
    "opa_policy_bundle": {
      "path": "bundles/opa/kfm-policy.bundle.tar.gz",
      "sha256": "sha256:<hex>",
      "policy_bundle_version": "v1.0.0"
    },
    "schemas_bundle": {
      "path": "bundles/schemas/kfm-schemas.bundle.tar.gz",
      "sha256": "sha256:<hex>",
      "schema_bundle_version": "v1.0.0"
    }
  },

  "toolchain": {
    "opa": "<version>",
    "conftest": "<version>",
    "schema_validator": "<tool+version>"
  }
}
```

---

## CI gates (merge-blocking expectations)

A PR that changes governed artifacts should fail if any of these checks fail:

- **OPA unit tests pass**
- **(Optional) Conftest policy tests pass** (if using conftest as the harness)
- **Schema validation passes** for policy inputs/outputs + receipts
- **Checksums match** for every file in `manifest/` and `bundles/`
- **(Optional) signatures verify** for bundles (when enabled)
- **Regression vectors pass** (deny-by-default, cite-or-abstain)
- **spec_hash reproducibility** holds for canonicalized specs (when receipts/manifests are present)

```mermaid
flowchart TD
  A[PR changes policy/schema sources] --> B[Build artifacts in CI]
  B --> C[OPA tests / Conftest tests]
  C -->|fail| X[❌ Merge blocked]
  C --> D[Validate JSON Schemas + test vectors]
  D -->|fail| X
  D --> E[Compute & verify sha256 checksums]
  E -->|fail| X
  E --> F[Verify signatures (optional)]
  F -->|fail| X
  F --> G[✅ Merge allowed]
```

---

## Versioning rules (do not improvise)

### Bundles
- Bundles **must** be content-addressed by checksum (sha256).
- A change to any policy/schema content ⇒ new bundle checksum.
- File naming should be stable; the checksum is the identity.

### Schemas
- JSON Schema `$id` values should be **versioned** (major version bumps for breaking changes).
- Prefer explicit semver (`v1`, `v2`, …) and keep old schemas available for audits.

### `spec_hash` (receipt determinism)
When receipts/manifests use `spec_hash`, it must be:
- `spec_hash = sha256(JCS(spec))`, where `spec` is validated against a schema-defined object.
- Include `spec_schema_id` + `spec_recipe_version` so hashes stay comparable across time.

---

## Local verification (recommended developer workflow)

> These commands are examples; wire them into your repo’s `make verify` or CI job.

```bash
# 1) Validate checksums
sha256sum -c manifest/artifact_manifest.v1.json.sha256
sha256sum -c bundles/opa/kfm-policy.bundle.tar.gz.sha256
sha256sum -c bundles/schemas/kfm-schemas.bundle.tar.gz.sha256

# 2) Run OPA unit tests (source paths vary by repo)
opa test <POLICY_SOURCE_DIR> -v

# 3) Run conftest (if your repo uses it as the harness)
conftest test <POLICY_SOURCE_DIR> -p <POLICY_SOURCE_DIR>
```

---

## Change control (PR checklist)

Any PR affecting policy/schema behavior must include:

- [ ] Updated source policy/schema definitions (not hand edits to bundles)
- [ ] Regenerated bundles + updated checksums
- [ ] Updated `artifact_manifest.v1.json`
- [ ] Added/updated unit tests and/or test vectors demonstrating expected deny/allow behavior
- [ ] Clear note if change is breaking (requires major version bump)
- [ ] Evidence that CI gates run and are merge-blocking

---

## Troubleshooting

### “CI denies everything”
- Confirm you did not remove required keys from policy input.
- Confirm bundle checksums match what CI expects.
- Confirm default-deny policies have an explicit allow path for the intended case.

### “Focus Mode answer rejected”
- Ensure `citations[]` is non-empty for non-abstain answers.
- Ensure `sensitivity_ok` is true and the citations are of allowed kinds.
- Ensure `audit_ref` exists on both allow and abstain outcomes.

### “Checksum mismatch”
- Bundles were rebuilt with different tool versions or non-deterministic inputs.
- Ensure canonicalization steps are deterministic and toolchain is pinned.

---

## Governance note

This directory is a **governed artifact surface**. Treat changes as production-impacting:
policy changes alter access; schema changes alter what can be published; both affect auditability.

If you are unsure whether a change is breaking or could weaken fail-closed behavior:
**default to deny** and add a test that proves the new behavior is safe.

