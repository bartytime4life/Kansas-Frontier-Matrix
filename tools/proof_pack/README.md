<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-proof-pack-readme
title: tools/proof_pack README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-proof-steward-plus-release-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: public; tooling-boundary; proof-pack-builder-and-checker; no-release-authority
owning_root: tools/
responsibility: proposed executable tooling boundary for composing, checking, summarizing, and dry-running ProofPack support bundles
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../data/proofs/proof_pack/README.md
  - ../../data/proofs/evidence_bundle/README.md
  - ../../data/proofs/catalog_matrix/README.md
  - ../../data/receipts/README.md
  - ../../data/catalog/README.md
  - ../../release/README.md
  - ../../contracts/
  - ../../schemas/
  - ../../policy/
notes:
  - "This README defines a proposed ProofPack tooling boundary, not a confirmed implementation."
  - "ProofPack instances belong under data/proofs/proof_pack/. Release decisions, manifests, rollback cards, correction notices, and signatures belong under release/."
  - "tools/proof_pack may compose, check, summarize, and dry-run ProofPack candidate envelopes; it does not store canonical ProofPacks, approve release, create source truth, or replace evidence/proof authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/proof_pack

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-proof--pack--tooling-informational)
![authority](https://img.shields.io/badge/authority-builder--checker--only-blueviolet)
![release](https://img.shields.io/badge/release--authority-denied-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/proof_pack/` is the proposed tooling lane for building, checking, summarizing, and dry-running KFM ProofPack candidate envelopes. It is not the canonical ProofPack storage lane, not a receipt root, not an EvidenceBundle root, not a catalog root, not a release root, and not publication authority.

---

## Quick jump

- [Purpose](#purpose)
- [Status](#status)
- [Authority boundary](#authority-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [ProofPack tooling posture](#proofpack-tooling-posture)
- [Standard finite outcomes](#standard-finite-outcomes)
- [Standard report envelope](#standard-report-envelope)
- [Validation](#validation)
- [Review checklist](#review-checklist)
- [Roadmap](#roadmap)

---

## Purpose

`tools/proof_pack/` exists to hold durable executable support for ProofPack workflows.

A helper in this lane may assemble candidate ProofPack envelopes from references, check that required support families are present, verify that release-adjacent references resolve, compare expected digests, render reviewer summaries, and produce dry-run reports.

The durable KFM question for this lane is:

> Does this ProofPack candidate have the required references and closure signals for steward review, without collapsing receipts, proofs, catalog records, release decisions, or published artifacts?

The answer should be a tool report or candidate envelope written to an explicit caller-selected location. It should not be treated as release approval, publication, EvidenceBundle truth, catalog truth, or policy approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/proof_pack/README.md` | **CONFIRMED** | This README replaces the prior greenfield stub. |
| ProofPack tooling executable | **PROPOSED-to-create / NEEDS VERIFICATION** | No script name is claimed as implemented by this README. |
| `tools/` root authority | **CONFIRMED in repo evidence** | `tools/` owns durable executable support and does not own policy, contracts, schemas, or release authority. |
| `data/proofs/proof_pack/` | **CONFIRMED in repo evidence** | Canonical ProofPack instance/storage lane. |
| ADR-0011 separation | **CONFIRMED in repo evidence / proposed ADR** | Separates receipts, proofs, catalogs, release manifests, release decisions, and published artifacts. |
| Release authority | **DENY here** | Release decisions live under `release/`, not this tooling lane. |
| ProofPack instance authority | **DENY here** | Canonical instances belong under `data/proofs/proof_pack/`. |
| EvidenceBundle authority | **DENY here** | EvidenceBundle creation/closure belongs under accepted proof/evidence lanes and governed workflows. |

> [!IMPORTANT]
> `tools/proof_pack/` may help build and check ProofPack candidates. It must not become a parallel home for ProofPack instances, receipts, catalogs, release manifests, rollback cards, correction notices, signatures, or published artifacts.

[Back to top](#top)

---

## Authority boundary

`tools/proof_pack/` inherits the `tools/` root boundary.

| Responsibility | Home |
|---|---|
| ProofPack builder/checker tooling | `tools/proof_pack/` |
| ProofPack instances and domain ProofPack lanes | `data/proofs/proof_pack/` |
| EvidenceBundles | `data/proofs/evidence_bundle/` or accepted evidence/proof lane |
| CatalogMatrix / proof-side closure | `data/proofs/catalog_matrix/` or embedded/referenced in a ProofPack |
| Process receipts | `data/receipts/` |
| Discovery/interchange catalog records | `data/catalog/` |
| Release manifests, promotion decisions, rollback/correction/withdrawal artifacts, signatures | `release/` |
| Published public-safe carriers | `data/published/` |
| Meaning, shape, admissibility | `contracts/`, `schemas/`, `policy/` |

Safe interpretation for this path:

- **CONFIRMED:** the README exists at `tools/proof_pack/README.md`.
- **PROPOSED:** deterministic ProofPack builder/checker code may live here when report-oriented, fixture-tested, and unable to approve release by itself.
- **NEEDS VERIFICATION:** exact executable names, schemas, CI wiring, and fixture locations.
- **DENY:** using this folder as canonical storage for proof packs, evidence bundles, receipts, catalogs, release records, published artifacts, policy, or schemas.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/proof_pack/` include:

- ProofPack candidate envelope builders;
- required-reference checkers;
- source descriptor / EvidenceBundle pointer checks;
- receipt-reference presence checks;
- catalog-reference presence checks;
- release-candidate reference checks;
- rollback-target reference checks;
- digest and integrity reference checks;
- citation-validation summary loaders;
- policy-decision reference checks;
- reviewer-summary renderers;
- dry-run report emitters;
- fixture-driven smoke checks.

A helper belongs here only when it is deterministic, explicit about inputs and outputs, conservative about missing references, and clear that the output is support for review rather than release authority.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/proof_pack/` | Correct home | Reason |
|---|---|---|
| Canonical ProofPack instances | `data/proofs/proof_pack/` | ProofPack storage is a proof lane, not tool code. |
| EvidenceBundles | `data/proofs/evidence_bundle/` or accepted proof lane | Evidence support must remain inspectable outside tooling. |
| Receipts | `data/receipts/` | Receipts record process memory. |
| Catalog records | `data/catalog/` | Catalog is discovery/interchange. |
| Release manifests or release decisions | `release/` | Release authority is separate. |
| Rollback cards or correction notices | `release/` | Release-state artifacts belong with release authority. |
| Published public-safe artifacts | `data/published/` | Published carriers are downstream of release. |
| Policy bundles | `policy/` | Tools enforce or check policy references; they do not define policy. |
| Contracts or schemas | `contracts/`, `schemas/` | Meaning and shape are authority roots. |
| Raw, work, quarantine, or processed data | lifecycle data roots | ProofPack tooling references data; it does not store lifecycle data. |
| Tests | `tests/proof_pack/` or existing test convention | Tests prove this tooling; they are not the tooling lane itself. |

[Back to top](#top)

---

## ProofPack tooling posture

The tooling should be understood as a **builder/checker/summarizer**.

It may create:

- a draft candidate envelope;
- a missing-reference report;
- an integrity-reference report;
- a release-readiness checklist report;
- a reviewer handoff summary;
- a fixture comparison report.

It must not create final authority by itself:

- no release decision;
- no release manifest;
- no rollback or correction authority;
- no EvidenceBundle closure;
- no catalog closure;
- no published artifact;
- no policy approval.

When a tool writes a candidate envelope, the caller should choose the output path explicitly. A dry-run default should write to `.tmp/` or stdout, not to authority roots.

[Back to top](#top)

---

## Standard finite outcomes

| Outcome | Meaning |
|---|---|
| `PROOF_PACK_CANDIDATE_BUILT` | A candidate envelope was generated for review. |
| `PROOF_PACK_CHECK_PASS` | Required references passed the configured checks. |
| `PROOF_PACK_CHECK_FAIL` | One or more required checks failed. |
| `REFERENCE_MISSING` | A required pointer is absent. |
| `REFERENCE_UNRESOLVED` | A required pointer is present but not resolvable in the checked context. |
| `DIGEST_MISMATCH` | A referenced digest does not match expectation. |
| `POLICY_REFERENCE_MISSING` | Required policy decision or policy posture reference is absent. |
| `RELEASE_REFERENCE_MISSING` | Required release-candidate or rollback reference is absent. |
| `CATALOG_REFERENCE_MISSING` | Required catalog or catalog-closure reference is absent. |
| `ABSTAIN` | The tool cannot decide with available evidence. |
| `ERROR` | The tool could not safely complete. |

[Back to top](#top)

---

## Standard report envelope

A first-slice proof-pack tool report should be compact and deterministic.

```json
{
  "tool": "proof-pack-checker",
  "status": "PROOF_PACK_CHECK_FAIL",
  "proof_pack_candidate": "candidate_placeholder",
  "checks": {
    "source_descriptors": "present",
    "evidence_bundles": "present",
    "receipts": "present",
    "catalog_records": "missing",
    "policy_references": "present",
    "release_references": "missing",
    "rollback_target": "missing",
    "digests": "not_checked"
  },
  "decision": {
    "outcome": "PROOF_PACK_CHECK_FAIL",
    "reason_codes": ["CATALOG_REFERENCE_MISSING", "RELEASE_REFERENCE_MISSING"],
    "release_approved": false,
    "publication": false,
    "authority_created": false
  },
  "next_review": [
    "resolve missing catalog reference",
    "resolve release candidate and rollback references",
    "rerun ProofPack checker before release review"
  ]
}
```

Reports are process outputs. They are not receipts unless separately adopted and stored under the receipt root by a governed workflow.

[Back to top](#top)

---

## Validation

Recommended first test surface:

```text
tests/proof_pack/
├── README.md
├── test_proof_pack_checker.py
└── fixtures/
    ├── valid_candidate/
    │   ├── proof_pack_candidate.json
    │   └── expected_report.json
    ├── missing_catalog_reference/
    │   ├── proof_pack_candidate.json
    │   └── expected_report.json
    ├── missing_release_reference/
    │   ├── proof_pack_candidate.json
    │   └── expected_report.json
    └── digest_mismatch/
        ├── proof_pack_candidate.json
        └── expected_report.json
```

Suggested future command pattern:

```bash
pytest -q tests/proof_pack
```

```bash
python tools/proof_pack/proof_pack_check.py \
  --candidate tests/proof_pack/fixtures/valid_candidate/proof_pack_candidate.json \
  --output .tmp/proof-pack-check-report.json \
  --dry-run
```

> [!NOTE]
> The command above is a proposed interface, not proof that `proof_pack_check.py` exists.

[Back to top](#top)

---

## Review checklist

Before adding or changing proof-pack tooling, reviewers should confirm:

- [ ] The tool is deterministic and explicit about inputs/outputs.
- [ ] The tool does not store canonical ProofPack instances under `tools/`.
- [ ] The tool keeps receipts, proofs, catalogs, release decisions, and published artifacts separate.
- [ ] Missing references fail closed.
- [ ] Release approval is never inferred from a successful local check alone.
- [ ] Output is machine-readable and reviewer-friendly.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Any promotion into a trust gate is documented with schemas, tests, and rollback plan.

[Back to top](#top)

---

## Roadmap

| Step | Status | Outcome |
|---|---|---|
| Replace greenfield stub with governed proof-pack tooling contract | **DONE in this README** | Establishes builder/checker boundary. |
| Add `tests/proof_pack/README.md` | **PROPOSED** | Defines public-safe fixture rules and expected reports. |
| Add `proof_pack_check.py` dry-run checker | **PROPOSED** | Emits deterministic reference-closure report. |
| Add candidate builder helper | **PROPOSED** | Creates draft envelope from explicit references. |
| Align with schemas/contracts | **PROPOSED / NEEDS VERIFICATION** | Match accepted ProofPack schema and contract once verified. |
| Wire into CI or release review as non-authoritative summary | **PROPOSED / later** | Supports stewards without replacing release authority. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for greenfield stub. |
| Next smallest safe change | Add `tests/proof_pack/README.md`, then add fixtures for valid candidate, missing references, unresolved references, and digest mismatch. |
