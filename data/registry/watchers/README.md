# KFM Watchers Registry (data/registry/watchers)

![Governed Artifact](https://img.shields.io/badge/KFM-governed%20artifact-2b6cb0)
![Fail-Closed](https://img.shields.io/badge/policy-fail--closed-critical)
![Evidence-First](https://img.shields.io/badge/evidence-first-important)

> [!IMPORTANT]
> This directory defines the **governed registry of Watchers**: machine-readable *definitions* for automated “upstream monitors” that detect material changes in external providers and initiate ingestion via a **PR-driven, fail-closed pipeline**.
>
> Watchers are treated as **first-class catalog objects**: discoverable, attestable, and auditable.

---

## 1) Why this exists

KFM uses Watchers to turn “data drift in the world” into controlled, reviewable changes in the KFM knowledge base:

- **Watcher detects change** (material change rules applied).
- **Opens PR** containing the proposed data update + receipts + catalog artifacts.
- **CI validates** (schemas, STAC/DCAT/PROV, policy, signatures, reproducibility).
- **Registry update** is merged only if **all gates pass**.
- **Attestations/signatures** make the whole chain auditable.

This is the “Watcher → PR → CI → Registry → Attestations” backbone described in KFM’s Feb-2026 integration work, designed to be “runnable today” and to keep governance enforceable at merge time.

---

## 2) Non‑negotiable invariants this folder MUST support

These are system-level contracts (not optional conventions):

1. **Fail-closed**: if a required proof/field/signature/policy decision is missing → deny promotion and deny merge.
2. **Trust membrane**: Watchers do not grant the UI any bypass; UI never talks to databases directly.
3. **Promotion requires catalogs**: dataset promotion requires **STAC/DCAT/PROV** artifacts (as applicable) and they must validate.
4. **Evidence-first**: downstream consumers (including Focus Mode) must be able to resolve evidence references (prov://, stac://, dcat://, etc.) to human-readable evidence views.

> [!NOTE]
> This README documents the **folder contract** for `data/registry/watchers/`. If your repository already has a different naming convention, keep the semantics and update filenames consistently—but do not weaken the invariants.

---

## 3) Directory layout

The registry is designed to be **both human-reviewable and machine-validated**.

```text
data/registry/watchers/
├─ README.md                         # you are here
├─ registry.json                     # registry index (list of watcher entries + integrity metadata)
├─ registry.dcat.jsonld              # DCAT wrapper publishing the registry as a dataset
├─ registry.signature.json           # registry-level signature/attestation reference bundle
│
├─ watchers/                         # individual watcher entry documents (one per watcher)
│  ├─ kfm.watcher.<...>.v1.json
│  └─ ...
│
├─ schema/                           # JSON Schemas (used by CI + tooling)
│  ├─ kfm.schema.watcher.v1.json
│  └─ kfm.schema.watcher_registry.v1.json
│
└─ policy/                           # optional policy overlays specific to watcher governance
   ├─ README.md
   └─ (rego bundles or references)
```

### What each file is for

| Path | Purpose | Must be present? | Consumed by |
|---|---|---:|---|
| `watchers/*.json` | Individual Watcher entries | ✅ | Orchestrator, CI validators, catalog UI/API |
| `registry.json` | Index/manifest for discoverability + integrity checks | ✅ | Orchestrator + registry publisher |
| `registry.dcat.jsonld` | Publishes Watchers Registry as a DCAT dataset/distribution | ✅ | Catalog services, evidence resolver |
| `registry.signature.json` | Registry signature/attestation references | ✅ | CI + clients verifying integrity |
| `schema/*.json` | JSON Schema validation for watcher entries/registry | ✅ | CI + tooling |

---

## 4) What is a Watcher?

A **Watcher** is a governed definition of:

- what to monitor (`endpoint`)
- how to monitor (`poll` or `webhook`)
- how to decide if a change matters (`policy` / materiality rules)
- what artifacts are produced (`outputs`)
- how to identify and trust the definition (`spec_hash`, `signature_ref`)

A Watcher is **not** a “cron job script” in this directory. The runnable implementation lives elsewhere (pipeline/orchestrator code). This registry holds the *governed spec*.

---

## 5) Watcher Entry contract (kfm.schema.watcher.v1)

### 5.1 Required fields (MUST)

The Feb-2026 Watchers Registry work specifies that Watcher JSON Schema requires:

- `watcher_id`
- `endpoint`
- `poll`
- `policy`
- `outputs`
- `spec_hash`
- `signature_ref`

This README makes that requirement explicit and adds safe defaults that keep CI and audits deterministic.

### 5.2 Field dictionary

| Field | Type | Required | Constraints | Meaning |
|---|---:|---:|---|---|
| `watcher_id` | string | ✅ | Stable, globally unique; **versioned** | Canonical ID for the watcher |
| `endpoint` | object | ✅ | No secrets stored inline | Target to monitor + fetch strategy |
| `poll` | object | ✅ | Must be unambiguous schedule | How the watcher runs (cron, interval, webhook) |
| `policy` | object | ✅ | Must reference governed policy packs | Materiality + governance rules |
| `outputs` | array | ✅ | Must declare produced artifact types | What the watcher produces/promotes |
| `spec_hash` | string | ✅ | `sha256:<64hex>` | Deterministic hash of the watcher spec (see §6) |
| `signature_ref` | string | ✅ | Must be resolvable reference | Where to verify integrity of this watcher entry |

### 5.3 Recommended fields (SHOULD)

| Field | Type | Why it matters |
|---|---:|---|
| `title` / `description` | string | Human reviewability in PRs/catalog UI |
| `owner.team` / `owner.contact` | object | Accountability + on-call routing |
| `tags` | array | Search/discovery |
| `enabled` | boolean | Kill-switch at the entry level (in addition to global kill-switch) |
| `created_at` / `updated_at` | string (ISO 8601) | Audit-friendly change history |
| `deprecation` | object | Safe retirement without breaking references |
| `rate_limit` | object | Provider compliance (backoff, quotas) |

> [!WARNING]
> **Do not store secrets** (API keys, tokens, credentials) inside Watcher entries. Use an `auth_ref` pattern (e.g., a secret name in Vault/KMS) and keep secrets in approved secret stores only.

---

## 6) `spec_hash` standard for Watchers

### 6.1 Goal

`spec_hash` exists to make watcher definitions:

- **deterministic** (reproducible across CI and machines)
- **diffable** (PR gate can validate “this spec is exactly what we reviewed”)
- **auditable** (proves equivalence even when filenames/formatting vary)

### 6.2 Definition (normative in this folder)

For watcher entries in this directory:

- Let `spec` = the Watcher entry object **with the following keys removed**:
  - `spec_hash`
  - `signature_ref`
- Canonicalize `spec` using **RFC 8785 JSON Canonicalization Scheme (JCS)**.
- Compute:

```text
spec_hash = "sha256:" + hex( SHA-256( JCS(spec) ) )
```

> [!NOTE]
> This aligns with the KFM guidance that `spec_hash` should be `sha256(JCS(spec))` and encourages adding schema identity/versioning (e.g., `spec_schema_id`, `spec_recipe_version`) to prevent “hashes that mean different things” across contexts.

### 6.3 Enforcement (CI MUST)

CI must:
- recompute `spec_hash` from the entry document
- fail if the stored `spec_hash` does not match
- fail if the entry is not valid against `kfm.schema.watcher.v1`

---

## 7) `signature_ref` standard for Watchers

### 7.1 Goal

`signature_ref` is the pointer that allows a verifier to answer:

> “Can I trust that this watcher entry and/or registry distribution is authentic and untampered?”

### 7.2 What `signature_ref` may point to

This repository allows `signature_ref` to be expressed as a URI-like reference to one of the following verification mechanisms:

- **Sigstore-style**: a reference to a transparency-log entry / attestation
- **OCI referrers**: an OCI digest for the watcher/registry artifact plus attached attestation
- **JWS**: a JSON Web Signature stored alongside the distribution

Because KFM standards explicitly note that the signing mechanism decision may be JWS vs Sigstore attestation, this README defines a *neutral* reference field (`signature_ref`) while requiring resolvability and verification in CI.

### 7.3 Minimum requirements (MUST)

- `signature_ref` MUST be a stable string and MUST be resolvable by KFM’s evidence resolver or verification tooling.
- CI MUST verify the referenced signature/attestation for:
  - the watcher entry file (or its digest-addressed equivalent), and/or
  - the registry dataset distribution (`registry.json` + DCAT wrapper), depending on packaging.

---

## 8) End-to-end flow

### 8.1 High-level flow (Mermaid)

```mermaid
flowchart LR
  W[Watcher run] -->|detects upstream change| M[Materiality decision]
  M -->|not material| N[No PR; record heartbeat receipt]
  M -->|material| PR[Open PR: data + receipts + catalogs]

  PR --> CI[CI acceptance harness]
  CI -->|pass| MERGE[Merge allowed]
  CI -->|fail| BLOCK[Merge blocked (fail-closed)]

  MERGE --> PUB[Publish artifacts (OCI/digest pinned)]
  PUB --> ATTEST[Attach attestations + signatures]
  ATTEST --> REG[Update Watchers Registry + DCAT wrapper]
```

### 8.2 CI acceptance harness responsibilities

The Feb-2026 acceptance harness concept includes:

- STAC/DCAT/PROV validation
- Policy tests (OPA/Rego via conftest)
- Signature verification (e.g., cosign verify)
- `spec_hash` reproducibility check

This directory is structured so CI can run those checks deterministically.

---

## 9) How to add or update a watcher (PR-driven workflow)

> [!IMPORTANT]
> **All changes to Watchers Registry content must flow through PRs**. No direct commits to main.

### Step-by-step

1. **Create or edit** a watcher entry:
   - `data/registry/watchers/watchers/<watcher_id>.json`

2. **Validate schema locally** (recommended):
   - Validate against `schema/kfm.schema.watcher.v1.json`

3. **Compute and set `spec_hash`**:
   - Use RFC 8785 JCS canonicalization of the watcher spec (excluding `spec_hash` + `signature_ref`)
   - Store `spec_hash` in the watcher entry

4. **Set `signature_ref`**:
   - If using a signing system that only runs in CI, set `signature_ref` to the expected verification reference format and let CI update it.
   - If signing is performed before PR, include the resolvable signature reference.

5. **Update `registry.json`**:
   - Add/update an index entry for the watcher (including watcher_id, path, spec_hash, signature_ref).

6. **Open PR**:
   - PR description must include:
     - what changed
     - why it changed (materiality rationale)
     - links to receipts/run manifests if the PR is generated by an automated watcher run

7. **CI must pass** (merge-blocking):
   - schema validity
   - spec_hash reproducibility
   - registry signature verification
   - policy gates

8. **Merge results in published registry dataset**:
   - `registry.dcat.jsonld` stays in sync with `registry.json`
   - registry-level signature bundle updated

---

## 10) Promotion & validation gates (what Watchers must satisfy)

Watcher-driven ingestion must align with KFM’s ingestion workflow and minimum validation gates:

### 10.1 Ingestion workflow (raw → work → processed)

- **Discover** upstream capabilities and auth needs
- **Acquire** incrementally where possible (diff/snapshot patterns)
- **Normalize** into canonical encodings, geometry (WGS84), and time (ISO 8601)
- **Validate** schema, geometry, time sanity, license/policy
- **Enrich** join keys and entity resolution candidates
- **Publish** to processed + update DCAT/STAC/PROV + refresh indexes

### 10.2 Minimum validation gates (MUST)

A watcher run MUST NOT promote or recommend promotion unless:

- Schema validation passes (required fields, type coercion documented)
- Geometry validity and bounds checks pass (when geospatial)
- Temporal consistency checks pass
- License/attribution is captured in DCAT
- Sensitivity classification is set and enforced
- Provenance completeness is present: promoted artifacts have a PROV chain + deterministic checksums

> [!WARNING]
> If the dataset is sensitive (e.g., precise archaeological site locations), watchers must follow policy labels and produce redacted derivatives with explicit provenance. Never publish precise restricted geometry into public zones.

---

## 11) Policy hooks: materiality + provenance guard

### 11.1 Materiality rules (provider-aware)

Watchers MUST reference a materiality policy pack (e.g., `kfm.policy.materiality_rules.v1`) rather than embedding ad-hoc thresholds in code.

Rationale:
- thresholds vary by provider and cadence
- governance review must be possible
- “when to open a PR” is a policy decision, not a developer whim

### 11.2 Provenance guard

Watchers MUST also reference a provenance guard policy pack (e.g., `kfm.policy.provenance_guard.v1`) to enforce:

- receipts present
- required attestations present
- signatures valid
- fail-closed on missing evidence

---

## 12) Operational standards

### 12.1 Conditional fetch (preferred)

When the provider supports it, watchers SHOULD use:
- `ETag` + `If-None-Match`
- `Last-Modified` + `If-Modified-Since`

This reduces load, respects provider limits, and makes “no change” runs cheap.

### 12.2 Backoff / rate-limit compliance

Watcher runtime implementations must:
- respect provider rate limits
- implement exponential backoff
- cache capability metadata when available

### 12.3 SLO & health gating (recommended)

Real-time or high-cadence feeds SHOULD define:
- freshness SLOs
- dedup fingerprints
- “stale feed” promotion blocks

---

## 13) Definition of Done checklist (adding a watcher)

- [ ] Watcher entry file exists under `watchers/` and validates against schema
- [ ] `spec_hash` recomputes deterministically (CI confirms)
- [ ] `signature_ref` is resolvable and verifiable (CI confirms)
- [ ] `registry.json` includes the watcher entry
- [ ] `registry.dcat.jsonld` updated and valid
- [ ] Registry signature bundle updated and verified
- [ ] Materiality policy reference present
- [ ] Provenance guard policy reference present
- [ ] Secrets are referenced via `auth_ref` only (no inline credentials)
- [ ] If sensitive: classification + redaction strategy documented and enforceable

---

## 14) Examples (copy/paste)

### 14.1 Example Watcher entry (JSON)

> [!NOTE]
> The `spec_hash` below is computed from the entry **excluding** `spec_hash` and `signature_ref`, using a deterministic JSON canonical form.

```json
{
  "watcher_id": "kfm.watcher.soils_ks_ssurgo_gnatsgo.v1",
  "spec_schema_id": "kfm.schema.watcher.v1",
  "spec_recipe_version": "1.0.0",
  "title": "Kansas soils: SSURGO + gNATSGO watcher",
  "endpoint": {
    "kind": "https",
    "uri": "https://example.invalid/usda/nrcs/soils/ssurgo-gnatsgo",
    "conditional_fetch": {
      "etag": true,
      "last_modified": true
    }
  },
  "poll": {
    "mode": "cron",
    "schedule": "0 6 * * *",
    "timezone": "UTC"
  },
  "policy": {
    "materiality_policy_id": "kfm.policy.materiality_rules.v1",
    "provenance_guard_policy_id": "kfm.policy.provenance_guard.v1",
    "classification": "public",
    "fail_closed": true,
    "kill_switch": {
      "env": "KFM_WATCHERS_KILL_SWITCH",
      "default": "off"
    }
  },
  "outputs": [
    {
      "kind": "dataset",
      "dataset_id": "kfm.dataset.soils_ks_ssurgo_gnatsgo",
      "catalogs": [
        "dcat",
        "prov",
        "stac"
      ],
      "zone": "processed"
    },
    {
      "kind": "run_manifest",
      "schema_id": "kfm.schema.run_manifest.v1",
      "zone": "work"
    }
  ],
  "owner": {
    "team": "data-stewards",
    "contact": "data-stewards@kfm.invalid"
  },
  "tags": [
    "soils",
    "kansas",
    "ssurgo",
    "gnatsgo"
  ],
  "spec_hash": "sha256:319f634dcd07ee225c57eea1d4b4f58004831007921ec96f428d12d0d2793ef2",
  "signature_ref": "sigstore://rekor/00000000-0000-0000-0000-000000000000"
}
```

### 14.2 Example registry index (`registry.json`)

```json
{
  "registry_id": "kfm.registry.watchers.v1",
  "registry_schema_id": "kfm.schema.watcher_registry.v1",
  "generated_at": "2026-02-14T00:00:00Z",
  "watchers": [
    {
      "watcher_id": "kfm.watcher.soils_ks_ssurgo_gnatsgo.v1",
      "path": "watchers/kfm.watcher.soils_ks_ssurgo_gnatsgo.v1.json",
      "spec_hash": "sha256:319f634dcd07ee225c57eea1d4b4f58004831007921ec96f428d12d0d2793ef2",
      "signature_ref": "sigstore://rekor/00000000-0000-0000-0000-000000000000"
    }
  ],
  "integrity": {
    "hash_alg": "sha256",
    "registry_hash": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  },
  "registry_signature_ref": "sigstore://rekor/11111111-1111-1111-1111-111111111111"
}
```

> [!CAUTION]
> `registry_hash` and `registry_signature_ref` are shown as examples. Your CI/publisher must compute and sign real values.

---

## 15) Related KFM governed entries (by ID)

These IDs are referenced by Watchers and/or their CI gates:

- `kfm.schema.watcher.v1` — Watcher Entry Schema
- `kfm.standard.watcher_registry.v1` — Signed Watchers Registry Standard
- `kfm.standard.spec_hash.v1` — Deterministic spec hashing (RFC 8785 JCS)
- `kfm.pattern.watcher_to_registry.v1` — Watcher → PR → CI → Registry → Attestations
- `kfm.policy.materiality_rules.v1` — Provider-aware materiality thresholds
- `kfm.policy.provenance_guard.v1` — Promotion guard (deny-by-default; fail-closed)
- `kfm.standard.promotion_contract.v1` — Promotion contract (receipts + attestations + signatures + kill-switch)

---

## 16) Governance & sensitivity handling

Watchers must respect KFM’s sensitivity posture:

- Classify datasets (`public`, `restricted`, `sensitive-location`, etc.)
- Produce redacted derivatives with explicit provenance when needed
- Enforce access policy at the API boundary (trust membrane)
- Fail closed when policy is missing or ambiguous

If a watcher touches **sensitive-location** data, do not publish precise geometry into public zones; use generalized geometry for public views and keep precise geometry in restricted storage with policy enforcement.

---

## 17) Troubleshooting

### “CI says spec_hash mismatch”
- Ensure `spec_hash` is computed from the watcher entry with `spec_hash` + `signature_ref` removed.
- Ensure the canonicalization is RFC 8785 JCS (not “pretty JSON”).
- Ensure you didn’t accidentally change array ordering (arrays are order-sensitive).

### “CI says signature_ref not verifiable”
- Confirm the signing workflow wrote the attestation/signature and that the reference is resolvable.
- Confirm the verifier (cosign/JWS tooling) is pinned to expected versions.

### “Watcher keeps opening PRs for tiny changes”
- Adjust provider-aware materiality thresholds in `kfm.policy.materiality_rules.v1` rather than hardcoding logic in the watcher implementation.
- Add explicit “no-op” receipt behavior for non-material deltas.

---

