<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/PLACEHOLDER-AI-RECEIPTS-README
title: AI Receipts
type: standard
version: v1
status: draft
owners: [NEEDS VERIFICATION]
created: 2026-03-28
updated: 2026-03-28
policy_label: public
related:
  - docs/security/README.md
  - docs/standards/README.md
  - policy/
  - tests/
tags: [kfm, security, provenance, ai, attestations]
notes: Source-bounded draft. Exact repo paths, owners, workflow names, and artifact references NEED VERIFICATION in a live checkout.
[/KFM_META_BLOCK_V2] -->

# AI Receipts

Governed, signed provenance records for AI-assisted runs and derived outputs.

> [!IMPORTANT]
> This document is **source-bounded** and **doctrine-aligned**. It proposes a KFM-compatible AI receipt pattern using in-toto attestations, DSSE envelopes, and Sigstore/Cosign verification. Live repo wiring, owners, and workflow paths **NEED VERIFICATION** before merge.

---

## Impact

**Status:** draft  
**Owners:** NEEDS VERIFICATION  
**Path:** `docs/security/ai-receipts/README.md`  
**Repo fit:** security / supply-chain governance / derived-output provenance  
**Truth posture:**  
- **CONFIRMED:** Cosign supports in-toto attestations and verification. :contentReference[oaicite:1]{index=1}  
- **CONFIRMED:** in-toto attestation specs recommend DSSE for envelopes. :contentReference[oaicite:2]{index=2}  
- **CONFIRMED:** JCS defines deterministic JSON canonicalization suitable for hashing. :contentReference[oaicite:3]{index=3}  
- **PROPOSED:** KFM-specific schema fields, evidence references, and policy gates  
- **NEEDS VERIFICATION:** exact CI workflows, repo paths, contract files, and test harness locations

![Status](https://img.shields.io/badge/status-draft-orange)
![Surface](https://img.shields.io/badge/surface-security-blue)
![Posture](https://img.shields.io/badge/posture-fail--closed-red)
![Evidence](https://img.shields.io/badge/evidence-source--bounded-lightgrey)

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Schema](#minimal-receipt-schema) · [Flow](#flow) · [Quickstart](#quickstart) · [Policy gate](#policy-gate) · [FAQ](#faq)

---

## Scope

This document defines a **minimal, auditable receipt** for AI-assisted execution in KFM.

An AI receipt is a signed record that binds:

- a canonicalized prompt representation,
- its cryptographic hash,
- model/runtime metadata,
- input/output digests,
- actor identity,
- timestamp,
- review state,

to a derived output artifact.

The receipt is intended to support:

- fail-closed promotion,
- tamper evidence,
- reproducible verification,
- policy enforcement in CI and runtime,
- evidence drill-through for derived AI outputs.

---

## Repo fit

**Path:** `docs/security/ai-receipts/README.md`  
**Upstream:**  
- `docs/security/README.md`
- `docs/architecture/TRUST_MEMBRANE.md` or equivalent (**NEEDS VERIFICATION**)
- `docs/architecture/TRUTH_PATH_LIFECYCLE.md` or equivalent (**NEEDS VERIFICATION**)
- `docs/standards/README.md`

**Downstream:**  
- `policy/` attestation gates
- `tests/policy/` and `tests/e2e/` verification flows
- release / promotion workflows
- derived-output publication surfaces

**Adjacent:**  
- `contracts/` for JSON Schema / predicate contract (**PROPOSED**)
- `tools/` for canonicalization / hashing / verification helpers (**PROPOSED**)
- `scripts/` for thin orchestration entrypoints (**PROPOSED**)

---

## Accepted inputs

This surface expects, at minimum:

- a canonicalizable prompt payload,
- a model identifier or version string,
- a deterministic config representation or config hash,
- digests for governed input and output artifacts,
- actor identity,
- timestamp,
- review state,
- subject artifact reference for attestation.

---

## Exclusions

This document does **not** authorize:

- treating AI outputs as authoritative truth,
- storing raw secrets in prompts or receipts,
- publishing unsigned or unverifiable derived artifacts,
- bypassing governed APIs, evidence resolution, or policy checks,
- burying canonical contract truth in ad hoc scripts,
- using receipts as a substitute for rights, sensitivity, or sovereignty review.

> [!CAUTION]
> AI receipts apply to **derived** artifacts. They do not elevate an AI result to authoritative status.

---

## Directory tree

```text
docs/security/ai-receipts/        # this document and examples (PROPOSED)
contracts/ai-receipts/            # predicate schema(s) (PROPOSED)
policy/ai-receipts/               # OPA / Conftest rules (PROPOSED)
tools/ai-receipts/                # canonicalization / verification helpers (PROPOSED)
tests/policy/ai-receipts/         # negative and positive policy cases (PROPOSED)
tests/e2e/ai-receipts/            # promotion / tamper / missing-attestation flows (PROPOSED)
