<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/validation/readme
name: Validation Receipts README
path: data/receipts/validation/README.md
type: data-receipts-validation-parent-readme
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
artifact_family: validation-receipts
receipt_scope: validation-process-memory
path_posture: existing-parent-stub-replaced; child-lanes-confirmed; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; validation-not-release; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - atmosphere/README.md
  - doctrine_artifact_check/README.md
  - flora/README.md
  - ../../proofs/README.md
  - ../../catalog/README.md
  - ../../registry/README.md
  - ../../../contracts/data/validation_report.md
  - ../../../contracts/domains/flora/domain_validation_report.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/standards/RUN_RECEIPT.md
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - validation
  - validator-output
  - process-memory
  - audit
  - governance
  - proof-separation
  - release-separation
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/receipts/validation/README.md`."
  - "Validation receipts record validator runs and validation outcomes. They do not create source truth, proof authority, catalog closure, policy approval, promotion decisions, release manifests, or public claims."
  - "Confirmed child lanes during this edit: `atmosphere/`, `doctrine_artifact_check/`, and `flora/`."
  - "Exact receipt subtype layout remains NEEDS VERIFICATION until accepted receipt-layout governance or ADR review confirms the pattern."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Validation Receipts

Parent lane for validation receipt process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Lane: validation" src="https://img.shields.io/badge/lane-validation-blue">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
  <img alt="Boundary: not release" src="https://img.shields.io/badge/boundary-not%20release-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Receipt boundary](#receipt-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/validation/` is for validation receipt process memory only. It is not source truth, proof authority, catalog closure, policy approval, review approval, release authority, public artifact storage, public UI/API material, or generated-answer authority.

---

## Scope

This directory is the parent lane for receipts emitted by validation activity across KFM. A validation receipt records that a bounded check ran, what it inspected, what rules or references it used, what outcome it produced, and what follow-up review or gate action is needed.

Validation receipts may support:

- schema, contract, fixture, lint, and validator runs;
- source-descriptor and source-registry preflight checks;
- evidence-resolution checks;
- policy, rights, sensitivity, and geoprivacy preflight checks;
- domain object validation;
- map/layer/tile/raster/vector validation;
- catalog-closure readiness review;
- release-candidate dry runs;
- correction, stale-state, supersession, and rollback checks;
- CI, local smoke, and no-network fixture validation records.

Receipts in this branch can support later proof assembly, catalog closure, release review, correction review, rollback review, Evidence Drawer readiness, or governed API/UI readiness. They do **not** replace any of those object families.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. This validation parent lane is:

```text
data/receipts/validation/
```

Child lanes may be organized by domain, validator family, artifact class, or special prerequisite check. Current child lanes are documentation evidence only unless emitted receipt payloads, schemas, validators, fixtures, CI checks, and release integrations are separately verified.

The exact choice between subtype-first lanes such as:

```text
data/receipts/validation/<domain>/
```

and domain-first lanes such as:

```text
data/receipts/<domain>/validation/
```

remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms the pattern.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/validation/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Receipt subtype | validation process memory |
| Parent lane | `data/receipts/` |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream producers | validators, dry-run checks, fixture tests, policy preflights, CI jobs, release dry runs, correction checks, rollback checks |
| Downstream consumers | review, proof assembly, catalog closure review, release review, drift review, correction review, rollback analysis, Evidence Drawer/API/UI readiness review |
| Lifecycle payload authority | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, and `data/published/`, not this lane |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Source registry authority | `data/registry/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Contract/schema authority | `contracts/` and `schemas/`, not this lane |
| Release authority | `release/`, not this lane |
| Default failure posture | `FAIL`, `DENY`, `ABSTAIN`, `HOLD`, `NEEDS_REVIEW`, `QUARANTINE`, or `ERROR` when evidence, source role, rights, sensitivity, policy, validation, correction, rollback, or release state is unresolved |

---

## Confirmed child lanes

The child lanes below were confirmed by current GitHub reads while replacing this parent stub. This confirms path/README evidence only; it does **not** prove emitted receipt payloads, validators, schemas, fixtures, CI enforcement, signing, review workflow, release integration, correction hooks, rollback hooks, or public-safe summaries.

| Child lane | Status | Purpose | Boundary |
|---|---:|---|---|
| [`atmosphere/`](atmosphere/README.md) | CONFIRMED README | Atmosphere/Air validation receipts for source descriptors, datasets, layer candidates, evidence bundles, policy checks, knowledge-character checks, temporal checks, no-life-safety posture, and release candidates. | Not public air-quality guidance, emergency alerting, proof, catalog, release, or source truth. |
| [`doctrine_artifact_check/`](doctrine_artifact_check/README.md) | CONFIRMED README | Required doctrine-artifact validation receipts emitted by the doctrine-artifact prerequisite check. | Not doctrine authority, artifact admission, proof, catalog closure, or promotion decision. |
| [`flora/`](flora/README.md) | CONFIRMED README | Flora validation receipts for taxon, source-role, evidence, geometry, sensitivity, redaction, rights, release-candidate, correction, and rollback checks. | Not Flora truth, exact-location authority, rare-plant authority, proof, policy, catalog, release, or public output. |

---

## Receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records a validator run or validation outcome. It is not the thing validated. |
| Validation is not truth | Passing validation does not create a source fact, evidence bundle, claim, or observation. |
| Validation is not policy approval | PolicyDecision and policy enforcement remain separate object families. |
| Validation is not proof | Proof packs, EvidenceBundle closure, citation validation, signatures, and integrity attestations remain in `data/proofs/` or the accepted proof lane. |
| Validation is not catalog closure | STAC/DCAT/PROV/catalog records remain in `data/catalog/`. |
| Validation is not release | ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, and release signature belong in `release/`. |
| Sensitive detail stays protected | Validation receipts and indexes must not expose restricted geometry, private identifiers, tokens, credentials, protected locations, culturally sensitive detail, or steward-only notes. |
| Public clients do not read receipts directly | Public surfaces consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to validation receipt instances and receipt-local sidecars:

- run receipt JSON or JSONL records;
- schema, contract, fixture, source-registry, evidence, policy-preflight, sensitivity, geoprivacy, layer, catalog-readiness, release-candidate, correction, rollback, and composite validation receipts;
- run IDs, validator refs, validator versions, ruleset refs, schema refs, contract refs, policy refs, source refs, subject refs, evidence refs, review refs, redaction refs, release-candidate refs, correction refs, rollback refs, timestamps, actor/runner identity, finite outcomes, reason codes, blocker status, severity counts, input/output hashes, and signatures;
- public-safe summaries with sensitive details removed;
- receipt manifests, checksums, signing sidecars, and reproducibility notes where applicable;
- README files and local indexes that help stewards inspect validation receipt state without becoming proof, catalog, policy, release, public output, source truth, location authority, or generated-answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw source payloads, exact sensitive coordinates, source-native files, private identifiers, or restricted records | `data/raw/` or governed restricted storage as applicable |
| Work/candidate outputs, scratch transforms, and unresolved validation experiments | `data/work/` |
| Quarantined or unresolved sensitive material | `data/quarantine/` |
| Processed payloads or public-safe derivatives | `data/processed/` after gates; `data/published/` only after release |
| EvidenceBundle, ProofPack, CatalogMatrix, citation-validation closure, signatures, or integrity proof | `data/proofs/` |
| STAC, DCAT, PROV, discovery records, or catalog closure output | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/` and source governance roots |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, signature, or release changelog | `release/` |
| Rights, sensitivity, geoprivacy, source-role, publication, access-control, or release policy | `policy/` and governed policy roots |
| Semantic contracts and machine schemas | `contracts/` and `schemas/` |
| Validator code, fixtures, package code, tests, or CI workflows | `tools/`, `fixtures/`, `packages/`, `tests/`, `.github/workflows/` |
| Full logs, crash dumps, stack traces, CI transcripts, or private review notes | appropriate private CI/runtime/log system or restricted review artifact path; reference bounded digest only |
| Public map/API/UI payloads, graph edges, vector-index content, reports, dashboards, or generated answer text | governed public outputs only after evidence, policy, validation, review, release, correction, and rollback gates close |

---

## Suggested directory shape

The following map is documentation guidance, not proof that these payloads exist.

```text
data/receipts/validation/
├── README.md
├── atmosphere/
│   └── README.md
├── doctrine_artifact_check/
│   └── README.md
├── flora/
│   └── README.md
├── <domain-or-check>/
│   ├── <run_id>/
│   │   ├── validation_receipt.json
│   │   ├── findings.jsonl
│   │   ├── checksums.sha256
│   │   └── README.md
│   └── index.local.json
└── index.local.json
```

`index.local.json` files are optional and receipt-local only. They are not proof indexes, catalog records, release manifests, public-layer pointers, search indexes, vector indexes, map sources, policy authorities, location authorities, or generated-answer sources.

---

## Suggested minimum receipt fields

The exact machine schema remains **NEEDS VERIFICATION** until accepted schema and validator evidence exists. A validation receipt should be structured enough for audit, replay, review, correction, and rollback.

| Field | Purpose |
|---|---|
| `id` | Stable receipt identity. |
| `receipt_type` | Usually `validation`. |
| `domain` or `check_family` | Domain lane or special validation family. |
| `run_ref` | Pipeline, CI, local smoke, or dry-run identifier. |
| `validator_ref` | Validator name, path, package, or ruleset. |
| `validator_version` | Version, commit, hash, or ruleset digest. |
| `subject_refs` | Records, files, artifacts, releases, catalog entries, or fixtures checked. |
| `schema_refs` / `contract_refs` | Schemas and semantic contracts used. |
| `policy_refs` | Policies or policy inputs checked. |
| `evidence_refs` | EvidenceRef/EvidenceBundle references evaluated. |
| `input_hashes` | Input artifact hashes used by the run. |
| `outcome` | Finite outcome: `PASS`, `WARN`, `FAIL`, `DENY`, `ABSTAIN`, or `ERROR`. |
| `promotion_blocking` | Whether findings block promotion or release review. |
| `reason_codes` | Stable reason codes for warnings, failures, denials, or abstentions. |
| `severity_counts` | Finding counts by severity. |
| `public_summary` | Optional redacted summary safe for review surfaces. |
| `created_at` | Run completion or receipt emission timestamp. |

---

## Required checks before use

- [ ] Confirm the receipt belongs under `data/receipts/validation/` or an accepted validation receipt lane.
- [ ] Confirm canonical receipt naming against accepted receipt-layout governance before relying on the path as final layout authority.
- [ ] Confirm receipt ID, run ID, validator ref, ruleset refs, schema refs, contract refs, policy refs, subject refs, evidence refs, input hashes, timestamps, actor/runner identity, outcome, blocker status, and signatures are present where applicable.
- [ ] Confirm sensitive details are not exposed in README/index/public-summary text.
- [ ] Confirm validation did not silently upgrade source role, evidence strength, rights state, review state, release state, or public-safe posture.
- [ ] Confirm EvidenceRef/EvidenceBundle closure is reported when the validation supports consequential claims.
- [ ] Confirm policy, review, correction, rollback, and release states remain separate object families.
- [ ] Confirm a `PASS` receipt is not treated as proof, catalog closure, release approval, public artifact authority, or source truth.
- [ ] Confirm a `FAIL`, `DENY`, `ABSTAIN`, or `ERROR` receipt is retained long enough to support correction, audit, and rollback analysis.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, map layer, generated answer, or released report reads this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the greenfield stub at `data/receipts/validation/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as a greenfield stub before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/receipts/validation/atmosphere/README.md` exists as a child validation receipt README. | CONFIRMED by GitHub contents API during this edit |
| `data/receipts/validation/doctrine_artifact_check/README.md` exists as a child validation receipt README. | CONFIRMED by GitHub contents API during this edit |
| `data/receipts/validation/flora/README.md` exists as a child validation receipt README. | CONFIRMED by GitHub contents API during this edit |
| Emitted validation receipt payloads exist under this parent lane. | UNKNOWN |
| CI currently emits validation receipts into this parent lane. | UNKNOWN |
| A canonical validation receipt schema is fully enforced across all child lanes. | NEEDS VERIFICATION |
| This README grants public access to validation internals. | DENY |

---

## Maintainer note

Validation receipts are valuable because they make checks inspectable, replayable, reviewable, correctable, and reversible. They become dangerous when treated as the same thing as proof, policy, catalog closure, or release. Keep the chain explicit:

```text
validation receipt -> review input -> proof/catalog/policy/release checks -> governed public surface
```

Never collapse it into:

```text
validation receipt -> public truth
```
