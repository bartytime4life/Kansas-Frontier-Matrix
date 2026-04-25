<!-- [KFM_META_BLOCK_V2]
doc_id: kfm.review_console.readme
title: Reviewer Console (Promotion & Decision Artifacts)
type: component-readme
version: v1
status: draft
owners: @bartytime4life
created: 2026-04-24
updated: 2026-04-25
policy_label: evidence-first
related: [../../data/receipts/README.md, ../../tools/validators/promotion_gate/README.md, ../../tools/attest/README.md, ../../tests/e2e/runtime_proof/README.md]
tags: [review, governance, evidence, dsse, cosign, rekor, opa, promotion-gate]
notes: [Source status was PROPOSED/docs-first. Target path and runtime enforcement remain NEEDS VERIFICATION until verified in the mounted repository.]
[/KFM_META_BLOCK_V2] -->

# Reviewer Console (Promotion & Decision Artifacts)

Stewardship shell for inspecting candidate promotion evidence, policy outcomes, receipt verification, and signed reviewer decisions before publication.

> [!IMPORTANT]
> The Reviewer Console is a **shell variation**, not a second truth regime. It may help a steward decide, but it must not replace the Promotion Gate, EvidenceBundle, receipts, signatures, policy checks, or governed publication path.

## Impact block

| Field | Value |
| --- | --- |
| **Status** | `experimental` · source posture: `PROPOSED / docs-first` |
| **Owners** | `@bartytime4life` |
| **Target path** | `apps/review-console/README.md` · **PROPOSED** |
| **Truth posture** | Evidence-first · fail-closed · implementation status **NEEDS VERIFICATION** |
| **Runtime role** | Steward review surface inside the same governed shell |

![status: experimental](https://img.shields.io/badge/status-experimental-orange)
![truth: evidence--first](https://img.shields.io/badge/truth-evidence--first-blue)
![policy: fail--closed](https://img.shields.io/badge/policy-fail--closed-red)
![runtime: shell--variation](https://img.shields.io/badge/runtime-shell--variation-lightgrey)

**Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Operating flow](#operating-flow) · [UI contract](#ui-contract) · [Decision actions](#decision-actions) · [Decision Artifact schema](#decision-artifact-schema) · [Verifier tooling](#verifier-tooling) · [Fail-closed rules](#fail-closed-rules) · [Directory layout](#directory-layout) · [Task list](#task-list)

---

## Scope

The Reviewer Console enables governed promotion review by showing the steward:

- **what changed** between a prior EvidenceBundle and a candidate EvidenceBundle;
- **why policy allowed, denied, or flagged** the candidate;
- **whether the run receipt is verifiable** through DSSE/cosign/Rekor or the repository-approved equivalent;
- **which provenance records changed** for touched fields only; and
- **which signed decision artifact** was emitted by the review action.

The console exists to make the promotion decision inspectable. It does not move files into publication by itself.

**Core principle:** the decision is part of the evidence chain.

---

## Repo fit

| Boundary | Placement |
| --- | --- |
| **Component path** | `apps/review-console/` **PROPOSED** |
| **Schema path** | `data/registry/schemas/decision_artifact.v1.json` **PROPOSED / NEEDS VERIFICATION** |
| **Upstream** | `../../tools/validators/promotion_gate/`, pipelines/watchers, receipt generation, attest tooling |
| **Downstream** | published/released artifacts, governed runtime APIs, Evidence Drawer, release/correction records |
| **Peer surfaces** | Evidence Drawer, Focus Mode, review queues, compare surfaces, export previews |

### Upstream links

- [`../../data/receipts/README.md`](../../data/receipts/README.md) — receipt family and candidate evidence inputs (**NEEDS VERIFICATION**)
- [`../../tools/validators/promotion_gate/README.md`](../../tools/validators/promotion_gate/README.md) — Promotion Gate output contract (**NEEDS VERIFICATION**)
- [`../../tools/attest/README.md`](../../tools/attest/README.md) — DSSE/cosign/Rekor or equivalent attestation tooling (**NEEDS VERIFICATION**)
- [`../../tests/e2e/runtime_proof/README.md`](../../tests/e2e/runtime_proof/README.md) — runtime proof checks (**NEEDS VERIFICATION**)

> [!NOTE]
> The links above preserve the source draft’s placement model. Verify the actual repository tree before treating these paths as implemented.

---

## Accepted inputs

Only governed review inputs belong in this console.

| Input | Expected role | Minimum review use |
| --- | --- | --- |
| `EvidenceBundle.json` | Candidate evidence bundle | Compare candidate against prior release or prior candidate. |
| Promotion Gate output | Policy result | Show `allow`, violations, policy version, engine, and affected JSON paths. |
| `receipt.dsse` | Signed run receipt envelope | Verify the candidate’s run receipt or attestation envelope. |
| `rekor.json` | Transparency-log proof | Show Rekor UUID, log index, and inclusion proof when required by policy. |
| Prior EvidenceBundle | Baseline evidence | Render changed fields only, using JSON Pointer paths. |
| PROV lineage payload | Field-level provenance | Explain Entity → Activity → Agent only for touched fields. |

---

## Exclusions

The Reviewer Console must not become a shortcut around the trust membrane.

| Do not put here | Where it belongs instead |
| --- | --- |
| RAW, WORK, or QUARANTINE records | Lifecycle storage and ingest/quarantine tools. |
| Direct canonical-store readers for public UI paths | Governed APIs and released artifacts. |
| Unreviewed model output or AI summaries | Governed AI runtime envelope after EvidenceBundle resolution and policy checks. |
| Source credentials, private keys, or signing secrets | Secret manager / platform identity controls. |
| Ad hoc reviewer notes without signature or actor identity | Signed DecisionArtifact / ReviewRecord family. |
| Map tiles, summaries, or graph projections as sovereign truth | Rebuildable derived layers with EvidenceRef → EvidenceBundle support. |
| Publication side effects | Promotion/release pipeline after decision validation. |

---

## Operating flow

```mermaid
flowchart LR
  candidate[Candidate EvidenceBundle] --> gate[Promotion Gate\npolicy outcome]
  candidate --> receipt[Run receipt\nDSSE envelope]
  receipt --> attest[Signature + Rekor\nverification]
  gate --> console[Reviewer Console\nsteward shell]
  attest --> console
  prior[Prior EvidenceBundle] --> diff[Evidence diff\nJSON Pointer paths]
  diff --> console
  console --> decision{Reviewer action}
  decision --> approve[approve]
  decision --> obligation[approve_with_obligation]
  decision --> deny[deny]
  approve --> artifact[DecisionArtifact]
  obligation --> artifact
  deny --> artifact
  artifact --> sign[Sign decision]
  sign --> release_gate[Release / promotion gate]
  release_gate -->|valid + allowed| published[Published / governed APIs]
  release_gate -->|invalid, denied, blocked| retained[Retained negative outcome]
```

The negative path is intentional: denied or blocked candidates remain visible as governance evidence rather than disappearing from the record.

---

## UI contract

### Header strip

The header should be compact, persistent, and visible while a reviewer scrolls.

| Field | Display rule |
| --- | --- |
| Candidate ID | Always visible. |
| `spec_hash → prior_spec_hash` | Show both values; mark missing prior hash as first-promotion / no-prior-state. |
| Source | Show `repo@ref` or the repository-approved source reference. |
| Timestamps | Show generated, recorded, and reviewed times separately when available. |
| Gate runner | Example: `promotion_gate@v1`; exact runner ID **NEEDS VERIFICATION**. |
| Review state | `unreviewed`, `approved`, `approved_with_obligation`, `denied`, `blocked`. |

### Evidence diff

Render only changed fields by JSON Pointer path.

| Region | Requirement |
| --- | --- |
| Left side | Prior value, prior provenance, prior release state. |
| Right side | Candidate value, candidate provenance, candidate review state. |
| Inline badges | Source, extractor, timestamp, evidence state, sensitivity state. |
| Empty diff | Must not imply approval; show `NO_CHANGE_DETECTED` and still require verification. |

### Policy outcome

Show the Promotion Gate result as a first-class object.

| Element | Required content |
| --- | --- |
| Result | `ALLOW` or `DENY`; additional `BLOCK` display may be derived by console fail-closed checks. |
| Violations | Rule ID, message, JSON path, severity if provided. |
| Policy identity | Policy version, engine, bundle/hash if available. |
| Replay affordance | Link or command to replay the policy decision. |

### Signature status

| Check | Display |
| --- | --- |
| DSSE envelope | `verified`, `missing`, `invalid`, or `not_required_by_policy` |
| cosign / equivalent | Verification summary and key identity. |
| Rekor | UUID, log index, inclusion proof, or reason omitted. |
| Transcript | Collapsible verifier transcript; never hide a failure behind a green summary. |

### Provenance view

Show field-level lineage only for touched fields.

```text
Entity → Activity → Agent
```

This view should answer: *What changed, who/what produced it, when was it recorded, and what evidence supports it?*

---

## Decision actions

All actions produce a **signed DecisionArtifact**. A UI action is not authoritative until the artifact is emitted, signed, and accepted by downstream validation.

| Action | Meaning | Required posture |
| --- | --- | --- |
| **Approve** | Candidate may proceed to publication gates. | Allowed only when policy and verification are valid. |
| **Approve with obligation** | Candidate may proceed only after machine-readable obligations are satisfied. | Obligations must be visible and enforceable downstream. |
| **Deny** | Candidate does not proceed. | Rationale required; negative outcome remains visible. |

### Obligation example

```json
{
  "type": "redact",
  "params": {
    "fields": ["owner_email", "utm"]
  }
}
```

---

## Decision Artifact schema

**Path:** `data/registry/schemas/decision_artifact.v1.json` (**PROPOSED / NEEDS VERIFICATION**)

A DecisionArtifact records the reviewer decision and the evidence/policy/receipt verification context that made the decision reviewable. It is adjacent to promotion; it is not the EvidenceBundle, not the run receipt, and not the release manifest.

| Field family | Purpose |
| --- | --- |
| Identity | `decision_id`, `candidate_id`, `spec_hash`, `prior_spec_hash` |
| Decision | `approve`, `approve_with_obligation`, or `deny` |
| Actor | Reviewer identity and signing key identity |
| Policy summary | Promotion Gate result, violations, policy version, engine |
| Receipt verification | DSSE/cosign/Rekor status or approved equivalent |
| Obligations | Machine-readable follow-up requirements |
| Signature | Signature over the decision artifact |

<details>
<summary>Draft JSON Schema sketch</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kfm.example/schemas/decision_artifact.v1.json",
  "title": "DecisionArtifact v1",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "decision_id",
    "candidate_id",
    "spec_hash",
    "decision",
    "actor",
    "timestamp",
    "policy_summary",
    "receipt_verification",
    "signature"
  ],
  "properties": {
    "decision_id": { "type": "string", "minLength": 1 },
    "candidate_id": { "type": "string", "minLength": 1 },
    "spec_hash": { "type": "string", "minLength": 1 },
    "prior_spec_hash": { "type": ["string", "null"] },
    "decision": {
      "type": "string",
      "enum": ["approve", "approve_with_obligation", "deny"]
    },
    "rationale": { "type": "string" },
    "obligations": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["type", "params"],
        "properties": {
          "type": { "type": "string", "minLength": 1 },
          "params": { "type": "object" }
        }
      }
    },
    "policy_summary": {
      "type": "object",
      "additionalProperties": false,
      "required": ["allow", "violations", "policy_version", "engine"],
      "properties": {
        "allow": { "type": "boolean" },
        "violations": {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": false,
            "required": ["id", "message", "path"],
            "properties": {
              "id": { "type": "string" },
              "message": { "type": "string" },
              "path": { "type": "string" }
            }
          }
        },
        "policy_version": { "type": "string" },
        "engine": { "type": "string" }
      }
    },
    "receipt_verification": {
      "type": "object",
      "additionalProperties": false,
      "required": ["dsse_verified", "rekor_verified", "verifier"],
      "properties": {
        "dsse_verified": { "type": "boolean" },
        "rekor_verified": { "type": "boolean" },
        "dsse_envelope_ref": { "type": "string" },
        "rekor_index": { "type": ["integer", "null"] },
        "rekor_uuid": { "type": ["string", "null"] },
        "verifier": { "type": "string" },
        "transcript_ref": { "type": "string" }
      }
    },
    "actor": {
      "type": "object",
      "additionalProperties": false,
      "required": ["id", "display", "keyid"],
      "properties": {
        "id": { "type": "string" },
        "display": { "type": "string" },
        "keyid": { "type": "string" }
      }
    },
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "signature": {
      "type": "object",
      "additionalProperties": false,
      "required": ["algorithm", "keyid", "signature"],
      "properties": {
        "algorithm": { "type": "string" },
        "keyid": { "type": "string" },
        "signature": { "type": "string" }
      }
    }
  }
}
```

</details>

Validator notes:

- `deny` should require a non-empty `rationale`.
- `approve_with_obligation` should require at least one obligation.
- `approve` should fail when `policy_summary.allow=false` or receipt verification fails.
- Exact JSON Schema home and `$id` remain **NEEDS VERIFICATION**.

---

## Verifier tooling

These examples preserve the intended CLI shape from the source draft. Treat them as **PROPOSED** until the `kfm` CLI and argument names are verified in the repository.

### Recompute `spec_hash`

```bash
CANDIDATE_ID="TODO-candidate-id"
BUNDLE_PATH="data/receipts/${CANDIDATE_ID}/EvidenceBundle.json"

kfm verify spec-hash "$CANDIDATE_ID" \
  --bundle "$BUNDLE_PATH"
```

### Verify signature and Rekor proof

```bash
CANDIDATE_ID="TODO-candidate-id"
ENVELOPE_PATH="data/receipts/${CANDIDATE_ID}/receipt.dsse"

kfm verify signature "$CANDIDATE_ID" \
  --envelope "$ENVELOPE_PATH"
```

### Replay policy decision

```bash
CANDIDATE_ID="TODO-candidate-id"
BUNDLE_PATH="data/receipts/${CANDIDATE_ID}/EvidenceBundle.json"

kfm verify policy \
  --bundle "$BUNDLE_PATH" \
  --policy "policy/promotion_contract/" \
  --expect allow
```

### Review actions

```bash
CANDIDATE_ID="TODO-candidate-id"

kfm review inspect "$CANDIDATE_ID" --evidence-diff

kfm review approve "$CANDIDATE_ID" \
  --rationale "Meets Promotion Contract A" \
  --sign

kfm review approve "$CANDIDATE_ID" \
  --rationale "Redact sensitive fields before release" \
  --obligation 'redact:fields=["owner_email","utm"]' \
  --sign

kfm review deny "$CANDIDATE_ID" \
  --rationale "PII policy violation" \
  --sign
```

---

## Fail-closed rules

| Condition | Console outcome | Publication consequence |
| --- | --- | --- |
| Missing EvidenceBundle | `BLOCK` | No decision artifact may approve publication. |
| `spec_hash` mismatch | `BLOCK` | Candidate must be regenerated or corrected. |
| DSSE envelope missing | `BLOCK` | Candidate remains unpublished. |
| Signature/cosign verification fails | `BLOCK` | Candidate remains unpublished. |
| Rekor proof missing or invalid when required | `BLOCK` | Candidate remains unpublished. |
| Promotion Gate `allow=false` | `DENY` | No approval path without policy correction or new candidate. |
| Unsigned DecisionArtifact | `DISCARD` | Decision has no release effect. |
| Actor key not trusted | `BLOCK` | Reviewer identity/key must be resolved. |
| Unresolved obligation | `HOLD` | Candidate cannot publish until obligation is satisfied and recorded. |
| Sensitivity or rights unresolved | `DENY` or `HOLD` | Public release must remain blocked until policy permits. |

---

## Directory layout

```text
apps/
  review-console/
    README.md

data/
  receipts/
    <candidate_id>/
      EvidenceBundle.json
      receipt.dsse
      rekor.json
      DecisionArtifact.json

  registry/
    schemas/
      decision_artifact.v1.json
```

Directory notes:

- `apps/review-console/` is the proposed shell/component home from the source draft.
- `data/receipts/<candidate_id>/` preserves the source draft’s receipt-centered layout.
- Schema home is **PROPOSED**; verify against the repository’s actual schema/contract convention before creating machine files.

---

## Task list

### Build gates

- [ ] Confirm target path and neighboring README/doc conventions.
- [ ] Confirm whether schema home is `data/registry/schemas/`, `schemas/contracts/v1/`, `contracts/objects/`, or another repo-standard location.
- [ ] Confirm Promotion Gate output shape and policy engine naming.
- [ ] Confirm DSSE/cosign/Rekor tooling, transcript storage, and required verification fields.
- [ ] Confirm whether a `ReviewRecord`, `DecisionEnvelope`, or `PromotionDecision` object already exists and should be reused.

### Component work

- [ ] Evidence diff generator using JSON Pointer paths.
- [ ] DSSE verification integration.
- [ ] Rekor inclusion validation.
- [ ] OPA / policy adapter normalization.
- [ ] Decision signing flow.
- [ ] CLI scaffold for `kfm review` commands.
- [ ] Evidence Drawer parity for policy, provenance, sensitivity, and receipt state.
- [ ] PROV lineage renderer for touched fields only.

### Definition of done

- [ ] Invalid or missing receipt produces `BLOCK`.
- [ ] Policy `allow=false` cannot be overridden by UI approval.
- [ ] Unsigned decisions are discarded by downstream validation.
- [ ] Denials and blocked decisions remain queryable as negative governance outcomes.
- [ ] Public publication path consumes only signed, validated, policy-allowed decisions.
- [ ] README links and relative paths are verified from `apps/review-console/`.

---

## FAQ

### Is the Reviewer Console allowed to publish directly?

No. It emits a signed DecisionArtifact. Publication remains a governed transition after validation, policy, and release checks.

### Can an approver override the Promotion Gate?

No. If policy denies or a verifier blocks, the console must fail closed. The appropriate path is correction, new evidence, or a new candidate.

### Is a DecisionArtifact the same as an EvidenceBundle?

No. The EvidenceBundle carries reviewable evidence. The DecisionArtifact records the review decision and its verification context.

### Can this surface show negative outcomes?

Yes. Denials, blocks, and discarded unsigned decisions are governance evidence and should remain inspectable.

---

## Final principle

> No unsigned decision, unverifiable receipt, unresolved obligation, or policy violation reaches publication.

[Back to top](#reviewer-console-promotion--decision-artifacts)
