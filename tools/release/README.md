<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-release-readme
title: tools/release README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-release-steward-plus-docs-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; release-tooling; review-support
owning_root: tools/
responsibility: release tooling boundary for dry-runs, manifest checks, rollback-card helpers, correction-note helpers, and release-review summaries
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../../release/README.md
  - ../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../proof_pack/README.md
  - ../qa/README.md
  - ../validators/README.md
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../data/catalog/
  - ../../data/published/
  - ../../contracts/
  - ../../schemas/
  - ../../policy/
notes:
  - "This README documents the release tooling lane. It does not confirm executable files."
  - "Release-governance records belong under release/. tools/release may prepare, check, summarize, or dry-run support files but does not approve release by itself."
  - "Promotion is a governed state transition, not a file move. Tool reports support review and do not replace steward decisions."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/release

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-release--tooling-informational)
![authority](https://img.shields.io/badge/authority-support--only-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/release/` is the tooling lane for KFM release-support helpers: dry-run checks, manifest inspectors, rollback-card helpers, correction-note helpers, and release-review summary renderers. It is not the `release/` governance root and does not approve publication by itself.

---

## Purpose

`tools/release/` holds deterministic helpers that support release review without becoming the release record.

A helper may inspect a candidate, check references, compare a manifest against expected support records, render a review summary, create a draft rollback-card scaffold, check a correction-note envelope, or produce a dry-run report.

The durable KFM question for this lane is:

> What release-facing support checks or draft records can be prepared for steward review without replacing governed release records?

The answer should be a tool report, draft scaffold, or reviewer handoff. Actual release governance remains under `release/`.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/release/README.md` | **CONFIRMED** | This README replaces the previous greenfield stub. |
| Release helper executables | **PROPOSED / NEEDS VERIFICATION** | No script is claimed here. |
| `tools/` root authority | **CONFIRMED in repo evidence** | Parent README names `tools/release/` as release dry-runs, manifest validators, rollback-card builders, and correction-notice helpers. |
| `release/` root authority | **CONFIRMED in repo evidence** | `release/` owns release governance records, review, decisions, manifests, corrections, notices, signatures, and changelog records. |
| Artifact-family separation | **CONFIRMED in repo evidence / proposed ADR** | ADR-0011 separates receipts, proofs, catalogs, release/publication artifacts, and published carriers. |

> [!IMPORTANT]
> A successful `tools/release/` check is not a release decision. It is support for release-steward review.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Release helper tooling | `tools/release/` |
| Release governance records | `release/` |
| Release manifests and decisions | `release/manifests/`, `release/decisions/`, `release/promotion_decisions/`, or accepted release lane |
| Rollback, correction, withdrawal, notice, and changelog records | `release/` lanes |
| Receipts | `data/receipts/` |
| EvidenceBundles, ProofPacks, CatalogMatrix, integrity/citation proof support | `data/proofs/` |
| Discovery/interchange catalog records | `data/catalog/` |
| Released public-safe carriers | `data/published/` |
| Contracts, schemas, and policy | `contracts/`, `schemas/`, `policy/` |
| Validators of record | `tools/validators/` or accepted validator home |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** deterministic release-support helper code may live here when report-oriented, fixture-tested, and explicit about inputs and outputs.
- **NEEDS VERIFICATION:** exact executable names, fixture locations, CI wiring, schema references, and output conventions.
- **DENY:** this folder must not store canonical release records, proof records, receipts, published artifacts, contracts, schemas, or policy rules.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/release/` include:

- release dry-run helpers;
- release-manifest reference checks;
- rollback-card scaffold helpers;
- correction-note scaffold helpers;
- withdrawal/supersession summary helpers;
- release-candidate support checkers;
- manifest-to-proof/receipt/catalog pointer checks;
- release-review summary renderers;
- changelog draft helpers;
- deterministic report formatters.

A helper belongs here only when it is deterministic, explicit about scan/input scope, explicit about output path, conservative about missing support records, and clear that its output is review support.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/release/` | Correct home |
|---|---|
| Release decisions and release manifests of record | `release/` |
| Rollback cards, correction notices, withdrawal notices, signatures, changelog records | `release/` |
| Receipts | `data/receipts/` |
| EvidenceBundles, ProofPacks, CatalogMatrix, integrity reports | `data/proofs/` |
| Catalog records | `data/catalog/` |
| Published data or public map/API artifacts | `data/published/` |
| Contracts | `contracts/` |
| Schemas | `schemas/` |
| Policy rules | `policy/` |
| Validators of record | `tools/validators/` |
| Tests | `tests/release/` or accepted test convention |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `RELEASE_TOOL_PASS` | Configured tool checks passed. |
| `RELEASE_TOOL_WARN` | Review issues were found. |
| `RELEASE_TOOL_FAIL` | Configured checks failed. |
| `MANIFEST_REFERENCE_MISSING` | Required manifest pointer is absent. |
| `PROOF_REFERENCE_MISSING` | Required proof support pointer is absent. |
| `RECEIPT_REFERENCE_MISSING` | Required receipt pointer is absent. |
| `ROLLBACK_REFERENCE_MISSING` | Required rollback target or card pointer is absent. |
| `POLICY_REFERENCE_MISSING` | Required policy review pointer is absent. |
| `DIGEST_MISMATCH` | Referenced digest does not match expectation. |
| `ABSTAIN` | Helper cannot decide with available context. |
| `ERROR` | Helper could not safely complete. |

[Back to top](#top)

---

## Standard report envelope

```json
{
  "tool": "release-check-placeholder",
  "status": "RELEASE_TOOL_WARN",
  "scan_scope": "release_candidate_placeholder",
  "checks": {
    "manifest_ref": "present",
    "proof_refs": "present",
    "receipt_refs": "missing",
    "rollback_ref": "present",
    "policy_ref": "needs_review"
  },
  "decision": {
    "outcome": "RELEASE_TOOL_WARN",
    "reason_codes": ["RECEIPT_REFERENCE_MISSING", "POLICY_REFERENCE_MISSING"],
    "release_decision_created": false,
    "publication_created": false,
    "authority_created": false
  },
  "next_review": [
    "resolve missing receipt reference",
    "resolve policy review pointer",
    "rerun release support check before steward decision"
  ]
}
```

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/release/
├── README.md
├── test_release_support_tools.py
└── fixtures/
    ├── valid_candidate/
    ├── missing_receipt/
    ├── missing_policy_ref/
    └── digest_mismatch/
```

Suggested future command pattern:

```bash
pytest -q tests/release
```

```bash
python tools/release/release_check.py --candidate tests/release/fixtures/valid_candidate/input.json --output .tmp/release-check-report.json --dry-run
```

> [!NOTE]
> This is a proposed interface, not proof that `release_check.py` or `tests/release/` exists.

[Back to top](#top)

---

## Review checklist

- [ ] Helper is deterministic.
- [ ] Helper is explicit about input and output paths.
- [ ] Helper output is release-review support, not the release record itself.
- [ ] Helper does not duplicate release records, receipts, proofs, catalogs, contracts, schemas, or policy.
- [ ] Missing evidence or governance pointers fail closed or warn clearly.
- [ ] Output is machine-readable where practical.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Roadmap

| Step | Status | Outcome |
|---|---|---|
| Replace greenfield stub with governed release tooling contract | **DONE in this README** | Establishes release-support tooling boundary. |
| Add `tests/release/README.md` | **PROPOSED** | Defines public-safe fixture rules and expected reports. |
| Add release support checker | **PROPOSED** | Emits deterministic release-review support report. |
| Add rollback/correction scaffold helpers | **PROPOSED** | Drafts review-ready scaffolds without deciding release state. |
| Align with release schemas/contracts | **PROPOSED / NEEDS VERIFICATION** | Match accepted release record schemas once verified. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for greenfield stub. |
| Next smallest safe change | Add `tests/release/README.md`, then add fixtures for valid candidate, missing receipt, missing policy reference, rollback gap, and digest mismatch. |
