<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/3c7a6cf8-4ad3-4cb8-9b9e-8c6f0c9c2c64
title: Identity and Time
type: standard
version: v1
status: draft
owners: KFM Core Maintainers (TBD)
created: 2026-03-01
updated: 2026-03-01
policy_label: public
related:
  - kfm://doc/core/evidence-and-citations (TBD)
  - kfm://doc/core/run-receipts-and-audit-ledger (TBD)
tags: [kfm, core, identity, time, governance]
notes:
  - This doc intentionally separates Confirmed vs Proposed vs Unknown so CI gates can be implemented without guesswork.
[/KFM_META_BLOCK_V2] -->

# Identity and Time
Map-first, time-aware systems fail without stable identity and unambiguous time semantics. This doc defines the KFM core vocabulary and minimum invariants so datasets, catalogs, APIs, UI, and Focus Mode can all agree.

![status](https://img.shields.io/badge/status-draft-orange) <!-- TODO: wire to real workflow -->
![domain](https://img.shields.io/badge/domain-core-blue)
![policy](https://img.shields.io/badge/policy-public-brightgreen)
![gates](https://img.shields.io/badge/promotion%20gates-A%2CF%2CD-blueviolet) <!-- TODO: confirm gate lettering in repo -->

**Status:** draft • **Owners:** KFM Core Maintainers (TBD)

---

## Navigation
- [Legend](#legend)
- [Why this exists](#why-this-exists)
- [Core terms](#core-terms)
- [Identity model](#identity-model)
  - [Identifier registry](#identifier-registry)
  - [Deterministic hashing](#deterministic-hashing)
  - [Promotion gates that depend on identity](#promotion-gates-that-depend-on-identity)
- [Time model](#time-model)
  - [Three time axes](#three-time-axes)
  - [Recommended field semantics](#recommended-field-semantics)
  - [Freshness](#freshness)
- [Evidence and citation binding](#evidence-and-citation-binding)
- [Tests and “fail closed” rules](#tests-and-fail-closed-rules)
- [Unknowns to resolve in the live repo](#unknowns-to-resolve-in-the-live-repo)
- [Assumptions, risks, tradeoffs, minimum verification steps](#assumptions-risks-tradeoffs-minimum-verification-steps)

---

## Legend

This doc uses explicit truth labeling so we don’t accidentally “invent” governance rules.

- ✅ **Confirmed**: backed by KFM reference docs (see Section 2 citations in the ChatGPT response).
- 🧪 **Proposed**: recommended convention; OK to implement, but do not claim it is enforced until CI/tests exist.
- ❓ **Unknown**: must be verified in the live repo (schemas, paths, existing IDs, exact formats, etc.).

> **WARNING**
> Do not claim specific repo subpackages or file paths exist unless verified in the live repo. Prefer “recommended placement” + a verification checklist.

---

## Why this exists

KFM is **governed, evidence-first, map-first, and time-aware**: every layer/claim/answer must be traceable to versioned sources with policy enforced in CI and at runtime. Stable identity and clear time semantics are the backbone that makes that possible.

---

## Core terms

✅ **Dataset**: a logical dataset identity, e.g., “NOAA Storm Events” or “USGS NWIS (Kansas)”.

✅ **DatasetVersion**: an **immutable** version of a dataset corresponding to a specific promoted output set. A dataset has many versions over time.

✅ **Artifact**: a concrete produced object (GeoParquet, PMTiles, COG, JSONL, PDF, etc.) referenced by STAC/DCAT/PROV.

✅ **EvidenceRef**: a stable reference to evidence using explicit schemes such as `dcat://`, `stac://`, `prov://`, `doc://`, `graph://`. Evidence must resolve in bounded calls.

✅ **EvidenceBundle**: the resolver’s returned evidence view (human + machine fields, policy decision results). Bundles should be immutable by digest so they are cacheable and reproducible.

✅ **Run receipt (run_record)**: emitted by every pipeline run (and Focus Mode query), capturing inputs/outputs by digest, environment, validation results, and policy decisions.

✅ **Audit ledger**: append-only; treated as a governed dataset (redactions applied as needed).

---

## Identity model

### Identifier registry

✅ KFM needs stable identifiers across catalogs (DCAT/STAC/PROV), governed APIs, UI “trust surfaces”, and citations. The Promotion Contract explicitly requires identity/versioning artifacts.

Use this registry as the canonical vocabulary:

| Identifier | What it identifies | Stability | Where it appears | Notes |
|---|---|---|---|---|
| `dataset_id` | Logical dataset | Stable over time | Registry, DCAT/STAC/PROV, API, UI, citations | ✅ Required for discovery + governance. |
| `dataset_version_id` | Immutable promoted dataset version | Immutable | Catalog triplet, API responses, EvidenceBundle, UI | ✅ Must exist for every promoted version. |
| `spec_ref` | Pointer to onboarding/spec definition | Stable per spec file | Registry, receipts | ✅ Used to link humans → transforms/QA definition. |
| `spec_hash` | Deterministic hash of the spec | Immutable for spec content | Registry, receipts, CI gates | ✅ Blocks silent drift; supports signing/caching. |
| `artifact_digest` | Digest-addressed artifact | Immutable | STAC/DCAT assets, receipts, EvidenceBundle | ✅ Artifact identity is by digest. |
| `bundle_id` | Digest-addressed evidence bundle | Immutable | Evidence resolver output | ✅ Enables safe caching + traceability. |
| `run_id` | A single run execution | Immutable | PROV, receipts, lineage APIs | ✅ Links outputs back to inputs + environment. |

> **NOTE**
> Exact string formats (prefixes, separators, length constraints) are 🧪 Proposed unless you can point to a schema/tests in the live repo.

---

### Deterministic hashing

✅ Reproducibility depends on stable dataset identity and stable version identity. Deterministic hashing (`spec_hash`) based on canonical JSON is a recommended pattern to prevent “hash drift” and to support signature verification and caching.

✅ KFM convention is 🧪 Proposed (but aligned to sources): **every artifact is addressed by digest**, and every catalog record points to digest-addressed artifacts.

**Recommended hashing rules (mix of ✅ Confirmed direction + 🧪 Proposed operationalization):**

1. ✅ **Hash canonical JSON, not “pretty JSON”.**
   - 🧪 Use RFC 8785 JSON Canonicalization Scheme (JCS) for any hashed JSON objects.
2. ✅/🧪 **Lock metadata versions explicitly before hashing.**
   - Example: for STAC, set `stac_version` explicitly and hash only canonicalized JSON.
3. ✅ **Record `spec_ref` + `spec_hash` in the dataset registry** to block silent drift.
4. ✅ **Recompute hashes in CI** (not only at build time) to detect drift before promotion.
5. 🧪 **Use explicit digest prefixes** (e.g., `sha256:<hex>`) consistently for artifacts/bundles.

---

### Promotion gates that depend on identity

✅ Promotion to **PUBLISHED** is blocked unless minimum gates are met. The two most identity-critical gates:

- ✅ **Gate A — Identity & versioning**: `dataset_id` + `dataset_version_id`; deterministic `spec_hash`; content digests.
- ✅ **Gate F — Run receipt & audit record**: run receipt capturing inputs/tooling/hashes/policy decisions; append-only audit record.

Identity also touches:

- ✅ **Gate D — Catalog triplet validation**: DCAT/STAC/PROV validate and cross-link; EvidenceRefs resolve without guessing.

---

## Time model

### Three time axes

✅ Historical and scientific data often needs more than one time axis:

- ✅ **Event time**: when something happened (example: flood peak).
- ✅ **Valid time**: the time a statement is considered true (example: county boundary existed from X to Y).
- ✅ **Transaction time**: when KFM recorded or published the data.

✅ Bitemporal or tritemporal modeling may be needed. Start with **event time + transaction time**, introduce valid time where boundary changes and administrative history require it.

---

### Recommended field semantics

Because this repo doc is meant to enable implementation, we need field-level conventions. These are **🧪 Proposed** until enforced by schema + CI:

#### 1) Event time (domain time)
- 🧪 `event_time`: an **instant** or **interval** describing when an observed phenomenon occurred.
- 🧪 If interval: represent as `[event_start, event_end)` (half-open) or an explicit `start/end` object.

#### 2) Valid time (truth-of-statement time)
- 🧪 `valid_time`: an interval describing when the record/geometry/claim is true “in the modeled world”.
- 🧪 Strongly recommended for administrative boundaries, jurisdictional changes, infrastructure “in-service” periods, etc.

#### 3) Transaction time (KFM system time)
- 🧪 `transaction_time`: an instant describing when KFM acquired/processed/published/recorded something.
- ✅ The run receipt and audit ledger are the canonical transaction-time record for KFM’s own actions.

#### Timezone + normalization
- 🧪 Prefer ISO 8601 timestamps.
- 🧪 Use UTC (`Z`) for KFM-generated timestamps (run receipts, publication timestamps).
- ✅ Some domains require special semantics; for example GTFS schedule times can be >24h and should retain domain semantics while generated timestamps normalize to UTC.

---

### Freshness

✅ “Freshness” is a trust surface. The Evidence Drawer should expose:

- Evidence bundle ID + digest
- DatasetVersion ID + dataset name
- License + attribution
- **Freshness (last run timestamp)** and validation status
- Provenance chain (run receipt link)
- Artifact links (only if policy allows)
- Redactions applied (obligations), with explanation

🧪 Proposed minimum freshness fields (until a schema exists):
- `last_run_at` (UTC instant; from run receipt)
- `upstream_snapshot_at` (when upstream was fetched; if applicable)
- `staleness_policy` (optional; from watcher/polling policy)

---

## Evidence and citation binding

✅ Evidence resolution is central: the evidence resolver accepts an EvidenceRef or structured reference, applies policy, and returns an EvidenceBundle (human card + machine metadata + digests + audit references). The UI should be able to use it in ≤2 calls.

✅ EvidenceBundle should include:
- immutable `bundle_id` (digest)
- `dataset_version_id`
- license/attribution
- policy decision + obligations applied
- provenance `run_id`
- artifact hrefs + digests (when allowed)
- audit reference

🧪 Proposed rule: **All externally-visible claims** (Stories + Focus Mode answers) MUST bind to resolvable EvidenceRefs that can be opened into EvidenceBundles.

---

## Tests and “fail closed” rules

✅ KFM’s governance posture is “fail closed”:
- If identity fields are missing → block promotion.
- If EvidenceRefs don’t resolve → block publishing.
- If hashes cannot be recomputed deterministically in CI → block.

**Minimum CI checks implied by the Promotion Contract (✅ Confirmed intent):**
- Recompute `spec_hash` and compare against committed registry/spec.
- Verify artifact digests match referenced objects.
- Validate DCAT + STAC + PROV schemas and cross-links.
- Ensure EvidenceRefs resolve without guessing.
- Validate run receipt schema (and signature/attestation if enabled).

---

## Unknowns to resolve in the live repo

These are deliberately marked ❓ until the repo is inspected (tree + schemas + tests):

- ❓ Exact `dataset_version_id` format (string pattern, sorting semantics, allowed chars).
- ❓ Canonical registry file location(s) and schema URLs.
- ❓ Run receipt schema location + required fields (beyond the conceptual list).
- ❓ EvidenceRef canonical scheme registry (are schemes enumerated?).
- ❓ Whether STAC/DCAT/PROV validators are already implemented and how they are invoked in CI.
- ❓ Exact definition of “content digest” for multi-file datasets (single manifest digest vs per-artifact digests).

---

## Assumptions, risks, tradeoffs, minimum verification steps

### Assumptions (explicit)
- We treat Dataset/DatasetVersion/Artifact/EvidenceRef/EvidenceBundle/Run receipt/Audit ledger as the core vocabulary across the system.
- Deterministic hashing is required for promotion and reproducibility.
- Time is multi-axis; at minimum, event time and transaction time must be supported.

### Risks
- **Identity drift** if canonicalization rules are not standardized and enforced (hashes become unstable; caches/signatures break).
- **Time ambiguity** if event/valid/transaction time are conflated (incorrect historical narratives; broken timeline UX).
- **Policy leakage** if evidence resolution isn’t the only way the UI/Focus Mode accesses artifacts.

### Tradeoffs
- Determinism adds up-front discipline (canonicalization, schemas, CI), but yields auditability and safe automation.
- Supporting valid time increases modeling complexity, but is necessary for administrative history and boundary changes.
- Digest-addressed artifacts improve reproducibility, but require careful manifesting and storage practices.

### Minimum verification steps (convert ❓ Unknown → ✅ Confirmed)
1. Capture repo commit hash + root tree (at least `tree -L 3`).
2. Locate dataset registry schema + confirm required fields/patterns.
3. Locate `spec_hash` computation code/tests (or implement golden tests).
4. Locate run receipt schema and confirm required receipt fields.
5. Confirm CI workflows include blocking gates for: spec_hash, catalog validation, evidence resolution, and receipt validation.
