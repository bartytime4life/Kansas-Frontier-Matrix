# `runtime/people/` — People Runtime Guardrail Lane

Runtime notes for People / Genealogy / DNA / Land-adjacent behavior in KFM. This lane is deny-by-default and must not become a public path for living-person, DNA/genomic, residential, land-title, consent-unclear, rights-unclear, or culturally sensitive material.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runtime-people-readme
title: runtime/people/README.md — People Runtime Guardrail Lane
type: readme; directory-readme; runtime-guardrail; sensitive-domain-runtime-index
version: v0.1
status: draft; empty-path-expanded; no-runtime-implementation-confirmed; deny-by-default; NEEDS VERIFICATION
owners: OWNER_TBD — Runtime steward · People/DNA/Land steward · Policy steward · Evidence steward · Security steward · Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-05
policy_label: restricted-review; runtime; people; living-person; dna; land; privacy
tags: [kfm, runtime, people, genealogy, dna, land, living-person, privacy, consent, deny-by-default, finite-outcomes]
related:
  - ../README.md
  - ../AI/README.md
  - ../model_adapters/README.md
  - ../model_adapters/AdapterContract.md
  - ../model_adapters/mock/README.md
  - ../mock/README.md
  - ../envelopes/README.md
  - ../../packages/domains/people-dna-land/README.md
  - ../../packages/domains/people-dna-land/land-ownership/README.md
  - ../../contracts/
  - ../../schemas/
  - ../../policy/
  - ../../fixtures/
  - ../../tests/
  - ../../data/
  - ../../release/
notes:
  - "Expanded from an empty runtime/people/README.md."
  - "Current-session search found no direct runtime/people files beyond this README."
  - "runtime/ is confirmed as local runtime wiring, model adapters, and service harnesses subordinate to evidence, policy, and release."
  - "The People / DNA / Land package README is restricted-review and denies or restricts living-person, DNA/genomic, DNA-derived relationship, residential, culturally sensitive, title-sensitive, and rights-uncertain outputs unless evidence, consent, policy, review, and release state explicitly allow otherwise."
  - "This README does not prove runtime implementation, API route behavior, model-adapter behavior, consent enforcement, policy enforcement, EvidenceBundle resolution, CI coverage, emitted receipts, release readiness, or public-client behavior."
[/KFM_META_BLOCK_V2] -->

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Policy: restricted review" src="https://img.shields.io/badge/policy-restricted__review-red">
  <img alt="Root: runtime" src="https://img.shields.io/badge/root-runtime%2F-blue">
  <img alt="Lane: people" src="https://img.shields.io/badge/lane-people-purple">
  <img alt="Boundary: deny by default" src="https://img.shields.io/badge/boundary-deny__by__default-critical">
</p>

**Status:** draft / sensitive runtime guardrail
**Path:** `runtime/people/`
**Current role:** README-only runtime boundary for People / Genealogy / DNA / Land-adjacent runtime behavior
**Truth posture:** CONFIRMED empty README path before this update; CONFIRMED no direct implementation files found in current search; CONFIRMED adjacent runtime and People / DNA / Land package boundaries; NEEDS VERIFICATION for runtime code, routes, policies, consent records, fixtures, tests, adapters, envelopes, receipts, CI, and release behavior.

## Quick jumps

[Purpose](#purpose) · [Boundary](#boundary) · [Current inventory](#current-inventory) · [Repo fit](#repo-fit) · [Runtime responsibilities](#runtime-responsibilities) · [Deny-by-default cases](#deny-by-default-cases) · [Allowed runtime flow](#allowed-runtime-flow) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Runtime note template](#runtime-note-template) · [Validation](#validation) · [Open questions](#open-questions)

---

## Purpose

`runtime/people/` is a runtime documentation and guardrail lane for People / Genealogy / DNA / Land-adjacent runtime behavior.

Use it to document how runtime callers should handle sensitive people-oriented requests without bypassing evidence, consent, policy, review, release, correction, rollback, and finite-outcome controls.

This path may describe runtime handoffs for:

- person assertion and genealogy helper calls;
- living-person risk checks;
- consent and revocation checks;
- DNA/genomic or DNA-derived relationship request handling;
- land-ownership and title-sensitive request handling;
- public-safe summary preparation;
- governed AI / Focus Mode denial, abstention, or answer envelopes;
- runtime receipt and envelope handoff.

## Boundary

This path is not a source of truth, not a person registry, not a genealogy database, not a DNA system, not a land-title authority, not an assessor or parcel authority, not a consent authority, not a policy engine, not an EvidenceBundle store, not lifecycle data storage, not a public API, not a UI surface, and not release authority.

Runtime behavior must remain downstream of:

```text
evidence -> consent/rights/sensitivity -> policy -> validation -> review -> release -> correction/rollback
```

> [!WARNING]
> People, genealogy, DNA, living-person, residential, private-landowner, and land-title-adjacent material is high risk. Default to `DENY`, `ABSTAIN`, quarantine, redaction, generalization, or restricted review when evidence, consent, rights, sensitivity, policy, release, or correction state is unclear.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `runtime/people/README.md` | present | Empty file expanded by this README. |
| `runtime/people/*` | no files found in current search | No runtime people implementation, adapter cards, tests, fixtures, or configs confirmed under this path. |
| `runtime/README.md` | present | Runtime root describes local runtime wiring, model adapters, and service harnesses subordinate to evidence, policy, and release. |
| `runtime/AI/README.md` | present | Governed AI runtime lane; AI is interpretive and not truth/release authority. |
| `runtime/model_adapters/README.md` | present | Provider-neutral model adapter lane. |
| `runtime/envelopes/README.md` | present | Finite-outcome runtime envelope helper lane. |
| `packages/domains/people-dna-land/README.md` | present | Restricted-review domain package README for People / DNA / Land helpers. |
| `packages/domains/people-dna-land/land-ownership/README.md` | present | Title-sensitive land-ownership helper README. |

## Repo fit

```text
runtime/
├── README.md
├── people/
│   └── README.md                     # this file; sensitive runtime guardrail
├── AI/                               # governed AI runtime compatibility/index lane
├── model_adapters/                   # provider-neutral model adapter lane
├── mock/                             # deterministic mock runtime lane
├── envelopes/                        # finite-outcome envelope helper lane
├── ollama/                           # local model runtime lane
├── local/                            # local runtime wiring
└── service_configs/                  # service configuration templates

packages/domains/people-dna-land/      # reusable People / DNA / Land helpers
contracts/                            # semantic meaning
schemas/                              # machine-checkable shape
policy/                               # allow / deny / restrict / abstain posture
data/                                 # lifecycle records, registries, receipts, proofs, catalogs, emitted data
fixtures/                             # synthetic/redacted examples
tests/                                # executable proof of behavior
release/                              # release, correction, rollback authority
```

## Runtime responsibilities

| Responsibility | Requirement |
|---|---|
| Preserve sensitive scope | Mark living-person, DNA, land-title, residential, consent, rights, and cultural sensitivity risk explicitly. |
| Preserve source roles | Do not collapse administrative, archival, family, court, tax, assessor, title, survey, tribal/cultural, vendor, user-upload, or model-derived material into truth. |
| Preserve consent posture | Treat missing, revoked, stale, or unknown consent as deny/restrict unless accepted policy says otherwise. |
| Preserve evidence posture | Require EvidenceRef / EvidenceBundle support before answer-like runtime output. |
| Preserve policy posture | Require policy decision or explicit access posture before exposing or summarizing sensitive material. |
| Preserve release posture | Do not expose unpublished, unreleased, corrected, withdrawn, or stale-sensitive claims. |
| Preserve finite outcomes | Return `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`; never unbounded free text alone. |
| Preserve receipt posture | Link AIReceipt, RunReceipt, validation receipt, or RuntimeResponseEnvelope when runtime behavior is claimed. |
| Preserve privacy | Do not log or store private identifiers, DNA kit/vendor IDs, residential addresses, raw GEDCOM, private notes, secrets, or private chain-of-thought here. |

## Deny-by-default cases

| Case | Default runtime outcome | Reason |
|---|---|---|
| Living-person status is true or unknown | `DENY` or restricted review | Living-person exposure needs explicit policy, consent, review, and release support. |
| DNA/genomic or DNA-derived relationship material appears | `DENY` | Consent, revocation, vendor-origin, and privacy posture must be explicit. |
| Residential address or private-landowner detail is requested | `DENY` or generalize | Precise exposure can create privacy or safety risk. |
| Land-title or ownership truth is requested | `ABSTAIN` or `DENY` | KFM may carry evidence-bound candidates; it is not title/legal authority. |
| Source role is unclear | `ABSTAIN` | Unsupported source authority cannot support an answer. |
| Rights, consent, or release state is missing | `DENY` | Public or semi-public exposure cannot proceed without governance state. |
| EvidenceRef cannot resolve to support | `ABSTAIN` | EvidenceBundle outranks runtime language. |
| Policy state blocks or is missing for sensitive material | `DENY` | Policy controls runtime exposure. |
| Request asks for private model reasoning or hidden internals | `DENY` | Private chain-of-thought and internals are not public outputs. |
| Runtime validation or adapter execution fails | `ERROR` | Safe failure is required. |

## Allowed runtime flow

```text
People runtime request
  -> classify scope and sensitivity
  -> check living-person / DNA / land-title / residential / cultural sensitivity risk
  -> resolve evidence support
  -> check consent, rights, access role, policy, release, stale, and correction state
  -> call package helper or model adapter only if allowed
  -> validate support and citations when answer-like output is produced
  -> return finite RuntimeResponseEnvelope / DecisionEnvelope
  -> emit or link receipt where applicable
  -> caller decides next governed action
```

Runtime may prepare a public-safe answer only when evidence, consent, rights, policy, review, release, and citation requirements are satisfied. Otherwise it should return `DENY`, `ABSTAIN`, or `ERROR` with safe reason codes.

## What belongs here

- This README.
- Runtime handoff notes for People / Genealogy / DNA / Land-sensitive requests.
- Runtime denial, abstention, and safe-error notes.
- Adapter handoff notes that point to `runtime/model_adapters/`.
- Envelope handoff notes that point to `runtime/envelopes/`.
- Pointers to People / DNA / Land package helpers, policy, fixtures, tests, schemas, contracts, receipts, and release gates.
- Review notes explaining how runtime behavior remains downstream of evidence, policy, consent, review, and release state.

## What does not belong here

| Do not put this in `runtime/people/` | Correct home |
|---|---|
| Real person, genealogy, DNA, residential, parcel, landowner, title, or private data | governed `data/` lifecycle roots, usually restricted/quarantined |
| Raw GEDCOM, DNA kit/vendor IDs, segment data, private family notes, or living-person records | governed restricted data roots; not runtime docs |
| Consent records or revocation authority | accepted consent registry, policy, review-console, or governed data root |
| Source descriptors, rights registers, sensitivity registers | `data/registry/` and `policy/` roots |
| Canonical semantic contracts | `contracts/` |
| JSON Schema definitions | `schemas/` |
| Policy rules or policy decisions | `policy/` and governed review/release roots |
| Fixture payloads or golden outputs | `fixtures/` |
| Executable tests | `tests/` |
| Validator source code | `tools/validators/` |
| Package helper implementation | `packages/domains/people-dna-land/` or accepted package lane |
| Public API routes or UI components | `apps/`, `ui/`, `web/`, or accepted public-client roots |
| Release manifests, correction notices, rollback records, publication approvals | `release/` |
| Generated text treated as truth, evidence, legal/title conclusion, policy, review, release, correction, rollback, or publication authority | nowhere |

## Runtime note template

```markdown
# <people-runtime-note-id>

## Status
DRAFT / READY_FOR_REVIEW / RESTRICTED_REVIEW / ACTIVE_GUARDRAIL / VALIDATION_REQUIRED / HELD / SUPERSEDED / RETIRED

## Runtime scope
people / genealogy / DNA / land / title-sensitive / residential / mixed / N/A

## Sensitivity posture
living-person: yes/no/unknown
DNA/genomic: yes/no/unknown
residential/private-landowner: yes/no/unknown
title-sensitive: yes/no/unknown
cultural/tribal sensitivity: yes/no/unknown

## Required outcome posture
ANSWER / ABSTAIN / DENY / ERROR / N/A

## Governed support pointers
- Contract: <path or N/A>
- Schema: <path or N/A>
- Policy: <path or N/A>
- EvidenceRef / EvidenceBundle: <path or N/A>
- Consent / revocation record: <path or N/A>
- Release / correction / rollback: <path or N/A>
- RuntimeResponseEnvelope: <path or N/A>
- AIReceipt / RunReceipt: <path or N/A>
- Fixture / test / validator: <path or N/A>

## Boundary notes
<what this runtime behavior may support and what it must not expose>

## Reviewer
<steward or maintainer>

## Review date
<YYYY-MM-DD>

## Follow-up
<open items or none>
```

## Validation

```bash
find runtime/people -maxdepth 4 -type f | sort
find runtime/AI runtime/model_adapters runtime/mock runtime/envelopes -maxdepth 4 -type f 2>/dev/null | sort
find packages/domains/people-dna-land policy contracts schemas fixtures tests data release -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/runtime tests/api tests/policy tests/domains/people-dna-land || true
```

Replace `|| true` with fail-closed CI behavior once the accepted runtime and People / DNA / Land test commands are confirmed.

## Review checklist

- [ ] Runtime scope is explicitly classified.
- [ ] Living-person, DNA/genomic, residential/private-landowner, title-sensitive, and cultural sensitivity posture are explicit.
- [ ] Consent, revocation, rights, and release state are explicit or outcome is `DENY` / restricted review.
- [ ] EvidenceRef resolves to EvidenceBundle before answer-like output is allowed.
- [ ] Policy decision or access posture is linked before sensitive material is exposed.
- [ ] Runtime output uses finite outcomes.
- [ ] RuntimeResponseEnvelope / DecisionEnvelope handoff is linked when applicable.
- [ ] AIReceipt, RunReceipt, validation receipt, or other receipt posture is linked when behavior is claimed.
- [ ] No private identifiers, DNA kit/vendor IDs, residential addresses, raw GEDCOM, private notes, secrets, or private chain-of-thought are stored here.
- [ ] No generated text is treated as evidence, title/legal conclusion, policy, review, release, correction, rollback, or publication authority.

## Open questions

| Question | Status |
|---|---|
| Should `runtime/people/` remain a compatibility/index lane, or should sensitive runtime behavior live only under `runtime/AI/`, `runtime/model_adapters/`, and domain package lanes? | NEEDS VERIFICATION |
| Which policy bundle governs living-person, DNA/genomic, consent, revocation, land-title, and residential runtime requests? | NEEDS VERIFICATION |
| Which consent/revocation registry, if any, is authoritative for runtime checks? | NEEDS VERIFICATION |
| Which fixtures prove `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` behavior for People / DNA / Land runtime requests? | NEEDS VERIFICATION |
| Which CI workflow, if any, validates people-sensitive runtime deny/restrict behavior? | NEEDS VERIFICATION |
| Should any People / DNA / Land runtime path ever be public-callable, or remain review-console/restricted-only by default? | NEEDS VERIFICATION / default DENY |
