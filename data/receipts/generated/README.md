<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/generated/readme
name: Generated Work Receipts README
path: data/receipts/generated/README.md
type: data-generated-receipts-lane-readme
version: v0.1.0
status: draft; repository-grounded
owners:
  - <receipt-steward>
  - <docs-steward>
  - <validation-steward>
created: 2026-07-17
updated: 2026-07-17
policy_label: internal-governance
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: generated-receipts
receipt_scope: AI-authored artifact provenance and process memory
path_posture: existing-populated-lane; fifty-nine-json-receipts-observed-at-base-snapshot; exact-emission-automation-needs-verification
sensitivity_posture: receipt-internal; no-public-path; no-secrets; no-hidden-reasoning; process-memory-not-proof; receipt-not-release
related:
  - ../README.md
  - ../../proofs/README.md
  - ../../../schemas/contracts/v1/receipts/generated_receipt.schema.json
  - ../../../docs/doctrine/ai-build-operating-contract.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../.github/PULL_REQUEST_TEMPLATE.md
tags:
  - kfm
  - data
  - receipts
  - generated-receipt
  - ai-provenance
  - audit
  - cite-or-abstain
  - no-public-path
notes:
  - "This README documents an existing populated lane; it does not certify every pre-existing receipt or prove an emitter is automated."
  - "A generated receipt records provenance for AI-authored work. It is not human approval, factual proof, policy permission, catalog closure, release authority, or publication authority."
[/KFM_META_BLOCK_V2] -->

# Generated work receipts

`data/receipts/generated/` stores repository-committed provenance records for AI-authored artifacts. It is a process-memory lane inside `data/receipts/`, not a truth, proof, policy, catalog, release, or public-delivery surface.

## Purpose

Generated receipts make an AI-authored change inspectable by recording the artifacts produced, their content hashes, the model identity, the prompt or contract hash, repository evidence, truth labels, validation gates, citations, and human-review state.

The lane supports review and rollback. It does not make the authored artifacts correct or mergeable by itself.

## Authority level

**Provenance-bearing process memory; non-authoritative for domain truth and release.**

A receipt may show what was authored and which checks were reported. It cannot:

- approve its own artifacts;
- substitute for repository evidence, tests, or reviewer judgment;
- create a policy decision, proof pack, catalog record, release manifest, or publication decision;
- authorize access to sensitive or unreleased material;
- convert generated language into sovereign truth.

Human review remains separate. A receipt whose `human_review.state` is `pending` is not merge authorization.

## Status

The bounded inventory at `main@2e31e0cf51c08d792cc1f301ceb21b235424cb40` found:

| Surface | Repository evidence | Status |
|---|---|---:|
| Lane | `data/receipts/generated/` exists and contains JSON files. | CONFIRMED |
| Bounded payload count | Fifty-nine direct-child `*.json` receipts existed before this README was added. | CONFIRMED at the recorded base commit |
| Machine shape | `schemas/contracts/v1/receipts/generated_receipt.schema.json` defines the receipt schema. | CONFIRMED schema file; enforcement breadth NEEDS VERIFICATION |
| PR requirement | `.github/PULL_REQUEST_TEMPLATE.md` requires a generated receipt when any diff file is AI-authored. | CONFIRMED |
| Filename pattern | Existing files predominantly use `genrec-<scope>-<digest>.json`. | CONFIRMED observation; not a naming authority |
| Generator or emitter automation | No canonical generator was established by this completion pass. | NEEDS VERIFICATION |
| Every pre-existing receipt validates and has approved human review | Not established by the bounded inventory. | UNKNOWN |

This README records current repository evidence only. It does not retroactively validate, approve, or normalize the existing receipts.

## What belongs here

- one bounded JSON provenance record for a related set of AI-authored repository artifacts;
- exact repository-relative artifact paths and content hashes;
- model identity and version information that is available to the emitter;
- a hash of the governing prompt or contract rather than prompt contents or hidden reasoning;
- pinned repository evidence references and per-artifact truth labels;
- validation gates with explicit `PASS`, `FAIL`, or `SKIPPED` outcomes and reasons;
- validated citations, policy-decision references when actually consulted, and human-review state;
- concise notes that preserve limitations, rollback posture, and no-public-authority boundaries.

Receipts should be deterministic, small, reviewable, and safe to commit. Existing filename practice may guide a new name, but the schema and governing contract control the payload.

## What does NOT belong here

- prompts, chain-of-thought, hidden reasoning, private review notes, or full tool transcripts;
- credentials, tokens, private keys, connection strings, source-system secrets, or sensitive operational details;
- raw/work/quarantine payloads, exact sensitive locations, living-person private data, or restricted source material;
- model output presented as fact, an EvidenceBundle, a proof pack, a catalog record, or a policy decision;
- release manifests, promotion decisions, correction notices, rollback cards, or published artifacts;
- a receipt that claims a check ran when it was not run, or reports `SKIPPED` work as success;
- duplicate schema, contract, policy, registry, proof, catalog, or release authority.

## Inputs

A generated receipt may derive from:

- the final AI-authored artifact set and its SHA-256 or BLAKE3 hashes;
- a pinned base commit and repository files inspected as evidence;
- the governing AI build contract and user prompt hash;
- validation commands and their observed outcomes;
- citations that were resolved to exact repository evidence;
- human-review state supplied by an authorized reviewer or review system.

Evidence references should be precise and stable. Unknown parameters should remain `null` or be omitted when the schema allows; they must not be invented.

## Outputs

The output is a JSON object conforming to `generated_receipt.schema.json`. Required fields include:

- `receipt_id`, `contract_version`, `artifact_paths`, and `artifact_hashes`;
- `model_identity`, `prompt_or_contract`, `parameters`, and `inputs`;
- `truth_labels`, `validation_gates`, `policy_decisions`, and `citations`;
- `human_review`, `created_at`, and `emitter`.

Optional links and notes may connect the receipt to a draft pull request, ADR, or drift record. Those links remain references; they do not confer authority.

## Validation

For a newly emitted receipt, reviewers should:

1. parse the JSON;
2. validate it against `schemas/contracts/v1/receipts/generated_receipt.schema.json` using JSON Schema Draft 2020-12 and format checking;
3. confirm that `artifact_paths` and `artifact_hashes` cover every AI-authored or substantively modified artifact named by the receipt;
4. recompute each content hash from the final file bytes;
5. verify that evidence references resolve at the pinned commit or branch;
6. compare every reported validation gate with the actual command result;
7. scan the receipt and artifacts for secrets and sensitive content;
8. run repository-native validation such as `make validate` when it applies;
9. keep human review `pending` until an authorized reviewer acts.

Useful bounded checks include:

```bash
python -m json.tool data/receipts/generated/<receipt>.json >/dev/null
make validate
git diff --check
```

`make validate` is a repository-wide schema/contract baseline. It does not, by itself, prove that every generated receipt was individually checked or that human review is complete.

## Review burden

Reviewers must check the artifact list, hashes, evidence citations, truth labels, validation outcomes, sensitive-data posture, Directory Rules placement, and rollback statement. They must also distinguish schema conformance from factual correctness and merge approval.

Changes that affect a sensitive domain, authority root, lifecycle boundary, public path, or release gate require the additional reviewers and ADR handling established by repository governance. The receipt cannot waive those requirements.

## Related folders

| Path | Relationship |
|---|---|
| [`../README.md`](../README.md) | Parent receipt boundary: process memory is not proof, catalog closure, release, or truth. |
| [`../../proofs/README.md`](../../proofs/README.md) | Separate proof authority; generated receipts do not replace proof closure. |
| [`../../../schemas/contracts/v1/receipts/generated_receipt.schema.json`](../../../schemas/contracts/v1/receipts/generated_receipt.schema.json) | Machine shape for generated receipts. |
| [`../../../docs/doctrine/ai-build-operating-contract.md`](../../../docs/doctrine/ai-build-operating-contract.md) | AI build discipline and receipt contract version. |
| [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) | Repository placement and responsibility boundaries; parallel copies remain a documented conflict outside this lane. |
| [`../../../.github/PULL_REQUEST_TEMPLATE.md`](../../../.github/PULL_REQUEST_TEMPLATE.md) | Pull-request field requiring a generated receipt for AI-authored diffs. |

## ADRs

[`ADR-0011`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) documents the intended separation between receipts, proofs, manifests, catalogs, and publication, but its repository status remains **proposed**. This README does not accept that ADR or resolve the repository's conflicting Directory Rules copies.

No accepted ADR was found that promotes this lane to proof, release, catalog, policy, or public authority.

## Last reviewed

- Date: 2026-07-17
- Evidence snapshot: `main@2e31e0cf51c08d792cc1f301ceb21b235424cb40`
- Direct-child JSON receipts observed before this README: 59
- Validation of every pre-existing receipt: NOT RUN
- Emitter automation and review workflow: NEEDS VERIFICATION

Re-review this README when the generated-receipt schema, AI build contract version, emitter, naming rules, validation wiring, or human-review workflow changes.
