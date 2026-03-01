<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/3f7c4c0e-6b6f-4e95-9f1f-4f219de8d3e1
title: ADR 0003 - Data Zones and Promotion Contract
type: adr
version: v1
status: draft
owners: kfm-maintainers (TBD)
created: 2026-03-01
updated: 2026-03-01
policy_label: public
related:
  - kfm://doc/ (TODO: link to gate schemas, policy pack, validator docs)
tags:
  - kfm
  - adr
  - governance
  - data-lifecycle
  - promotion-contract
notes:
  - Defines KFM zones (RAW, WORK/QUARANTINE, PROCESSED, CATALOG/TRIPLET, PUBLISHED) and fail-closed promotion gates.
[/KFM_META_BLOCK_V2] -->

# ADR 0003: Data Zones and Promotion Contract

**Purpose:** Define KFM’s **data zones** and the **Promotion Contract** so that governance intent becomes **enforceable behavior** (CI + runtime), not just documentation.

![ADR](https://img.shields.io/badge/ADR-0003-blue)
![Status](https://img.shields.io/badge/status-draft-yellow)
![Domain](https://img.shields.io/badge/domain-governance-lightgrey)
![Promotion](https://img.shields.io/badge/promotion-fail--closed-critical)

---

## Navigation

- [Context](#context)
- [Decision](#decision)
- [Definitions](#definitions)
- [Data zones](#data-zones)
- [Promotion Contract](#promotion-contract)
- [Enforcement](#enforcement)
- [Consequences](#consequences)
- [Alternatives considered](#alternatives-considered)
- [Minimum verification steps](#minimum-verification-steps)
- [Appendix](#appendix)

---

## Context

KFM is an evidence-first geospatial platform. In practice, that means:

- user-facing layers, story claims, and AI answers must be traceable to **versioned sources**,
- runtime access must be policy-controlled (no bypass),
- and publishing must be blocked unless provenance + metadata + validation are present.

This ADR standardizes how data moves through KFM by defining:

1. a **truth path** of zones (storage + governance boundaries), and  
2. a **Promotion Contract** (fail-closed gates) required before anything is served via APIs/UI.

---

## Decision

We adopt the lifecycle model as a **hard contract**:

1. Data flows through the following zones:

   **RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED**

2. **RAW is append-only.** You do not edit RAW; you supersede it with a new acquisition and version.

3. **QUARANTINE blocks promotion.** Anything with validation failures, unclear licensing, or sensitivity concerns must not be promoted.

4. **Promotion is a governed act** that:
   - emits run receipts (audit artifacts),
   - emits a promotion manifest (release record referencing digests),
   - and is blocked unless all minimum gates pass.

5. **Canonical vs rebuildable:**
   - Canonical truth = artifacts + catalogs + provenance/receipts.
   - Rebuildable projections = DB/search/graph/tiles derived from canonical truth.

6. **Trust membrane:** clients (UI/external) must never bypass policy enforcement. All runtime access is through governed APIs that evaluate policy and return **evidence bundles**, not guessed citations.

---

## Definitions

- **Zone:** a storage + governance boundary with defined mutability and allowed consumers.
- **Promotion:** moving a dataset version from Raw/Work into **Processed + Catalog/Lineage**, thereby making it eligible to appear in runtime surfaces.
- **Promotion Contract:** the CI/runtime-enforced gates required for promotion (fail closed).
- **Dataset ID (`dataset_id`):** stable identifier across catalogs/UI/citations.
- **Dataset Version ID (`dataset_version_id`):** immutable ID derived from a deterministic `spec_hash`.
- **spec_hash:** deterministic hash of a canonical dataset onboarding spec (requires stable canonicalization).
- **EvidenceRef:** a structured reference that resolves to an EvidenceBundle containing metadata + artifacts + provenance.

---

## Data zones

### Truth path diagram

```mermaid
flowchart LR
  U[Upstream sources] --> R[RAW zone]
  R --> W[WORK and QUARANTINE]
  W --> P[PROCESSED zone]
  P --> C[CATALOG TRIPLET]
  C --> X[Rebuildable projections]
  X --> A[Governed API and PEP]
  A --> UI[UI surfaces]
```

### Zone contract (summary)

| Zone | Purpose | Mutability | Must contain | Must NOT contain | Typical consumers |
|---|---|---|---|---|---|
| **RAW** | Immutable acquisition copy of upstream payloads | **Append-only** | acquisition manifest, raw artifacts, checksums, minimal metadata + terms snapshot | edited “fixes” to upstream artifacts | ingestion tooling, auditors |
| **WORK** | Intermediate transforms + QA | Rewrite allowed | normalized representations, QA reports, candidate redactions, provisional entity resolution | anything served to end users | pipeline tooling, QA |
| **QUARANTINE** | Isolation for failures/uncertainty | Rewrite allowed | failed validations, unclear rights, sensitivity concerns, upstream instability notes | promotion manifests | stewards, engineers |
| **PROCESSED** | Publishable artifacts in approved formats | Immutable per version | approved-format artifacts + checksums + derived metadata | undocumented transforms, missing digests | index builders, evidence resolver |
| **CATALOG/TRIPLET** | Cross-linked metadata + lineage | Immutable per version | DCAT + STAC + PROV + run receipts + link maps | dangling links / unverifiable IDs | API discovery, UI evidence drawer |
| **PUBLISHED** | Governed runtime surfaces | Governed | policy-filtered API responses, tiles, story nodes, focus answers (each with receipts) | direct access to RAW/WORK | users, clients |

### Zone invariants

- **RAW is never edited.** Fixes happen by superseding with a new acquisition and version.
- **QUARANTINE is a blocker state.** Quarantined items are not promotable.
- **Nothing in WORK/QUARANTINE is served publicly.**
- Every promoted artifact must be **content-addressable by digest** (at least recorded and validated as a checksum).

---

## Promotion Contract

### Intent

Promotion MUST be blocked unless all required artifacts exist and validate. Gates are designed to be automated in CI and reviewed during steward sign-off.

> **Fail-closed default:** if a gate cannot be evaluated (missing license snapshot, missing policy decision, missing receipts), treat it as **FAILED**.

### Minimum gates (v1)

| Gate | What must be true | Evidence produced | Typical enforcement |
|---|---|---|---|
| **A. Identity and versioning** | stable `dataset_id`; immutable `dataset_version_id`; deterministic `spec_hash`; promotion manifest exists | onboarding spec + spec_hash; promotion manifest | schema + “golden hash” tests |
| **B. Licensing and rights metadata** | license/rights explicit; upstream terms snapshot captured; unclear license → QUARANTINE | license fields + terms snapshot artifact | CI denies missing/unknown |
| **C. Sensitivity classification and redaction plan** | `policy_label` assigned; obligations recorded; sensitive outputs generalized/redacted | policy decision record; PROV obligations | OPA tests; redaction verification |
| **D. Catalog triplet validation** | DCAT/STAC/PROV validate; cross-links resolvable; EvidenceRefs resolvable | validated catalogs + link check report | validators + linkcheck in CI |
| **E. Run receipts, QA, and checksums** | run receipt exists per producing run; inputs/outputs enumerated with checksums; environment recorded; QA report present and pass | run receipts + QA report + digests | receipt schema validation + QA gates |
| **F. Policy tests and contract tests** | policy pack tests pass; EvidenceRef resolves in CI; API/catalog schemas validate | conftest/OPA results; integration test artifacts | required CI status checks |
| **Optional (recommended)** | supply-chain attestations, SBOM; perf + accessibility smoke checks | attestations + smoke test outputs | pre-promotion job gates |

### Required artifacts (v1)

At minimum, a promoted dataset version MUST have:

- **Processed artifacts** in approved formats + checksums
- **Catalog triplet**: DCAT + STAC + PROV (cross-linked)
- **Run receipts** (for acquisition + transform + publish steps)
- **Policy label assignment** (and obligation evidence when applicable)
- **Promotion manifest** (release record binding it all together)

---

## Enforcement

### CI enforcement (minimum)

Make these required status checks:

- Validate onboarding spec schema; compute and verify deterministic `spec_hash`.
- Validate DCAT/STAC/PROV against profiles; verify cross-links and EvidenceRef resolution.
- Run OPA/Rego policy tests (default deny); verify redaction obligations for restricted/sensitive layers.
- Validate run_receipt and promotion_manifest schemas; verify referenced digests exist.
- Optional hardening: verify attestations for pipeline outputs before promotion.

### Runtime enforcement (minimum)

- **PEP (policy enforcement point)** sits in front of runtime surfaces.
- **Evidence resolver** resolves EvidenceRefs into EvidenceBundles. If resolution fails or is denied by policy, the system must narrow scope or abstain (never guess).
- Every user-facing response that claims facts must be bound to a dataset version and evidence bundle.

---

## Consequences

### Benefits

- Reproducible truth path from upstream → published UI answers.
- Strong audit posture: every promotion is explainable, reversible, and evidenced.
- Operational safety: projections can be rebuilt without losing canonical truth.
- Safer handling of sensitive locations and unclear rights via quarantine + default deny.

### Costs / tradeoffs

- More upfront work: specs, catalogs, receipts, and checksums are mandatory.
- Longer CI times; more artifacts to store and manage.
- Requires disciplined versioning and controlled vocabularies.

---

## Alternatives considered

1. **Single “staging” bucket without strict zones**  
   Rejected: does not enforce immutability; audits and rollbacks become fragile.

2. **Treat database as canonical store**  
   Rejected: breaks rebuildability; increases drift risk and complicates provenance.

3. **Manual steward sign-off without automated gates**  
   Rejected: does not scale; cannot reliably fail closed.

---

## Minimum verification steps

> This ADR defines the contract. The repo implementation MUST be verified against the live repository.

- [ ] Capture current commit hash and a root directory tree.
- [ ] Confirm current CI workflows and required status checks.
- [ ] Choose a pilot dataset and run it through RAW → WORK → PROCESSED → CATALOG → promotion manifest.
- [ ] Confirm EvidenceRef resolution end-to-end in Map Explorer and Story publishing.
- [ ] Confirm Focus Mode emits run receipts and fails closed on unverifiable citations.

---

## Appendix

### A. Run receipt (template)

```json
{
  "run_id": "kfm://run/2026-03-01T12:00:00Z.example",
  "actor": {"principal": "svc:pipeline", "role": "pipeline"},
  "operation": "ingest+publish",
  "dataset_version_id": "2026-03.example1234",
  "inputs": [{"uri": "raw/source.ext", "digest": "sha256:..."}],
  "outputs": [{"uri": "processed/output.ext", "digest": "sha256:..."}],
  "environment": {
    "container_digest": "sha256:...",
    "git_commit": "deadbeef",
    "params_digest": "sha256:..."
  },
  "validation": {"status": "pass", "report_digest": "sha256:..."},
  "policy": {"decision_id": "kfm://policy_decision/..."},
  "created_at": "2026-03-01T12:05:00Z"
}
```

### B. Promotion manifest (template)

```json
{
  "kfm_promotion_manifest_version": "v1",
  "dataset_slug": "example_dataset",
  "dataset_version_id": "2026-03.example1234",
  "spec_hash": "sha256:...",
  "released_at": "2026-03-01T13:00:00Z",
  "artifacts": [
    {"path": "events.parquet", "digest": "sha256:...", "media_type": "application/x-parquet"}
  ],
  "catalogs": [
    {"path": "dcat.jsonld", "digest": "sha256:..."},
    {"path": "stac/collection.json", "digest": "sha256:..."}
  ],
  "qa": {"status": "pass", "report_digest": "sha256:..."},
  "policy": {"policy_label": "public", "decision_id": "kfm://policy_decision/..."},
  "approvals": [
    {"role": "steward", "principal": "<id>", "approved_at": "2026-03-01T12:59:00Z"}
  ]
}
```

### C. Glossary

- **DCAT:** dataset-level metadata (license, publisher, distributions)
- **STAC:** asset-level spatiotemporal metadata (collections, items, assets)
- **PROV:** lineage graph for how artifacts were created (activities, agents, entities)

---

*Back to top:* [Navigation](#navigation)# ADR 0003: Data Zones and Promotion Contract

- **Status:** proposed

Planned ADR placeholder.
