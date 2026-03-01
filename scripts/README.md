<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/9f9a88f5-4dd7-4ae9-8b64-5310a2b1f7fd
title: scripts/README.md
type: standard
version: v1
status: draft
owners: TBD (add CODEOWNERS rule)
created: 2026-02-26
updated: 2026-03-01
policy_label: public
related:
  - kfm://doc/<TBD>  # TODO: link to in-repo KFM governance/design guide (truth path, promotion contract, trust membrane)
  - kfm://doc/<TBD>  # TODO: link to in-repo pipeline/tooling guide (validators, policy gates, receipts)
tags:
  - kfm
  - scripts
  - ops
  - governance
notes:
  - This README documents conventions and governance expectations for scripts.
  - This README describes the target contract; update the directory tree + registry to match the repo.
  - 2026-03-01: aligned promotion gates + receipt expectations to vNext briefing snapshots.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `scripts/` — Governed operational scripts (receipt-emitting, fail-closed)

Operational scripts for KFM ingestion/orchestration, validation, cataloging, indexing, and maintenance — **governed, reproducible, and auditable**.

![status](https://img.shields.io/badge/status-draft-yellow)
![policy](https://img.shields.io/badge/policy-default--deny-critical)
![gates](https://img.shields.io/badge/promotion-gates_required-orange)
![receipts](https://img.shields.io/badge/receipts-required-orange)
![safety](https://img.shields.io/badge/safety-no_secrets-red)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)

> [!IMPORTANT]
> In KFM, “scripts” are **governed operations**. If a script can change what users see (directly or indirectly),
> it must be: **scope-controlled**, **receipt-emitting**, and **fail-closed**.

> [!NOTE]
> This README mixes:
> - **Confirmed invariants** (from KFM governance docs),
> - a **directory contract** (what we expect `scripts/` to look like), and
> - **repo-specific details** (paths, tooling, CI gates) that must be verified in the live repo.
>
> Keep those distinct. If something can’t be verified, mark it **Unknown** and fail closed.

---

## Quick navigation

- [Purpose](#purpose)
- [Non-negotiables](#non-negotiables)
- [Where this fits in the system](#where-this-fits-in-the-system)
- [Promotion Contract gates](#promotion-contract-gates)
- [Directory contract](#directory-contract)
- [Directory layout](#directory-layout)
- [Truth path IO discipline](#truth-path-io-discipline)
- [Run receipts](#run-receipts)
- [Policy gates and local checks](#policy-gates-and-local-checks)
- [Conventions](#conventions)
- [Adding a new script](#adding-a-new-script)
- [Script registry](#script-registry)
- [Minimum verification steps](#minimum-verification-steps)
- [Troubleshooting](#troubleshooting)

---

## Purpose

This directory exists for **operational scripts** that:

- snapshot upstream sources into the **Truth Path** (Upstream → RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED),
- normalize and validate datasets (QA + schema + geo/time checks),
- generate/validate catalogs (DCAT/STAC/PROV) and cross-links,
- build **rebuildable projections** (search/graph/tiles/indexes) from canonical artifacts,
- run maintenance tasks (linting, audits, migrations) **without bypassing governance**.

> [!NOTE]
> Prefer “thin scripts / fat libraries”:
> - Put core logic in versioned libraries/use-cases (domain + validators + catalog builders).
> - Keep scripts as orchestration wrappers that call those use-cases deterministically.

[Back to top](#top)

---

## Non-negotiables

These are KFM invariants that scripts must **preserve**:

- **Truth Path** is enforced with lifecycle zones and promotion gates (no silent drift, reproducible runs).
- **Promotion Contract** blocks publishing unless minimum gates are satisfied (**fail closed**).
- **Trust membrane**: clients/UI never access stores directly; policy is enforced at the PEP/API boundary.
- **Catalog triplet** (DCAT + STAC + PROV) is the evidence surface; links must resolve deterministically.
- **Cite-or-abstain**: if citations/evidence cannot be verified, the system must abstain or reduce scope.

> [!WARNING]
> Scripts that mutate canonical storage without receipts, checksums, or provenance break auditability and must
> be treated as a governance incident.

[Back to top](#top)

---

## Where this fits in the system

Scripts execute *inside* the KFM Truth Path. They must not bypass enforcement boundaries.

```mermaid
flowchart LR
  U[Upstream sources] --> A[scripts acquire]
  A --> R[RAW zone]
  R --> T[scripts transform]
  T --> W[WORK and QUARANTINE zone]
  W --> P[PROCESSED zone]
  P --> C[scripts catalog]
  C --> K[CATALOG TRIPLET]
  K --> I[scripts index]
  I --> X[projections]
  X --> S[PUBLISHED runtime]
  S --> API[Governed API PEP]
  API --> UI[Map Story Focus UI]
```

### Trust membrane reminder

- UI/external clients **must not** access DB/object storage directly.
- Scripts must not create “side channels” (e.g., copying restricted artifacts into public outputs).
- Enforcement is owned by **governed APIs** and promotion gates; scripts must **invoke** those mechanisms, not replace them.

```mermaid
flowchart LR
  Client[UI and external clients] --> PEP[Governed API PEP]
  PEP --> Policy[Policy engine]
  PEP --> Evidence[Evidence resolver]
  PEP --> Stores[Stores and projections]
  Stores --> PEP
```

[Back to top](#top)

---

## Promotion Contract gates

The **Promotion Contract** is the fail-closed mechanism that blocks a dataset version from reaching **PUBLISHED**
unless minimum gates are satisfied.

> [!IMPORTANT]
> Promotion gates apply at each transition. The CATALOG/TRIPLET must cross-link identifiers so **EvidenceRefs resolve**
> without guessing.

### Minimum gates (v1)

| Gate | What must be present | Example CI check (illustrative) | Script implications (examples) |
|---|---|---|---|
| **A — Identity & versioning** | `dataset_id`, `dataset_version_id`, deterministic `spec_hash`, content digests | schema validation; **spec_hash golden tests**; artifact digest verification | Scripts must compute/verify hashes and record them in receipts/manifests. |
| **B — Licensing & rights metadata** | license/rights fields + snapshot of upstream terms | fail if license missing/unknown; store terms snapshot artifact | Acquisition scripts must snapshot terms and fail closed if rights are unclear. |
| **C — Sensitivity classification & redaction plan** | `policy_label` + obligations (generalize geometry, remove fields, etc.) | policy tests are **default-deny**; verify obligations honored | Scripts must apply obligations and avoid leaking restricted details in logs/receipts. |
| **D — Catalog triplet validation** | DCAT/STAC/PROV validate and cross-link; EvidenceRefs resolve | validators + linkcheck; fail on broken links/missing IDs | Catalog/validate scripts must schema-validate and link-check deterministically. |
| **E — QA & thresholds** | dataset-specific QA checks + documented thresholds | QA report exists; thresholds met; else quarantine | Transform scripts must emit QA reports; failures go to QUARANTINE. |
| **F — Run receipt & audit record** | run receipt capturing inputs/tooling/hashes/policy decisions; append-only audit record | receipt schema validation; signature/attestation checks (if enabled) | All artifact-writing scripts must emit receipts; treat audit outputs as append-only. |
| **G — Release manifest** | promotion recorded as a release manifest referencing artifacts + digests | release manifest exists; references match objects | Promotion scripts must write a manifest tying IDs, digests, catalogs, QA, and approvals. |

> [!NOTE]
> These gates should be automatable in CI. If a gate cannot be evaluated, **fail closed**.

[Back to top](#top)

---

## Directory contract

### What belongs here

✅ **Put these here:**

- **Acquisition scripts**: upstream snapshot → `data/raw/**` (append-only), including terms snapshot + checksums.
- **Transform scripts**: RAW/WORK → WORK/PROCESSED, producing QA outputs and checksums.
- **Validation scripts**: schema validation, link checking, promotion gate checks, policy fixture checks.
- **Catalog scripts**: generate/validate DCAT/STAC/PROV and cross-links; emit receipts.
- **Index builder scripts**: rebuild DB/search/graph/tiles from canonical artifacts (never from “mystery inputs”).
- **Maintenance scripts**: migrations/backfills only when **reversible** and **receipt-emitting**.

### What must not go here

🚫 **Do not put these here:**

- secrets (API keys, tokens, service-account JSON, kubeconfigs),
- raw datasets or large artifacts (store in governed zones; don’t commit to git),
- “one-off” scripts that aren’t reproducible or reviewed,
- scripts that bypass policy enforcement (e.g., “just copy restricted tiles to public”),
- scripts that print restricted coordinates/PII into logs or receipts.

> [!TIP]
> If it would be unsafe to paste into a public issue, it doesn’t belong in `scripts/` outputs (logs, receipts, examples).

[Back to top](#top)

---

## Directory layout

> [!IMPORTANT]
> This section describes the **target contract**.
> Keep it accurate: after changes, run `tree -L 2 scripts/` and update this README **and** the Script Registry.

```text
scripts/
├─ README.md
│
├─ registry/                                      # Machine-readable registry + schemas + fixtures (small, diff-friendly)
│  ├─ scripts.v1.json                             # Canonical registry: scripts, owners, scope, receipts, zones touched
│  ├─ scripts.lock.json                           # (Optional) digests/spec_hashes for registry + schemas (repro/audit)
│  ├─ schemas/                                    # Schemas for registry + receipt shapes (optional but recommended)
│  │  ├─ scripts_registry.v1.schema.json          # Validates scripts.v1.json
│  │  ├─ run_receipt.v1.schema.json               # Validates run receipts emitted by scripts
│  │  └─ promotion_manifest.v1.schema.json        # Validates promotion/release manifests (if standardized)
│  ├─ fixtures/                                   # Fixtures for CI validation of schemas + registry correctness
│  │  ├─ valid/
│  │  └─ invalid/
│  └─ README.md                                   # Registry contract + how to add a script entry (fail-closed rules)
│
├─ acquire/                                       # Upstream snapshot → RAW (append-only; never served)
├─ transform/                                     # RAW/WORK → WORK/PROCESSED (deterministic transforms)
├─ validate/                                      # Validators + promotion-gate checks (fail-closed)
├─ catalog/                                       # Catalog generation + normalization (DCAT/STAC/PROV)
├─ index/                                         # Rebuildable projections (never canonical truth)
├─ maintenance/                                   # One-off ops (migrations/backfills) — reversible + receipted
├─ lib/                                           # Shared helpers (prefer pure helpers; minimal side effects)
└─ _shared/                                       # Optional: tiny policy-safe fixtures and test helpers
```

[Back to top](#top)

---

## Truth path IO discipline

Scripts must respect KFM’s lifecycle zones and mutability rules.

| Zone | Typical contents | Script rules of the road |
|---|---|---|
| RAW | raw artifacts (original files/API responses), license/terms snapshot, checksums, acquisition manifest | **Append-only**. Never edit in place; supersede via new acquisition. |
| WORK / QUARANTINE | normalized intermediates, QA reports, redaction/generalization candidates; quarantine holds failures | WORK is regeneratable; QUARANTINE blocks promotion. Always record reasons. |
| PROCESSED | publishable artifacts in KFM-approved formats (e.g., GeoParquet/COG/PMTiles) + checksums | Deterministic; digest-addressed; no “hand fixes” without provenance. |
| CATALOG/TRIPLET | cross-linked DCAT + STAC + PROV (+ run receipts + release manifest pointers) | Must validate + cross-link; this is the evidence surface. |
| PROJECTIONS | search/graph/tiles/db indexes | Rebuildable only; never treated as source truth. |
| PUBLISHED | governed runtime surfaces (API + UI) serving promoted versions only | Nothing reaches runtime without passing gates; logs/errors must remain policy-safe. |

> [!WARNING]
> A script that writes “public outputs” must never read from restricted artifacts unless policy explicitly allows and
> obligations are applied.

[Back to top](#top)

---

## Run receipts

Every script that produces artifacts **must** emit a run receipt that makes the run reproducible and auditable.

### Receipt rules (non-negotiable)

- Enumerate **inputs and outputs** with digests/checksums.
- Record enough environment detail to reproduce the run (prefer container image digests).
- Include policy outcomes (decision + obligations + reason codes) when relevant.
- Never store secrets, raw restricted coordinates, or PII in receipts.
- Treat the audit trail as **append-only**.

### Recommended receipt placement

- Promotion-affecting runs (catalog/prov/publish): near the dataset version’s catalog artifacts, e.g.:
  - `data/catalog/<dataset_slug>/<dataset_version_id>/receipts/<run_id>.json`
- Work-stage runs: under the work run, e.g.:
  - `data/work/<dataset_slug>/<work_run_id>/receipts/<run_id>.json`

> [!NOTE]
> Exact paths are repo-specific. The invariant is: **discoverable, deterministic location** and cross-linked from catalogs/provenance when promotion is involved.

<details>
<summary><strong>Minimal receipt shape (template)</strong></summary>

```json
{
  "@type": "prov:run_receipt",
  "run_id": "kfm://run/2026-03-01T12:00:00Z.abcd",
  "actor": { "principal": "svc:pipeline", "role": "pipeline" },
  "operation": "acquire|transform|validate|catalog|index|maintenance",

  "dataset_id": "example_dataset",
  "dataset_version_id": "2026-03.abcd1234",
  "spec_hash": "sha256:...",

  "created_at": "2026-03-01T12:05:00Z",

  "inputs": [
    { "uri": "data/raw/example_dataset/<acq_id>/artifacts/source.csv", "digest": "sha256:..." }
  ],
  "outputs": [
    { "uri": "data/processed/example_dataset/<dataset_version_id>/events.parquet", "digest": "sha256:..." },
    { "uri": "data/processed/example_dataset/<dataset_version_id>/qa/report.json", "digest": "sha256:..." }
  ],

  "environment": {
    "container_digest": "sha256:img...",
    "git_commit": "deadbeef",
    "params_digest": "sha256:..."
  },

  "validation": {
    "status": "pass",
    "checks": [
      { "id": "schema.validate", "status": "pass" },
      { "id": "geo.bounds", "status": "pass" }
    ]
  },

  "policy": {
    "decision_id": "kfm://policy_decision/xyz",
    "policy_label": "public",
    "obligations_applied": [],
    "reason_codes": ["POLICY.ALLOW.PUBLIC.READ"]
  },

  "notes": "Optional human context. Must be policy-safe."
}
```

</details>

[Back to top](#top)

---

## Policy gates and local checks

Policy gates are how governance intent becomes **enforceable behavior**. Scripts are expected to run policy gates locally (when practical) and CI must run them pre-merge.

> [!IMPORTANT]
> If a policy gate cannot be evaluated (missing policy pack, missing fixtures, missing evidence), **fail closed**.

### Local “receipt gate” pattern (illustrative)

- Generate receipt
- Validate receipt schema
- Run policy pack (deny-by-default) over the receipt

Example (paths are repo-specific; update once verified):

```bash
# 1) run script -> emits receipt.json
# 2) schema validate receipt (JSON Schema)
# 3) policy-gate it (Conftest + OPA/Rego)
conftest test receipt.json -p policy/opa
```

[Back to top](#top)

---

## Conventions

### Script interface (required)

All scripts should:

- be runnable from the repo root,
- support `--help`,
- support `--dry-run` when meaningful,
- exit non-zero on failure,
- write human logs to stderr; write machine outputs to files.

### Determinism (required posture)

Prefer deterministic outputs:

- same inputs + same parameters ⇒ same outputs + same digests,
- avoid embedding timestamps in artifacts unless domain-required (timestamps belong in receipts),
- use stable ordering when writing JSON (canonical JSON if used for hashing).

### Naming

Use names that describe intent:

- `acquire_*` (upstream → RAW)
- `transform_*` (RAW/WORK → WORK/PROCESSED)
- `validate_*` (schema/link/policy/gates)
- `build_*` / `catalog_*` (DCAT/STAC/PROV)
- `index_*` (rebuildable projections)
- `migrate_*` / `backfill_*` (maintenance — reversible + receipted)

### Safety defaults (non-negotiable)

- Default-deny when licensing/sensitivity is unclear.
- Never print restricted coordinates/attributes into logs or receipts.
- If a required gate cannot be evaluated, **fail closed** and emit a remediation path.

[Back to top](#top)

---

## Adding a new script

Use this checklist to keep changes small, reviewable, and governed:

- [ ] Script has a clear purpose statement and a stable name.
- [ ] Core logic lives in libraries/use-cases; script is orchestration-only where possible.
- [ ] Inputs and outputs are explicit (paths/URIs + formats).
- [ ] Script writes only to the correct zone(s).
- [ ] Script emits a run receipt and output digests.
- [ ] Script is idempotent **or** documents non-idempotence + rollback.
- [ ] Script does not embed or print secrets.
- [ ] Script does not leak restricted information (including “restricted existence” inference).
- [ ] If script affects promotion/publishing, it runs required Promotion Contract gates (or is run by a promotion runner).
- [ ] Add an entry to the Script Registry (`scripts/registry/scripts.v1.json`).
- [ ] Add/adjust CODEOWNERS so scripts are reviewed by the right stewards.

### Script header (copy/paste)

```text
Purpose:
Inputs:
Outputs:
Zones touched:
Promotion gates impacted:
Policy considerations:
Receipt path:
Rollback (if non-idempotent):
Owner:
```

[Back to top](#top)

---

## Script registry

To keep scripts discoverable and reviewable, maintain a machine-readable registry.

- **Registry file (target):** `scripts/registry/scripts.v1.json`
- **Rule:** if a script exists, it must be registered with an owner and declared zones.

### Recommended registry fields

- `script_id` (stable)
- `path`
- `kind` (`acquire|transform|validate|catalog|index|maintenance`)
- `owner`
- `zones_touched[]`
- `requires_receipt` (true/false; default true for zone-writing scripts)
- `supports_dry_run` (true/false)
- `policy_sensitive` (true/false; triggers steward review)
- `spec_hash` (required when it touches RAW/PROCESSED/CATALOG/PUBLISHED)
- `signature_ref` (optional but recommended for allow-listed automation)
- `notes` (policy-safe)

> [!NOTE]
> Registry content must remain policy-safe. Do not encode sensitive dataset details in registry entries.

[Back to top](#top)

---

## Minimum verification steps

Use this as a “smallest acceptable” checklist when changing scripts that touch the truth path:

- [ ] Capture repo commit hash and scripts subtree: `git rev-parse HEAD` + `tree -L 3 scripts/`
- [ ] Registry validates (JSON Schema) and every script path is registered
- [ ] If the change produces artifacts: receipt exists, validates, and includes digests + `spec_hash`
- [ ] Catalog changes pass schema validation + linkcheck (DCAT/STAC/PROV)
- [ ] Policy gates run (deny-by-default) and pass for the intended policy label(s)
- [ ] If promotion/publishing is involved: release manifest produced and cross-linked

[Back to top](#top)

---

## Troubleshooting

### “It ran, but I can’t reproduce the output”
- Confirm a run receipt exists and includes exact inputs/outputs + digests.
- Confirm environment pinning (container digest / tool versions) is present.
- Confirm the same spec/config inputs (and `spec_hash`) were used.

### “Why did it fail closed?”
Common causes:
- missing or unclear license/rights metadata,
- missing policy label or unresolved sensitivity classification,
- catalog triplet schema/linkcheck failures,
- missing digests, receipts, or release manifest required by promotion gates,
- QA thresholds not met → quarantine,
- policy gate failures (e.g., receipt missing `spec_hash` or using insecure access URLs).

### “How do I know it’s safe to run?”
- It should be receipt-emitting, deterministic, and scoped to specific zones.
- If it touches published surfaces, it must be gated by promotion checks and produce policy-safe errors.

[Back to top](#top)
