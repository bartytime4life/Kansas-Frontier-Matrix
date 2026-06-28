<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/readme
name: Receipts README
path: data/receipts/README.md
type: data-receipts-root-readme
version: v0.2.0
status: draft
owners:
  - <receipt-steward>
  - <validation-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: internal-governance
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: receipts
receipt_scope: process-memory
path_posture: existing-root-stub-replaced; child-lanes-observed-by-github-search; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; receipt-not-catalog; receipt-not-release; policy-aware; release-blocked-until-gates-close
related:
  - validation/README.md
  - telemetry/README.md
  - flora/README.md
  - redaction/flora/README.md
  - aggregation/README.md
  - ai/README.md
  - fauna/README.md
  - soil/README.md
  - ../proofs/README.md
  - ../catalog/README.md
  - ../registry/README.md
  - ../../release/
  - ../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../docs/standards/RUN_RECEIPT.md
  - ../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - run-receipts
  - process-memory
  - audit
  - provenance
  - validation
  - telemetry
  - redaction
  - aggregation
  - governed-ai
  - proof-separation
  - catalog-separation
  - release-separation
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/receipts/README.md`."
  - "Directory Rules identify path placement as governance: a file location encodes responsibility root, lifecycle phase, and governance posture."
  - "ADR-0011 is proposed and states the core boundary: receipt != proof != catalog != publication."
  - "RunReceipt standard states receipts live under `data/receipts/` and that a receipt does not prove factual correctness, legal admissibility, historical truth, scientific certainty, or public-safety suitability."
  - "Child-lane presence is README/path evidence only; emitted payloads, schemas, validators, CI checks, signing, release integration, correction hooks, and rollback hooks remain NEEDS VERIFICATION unless separately proven."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Receipts

Root lane for KFM receipt process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Root: data" src="https://img.shields.io/badge/root-data-blue">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
  <img alt="Boundary: not catalog" src="https://img.shields.io/badge/boundary-not%20catalog-critical">
  <img alt="Boundary: not release" src="https://img.shields.io/badge/boundary-not%20release-critical">
</p>

**Quick links:** [Purpose](#purpose) · [Path posture](#path-posture) · [Receipt boundary](#receipt-boundary) · [Repo fit](#repo-fit) · [Observed child lanes](#observed-child-lanes) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested receipt envelope](#suggested-receipt-envelope) · [Suggested directory shape](#suggested-directory-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/` is for process-memory records. A receipt can show that a governed run, validation, transform, redaction, aggregation, AI call, telemetry collection, migration, correction, rollback, or release-support action happened. It does **not** prove the claim is true, does **not** approve publication, does **not** replace evidence, does **not** close the catalog, and does **not** become a public artifact by itself.

---

## Purpose

Receipts make KFM operations inspectable, replayable, reviewable, correctable, and reversible. They preserve the small audit record of **what a process did**, **what inputs and rules it used**, **what outcome it produced**, and **what downstream gates still have to happen**.

Receipts may support:

- source intake and watcher runs;
- schema, contract, fixture, policy, and validation checks;
- transformation, normalization, redaction, generalization, aggregation, and model-materialization runs;
- governed-AI invocations and abstentions;
- telemetry and observability snapshots;
- migration, correction, stale-state, supersession, rollback, and release-support actions;
- promotion review and release dry runs.

Receipts are intentionally separate from the payloads, proofs, catalogs, release decisions, and public outputs they reference.

---

## Path posture

The receipt family root is:

```text
data/receipts/
```

This path belongs under the `data/` responsibility root because receipt instances are lifecycle artifacts emitted by governed work. Directory placement is part of governance: the path tells reviewers that these objects are process memory, not source payloads, proof packs, catalog records, release manifests, or published artifacts.

Receipt subtype and domain lanes may exist below this root, for example:

```text
data/receipts/validation/
data/receipts/telemetry/
data/receipts/flora/
data/receipts/redaction/flora/
```

Exact subtype/domain ordering remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms the pattern.

---

## Receipt boundary

KFM keeps these artifact families separate:

```text
receipt != proof != catalog != publication
```

| Family | Canonical role | Typical home | Boundary |
|---|---|---|---|
| Receipt | Process memory: what a run or governed action did. | `data/receipts/` | Not proof, not catalog closure, not release approval, not public truth. |
| Proof | Release-grade support: EvidenceBundle, ProofPack, citation validation, integrity support, closure objects. | `data/proofs/` | Not a discovery catalog and not a release decision by itself. |
| Catalog | Discovery and interchange records such as STAC, DCAT, and PROV. | `data/catalog/` | Catalog entries are carriers; they do not make claims true or publishable. |
| Release / publication | Promotion decisions, release manifests, rollback cards, correction notices, withdrawal notices, signatures, and released public-safe artifacts. | `release/` and `data/published/` | Publication is a governed state transition, not a file move. |

> [!IMPORTANT]
> A valid signed receipt can prove that a specific governed execution occurred, but it does not prove factual correctness, legal admissibility, scientific certainty, cultural suitability, rights clearance, or public-safety suitability. Those remain evidence, policy, review, proof, catalog, and release concerns.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Lifecycle role | process memory and audit trail for governed operations |
| Upstream producers | watchers, pipelines, validators, redactors, aggregators, model runners, governed-AI adapters, telemetry collectors, migration tools, release dry runs, correction/rollback tools, CI jobs |
| Downstream consumers | reviewers, proof assemblers, catalog-closure checks, release stewards, correction reviewers, rollback reviewers, audit tools, drift registers, governed API/UI readiness checks |
| Public access posture | No direct public path. Public clients use governed APIs and released artifacts. |
| Payload authority | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, and `data/published/`, not this lane |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Source registry authority | `data/registry/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Contract/schema authority | `contracts/` and `schemas/`, not this lane |
| Release authority | `release/`, not this lane |
| Default failure posture | `DENY`, `ABSTAIN`, `HOLD`, `NEEDS_REVIEW`, `QUARANTINE`, `FAIL`, or `ERROR` when evidence, source role, rights, sensitivity, policy, review, validation, correction, rollback, or release state is unresolved |

---

## Observed child lanes

The lanes below were observed through current GitHub reads/searches while replacing this root stub. This confirms path or README evidence only. It does **not** prove emitted receipts, schemas, validators, fixtures, CI enforcement, signatures, policy enforcement, review workflows, release integration, correction hooks, rollback hooks, or public-safe summaries.

| Child lane | Status | Purpose | Boundary |
|---|---:|---|---|
| [`validation/`](validation/README.md) | CONFIRMED README | Parent lane for validation receipt process-memory records. | Validation receipts are not proofs, catalog closure, policy approval, release authority, or source truth. |
| [`validation/atmosphere/`](validation/atmosphere/README.md) | CONFIRMED README | Atmosphere/Air validation receipt lane. | Not public air-quality guidance, emergency alerting, proof, catalog, release, or source truth. |
| [`validation/doctrine_artifact_check/`](validation/doctrine_artifact_check/README.md) | CONFIRMED README | Required doctrine-artifact prerequisite check receipts. | Not doctrine authority, artifact admission, proof, catalog closure, or promotion decision. |
| [`validation/flora/`](validation/flora/README.md) | CONFIRMED README | Flora validation receipt lane. | Not Flora truth, exact-location authority, policy, proof, catalog, release, or public output. |
| [`telemetry/`](telemetry/README.md) | CONFIRMED PATH | Telemetry receipt lane. | Not runtime authority, proof, catalog, release, or public truth by itself. |
| [`flora/`](flora/README.md) | CONFIRMED README | Flora domain parent receipt lane. | Not rare-plant truth, exact-location authority, sensitivity policy, proof, release approval, or public artifact authority. |
| [`redaction/flora/`](redaction/flora/README.md) | CONFIRMED README | Flora redaction/geoprivacy receipt lane. | Redaction receipt is not release approval or public geometry authority. |
| [`aggregation/`](aggregation/README.md) | CONFIRMED PATH | Aggregation receipt lane. | Aggregation receipts do not prove source truth or release safety. |
| [`ai/`](ai/README.md) | CONFIRMED PATH | Governed-AI receipt lane. | AI receipts are not sovereign truth and do not replace EvidenceBundle resolution. |
| [`fauna/`](fauna/README.md) | CONFIRMED PATH | Fauna domain receipt lane. | Sensitive species and geoprivacy controls still govern downstream use. |
| [`soil/`](soil/README.md) | CONFIRMED PATH | Soil domain receipt lane. | Soil process memory is not source payload, proof, catalog closure, or release approval. |

---

## Accepted material

Accepted content is limited to receipt instances and receipt-local sidecars:

- `RunReceipt`, `TransformReceipt`, `ValidationReport`, `RedactionReceipt`, `AggregationReceipt`, `AIReceipt`, `ModelRunReceipt`, `ReviewRecord`, telemetry receipts, migration receipts, correction-support receipts, rollback-support receipts, release-support receipts, and other governed process-memory records;
- run IDs, source refs, object refs, input/output hashes, evidence refs, policy refs, schema refs, contract refs, validator refs, transform refs, reviewer refs, finite outcomes, reason codes, correction refs, rollback refs, release-candidate refs, timestamps, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, DSSE/cosign sidecars, and local reproducibility notes where applicable;
- README files and local indexes that help stewards inspect receipt state without becoming proof, catalog, policy, release, public output, source truth, or generated-answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw source payloads, exact sensitive coordinates, source-native files, private identifiers, restricted records, or acquired source packages | `data/raw/` or governed restricted storage as applicable |
| Work/candidate outputs, scratch transforms, unresolved checks, or intermediate payloads | `data/work/` |
| Quarantined material and unresolved sensitive records | `data/quarantine/` |
| Processed objects or public-safe derivatives | `data/processed/` after gates; `data/published/` only after release |
| EvidenceBundle, ProofPack, CatalogMatrix, citation-validation closure, signatures, or integrity proof | `data/proofs/` |
| STAC, DCAT, PROV, discovery records, or catalog closure output | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/` and source governance roots |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, release signature, or release changelog | `release/` |
| Rights, sensitivity, geoprivacy, source-role, publication, access-control, or release policy | `policy/` and governed policy roots |
| Semantic contracts and machine schemas | `contracts/` and `schemas/` |
| Validator code, pipeline code, packages, fixtures, tests, CI workflows, or runtime services | `tools/`, `pipelines/`, `packages/`, `fixtures/`, `tests/`, `.github/workflows/`, `runtime/`, or app roots as applicable |
| Full logs, crash dumps, stack traces, CI transcripts, credentials, tokens, secrets, private review notes, or sensitive operational telemetry | appropriate private CI/runtime/log system or restricted review artifact path; reference bounded digest only |
| Public map/API/UI payloads, graph edges, vector-index content, reports, dashboards, or generated answer text | governed public outputs only after evidence, policy, validation, review, release, correction, and rollback gates close |

---

## Suggested receipt envelope

The exact machine schema remains **NEEDS VERIFICATION** until accepted schema and validator evidence exists. Receipt instances should remain small, deterministic, reviewable, and hashable.

| Field | Purpose |
|---|---|
| `id` | Stable receipt identity. |
| `receipt_type` | Receipt family such as `run`, `validation`, `transform`, `redaction`, `aggregation`, `ai`, `telemetry`, `migration`, `correction`, `rollback`, or `release_support`. |
| `domain` or `lane` | Domain lane, system lane, or check family. |
| `run_ref` | Pipeline, CI, local smoke, dry-run, model, review, correction, or release-support run identifier. |
| `actor` / `runner_id` | Tool, service, or human/steward identity responsible for the run. |
| `started_at` / `completed_at` | Run timing. |
| `source_refs` | Source descriptors, source versions, registry entries, URLs, commits, or source-state refs used. |
| `subject_refs` | Records, files, artifacts, layers, releases, catalog entries, or fixtures affected. |
| `input_hashes` / `output_hashes` | Integrity pins for material inputs and outputs. |
| `schema_refs` / `contract_refs` | Schemas and semantic contracts used. |
| `policy_refs` | Policies or policy decisions applied. |
| `evidence_refs` | EvidenceRef/EvidenceBundle references evaluated or produced. |
| `outcome` | Finite outcome such as `PASS`, `WARN`, `FAIL`, `DENY`, `ABSTAIN`, `HOLD`, `QUARANTINE`, or `ERROR`. |
| `reason_codes` | Stable reason codes for the outcome. |
| `promotion_blocking` | Whether the receipt blocks promotion or release review. |
| `correction_refs` / `rollback_refs` | Correction and rollback references when applicable. |
| `signature_refs` | DSSE/cosign/signing sidecars when applicable. |
| `public_summary` | Optional redacted summary safe for review surfaces. |

---

## Suggested directory shape

The following map is documentation guidance, not proof that these payloads exist.

```text
data/receipts/
├── README.md
├── validation/
│   ├── README.md
│   ├── atmosphere/
│   ├── doctrine_artifact_check/
│   └── flora/
├── telemetry/
│   └── README.md
├── flora/
│   └── README.md
├── redaction/
│   └── flora/
├── aggregation/
├── ai/
├── fauna/
├── soil/
├── <domain-or-lane>/
│   ├── <run_id>/
│   │   ├── receipt.json
│   │   ├── checksums.sha256
│   │   └── README.md
│   └── index.local.json
└── index.local.json
```

`index.local.json` files are optional and receipt-local only. They are not proof indexes, catalog records, release manifests, public-layer pointers, search indexes, vector indexes, map sources, policy authorities, location authorities, or generated-answer sources.

---

## Required checks before use

- [ ] Confirm the record belongs under `data/receipts/` or an accepted receipt lane.
- [ ] Confirm canonical receipt naming against accepted receipt-layout governance before relying on the path as final layout authority.
- [ ] Confirm receipt ID, run ID, actor/runner identity, source refs, subject refs, input/output hashes, schema/contract refs, policy refs, evidence refs, timestamps, outcome, reason codes, blocker status, and signatures are present where applicable.
- [ ] Confirm sensitive details are not exposed in README/index/public-summary text.
- [ ] Confirm the receipt does not silently upgrade evidence strength, source role, rights state, review state, release state, or public-safe posture.
- [ ] Confirm EvidenceRef/EvidenceBundle closure is separately proven when the receipt supports consequential claims.
- [ ] Confirm policy, proof, catalog, correction, rollback, and release states remain separate object families.
- [ ] Confirm a `PASS` receipt is not treated as proof, catalog closure, release approval, public artifact authority, or source truth.
- [ ] Confirm a `FAIL`, `DENY`, `ABSTAIN`, `HOLD`, `QUARANTINE`, or `ERROR` receipt is retained long enough to support correction, audit, and rollback analysis.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, map layer, generated answer, or released report reads this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the greenfield stub at `data/receipts/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as a greenfield stub before this edit. | CONFIRMED by GitHub contents API during this edit |
| Directory Rules state that file location encodes responsibility root, lifecycle phase, and governance posture. | CONFIRMED from repo documentation |
| ADR-0011 states the intended boundary `receipt != proof != catalog != publication`. | CONFIRMED proposed ADR text; acceptance remains proposed unless separately verified |
| RunReceipt standard states receipt storage belongs under `data/receipts/` and that receipts do not prove factual correctness or public-safety suitability. | CONFIRMED from repo documentation |
| Child README/path evidence exists for validation, atmosphere validation, doctrine artifact check, flora validation, telemetry, flora, redaction/flora, aggregation, ai, fauna, and soil lanes. | CONFIRMED by current GitHub reads/searches |
| Emitted receipt payloads exist across all listed lanes. | UNKNOWN |
| CI currently emits receipts into all relevant lanes. | UNKNOWN |
| A canonical receipt schema is fully enforced across all child lanes. | NEEDS VERIFICATION |
| This README grants public access to receipt internals. | DENY |

---

## Maintainer note

Receipts are valuable because they make governed work reconstructible. They become dangerous when treated as the same thing as proof, policy, catalog closure, release, or truth. Keep the chain explicit:

```text
source / candidate / run -> receipt -> review input -> proof/catalog/policy/release checks -> governed public surface
```

Never collapse it into:

```text
receipt -> public truth
```
