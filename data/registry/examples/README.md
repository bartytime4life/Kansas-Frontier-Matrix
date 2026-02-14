<!--
GOVERNED ARTIFACT (examples)
Path: data/registry/examples/README.md
Scope: Example-only, non-production. Copy/paste snippets to seed real registries.
-->

# KFM Registry Examples (data/registry/examples)

![Governed Artifact](https://img.shields.io/badge/KFM-governed%20artifact-blue)
![Examples](https://img.shields.io/badge/purpose-examples-informational)
![Fail-Closed](https://img.shields.io/badge/policy-fail--closed-critical)

This folder is a **self-contained example pack** for KFM’s governed registries.

It provides copy/paste-ready examples for:
- **KFM “entry registry” objects** (standards, schemas, playbooks, policy packs, patterns)
- **Watcher registry objects** (watcher definitions + a signed/DCAT-wrapped “watchers registry dataset”)
- **Run manifest / run receipt** example (what CI validates + what promotion gates depend on)
- **Policy-as-code** snippets (OPA/Rego) for “cite-or-abstain” and “fail-closed” gating

> [!IMPORTANT]
> **Examples are not production truth.** Production registries must be validated in CI and must not weaken KFM’s invariants (trust membrane, cite-or-abstain, fail-closed gates, promotion requires STAC/DCAT/PROV, etc.).  
> This README is intentionally “complete in one file” so it can be used even when the repo is missing other example files.

---

## Table of contents

- [What is a “registry” in KFM?](#what-is-a-registry-in-kfm)
- [How these examples map to KFM’s trust guarantees](#how-these-examples-map-to-kfms-trust-guarantees)
- [Suggested directory layout](#suggested-directory-layout)
- [Conventions](#conventions)
  - [IDs, filenames, and versioning](#ids-filenames-and-versioning)
  - [`spec_hash` (deterministic hashing) + signatures](#spec_hash-deterministic-hashing--signatures)
  - [Sensitivity & policy labels](#sensitivity--policy-labels)
- [Example pack](#example-pack)
  - [Example A — KFM entry proposal pack (YAML)](#example-a--kfm-entry-proposal-pack-yaml)
  - [Example B — Watcher definition (JSON)](#example-b--watcher-definition-json)
  - [Example C — Watchers registry DCAT wrapper (JSON-LD)](#example-c--watchers-registry-dcat-wrapper-json-ld)
  - [Example D — Run manifest / run receipt (JSON)](#example-d--run-manifest--run-receipt-json)
  - [Example E — OPA/Rego snippets (policy gates)](#example-e--oparego-snippets-policy-gates)
- [Validation workflow (reference)](#validation-workflow-reference)
- [How to add a new example](#how-to-add-a-new-example)
- [Troubleshooting](#troubleshooting)

---

## What is a “registry” in KFM?

In KFM, a **registry** is a *governed, machine-readable catalog of definitions* that other parts of the system rely on, such as:
- Schemas (what fields are required)
- Standards/contracts (what must be true to publish/promote)
- Policies (deny-by-default rules that block unsafe publishing)
- Watcher definitions (how upstream sources are monitored and transformed into receipts + catalogs)
- Playbooks/patterns (repeatable “runnable today” integration wiring)

A registry object is usually:
- **Versioned**
- **Validatable** (schema + policy)
- **Auditable** (provenance anchors)
- **Deterministically hashable** (`spec_hash`) and optionally **signable** (`signature_ref`)

---

## How these examples map to KFM’s trust guarantees

KFM’s “truth path” (conceptual) looks like this:

```mermaid
flowchart LR
  UP[Upstream provider] --> W[Watcher\npoll/webhook/hybrid]
  W --> R[Typed receipt\nrun_manifest / run_receipt]
  R --> CI[CI gates\nvalidators + OPA/Rego]
  CI -->|pass| PUB[Publish/Promote\n(digest-pinned, cataloged)]
  CI -->|fail| STOP[Fail closed\nmerge blocked]
  PUB --> API[KFM API\n(policy boundary)]
  API --> UI[Web UI + Story Nodes\nFocus Mode cite-or-abstain]
```

**What matters for this folder**:
- Registries and receipts are designed to support **fail-closed CI gates**
- Objects include fields for **license/rights**, **sensitivity**, and **provenance**
- Watcher specs are **discoverable** and can be **published as a signed DCAT dataset** (the “watchers registry dataset”)

---

## Suggested directory layout

> [!NOTE]
> The exact layout of *production* registries is repo-specific. This is a **suggested** layout that keeps “examples” separate from “live registries”.

```text
data/
└─ registry/
   ├─ examples/
   │  └─ README.md                          # ← you are here
   │
   ├─ kfm_entries/                          # standards/schemas/policies/playbooks/patterns (suggested)
   ├─ watchers/                             # watcher definitions (suggested)
   ├─ datasets/                             # dataset registry entries (suggested)
   └─ policy/                               # policy packs + tests (suggested)
```

---

## Conventions

### IDs, filenames, and versioning

**ID convention (recommended):**
- `kfm.<category>.<name>.v<major>`
  - Examples:
    - `kfm.standard.promotion_contract.v1`
    - `kfm.schema.run_manifest.v1`
    - `kfm.policy.provenance_guard.v1`
    - `kfm.watcher.example.http_etag.v1`

**Filename convention (recommended):**
- `ID` becomes filename-safe (dots kept or replaced), e.g.:
  - `kfm.standard.promotion_contract.v1.yaml`
  - `kfm.watcher.example.http_etag.v1.json`

**Versioning:**
- Use **SemVer** for entry content changes.
- Treat schema-breaking changes as a **major** bump (`v1 → v2`).

---

### `spec_hash` (deterministic hashing) + signatures

`spec_hash` is a deterministic SHA-256 hash over a canonicalized JSON “spec” object.

**Normative definition (recommended):**
- `spec_hash = sha256(JCS(spec))`
  - where `JCS` is RFC 8785 JSON Canonicalization Scheme (deterministic key ordering, no whitespace, stable encoding)
  - also include `spec_schema_id` and `spec_recipe_version` as explicit fields *alongside* the spec (so auditors know what rules produced the spec)  

> [!IMPORTANT]
> Do **not** include `spec_hash` inside the JSON object being hashed (that’s self-referential).  
> The examples below use a wrapper object that contains:
> - `spec_schema_id`
> - `spec_recipe_version`
> - `spec` (the hashed object)
> - `spec_hash` (hash of `spec`)
> - `signature_ref` (optional signature/attestation pointer)

#### Reference: compute `spec_hash` (Python)

```bash
python - <<'PY'
import json, hashlib

# Load a wrapper file and hash ONLY the `.spec` object.
doc = json.load(open("watcher.example.http_etag.v1.json", "r", encoding="utf-8"))
spec = doc["spec"]

canonical = json.dumps(spec, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
print(hashlib.sha256(canonical.encode("utf-8")).hexdigest())
PY
```

---

### Sensitivity & policy labels

KFM examples commonly use a coarse policy label taxonomy to keep “what’s safe to publish” explicit:
- `public`
- `restricted`
- `sensitive-location`

> [!WARNING]
> If a dataset includes **precise locations** or culturally restricted information, treat it as `restricted` or `sensitive-location`, and ensure the API/policy layer redacts or generalizes outputs before anything reaches the UI.

---

## Example pack

> [!TIP]
> You can copy each block into a separate file **exactly as named** in the header line of each example.

---

### Example A — KFM entry proposal pack (YAML)

<details>
<summary><strong>Save as: kfm_entries.proposal_pack.example.yaml</strong></summary>

```yaml
schema_id: kfm.schema.kfm_entry_pack.v1
status: example
generated_at: "2026-02-14T00:00:00Z"

# A "proposal pack" can be dropped into a repo as seed material.
# Entries are designed to be auditable (provenance), versioned (semver), and dependency-linked.
proposed_kfm_entries:
  - id: kfm.standard.promotion_contract.v1
    title: Promotion Contract for Provenance-First Publishing
    entry_type: standard
    summary: >
      Normative requirements for promoting/publishing any dataset or catalog artifact in KFM:
      required receipts/manifests, required validation, and mandatory fail-closed behavior.
    tags: [governance, fail-closed, provenance, promotion, policy]
    provenance:
      source_document: "New Ideas Feb-2026-1.pdf"
      source_sections:
        - "Fail-closed CI/CD orchestration blueprint"
        - "PR gate: require receipts"
      canonical_refs:
        - "W3C PROV-DM"
        - "W3C DCAT"
        - "STAC Spec"
    confidence: high
    dependencies:
      - kfm.schema.run_manifest.v1
      - kfm.policy.provenance_guard.v1
    related_entries:
      - kfm.playbook.acceptance_harness.v1
      - kfm.playbook.oci_provenance_hub.v1
    versioning:
      scheme: semver
      current: "1.0.0"
      review_cadence: "quarterly or after major toolchain/security updates"
      review_notes:
        - "Security review: signature verification"
        - "Data governance: license/rights required fields"

  - id: kfm.schema.run_manifest.v1
    title: Run Manifest Schema
    entry_type: schema
    summary: >
      JSON schema for the canonical run_manifest / run_receipt that anchors spec_hash,
      rights/license, attestation references, produced artifacts, and materiality decisions.
    tags: [schema, receipt, manifest, provenance, reproducibility]
    provenance:
      source_document: "New Ideas Feb-2026-1.pdf"
      source_sections:
        - "Suggested receipt fields"
        - "PR invariants: required keys"
    confidence: medium
    dependencies:
      - kfm.standard.spec_hash.v1
    related_entries:
      - kfm.policy.provenance_guard.v1
    versioning:
      scheme: semver
      current: "1.0.0"
      review_cadence: "on schema changes"
      review_notes:
        - "Align key names: rekor_uuid vs cosign_rekor_id"
        - "Define required vs optional fields per dataset class"

  - id: kfm.policy.provenance_guard.v1
    title: Provenance Guard Policy Pack
    entry_type: policy_pack
    summary: >
      OPA/Rego rules that deny promotion when provenance, attestations, signatures,
      or required governance fields are missing or invalid.
    tags: [opa, rego, conftest, policy, fail-closed]
    provenance:
      source_document: "New Ideas Feb-2026-1.pdf"
      source_sections:
        - "Minimal Rego invariants"
        - "Acceptance harness policy gate"
    confidence: high
    dependencies:
      - kfm.schema.run_manifest.v1
    related_entries:
      - kfm.standard.promotion_contract.v1
    versioning:
      scheme: semver
      current: "1.0.0"
      review_cadence: "after policy changes or incident learnings"
      review_notes:
        - "Add dataset-class-specific overlays"
        - "Keep deny-by-default semantics"

  - id: kfm.standard.spec_hash.v1
    title: Spec Hash Standard
    entry_type: standard
    summary: >
      Defines canonicalization and hashing inputs for spec_hash to ensure reproducible diffs.
      JSON uses RFC 8785 JCS.
    tags: [hashing, canonicalization, rfc8785, etag, reproducibility]
    provenance:
      source_document: "New Ideas Feb-2026-1.pdf"
      source_sections:
        - "HTTP caching: RFC 8785"
        - "Acceptance harness spec_hash"
      canonical_refs:
        - "RFC 8785"
    confidence: high
    dependencies: []
    related_entries:
      - kfm.schema.run_manifest.v1
    versioning:
      scheme: semver
      current: "1.0.0"
      review_cadence: "rare; only if canonicalization rules change"
      review_notes:
        - "Clarify when YAML hashing is acceptable vs JCS JSON hashing"

  - id: kfm.schema.watcher.v1
    title: Watcher Entry Schema
    entry_type: schema
    summary: >
      JSON Schema for defining watchers (endpoint, poll/webhook mode, outputs, policy thresholds,
      spec_hash, signature_ref) as attestable, publishable objects.
    tags: [watchers, schema, registry, governance]
    provenance:
      source_document: "New Ideas Feb-2026-1.pdf"
      source_sections:
        - "KFM Watcher JSON Schema"
        - "DCAT watchers registry wrapper"
    confidence: high
    dependencies:
      - kfm.standard.spec_hash.v1
    related_entries:
      - kfm.standard.watcher_registry.v1
    versioning:
      scheme: semver
      current: "1.0.0"
      review_cadence: "on schema changes"
      review_notes:
        - "Define watcher_id namespace conventions"

  - id: kfm.standard.watcher_registry.v1
    title: Signed Watchers Registry Standard
    entry_type: standard
    summary: >
      Defines how watchers are published as a registry dataset (e.g., DCAT wrapper) with an
      integrity hash and signature_ref so KFM can trust and discover watcher definitions.
    tags: [registry, dcat, signatures, governance]
    provenance:
      source_document: "New Ideas Feb-2026-1.pdf"
      source_sections:
        - "Watchers registry DCAT wrapper"
    confidence: medium
    dependencies:
      - kfm.schema.watcher.v1
    related_entries:
      - kfm.pattern.watcher_to_registry.v1
    versioning:
      scheme: semver
      current: "1.0.0"
      review_cadence: "quarterly"
      review_notes:
        - "Decide signing mechanism (JWS vs Sigstore attestation)"

  - id: kfm.playbook.acceptance_harness.v1
    title: CI Acceptance Harness for STAC, DCAT, PROV, Policy, and Attestations
    entry_type: playbook
    summary: >
      CI-ready harness: validates STAC/DCAT/PROV, runs policy tests, verifies attestations,
      and checks deterministic spec_hash.
    tags: [ci, validation, stac, dcat, prov, cosign, reproducibility]
    provenance:
      source_document: "New Ideas Feb-2026-1.pdf"
      source_sections:
        - "Acceptance harness (CI-ready)"
      canonical_refs:
        - "W3C PROV"
        - "W3C DCAT"
        - "STAC"
        - "RFC 8785"
    confidence: high
    dependencies:
      - kfm.standard.spec_hash.v1
      - kfm.policy.provenance_guard.v1
    related_entries:
      - kfm.standard.promotion_contract.v1
    versioning:
      scheme: semver
      current: "1.0.0"
      review_cadence: "on toolchain updates"
      review_notes:
        - "Pin validator versions"
        - "Decide canonical DCAT validation toolchain"

  - id: kfm.pattern.watcher_to_registry.v1
    title: Watcher to Registry Pattern
    entry_type: pattern
    summary: >
      End-to-end pattern: watcher detects material upstream change, opens PR with receipts + catalogs,
      CI validates/signs, registry stores immutable subject + referrers/attestations.
    tags: [watchers, pr-driven, registry, oras, cosign, provenance]
    provenance:
      source_document: "New Ideas Feb-2026-1.pdf"
      source_sections:
        - "Watcher→PR→CI→Registry→Attestations"
    confidence: high
    dependencies:
      - kfm.standard.spec_hash.v1
      - kfm.playbook.acceptance_harness.v1
    related_entries:
      - kfm.schema.watcher.v1
      - kfm.standard.watcher_registry.v1
    versioning:
      scheme: semver
      current: "1.0.0"
      review_cadence: "quarterly"
      review_notes:
        - "Standardize receipt naming"
        - "Define canonical folder contracts"
```

</details>

---

### Example B — Watcher definition (JSON)

<details>
<summary><strong>Save as: watcher.example.http_etag.v1.json</strong></summary>

```json
{
  "watcher_id": "kfm.watcher.example.http_etag.v1",
  "spec_schema_id": "kfm.schema.watcher.v1",
  "spec_recipe_version": "1.0.0",
  "spec": {
    "description": "Example watcher (poll + conditional HTTP) for an upstream JSON endpoint. Demonstrates ETag/If-None-Match and Last-Modified/If-Modified-Since semantics.",
    "mode": "poll",
    "endpoint": {
      "method": "GET",
      "url": "https://example.org/api/v1/example_dataset.json",
      "headers": {
        "accept": "application/json"
      }
    },
    "poll": {
      "interval": "PT6H",
      "use_etag": true,
      "use_last_modified": true,
      "max_backoff_seconds": 3600,
      "jitter": true
    },
    "policy": {
      "classification": "public",
      "materiality": {
        "max_unchanged_polls": 28,
        "change_triggers": [
          {
            "path": "$.meta.last_updated",
            "type": "string"
          },
          {
            "path": "$.records",
            "type": "array_length"
          }
        ]
      }
    },
    "outputs": [
      {
        "kind": "raw_snapshot",
        "uri_template": "data/raw/example_dataset/{yyyy}/{mm}/{dd}/snapshot.json"
      },
      {
        "kind": "run_manifest",
        "uri_template": "data/work/example_dataset/{run_id}/run_manifest.json"
      }
    ]
  },
  "spec_hash": "24153bdf5c16a47670fc3da9aa743bb4b6ca4cef7e0661c5f6079ca61709558f",
  "signature_ref": "sigstore://rekor/00000000-0000-0000-0000-000000000000#sha256=0000000000000000000000000000000000000000000000000000000000000000",
  "owners": [
    {
      "role": "data-steward",
      "name": "KFM Example Team",
      "email": "stewards@example.org"
    }
  ]
}
```

</details>

---

### Example C — Watchers registry DCAT wrapper (JSON-LD)

<details>
<summary><strong>Save as: watchers_registry.dcat.example.jsonld</strong></summary>

```json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "prov": "http://www.w3.org/ns/prov#",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "kfm": "https://kansas-frontier-matrix.example/ns#"
  },
  "@id": "dcat://registry/watchers/example",
  "@type": "dcat:Dataset",
  "dct:identifier": "registry:watchers:example",
  "dct:title": "KFM Watchers Registry (Example)",
  "dct:description": "Example DCAT-wrapped watchers registry. Provides discoverability + an integrity anchor (spec_hash + signature_ref).",
  "dct:license": "CC-BY-4.0",
  "dct:publisher": {
    "@type": "foaf:Organization",
    "foaf:name": "Kansas Frontier Matrix (KFM)"
  },
  "dcat:keyword": [
    "kfm",
    "watchers",
    "registry",
    "provenance"
  ],
  "dct:modified": "2026-02-14T00:00:00Z",
  "kfm:integrity": {
    "kfm:spec_hash": "0000000000000000000000000000000000000000000000000000000000000000",
    "kfm:signature_ref": "sigstore://rekor/00000000-0000-0000-0000-000000000000#sha256=0000000000000000000000000000000000000000000000000000000000000000"
  },
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:title": "Watchers registry index (JSON)",
      "dct:format": "application/json",
      "dcat:downloadURL": "https://example.org/kfm/registry/watchers.example.json",
      "kfm:signature_ref": "sigstore://rekor/00000000-0000-0000-0000-000000000000#sha256=0000000000000000000000000000000000000000000000000000000000000000"
    }
  ],
  "prov:wasGeneratedBy": "prov://run/example/watchers_registry_build/2026-02-14T000000Z"
}
```

</details>

---

### Example D — Run manifest / run receipt (JSON)

<details>
<summary><strong>Save as: run_manifest.example.json</strong></summary>

```json
{
  "schema_id": "kfm.schema.run_manifest.v1",
  "run_id": "run_2026-02-14T120000Z__example_dataset__v1",
  "dataset_id": "example_dataset",
  "dataset_version": "2026-02-14",
  "trigger": {
    "watcher_id": "kfm.watcher.example.http_etag.v1",
    "reason": "upstream_changed",
    "upstream_etag": "\"abc123\"",
    "observed_at": "2026-02-14T12:00:00Z"
  },
  "inputs": [
    {
      "uri": "data/raw/example_dataset/2026/02/14/snapshot.json",
      "sha256": "0000000000000000000000000000000000000000000000000000000000000000",
      "content_type": "application/json"
    }
  ],
  "code": {
    "git_sha": "0000000000000000000000000000000000000000",
    "image": "ghcr.io/kfm/pipeline-example@sha256:0000000000000000000000000000000000000000000000000000000000000000"
  },
  "outputs": [
    {
      "uri": "data/processed/example_dataset/example.parquet",
      "sha256": "0000000000000000000000000000000000000000000000000000000000000000",
      "content_type": "application/parquet"
    }
  ],
  "catalog_refs": {
    "dcat": "data/catalog/dcat/example_dataset.jsonld",
    "stac": "data/catalog/stac/example_dataset/collection.json",
    "prov": "data/catalog/prov/example_dataset/run_2026-02-14T120000Z.json"
  },
  "validation": {
    "status": "pass",
    "reports": [
      {
        "tool": "schema-validator",
        "result": "pass",
        "report_uri": "data/work/example_dataset/run_2026-02-14T120000Z/schema_report.json"
      },
      {
        "tool": "stac-validator",
        "result": "pass",
        "report_uri": "data/work/example_dataset/run_2026-02-14T120000Z/stac_report.json"
      },
      {
        "tool": "dcat-validator",
        "result": "pass",
        "report_uri": "data/work/example_dataset/run_2026-02-14T120000Z/dcat_report.json"
      },
      {
        "tool": "prov-validator",
        "result": "pass",
        "report_uri": "data/work/example_dataset/run_2026-02-14T120000Z/prov_report.json"
      },
      {
        "tool": "opa/conftest",
        "result": "pass",
        "report_uri": "data/work/example_dataset/run_2026-02-14T120000Z/policy_report.json"
      }
    ]
  },
  "governance": {
    "license": "CC-BY-4.0",
    "policy_label": "public",
    "sensitivity": {
      "class": "public",
      "notes": "No sensitive locations; safe for public map rendering."
    }
  },
  "attestations": {
    "signature_ref": "sigstore://rekor/00000000-0000-0000-0000-000000000000#sha256=0000000000000000000000000000000000000000000000000000000000000000",
    "rekor_uuid": "00000000-0000-0000-0000-000000000000",
    "bundle_ref": "oci://ghcr.io/kfm/bundles/example_dataset@sha256:0000000000000000000000000000000000000000000000000000000000000000"
  },
  "notes": [
    "This is an example-only manifest.",
    "In production, ensure the manifest is complete before promotion; missing required fields must fail closed."
  ]
}
```

</details>

---

### Example E — OPA/Rego snippets (policy gates)

<details>
<summary><strong>Save as: policy.cite_or_abstain.example.rego</strong></summary>

```rego
package kfm.ai

# Deny by default (fail-closed).
default allow := false

# Minimum example for Focus Mode: answers must have citations AND must pass sensitivity checks.
allow if {
  input.answer.has_citations == true
  input.answer.sensitivity_ok == true
}
```

</details>

<details>
<summary><strong>Save as: policy.provenance_guard.example.rego</strong></summary>

```rego
package kfm.promotion

# Deny by default (fail-closed).
default allow := false

# Minimal example: block promotion unless required governance + provenance fields are present.
# (In production, this should be expanded and tested with Conftest.)
allow if {
  has_required_fields
  has_valid_license
  has_catalog_refs
  has_attestation_ref
}

has_required_fields if {
  input.run_manifest.schema_id != ""
  input.run_manifest.run_id != ""
  input.run_manifest.dataset_id != ""
}

has_valid_license if {
  input.run_manifest.governance.license != ""
}

has_catalog_refs if {
  input.run_manifest.catalog_refs.dcat != ""
  input.run_manifest.catalog_refs.stac != ""
  input.run_manifest.catalog_refs.prov != ""
}

has_attestation_ref if {
  input.run_manifest.attestations.signature_ref != ""
}
```

</details>

---

## Validation workflow (reference)

> [!IMPORTANT]
> The system’s default posture is **fail-closed**:
> - If a required field is missing → block merge/promotion.
> - If a signature is missing/invalid → block merge/promotion.
> - If catalogs are missing (DCAT/STAC/PROV) → block promotion.

**Reference gate sequence (conceptual):**
1. Canonicalize JSON → compute `spec_hash`
2. Open PR with registry changes + receipts/catalogs
3. CI runs validators (schema + STAC/DCAT/PROV + policy)
4. If pass, publish / promote (often digest-pinned) + attach attestations
5. If fail, merge is blocked (fail-closed)

### Suggested validation matrix

| Artifact | Minimum checks | Why it matters |
|---|---|---|
| Watcher JSON | JSON Schema + `spec_hash` reproducibility | watcher specs are “operational truth” |
| Run manifest | Required keys + policy checks | promotion gate anchor |
| DCAT wrapper | JSON-LD validity + required metadata | discoverability + rights |
| STAC/PROV | spec validation | traceability + map/time rendering |

---

## How to add a new example

**Definition of Done (for an example contribution):**
- [ ] Example is copy/paste-ready and self-contained
- [ ] Example includes **license/rights**
- [ ] Example includes **policy_label / sensitivity**
- [ ] Example includes `spec_schema_id` and `spec_recipe_version` where relevant
- [ ] `spec_hash` is either computed (preferred) or explicitly documented as a placeholder
- [ ] No external file dependencies required to understand the example (README must stand alone)
- [ ] If you reference a tool (OPA, Conftest, stac-validator), include a “how to run” snippet

---

## Troubleshooting

**`spec_hash` mismatches**
- Confirm you are hashing the correct object (`.spec`, not the wrapper).
- Confirm canonicalization: sorted keys, no whitespace, UTF-8.

**Promotion blocked**
- Check for missing `license`, missing `policy_label`, missing `catalog_refs`, missing signature/attestation refs.

**Sensitive locations**
- If a dataset can reveal precise locations, set `policy_label: sensitive-location` and ensure downstream layers are redacted/generalized.

---

_End of file._

