<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-standards-run-receipt
title: RunReceipt — Current KFM Runtime Receipt Standard
type: standard
version: v2.0.0
status: draft; repository-grounded; schema-paired; validator-implemented; release-authority-none
owners:
  - "@bartytime4life"
created: 2026-05-14
updated: 2026-08-19
policy_label: public
base_commit: cc52dba82d3b1c62e0a0d97fc49a6d205cf1c5ba
prior_blob: 144f6a153ba9223a617e2718bca3e161bf24e605
directory_governance: ADR-0029 adopts docs/doctrine/directory-rules.md as the writable human placement authority; this page remains explanatory standards documentation under docs/.
truth_posture: CONFIRMED current runtime contract, schema, validator, fixture root, and bounded PMTiles attestation producer; PROPOSED broader signing, cross-family receipt composition, and release use unless separately evidenced
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/truth-posture.md
  - docs/architecture/contract-schema-policy-split.md
  - contracts/runtime/run_receipt.md
  - schemas/contracts/v1/runtime/run_receipt.schema.json
  - fixtures/contracts/v1/runtime/run_receipt/README.md
  - tools/validators/validate_run_receipt.py
  - tools/attest/build_runreceipt.py
  - tools/validators/pmtiles/schemas/runreceipt.schema.json
  - data/receipts/README.md
tags: [kfm, standard, runtime, run-receipt, provenance, audit, spec-hash, smart-sync, validation, receipts]
notes:
  - "The current canonical runtime RunReceipt machine shape is schemas/contracts/v1/runtime/run_receipt.schema.json, not the former proposed schemas/contracts/v1/receipts/run_receipt.v1.schema.json path."
  - "The runtime schema uses sha256:<hex> for spec_hash and SUCCESS | PARTIAL | FAIL for run outcome."
  - "DSSE/cosign is not part of the current runtime RunReceipt schema and is not required by this standard unless another accepted profile or release surface requires it."
  - "A separate PMTiles attestation producer uses a SLSA-shaped run receipt and must not be silently treated as the runtime RunReceipt contract."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# RunReceipt — Current KFM Runtime Receipt Standard

> **Operating rule.** A `RunReceipt` records accountable execution provenance for one governed runtime or pipeline stage. It does not prove truth, approve policy, authorize release, publish data, or grant public-client access.

| Field | Current bounded result |
|---|---|
| Evidence snapshot | `main@cc52dba82d3b1c62e0a0d97fc49a6d205cf1c5ba` |
| Semantic contract | [`contracts/runtime/run_receipt.md`](../../contracts/runtime/run_receipt.md) — draft / `PROPOSED` |
| Machine schema | [`schemas/contracts/v1/runtime/run_receipt.schema.json`](../../schemas/contracts/v1/runtime/run_receipt.schema.json) — present, closed, `PROPOSED` |
| Validator | [`tools/validators/validate_run_receipt.py`](../../tools/validators/validate_run_receipt.py) — implemented, deterministic, no-network |
| Fixture root | [`fixtures/contracts/v1/runtime/run_receipt/`](../../fixtures/contracts/v1/runtime/run_receipt/) — present |
| Run outcome vocabulary | `SUCCESS | PARTIAL | FAIL` |
| `spec_hash` shape | `sha256:<64 lowercase hex>` |
| Optional current profile | `smart_sync` HTTP-conditional receipt profile |
| Signing / DSSE | **NOT part of the current runtime schema**; separate profiles may define attestation requirements |
| Release/publication authority | None |

> [!IMPORTANT]
> The previous version of this page described a synthetic universal receipt containing policy decisions, evidence references, licenses, target zones, DSSE envelopes, and cosign signatures. Current repository evidence does **not** establish that object as the runtime `RunReceipt`. The current runtime contract and schema are narrower and authoritative for the shape described here.

**Quick links:** [Purpose](#1-purpose--scope) · [Authority](#2-normative-status--authority) · [Meaning](#3-doctrine--what-a-runreceipt-is) · [Flow](#4-end-to-end-flow) · [Fields](#5-required-fields-canonical-shape) · [`spec_hash`](#6-spec_hash--deterministic-identity) · [Attestation](#7-dsse-envelope-and-signing) · [Verification](#8-verification-fail-closed) · [Placement](#9-storage-placement-and-lifecycle) · [Outcomes](#10-policy-gates-and-finite-outcomes) · [Open items](#11-open-questions--needs-verification) · [Related](#12-related-docs)

---

## 1. Purpose & scope

This page documents the repository's current `RunReceipt` standard without replacing the owning contract or schema.

The current object records:

- a stable `run_id`;
- the executed `stage`;
- input and output references;
- the `code_ref` used by the run;
- a SHA-256 `spec_hash` binding;
- relevant `source_descriptor_refs`;
- relevant `validation_refs`; and
- the finite execution result `SUCCESS`, `PARTIAL`, or `FAIL`.

The current schema also supports an optional `smart_sync` profile for one bounded HTTP conditional-polling decision.

This page does **not** define evidence truth, policy admissibility, rights clearance, sensitivity decisions, review approval, release contents, correction state, rollback authorization, or public runtime envelopes. Those remain in their owning contracts, schemas, policy, evidence, validation, review, release, and runtime surfaces.

[Back to top](#top)

---

## 2. Normative status & authority

| Concern | Owning repository surface | Current state |
|---|---|---|
| RunReceipt semantic meaning | [`contracts/runtime/run_receipt.md`](../../contracts/runtime/run_receipt.md) | Present; draft / `PROPOSED` |
| RunReceipt machine shape | [`schemas/contracts/v1/runtime/run_receipt.schema.json`](../../schemas/contracts/v1/runtime/run_receipt.schema.json) | Present; Draft 2020-12; `PROPOSED`; `additionalProperties: false` |
| RunReceipt validation | [`tools/validators/validate_run_receipt.py`](../../tools/validators/validate_run_receipt.py) | Implemented; deterministic; no-network |
| RunReceipt fixtures | [`fixtures/contracts/v1/runtime/run_receipt/`](../../fixtures/contracts/v1/runtime/run_receipt/) | Present valid/invalid fixture lanes |
| Policy admissibility | `policy/runtime/` and applicable policy families | Separate authority |
| Evidence truth | Evidence contracts/bundles and proof surfaces | Separate authority |
| Release decision | `release/` families and governed release records | Separate authority |
| Receipt persistence | `data/receipts/` families | Repository lane exists; exact runtime persistence binding remains to be proved |
| Public response | Runtime/Governed API response contracts | Separate authority |

Accepted Directory Rules govern placement; this standards page explains the current contract/schema/validator relationship and does not create a second receipt authority.

[Back to top](#top)

---

## 3. Doctrine — what a RunReceipt is

### 3.1 What a validated RunReceipt establishes

A schema-valid, validator-valid runtime `RunReceipt` establishes that a record conforms to the current runtime receipt shape and the validator's bounded semantic checks. It can bind an execution to its input/output refs, code ref, spec hash, source descriptor refs, validation refs, and completion outcome.

For `smart_sync`, the validator additionally checks bounded HTTP metadata and decision consistency without performing network I/O.

### 3.2 What a RunReceipt does not establish

A `RunReceipt` does not by itself establish:

- factual correctness;
- evidence sufficiency;
- successful validation of every referenced artifact;
- policy permission;
- rights or sensitivity clearance;
- review approval;
- release approval or publication;
- runtime serving permission; or
- that a signature or attestation exists.

Those claims require evidence from their owning surfaces.

### 3.3 No object-family collapse

Keep these distinct:

| Object | Owns |
|---|---|
| `RunReceipt` | Execution provenance and finite run outcome |
| `ValidationReport` / validation records | Validation findings and validation outcome |
| `SourceDescriptor` | Source identity, role, rights/access and source posture |
| `EvidenceBundle` | Claim-supporting evidence closure |
| `PolicyDecision` | Admissibility decision and obligations |
| `ReleaseManifest` / promotion records | Release contents and governed release state |
| `AIReceipt` | AI-mediated accountability where its contract applies |
| Runtime response envelope | Client-facing finite runtime outcome |

[Back to top](#top)

---

## 4. End-to-end flow

```mermaid
flowchart LR
  A["Governed inputs"] --> B["Runtime / pipeline stage"]
  B --> C["Outputs + validation records"]
  C --> D["RunReceipt"]
  D --> E["Schema + semantic validation"]
  E --> F["Policy / review / release checks"]
  F --> G["Governed downstream use if separately allowed"]
```

The receipt records the execution edge. Downstream policy, evidence, review, promotion, release, correction, rollback, and public serving remain separate gates.

### Smart Sync bounded flow

```text
prior receipt/content binding
  + declared conditional-request validators
  + declared HTTP 200/304 observation
  -> smart_sync profile
  -> schema validation
  -> no-network semantic validation
  -> materialize | no_op
```

The Smart Sync profile records a reviewable decision; it does not fetch, admit, promote, release, or publish source material.

[Back to top](#top)

---

## 5. Required fields (canonical shape)

### 5.1 Current required top-level fields

The current runtime schema requires exactly these top-level families:

| Field | Shape | Meaning |
|---|---|---|
| `run_id` | string matching `^[a-z][a-z0-9_:.-]*$` | Stable run identifier |
| `stage` | string | Executed runtime/pipeline stage |
| `inputs` | array of strings | Input references |
| `outputs` | array of strings | Output references |
| `code_ref` | string | Code/workflow/package/commit reference |
| `spec_hash` | `sha256:<64 lowercase hex>` | Run-spec/config identity binding |
| `source_descriptor_refs` | array of strings | Relevant SourceDescriptor refs |
| `validation_refs` | array of strings | Relevant validation refs |
| `outcome` | `SUCCESS | PARTIAL | FAIL` | Execution result |

`additionalProperties` is `false` at the root.

### 5.2 Optional `smart_sync`

When `stage == "smart_sync"`, the schema requires a `smart_sync` object containing:

- `transport: "http_conditional"`;
- timezone-aware `fetch_time`;
- HTTPS `source_url`;
- `http_status` of `200` or `304`;
- request HTTP validators and, where required, response validators;
- `decision: materialize | no_op`;
- `reason: content_changed | not_modified | validator_drift`;
- `prior_run_receipt_ref`;
- `prior_content_digest`;
- `validator_drift`; and
- conditional `content_digest` where a 200 decision requires it.

The schema constrains 304 to `no_op/not_modified`, 200+`materialize` to changed content with outputs, and 200+`no_op` to validator drift without outputs. For Smart Sync the top-level `outcome` is constrained to `SUCCESS`.

### 5.3 Former synthetic v1 shape

The former page's fields such as `object_type`, `schema_version`, `receipt_id`, `actor`, `decision_log`, `license`, `evidence_refs`, `attestations`, and `target_zone` are **not fields in the current runtime schema**. They may belong to other receipt, policy, evidence, attestation, or release designs, but must not be presented as required runtime RunReceipt fields without an owning contract/schema change.

[Back to top](#top)

---

## 6. `spec_hash` — deterministic identity

The runtime schema requires:

```text
sha256:<64 lowercase hexadecimal characters>
```

The dedicated validator rejects an all-zero SHA-256 placeholder. The current schema and validator do **not**, by themselves, establish that runtime `spec_hash` must be encoded as `jcs:sha256:<hex>`; the previous standard's JCS-prefixed requirement therefore no longer appears as a current RunReceipt rule.

Canonicalization policy for producing the SHA-256 value must be established by the owning spec/config producer and any applicable canonicalization standard. A verifier must not silently reinterpret an existing hash namespace.

[Back to top](#top)

---

## 7. DSSE envelope and signing

The current runtime `RunReceipt` contract, schema, and validator do not require a DSSE envelope, cosign signature, Fulcio certificate, Rekor entry, `attestations[]`, or the media type `application/vnd.kfm.run_receipt+json`.

That does **not** prohibit signed receipt profiles. It means signing is a separate attestation/release concern unless an applicable accepted contract, schema, workflow, or release profile makes it mandatory.

A separate repository surface demonstrates this distinction: [`tools/attest/build_runreceipt.py`](../../tools/attest/build_runreceipt.py) builds a minimal **PMTiles** SLSA-shaped run receipt with `schema_version: kfm.runreceipt.pmtiles.v1`, a SLSA provenance `type`, `subject`, and `predicate`. Its paired PMTiles validator schema lives under `tools/validators/pmtiles/schemas/runreceipt.schema.json`. That is a separate attestation profile, not the runtime schema defined in §5.

[Back to top](#top)

---

## 8. Verification (fail-closed)

The implemented validator is deterministic and no-network. It:

1. reads only bounded regular files and rejects unsafe file forms;
2. rejects malformed, duplicate-key, non-finite, or overly complex JSON;
3. validates against the current Draft 2020-12 runtime schema;
4. rejects all-zero `spec_hash` placeholders;
5. validates Smart Sync timestamps, HTTPS source URLs, ETag/date syntax, conditional-validator consistency, digest relationships, and decision semantics; and
6. emits finite findings without fetching a source or granting downstream authority.

A validator pass means **receipt validation passed within this profile**. It does not imply policy approval, evidence closure, release readiness, publication, or successful runtime deployment.

Repository command:

```bash
python tools/validators/validate_run_receipt.py <receipt.json>
```

[Back to top](#top)

---

## 9. Storage, placement, and lifecycle

`data/receipts/` is the repository responsibility lane for receipt records. The runtime contract and schema do not themselves prove that every runtime `RunReceipt` instance is persisted there, nor do they define a universal per-stage subdirectory taxonomy.

The safe responsibility boundary is:

```text
execution code / workflow
  -> RunReceipt record
  -> validation
  -> receipt persistence in an approved receipt lane
  -> downstream policy/review/release use by reference
```

A receipt is process/audit memory. It is not a proof, catalog record, release manifest, correction notice, rollback card, or published artifact merely because it is stored under `data/receipts/`.

The lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

`RunReceipt` can support traceability across these stages, but the receipt does not perform a lifecycle transition.

[Back to top](#top)

---

## 10. Policy gates and finite outcomes

### 10.1 Run outcome is not policy outcome

The current RunReceipt execution vocabulary is:

| Run outcome | Meaning |
|---|---|
| `SUCCESS` | Immediate execution completed under its stage criteria |
| `PARTIAL` | Execution completed with incomplete/degraded/skipped/restricted components |
| `FAIL` | Execution did not safely complete its intended work |

These values are **not** the public runtime vocabulary `ANSWER | ABSTAIN | DENY | ERROR`, and they are not `PolicyDecision` outcomes. Do not coerce one family into another.

### 10.2 Downstream handling

A `SUCCESS` receipt may be eligible for later validation, policy, review, promotion, or release checks. It is not automatically publishable. `PARTIAL` and `FAIL` must remain visible and cannot be rewritten as success to pass downstream gates.

The previous embedded illustrative OPA promotion policy has been removed from normative guidance because policy authority belongs under `policy/` and current RunReceipt fields do not contain the former synthetic `validation_report`, `rights_status`, `sensitivity`, or `decision_log` structure.

[Back to top](#top)

---

## 11. Open questions & `NEEDS VERIFICATION`

- **OPEN:** whether the runtime `stage` field should adopt a controlled central vocabulary.
- **OPEN:** whether `inputs` and `outputs` should remain string refs or graduate to structured reference objects.
- **OPEN:** the precise canonicalization/profile used by every producer to calculate `spec_hash`.
- **OPEN:** the required format and immutability strength of `code_ref`.
- **OPEN:** the repository-wide persistence rule for runtime RunReceipt instances and their linkage into release/correction/rollback traces.
- **OPEN:** whether the runtime contract should directly reference proof or receipt families beyond `validation_refs`.
- **OPEN:** whether signing/attestation becomes mandatory for any runtime RunReceipt boundary; current runtime schema does not require it.
- **NEEDS VERIFICATION:** complete current fixture coverage beyond the fixture-family landing page and specialized Smart Sync cases.
- **NEEDS VERIFICATION:** exact CI workflows that make RunReceipt validation merge-significant at current main.

[Back to top](#top)

---

## 12. Related docs

- [`contracts/runtime/run_receipt.md`](../../contracts/runtime/run_receipt.md) — semantic authority for the runtime object.
- [`schemas/contracts/v1/runtime/run_receipt.schema.json`](../../schemas/contracts/v1/runtime/run_receipt.schema.json) — current machine shape.
- [`tools/validators/validate_run_receipt.py`](../../tools/validators/validate_run_receipt.py) — current no-network validator.
- [`fixtures/contracts/v1/runtime/run_receipt/README.md`](../../fixtures/contracts/v1/runtime/run_receipt/README.md) — fixture-family boundary.
- [`data/receipts/README.md`](../../data/receipts/README.md) — receipt-lane orientation.
- [`docs/architecture/contract-schema-policy-split.md`](../architecture/contract-schema-policy-split.md) — authority separation.
- [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) — accepted placement authority through ADR-0029.
- [`docs/doctrine/lifecycle-law.md`](../doctrine/lifecycle-law.md) — lifecycle semantics.
- [`docs/doctrine/truth-posture.md`](../doctrine/truth-posture.md) — truth/evidence posture.
- [`tools/attest/build_runreceipt.py`](../../tools/attest/build_runreceipt.py) — separate PMTiles attestation producer.

[Back to top](#top)

---

## Appendix A — Field-name drift across the corpus

The material issue is no longer alias spelling inside one runtime schema; it is **object-family drift** between the older synthetic standard, the current runtime contract/schema, and specialized attestation receipts.

| Surface | Current identifying shape | Disposition |
|---|---|---|
| Runtime RunReceipt | `run_id`, `stage`, refs, `code_ref`, `sha256:` `spec_hash`, `outcome` | Current runtime contract/schema |
| Runtime Smart Sync | Runtime RunReceipt + `smart_sync` object | Current optional runtime profile |
| Former synthetic standard | `object_type`, `receipt_id`, `actor`, policy/evidence/license/target fields | Historical proposal; not current runtime shape |
| PMTiles run receipt | SLSA-shaped `schema_version`, `type`, `subject`, `predicate` | Separate bounded attestation profile |

Do not implement compatibility aliases between these families without an explicit contract/schema migration. Similar names do not establish identical semantics.

[Back to top](#top)

---

## Appendix B — Worked example

A minimal runtime receipt matching the current required field surface is:

```json
{
  "run_id": "run:ingest:example",
  "stage": "ingest",
  "inputs": ["source:example"],
  "outputs": ["artifact:example"],
  "code_ref": "git:example",
  "spec_hash": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "source_descriptor_refs": ["source-descriptor:example"],
  "validation_refs": ["validation:example"],
  "outcome": "SUCCESS"
}
```

This example illustrates schema shape only. Real records must use genuine identity bindings and governed references; all-zero SHA-256 placeholders are rejected by the dedicated validator.

[Back to top](#top)

---

## Appendix C — Negative fixture catalog

The current fixture root has valid and invalid lanes, and the dedicated validator supports substantially stronger negative behavior than the former hypothetical DSSE catalog.

Minimum negative categories to preserve or expand include:

| Category | Expected posture |
|---|---|
| missing required top-level field | schema reject |
| invalid `run_id` pattern | schema reject |
| invalid `spec_hash` syntax | schema reject |
| all-zero `spec_hash` | semantic reject |
| unknown `outcome` | schema reject |
| extra top-level field | schema reject |
| malformed/duplicate-key/non-finite JSON | parser reject |
| unsafe Smart Sync URL | semantic reject |
| malformed ETag or HTTP date | semantic reject |
| inconsistent 304/materialize decision | schema/semantic reject |
| inconsistent 200 digest/output decision | schema/semantic reject |
| unsafe or non-regular receipt file | validator reject |

Fixtures must remain deterministic, no-network, public-safe, and non-authoritative.

[Back to top](#top)

---

**Last reviewed:** 2026-08-19  
**Evidence base:** `main@cc52dba82d3b1c62e0a0d97fc49a6d205cf1c5ba`  
**Rollback:** restore prior blob `144f6a153ba9223a617e2718bca3e161bf24e605`; no runtime, schema, policy, receipt instance, release, deployment, or publication state is changed by this documentation update.
