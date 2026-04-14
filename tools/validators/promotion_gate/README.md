<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: Promotion Gate (A–G)
type: standard
version: v1
status: draft
owners: @bartytime4life
created: YYYY-MM-DD
updated: 2026-04-13
policy_label: public
related: [../../../contracts/README.md, ../../../schemas/promotion/decision-envelope.schema.json, ../../../schemas/promotion/promotion-record.schema.json, ../../../schemas/promotion/promotion-prov.schema.json, ../../../schemas/promotion/promotion-bundle.schema.json, ../../../schemas/promotion/promotion-bundle-diff-policy.schema.json, ../../../policy/README.md, ../../../policy/promotion_bundle_diff_policy.json, ../../../data/receipts/README.md, ../../../data/proofs/README.md, ../../../data/catalog/stac/README.md, ../../../data/catalog/dcat/README.md, ../../../data/catalog/prov/README.md, ../../../tests/README.md, ../../../tests/validators/test_promotion_gate_e2e.py, ../../../tests/validators/test_bundle_diff_policy.py, ../../../tests/validators/test_validate_bundle_diff_policy.py, ../../../tests/ci/test_render_promotion_review_handoff.py, ../../../tools/ci/render_promotion_summary.py, ../../../tools/ci/render_promotion_bundle_summary.py, ../../../tools/ci/render_diff_summary.py, ../../../tools/ci/render_bundle_diff_policy_summary.py, ../../../tools/ci/render_promotion_review_handoff.py, ../../../tools/diff/stable_diff.py, ../../../tools/catalog/catalog_crosslink.py, ../../../.github/workflows/README.md]
tags: [kfm, validators, promotion, governance, evidence, ci, diff-policy, review-handoff]
notes: [Updated to reflect the promotion bundle diff-policy thin slice plus the downstream composed promotion-review handoff artifact, including checked-in policy JSON, schema validation, prior/current bundle diff review, reviewer-facing policy summaries, and a single steward-facing handoff document. This revision also aligns the promotion-gate lane with the shared four-step reviewer publication order used in tools/ci and workflow docs. Active-branch inventory, exact workflow wiring, and merge-blocking enforcement still require direct verification where not proven by mounted files.]
[/KFM_META_BLOCK_V2] -->

# Promotion Gate (A–G)

Fail-closed, evidence-first promotion validation for KFM release candidates.

> **Status:** experimental  
> **Owners:** `@bartytime4life`  
> ![Status: Experimental](https://img.shields.io/badge/status-experimental-orange) ![Lane: tools/validators](https://img.shields.io/badge/lane-tools%2Fvalidators-1f6feb) ![Posture: Fail Closed](https://img.shields.io/badge/posture-fail--closed-critical) ![KFM: Evidence First](https://img.shields.io/badge/kfm-evidence--first-6f42c1) ![Implementation: Needs Verification](https://img.shields.io/badge/implementation-NEEDS%20VERIFICATION-lightgrey)  
> **Quick jumps:** [Scope](#scope) • [Repo fit](#repo-fit) • [Inputs](#inputs) • [Exclusions](#exclusions) • [Directory tree](#directory-tree) • [Decision contract](#decision-contract) • [Gate matrix](#gate-matrix-ag) • [Execution flow](#execution-flow) • [Quickstart](#quickstart) • [Outputs](#outputs) • [Trust chain](#trust-chain) • [Policy evaluation](#policy-evaluation) • [CI integration](#ci-integration) • [Tests](#tests) • [FAQ](#faq)

> [!IMPORTANT]
> This document defines both a **validator contract** and the current **executable thin-slice surface** for promotion validation. It does **not** by itself prove that all mounted paths, workflows, schemas, or merge-blocking integrations are present on the active branch. Exact executable paths, schema locations, and enforcement posture remain **NEEDS VERIFICATION** where not directly confirmed.

> [!TIP]
> **Current executable snapshot (thin slice)**  
> The current documented thin slice for this lane includes the following executable and contract-bearing surfaces:
>
> **Core gate execution**
> - `tools/validators/promotion_gate/prepare_candidate_fixture.py`
> - `tools/validators/promotion_gate/promotion_gate.py`
> - `tools/validators/promotion_gate/validate_decision_envelope.py`
>
> **Derived trust objects**
> - `tools/validators/promotion_gate/write_promotion_record.py`
> - `tools/validators/promotion_gate/validate_promotion_record.py`
> - `tools/validators/promotion_gate/emit_promotion_prov.py`
> - `tools/validators/promotion_gate/validate_promotion_prov.py`
> - `tools/validators/promotion_gate/write_promotion_bundle.py`
> - `tools/validators/promotion_gate/validate_promotion_bundle.py`
>
> **Bundle diff-policy helpers**
> - `tools/validators/promotion_gate/evaluate_bundle_diff_policy.py`
> - `tools/validators/promotion_gate/validate_bundle_diff_policy.py`
>
> **Reviewer / auditor outputs**
> - `tools/ci/render_promotion_summary.py`
> - `tools/ci/render_promotion_bundle_summary.py`
> - `tools/ci/render_diff_summary.py`
> - `tools/ci/render_bundle_diff_policy_summary.py`
> - `tools/ci/render_promotion_review_handoff.py`
>
> **Attestation helpers**
> - `tools/attest/sign_decision_envelope.py`
> - `tools/attest/verify_decision_envelope.py`
>
> **Comparison and closure helpers consumed by this lane**
> - `tools/diff/stable_diff.py`
> - `tools/catalog/catalog_crosslink.py`
>
> **Policy and schema surfaces**
> - `tools/validators/promotion_gate/policies/*.rego`
> - `schemas/promotion/decision-envelope.schema.json`
> - `schemas/promotion/promotion-record.schema.json`
> - `schemas/promotion/promotion-prov.schema.json`
> - `schemas/promotion/promotion-bundle.schema.json`
> - `schemas/promotion/promotion-bundle-diff-policy.schema.json`
> - `policy/promotion_bundle_diff_policy.json`
>
> **Thin-slice tests**
> - `tests/validators/test_promotion_gate_e2e.py`
> - `tests/validators/test_bundle_diff_policy.py`
> - `tests/validators/test_validate_bundle_diff_policy.py`
> - `tests/ci/test_render_promotion_review_handoff.py`
>
> **Preferred reviewer publication sequence**
>
> When the thin-slice reviewer artifacts are published together, keep the order stable:
>
> 1. `promotion-bundle-summary.md`
> 2. `promotion-bundle-diff-summary.md`
> 3. `promotion-bundle-diff-policy-summary.md`
> 4. `promotion-review-handoff.md`
>
> That sequence preserves the review story:
>
> - first the governed bundle
> - then prior/current drift
> - then policy interpretation of drift
> - then the composed steward-facing conclusion
>
> Keep this block synchronized with the mounted implementation as additional scripts, schemas, or trust objects land.

---

## Scope

This lane decides whether a release candidate is promotable under KFM governance. It validates the candidate, emits a machine-readable decision, and routes the result into governed review. It is **not** the act of publication.

This README serves two purposes at once:

1. a **normative lane contract** for promotion decisions; and  
2. an **implementation-facing directory README** for the executable thin slice scaffolded under this path.

| Posture | Meaning in this document |
|---|---|
| **CONFIRMED** | KFM requires typed contracts, evidence-bearing release objects, policy-visible decisions, catalog closure, and fail-closed behavior. |
| **PROPOSED** | Some exact field choices, helper names, and wider thin-slice growth below. |
| **UNKNOWN / NEEDS VERIFICATION** | Mounted validator code, workflow enforcement, exact branch inventory, and any deeper integration not directly confirmed. |

---

## Repo fit

**Path (INFERRED):** `tools/validators/promotion_gate/README.md`

**Lane:** `tools/validators/`  
**Role:** deterministic validation surface for governed promotion decisions

### Upstream inputs

- shared release contracts
- shared schemas
- policy bundles and reason / obligation vocabularies
- receipts from candidate-producing runs
- proofs and attestations
- catalog closure objects across STAC / DCAT / PROV
- candidate fixtures in `tests/fixtures/promotion/`
- geospatial candidate assets in `data/work/...`
- prior/current bundle diff results for governed review visibility
- checked-in diff-policy classification data

### Downstream consumers

- reviewer approval flows
- release and correction workflows
- CI summaries and annotations
- promotion records and rollback preparation
- release pipelines that require a machine-readable promotion decision
- reviewer-facing prior/current bundle change review
- diff-policy classification for release-significant drift
- composed steward-facing handoff documents derived from bundle, diff, and diff-policy artifacts

### Role in the system

- sits **after** candidate assembly
- sits **before** governed publication
- emits a **DecisionEnvelope**
- derives record / PROV / bundle trust objects
- supports prior/current bundle comparison and classification
- feeds reviewer-facing summaries and a composed review handoff
- must not become a hidden direct-publish shortcut

---

## Inputs

Accepted inputs are the minimum evidence-bearing objects required to judge one promotion candidate.

| Input | Required | Purpose |
|---|---:|---|
| `candidate_id` | Yes | Stable identifier for the promoted subject. |
| `spec_path` or equivalent canonical source | Yes | Source bytes used to compute the candidate `spec_hash`. |
| `declared_spec_hash` | Yes | Declared canonical hash for the candidate. |
| `release_manifest` or equivalent | Yes | Declares what outward release would contain. |
| `assets[]` with checksums | Yes | Binds reviewed asset inventory to exact bytes. |
| `catalog_refs` / `catalog_closure` | Yes | Links the candidate to STAC / DCAT / PROV closure. |
| `run_receipt` | Yes | Carries machine-checkable execution facts. |
| `attestation_refs` | Yes | Carries integrity and origin evidence. |
| `policy_label` / policy context | Yes | Supplies classification and governance context. |
| `review` | Yes | Carries approval state and steward identity. |
| `rollback` / prior release reference | Yes for promotable release | Preserves reversal and supersession visibility. |
| `ai_receipt` | Conditional | Required when model mediation affected the candidate. |
| `diff_artifact` | Conditional | Required when change visibility matters materially. |
| `correction_notice_ref` | Conditional | Required when the candidate supersedes or narrows a prior release. |
| `prior_bundle` | Conditional | Needed when governed prior/current bundle review is enabled. |
| `bundle_diff_policy` | Conditional | Needed when bundle diff policy classification is part of the review path. |

### Current thin-slice file inputs

| Input | Expected path family |
|---|---|
| candidate fixture | `tests/fixtures/promotion/*.json` |
| spec file | `data/work/.../stac-item.json` |
| asset files | `data/work/.../assets/*` |
| policy bundle | `tools/validators/promotion_gate/policies/*.rego` |
| decision schema | `schemas/promotion/decision-envelope.schema.json` |
| record schema | `schemas/promotion/promotion-record.schema.json` |
| PROV schema | `schemas/promotion/promotion-prov.schema.json` |
| bundle schema | `schemas/promotion/promotion-bundle.schema.json` |
| bundle diff-policy schema | `schemas/promotion/promotion-bundle-diff-policy.schema.json` |
| bundle diff-policy file | `policy/promotion_bundle_diff_policy.json` |
| prior/current diff report | `promotion-bundle-diff.json` or equivalent |
| diff-policy report | `promotion-bundle-diff-policy.json` or equivalent |
| composed review handoff inputs | `promotion-bundle.json` + `promotion-bundle-diff.json` + `promotion-bundle-diff-policy.json` |

---

## Exclusions

This lane does **not**:

- publish artifacts directly
- merge branches directly
- replace domain-specific validation in hydrology, hazards, soils, or other subject lanes
- stand in for runtime answer accountability such as `RuntimeResponseEnvelope`
- redefine schemas or policy owned elsewhere
- convert a prose README into proof that implementation already exists
- embed governance authority in helpers where policy should remain the source of truth
- compute general diff law inside policy renderers
- turn CI presentation helpers into policy authority
- replace underlying machine artifacts with one composed Markdown reviewer handoff

---

## Directory tree

```text
# Thin executable slice documented here — broader inventory still NEEDS VERIFICATION against active branch

tools/validators/promotion_gate/
├── README.md
├── promotion_gate.py
├── prepare_candidate_fixture.py
├── validate_decision_envelope.py
├── validate_promotion_record.py
├── validate_promotion_prov.py
├── validate_promotion_bundle.py
├── write_promotion_record.py
├── write_promotion_bundle.py
├── emit_promotion_prov.py
├── evaluate_bundle_diff_policy.py
├── validate_bundle_diff_policy.py
├── policies/
│   ├── a_identity.rego
│   ├── b_integrity.rego
│   ├── c_geometry.rego
│   ├── d_temporal.rego
│   ├── e_policy.rego
│   ├── f_proof.rego
│   ├── g_review.rego
│   └── promotion.rego
```

Related surfaces:

```text
tools/attest/sign_decision_envelope.py
tools/attest/verify_decision_envelope.py
tools/diff/stable_diff.py
tools/catalog/catalog_crosslink.py
tools/ci/render_promotion_summary.py
tools/ci/render_promotion_bundle_summary.py
tools/ci/render_diff_summary.py
tools/ci/render_bundle_diff_policy_summary.py
tools/ci/render_promotion_review_handoff.py
policy/promotion_bundle_diff_policy.json
schemas/promotion/
tests/fixtures/promotion/
tests/validators/test_promotion_gate_e2e.py
tests/validators/test_bundle_diff_policy.py
tests/validators/test_validate_bundle_diff_policy.py
tests/ci/test_render_promotion_review_handoff.py
```

> [!NOTE]
> Shared contracts, schemas, and policy surfaces should remain authoritative in their own repo homes. This lane validates and consumes them; it does not replace them.

---

## Decision contract

Every promotion attempt must end in one finite result:

| Result | Meaning |
|---|---|
| `PROMOTE` | Candidate satisfied all required gates and may proceed to governed release flow. |
| `ABSTAIN` | Evidence is insufficient to promote safely, but no direct contradiction has been proven. |
| `DENY` | Candidate failed one or more required gates. |
| `ERROR` | The gate could not safely evaluate due to parse, execution, or other fail-closed faults. |

> [!WARNING]
> A `PROMOTE` result does **not** publish directly. It means the candidate is valid for the governed review / release path.

### Gate status vocabulary

Each gate emits its own status:

| Status | Meaning |
|---|---|
| `PASS` | Required checks for that gate succeeded. |
| `FAIL` | The gate found a concrete promotability violation. |
| `SKIP` | The gate was not applicable or not yet implemented. |
| `ERROR` | The gate could not safely evaluate due to parse or execution failure. |

### Bundle diff-policy vocabulary

The current thin-slice bundle-diff policy layer classifies prior/current bundle key drift into:

| Classification | Meaning |
|---|---|
| `informational` | expected or non-blocking by current policy |
| `review` | trust-visible or otherwise review-significant |
| `blocking` | release-significant drift that must not pass silently |

These are **review classifications**, not a replacement for the main promotion decision grammar.

---

## Outputs

This lane emits a **DecisionEnvelope**, not a `RuntimeResponseEnvelope`.

### Minimum output shape

```yaml
decision: PROMOTE | ABSTAIN | DENY | ERROR
candidate_id: string
spec_hash: string
prior_spec_hash: string?
release_ref: string?
steward_id: string?
reason_codes: []
obligations: []
gates:
  - gate: A
    status: PASS | FAIL | SKIP | ERROR
    details: []
generated_at: RFC3339 timestamp
```

### Output intent

| Field | Purpose |
|---|---|
| `decision` | Finite machine-readable promotion result. |
| `candidate_id` | Stable subject the decision applies to. |
| `spec_hash` | Canonical identity anchor for the candidate spec. |
| `prior_spec_hash` | Rollback / supersession anchor for the prior release. |
| `reason_codes` | Explicit failure, abstention, or error reasons. |
| `obligations` | Required follow-up actions before promotion can continue. |
| `gates[]` | Per-gate results for reviewer and CI visibility. |
| `generated_at` | Time the decision was produced. |

### Secondary and derived outputs

The current thin slice may also emit:

| Object | Purpose |
|---|---|
| `promotion-summary.md` | reviewer-readable summary of the DecisionEnvelope |
| `promotion-record.json` | compact promotion ledger entry derived from the decision |
| `promotion-prov.json` | minimal PROV document derived from the promotion record |
| `promotion-bundle.json` | index of the full governed promotion artifact set |
| `promotion-bundle-summary.md` | reviewer / auditor summary of the full bundle |
| `decision-sign-result.json` | signing command result |
| `decision-verify-result.json` | attestation verification result |
| `promotion-bundle-diff.json` | prior/current bundle diff report |
| `promotion-bundle-diff-summary.md` | reviewer-facing diff summary |
| `promotion-bundle-diff-policy.json` | machine-readable policy classification of bundle drift |
| `promotion-bundle-diff-policy-summary.md` | reviewer-facing policy summary for bundle drift |
| `promotion-review-handoff.md` | composed steward-facing review document derived from bundle, diff, diff-policy, and attestation visibility |

### Preferred reviewer publication order

When these reviewer-facing artifacts are published together, keep the order stable:

1. `promotion-bundle-summary.md`
2. `promotion-bundle-diff-summary.md`
3. `promotion-bundle-diff-policy-summary.md`
4. `promotion-review-handoff.md`

Why this order matters:

- the reviewer first sees the governed bundle as released evidence
- then the prior/current drift surface
- then the policy interpretation of that drift
- then the final steward-facing composed conclusion

That ordering improves reviewer ergonomics while preserving the authority split between machine artifacts and the final Markdown convenience surface.

---

## Gate matrix (A–G)

| Gate | Name | What it checks | Minimum evidence |
|---|---|---|---|
| **A** | Identity & closure | Stable identifier, canonical `spec_hash`, required STAC identity fields, immutable target intent. | `candidate_id`, spec bytes, declared hash, release subject identity. |
| **B** | Asset integrity | Every declared asset exists, is checksummed, and matches reviewed bytes. | `assets[]`, checksums, manifest / STAC asset linkage. |
| **C** | Geometry & CRS invariants | Geometry validity, CRS allowlist, bbox consistency, deterministic generalization, sane geometric summaries. | Geometry-bearing assets, CRS metadata, bbox, generalization parameters when applicable. |
| **D** | Temporal & coverage semantics | Valid intervals, coherent spatial / temporal coverage, freshness declarations where required. | Time fields, coverage metadata, source-aligned scope declarations. |
| **E** | Rights, sensitivity, and policy | License, rights, policy label, sensitivity handling, deny-by-default for unknown or missing classification. | Rights metadata, policy label, reviewable classification context. |
| **F** | Provenance, proofs, and receipts | Receipts present, attestations validate, proof hashes match, catalog / provenance closure is coherent. | `run_receipt`, `attestation_refs`, `catalog_refs`, proof objects. |
| **G** | Reviewer intent & rollback readiness | Approval present, steward recorded, rollback target exists, supersession is visible and reversible. | `review`, prior release reference, correction / rollback posture, immutable version / tag intent. |

### Gate-to-outcome collapse

| Condition | Final decision |
|---|---|
| all required gates `PASS` | `PROMOTE` |
| one or more required gates `FAIL` | `DENY` |
| insufficient evidence but no contradiction | `ABSTAIN` |
| evaluator or gate error | `ERROR` |

---

## Execution flow

```mermaid
flowchart LR
    A[Candidate fixture] --> B[prepare_candidate_fixture.py]
    B --> C[promotion_gate.py]
    C --> D[Canonical spec hash]
    D --> E[Per-gate evaluation A–G]
    E --> F[DecisionEnvelope JSON]
    F --> G[validate_decision_envelope.py]
    F --> H[render_promotion_summary.py]
    F --> I[sign_decision_envelope.py]
    I --> J[verify_decision_envelope.py]
    F --> K[write_promotion_record.py]
    K --> L[emit_promotion_prov.py]
    K --> M[write_promotion_bundle.py]
    M --> N[render_promotion_bundle_summary.py]
    M --> O[stable_diff.py]
    O --> P[render_diff_summary.py]
    O --> Q[evaluate_bundle_diff_policy.py]
    Q --> R[validate_bundle_diff_policy.py]
    Q --> S[render_bundle_diff_policy_summary.py]
    M --> T[render_promotion_review_handoff.py]
    O --> T
    Q --> T
```

### Execution steps

1. Load the candidate and canonical spec bytes.
2. Compute `spec_hash`.
3. Normalize fixture hashes where needed.
4. Validate gate inputs and shared contracts.
5. Evaluate Gates A–G in deterministic order.
6. Emit per-gate statuses.
7. Collapse the result to one finite `decision`.
8. Validate the decision against schema.
9. Render reviewer-readable output where needed.
10. Optionally sign and verify the decision.
11. Derive record, PROV, and bundle objects.
12. Optionally compare prior/current bundles.
13. Classify bundle drift using checked-in diff policy.
14. Render reviewer-facing diff and policy summaries.
15. Optionally compose one steward-facing review handoff document from bundle, diff, and diff-policy artifacts.
16. Route the result into governed review or rework.

---

## Trust chain

The current thin slice now supports a fuller governed promotion evidence chain.

```mermaid
flowchart LR
    A[Candidate] --> B[DecisionEnvelope]
    B --> C[Signed Decision]
    C --> D[Verified Attestation]
    B --> E[Promotion Summary]
    B --> F[Promotion Record]
    F --> G[Promotion PROV]
    B --> H[Promotion Bundle]
    H --> I[Bundle Summary]
    H --> J[Bundle Diff]
    J --> K[Diff Policy]
    K --> L[Policy Summary]
    H --> M[Promotion Review Handoff]
    J --> M
    K --> M
    D --> M
```

### Trust object split

| Surface | Role |
|---|---|
| `decision.json` | finite machine-readable decision |
| `decision-sign-result.json` | receipt-like signing outcome |
| `decision-verify-result.json` | receipt-like verification outcome |
| `promotion-record.json` | compact governed ledger entry |
| `promotion-prov.json` | provenance activity for promotion |
| `promotion-bundle.json` | bundle manifest indexing the full promotion artifact set |
| `promotion-bundle-diff.json` | deterministic prior/current comparison report |
| `promotion-bundle-diff-policy.json` | reviewed interpretation layer for changed keys |
| `promotion-review-handoff.md` | composed reviewer-facing document derived from, but not replacing, the underlying machine artifacts |

### Review publication sequence

When steward-facing Markdown artifacts are published together, the preferred order is:

1. bundle summary
2. diff summary
3. diff-policy summary
4. review handoff

That keeps the reviewer’s view aligned with the trust chain itself: bundle first, then drift, then classification, then composed conclusion.

> [!NOTE]
> This preserves KFM’s **receipts vs proofs** doctrine: receipts capture process memory; proofs and release-significant trust objects remain separately identifiable. The diff-policy layer interprets change visibility; it does not replace the release decision itself. The review handoff document is a derived steward convenience surface, not a new authoritative machine object.

---

## Catalog closure

Minimal closure expectations are not decorative metadata checks. They are release-scope identity checks.

| Surface | Minimum expectation |
|---|---|
| **STAC** | Release-bearing item or collection for the outward spatial or spatiotemporal assets. |
| **DCAT** | Dataset / distribution discovery for the same promoted subject. |
| **PROV** | Lineage linking entity, activity, and agent for the same outward release. |
| **Cross-surface rule** | STAC, DCAT, and PROV must agree on subject identity, scope, and correction posture. |

---

## Quickstart

### 1. Prepare fixture hashes

```bash
python tools/validators/promotion_gate/prepare_candidate_fixture.py \
  tests/fixtures/promotion/candidate.runtime.json
```

### 2. Run the promotion gate

```bash
python tools/validators/promotion_gate/promotion_gate.py \
  tests/fixtures/promotion/candidate.runtime.json \
  > decision.json
```

### 3. Validate the decision envelope

```bash
python tools/validators/promotion_gate/validate_decision_envelope.py \
  schemas/promotion/decision-envelope.schema.json \
  decision.json
```

### 4. Render reviewer summary

```bash
python tools/ci/render_promotion_summary.py \
  decision.json \
  --output promotion-summary.md
```

### 5. Write the promotion record

```bash
python tools/validators/promotion_gate/write_promotion_record.py \
  decision.json \
  --output promotion-record.json \
  --summary-ref "artifact://promotion-summary.md"
```

### 6. Emit promotion PROV

```bash
python tools/validators/promotion_gate/emit_promotion_prov.py \
  promotion-record.json \
  --output promotion-prov.json
```

### 7. Write the promotion bundle

```bash
python tools/validators/promotion_gate/write_promotion_bundle.py \
  --decision decision.json \
  --summary promotion-summary.md \
  --record promotion-record.json \
  --prov promotion-prov.json \
  --output promotion-bundle.json
```

### 8. Render bundle summary

```bash
python tools/ci/render_promotion_bundle_summary.py \
  promotion-bundle.json \
  --output promotion-bundle-summary.md
```

### 9. Diff prior/current promotion bundles

```bash
python tools/diff/stable_diff.py \
  --left promotion-bundle.previous.json \
  --right promotion-bundle.json \
 
