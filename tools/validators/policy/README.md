<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-policy-readme
title: tools/validators/policy README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-policy-steward-plus-schema-steward-plus-contract-steward-plus-evidence-steward-plus-release-steward-plus-runtime-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; policy-validator-index; policy-decision-aware; policy-input-bundle-aware; sensitivity-aware; allow-deny-restrict-hold-abstain; fail-closed; release-gated; non-authoritative
owning_root: tools/
responsibility: parent policy validator routing README under tools/validators; indexes policy-validation expectations for policy input bundles, policy decision records, sensitivity labels, policy bundle references, finite outcomes, obligations, reason codes, evidence context, lifecycle context, release/correction/rollback posture, fixture/schema/test routing, and public-surface denial while deferring policy rule authority, canonical schemas, semantic contracts, evidence records, receipts, lifecycle data, public runtime code, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../evidence/README.md
  - ../lifecycle/README.md
  - ../maplibre/README.md
  - ../joins/README.md
  - ../geoprivacy/README.md
  - ../citation/README.md
  - ../../packages/policy-runtime/README.md
  - ../../packages/policy-runtime/src/README.md
  - ../../schemas/contracts/v1/policy/README.md
  - ../../contracts/policy/
  - ../../policy/
  - ../../fixtures/contracts/v1/policy/policy_decision/README.md
  - ../../data/proofs/
  - ../../data/receipts/
  - ../../release/
  - ../../tests/
notes:
  - "This README replaces an empty placeholder at tools/validators/policy/README.md. It does not confirm executable policy validators, registry wiring, policy bundles, or CI behavior."
  - "Directory responsibility split: policy rules and policy authority belong in policy/; schemas belong in schemas/; semantic meaning belongs in contracts/; receipts/proofs belong in data/receipts and data/proofs; release authority belongs in release/."
  - "packages/policy-runtime/ is an executor/helper package for approved policy inputs and finite decision carriers; it is not policy authority."
  - "schemas/contracts/v1/policy/ defines policy object shape only; schema-valid PolicyDecision records do not prove the right policy ran, the inputs were complete, sensitivity was correct, or release is allowed."
  - "Validators may check policy references, input shape, policy-decision shape, bundle identity/digest, reason codes, obligations, and release readiness; they do not decide policy, approve release, redact data, downgrade sensitivity, or publish outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/policy

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-policy--validator--index-informational)
![authority](https://img.shields.io/badge/authority-validator--not--policy--root-lightgrey)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/policy/` is the parent policy validator routing index for checking policy input, policy decision, sensitivity, obligations, bundle identity, evidence context, lifecycle state, release readiness, correction/rollback posture, and public-surface denial without becoming the policy rule root, policy runtime package, schema home, receipt store, proof store, or release authority.

---

## Purpose

`tools/validators/policy/` exists to organize policy-facing validation under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a candidate carry the policy inputs, policy bundle reference, decision record shape, finite outcome, reason codes, obligations, sensitivity posture, evidence context, lifecycle state, review state, release reference, correction path, rollback target, and public-surface limits required before it can proceed through a governed KFM step?

The answer should be a deterministic validation result or routing decision. This folder should not author policy rules, execute policy as authority, define policy object meaning, define machine schemas, write receipts, write proofs, store lifecycle data, approve release, redact or generalize data as authority, downgrade sensitivity, expose public routes, render UI, or generate truth claims.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/policy/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `packages/policy-runtime/README.md` | **CONFIRMED README / implementation NEEDS VERIFICATION** | Documents policy-runtime as helper/executor code for approved policy bundles and finite decision carriers, not policy authority. |
| `schemas/contracts/v1/policy/README.md` | **CONFIRMED README / mixed schema maturity** | Defines policy object shapes only and states schema-valid PolicyDecision records do not prove policy evaluation, correct inputs, sensitivity, or release allowance. |
| `fixtures/contracts/v1/policy/policy_decision/README.md` | **CONFIRMED README / fixture behavior NEEDS VERIFICATION** | PolicyDecision fixtures are schema fixtures only, not executable policy, policy approval, release approval, evidence, receipts, proofs, or semantic authority. |
| `tools/validators/hydro/policy/README.md` | **CONFIRMED example README** | Validator-local policy folder is routing guidance and not policy authority; confirms the placement pattern used here. |
| Executable policy validator scripts, registry wiring, policy bundles, bundle digests, schema bindings, fixture coverage, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Placement decision

`tools/validators/policy/` is a **validator routing index**, not the policy authority root.

| Responsibility | Preferred root | Validator relationship |
|---|---|---|
| Policy rules, bundles, allow/deny/restrict/hold/abstain posture, and policy-operation documentation | `policy/` | Validators reference accepted policy bundle ids, versions, digests, and outcomes. |
| Policy runtime helper code | `packages/policy-runtime/` | Runtime helpers may execute approved bundles; validators can check outputs and metadata. |
| Policy object machine shape | `schemas/contracts/v1/policy/` | Validators check schema conformance; schemas do not prove policy evaluation. |
| Policy semantic meaning | `contracts/policy/` | Validators check conformance to contracts; they do not define meaning. |
| Policy fixtures | `fixtures/contracts/v1/policy/` and accepted fixture homes | Fixtures prove shape or behavior only when tests verify them. |
| Policy tests | `tests/` and accepted test homes | Tests prove validators and policy-runtime behavior. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Validators may emit reports or receipt-ready metadata only to accepted homes. |
| Release decisions and rollback | `release/` | Validator success is not release approval. |

Validators may fail closed when required policy support is absent, stale, contradictory, unsupported, or unresolved. They must not silently substitute generated language, UI state, map state, file path presence, or schema validity for policy authority.

[Back to top](#top)

---

## Validator focus

Policy validators routed through this folder should check:

- required `PolicyInputBundle` shape, schema id, version, and input hash;
- policy bundle id, bundle version, bundle digest, evaluator profile, and freshness/stale-state posture;
- explicit operation, audience, lifecycle phase, release state, object refs, domain refs, source refs, source roles, rights posture, sensitivity posture, and intended public surface;
- required EvidenceRef, EvidenceBundle resolver status, citation-validation status, and evidence-closure posture where the policy depends on evidence;
- finite decision outcome such as `ALLOW`, `DENY`, `RESTRICT`, `HOLD`, `ABSTAIN`, or `ERROR`;
- reason codes, obligations, redaction/generalization instructions, review flags, correction paths, rollback targets, and expiration/reevaluation requirements;
- most-restrictive policy propagation across joins, maps, exports, screenshots, Focus Mode, AI answers, and public clients;
- missing, stale, contradictory, or unsupported policy context as deny/restrict/hold/abstain rather than best-effort publication;
- report output placement so generated validation outputs do not become policy decisions or release records by accident.

[Back to top](#top)

---

## Fail-closed conditions

A policy candidate should fail closed, deny, restrict, hold, abstain, or route to steward review when:

- policy input bundle is missing, malformed, stale, ambiguous, or lacks required object/source/lifecycle/evidence context;
- accepted policy bundle id, version, digest, evaluator profile, or rule family is missing or unsupported;
- policy evaluator output is missing, non-finite, contradictory, non-replayable, or lacks reason codes/obligations required for the decision;
- sensitivity posture is unknown, contradicted, downgraded, or unsupported;
- rights, license, consent, living-person, DNA/genomic, archaeology, rare-species, infrastructure, cultural/tribal, private parcel/person, precise-location, or source-role risk is unresolved;
- release, correction, withdrawal, rollback, supersession, expiration, or reevaluation references are required but absent;
- schema validity, fixture pass status, policy-runtime success, or validator success is treated as policy authority, evidence closure, release approval, or public-safety proof;
- public surfaces would expose unreleased, restricted, denied, stale, sensitive, private, or unsupported content;
- AI, UI, map, source descriptor, file path, generated text, operator memory, or runtime state is used to invent or imply policy approval.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Policy validator parent index | `tools/validators/policy/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Policy runtime helper code | `packages/policy-runtime/` |
| Policy rules and bundles | `policy/` |
| Policy semantic contracts | `contracts/policy/` |
| Policy machine schemas | `schemas/contracts/v1/policy/` |
| Policy fixtures | `fixtures/contracts/v1/policy/` or accepted fixture homes |
| Policy tests | `tests/` or accepted test homes |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/published/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Public API, UI, map, export, graph, Focus Mode, and AI runtime | governed application/runtime roots |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared policy validation invariants and delegates policy rules, policy execution authority, schemas, contracts, evidence, receipts, lifecycle data, and release authority to owning roots.
- **NEEDS VERIFICATION:** exact executable files, registry entries, policy bundle homes, policy bundle digests, schema ids, schema digests, fixture files, test paths, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as policy rule authority, policy bundle store, policy runtime package, canonical schema home, semantic contract home, lifecycle data store, proof store, receipt store, release record store, public runtime surface, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/policy/` include:

- this parent README;
- small policy validation adapters that check policy input/output shape and references;
- checks that accepted policy bundles, versions, and digests are explicitly referenced;
- checks that policy decisions carry finite outcomes, reason codes, obligations, sensitivity posture, review flags, and reevaluation/correction/rollback posture;
- checks that public-bound candidates do not proceed without policy and release support;
- routing notes for domain-specific validator-local policy subfolders;
- test planning notes that route generated outputs to accepted report/proof/receipt/artifact roots.

[Back to top](#top)

---

## What does not belong here

| Do not put in this folder | Correct home |
|---|---|
| Policy source rules, Rego files, policy bundles as governance artifacts, allowlists, denylists, thresholds, steward decisions | `policy/` |
| Policy runtime implementation package code | `packages/policy-runtime/` |
| Canonical JSON Schemas, DTOs, enums, or machine shape | `schemas/contracts/v1/policy/` or accepted schema homes |
| Semantic contracts | `contracts/policy/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Source descriptors or source registries | `data/registry/`, `data/registry/sources/` |
| EvidenceBundles, proof packs, receipts, ValidationReports | `data/proofs/`, `data/receipts/`, accepted report lanes |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawals | `release/` |
| Tests and fixtures | `tests/` and `fixtures/` conventions |
| Public API, UI, MapLibre runtime code, tile service code, Focus Mode, export, screenshot, graph, embedding, or AI runtime code | governed application/runtime roots |
| Secrets, source credentials, private source content, sensitive exact locations, hidden thresholds, production policy keys, or reconstruction hints | denied here; keep out of repository-facing validator docs |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `POLICY_VALIDATOR_PASS` | Candidate passed configured policy validation checks. |
| `POLICY_VALIDATOR_FAIL` | Candidate failed one or more configured checks. |
| `POLICY_VALIDATOR_DENY` | Candidate is denied because policy, rights, sensitivity, evidence, release, correction, rollback, or public-surface support cannot be resolved. |
| `POLICY_VALIDATOR_RESTRICT` | Candidate may proceed only in restricted/steward-gated contexts. |
| `POLICY_VALIDATOR_HOLD` | Candidate must remain held pending review, evidence, rights, or policy closure. |
| `POLICY_VALIDATOR_ABSTAIN` | Candidate lacks enough support for a policy assertion. |
| `POLICY_INPUT_BUNDLE_MISSING` | Required policy input bundle is absent. |
| `POLICY_INPUT_BUNDLE_INVALID` | Policy input bundle fails accepted schema/contract checks. |
| `POLICY_BUNDLE_REF_MISSING` | Policy bundle id, version, digest, or evaluator profile is absent. |
| `POLICY_BUNDLE_STALE_OR_UNSUPPORTED` | Referenced policy bundle is stale, unsupported, contradicted, or not accepted. |
| `POLICY_DECISION_MISSING` | Required PolicyDecision-like result is absent. |
| `POLICY_DECISION_INVALID` | PolicyDecision-like result fails accepted schema/contract checks. |
| `POLICY_DECISION_OVERCLAIM` | Schema-valid decision is treated as proof that the right policy ran or release is allowed. |
| `POLICY_REASON_CODES_MISSING` | Required reason codes are absent. |
| `POLICY_OBLIGATIONS_MISSING` | Required obligations, redaction/generalization instructions, or review flags are absent. |
| `SENSITIVITY_POSTURE_UNRESOLVED` | Sensitivity, rights, consent, living-person, DNA/genomic, archaeology, rare-species, infrastructure, cultural/tribal, precise-location, or private-person/parcel risk is unresolved. |
| `EVIDENCE_CONTEXT_MISSING` | Required evidence or citation-validation context is absent. |
| `RELEASE_REFERENCE_MISSING` | Required release, correction, rollback, withdrawal, or reevaluation reference is absent. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Candidate would expose unsafe or unreleased content to public API, map, tile, export, screenshot, graph, Focus Mode, embedding, or AI surfaces. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, evaluator error, timeout, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/validators/policy/
├── README.md
├── validate_policy_input_bundle.py      # PROPOSED; not confirmed
├── validate_policy_decision.py          # PROPOSED; not confirmed here
├── validate_policy_binding.py           # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

Do not add executable validators, policy bundles, local schema files, or fixtures unless the placement decision is documented, the canonical authority relationship is explicit, and tests prove fail-closed behavior without granting policy or release authority.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty placeholder at `tools/validators/policy/README.md`.
- [x] It marks this path as policy validator routing, not policy rule, policy runtime, schema, contract, proof, receipt, release, public runtime, or AI authority.
- [x] It routes policy rules to `policy/`, runtime helpers to `packages/policy-runtime/`, schemas to `schemas/contracts/v1/policy/`, contracts to `contracts/policy/`, fixtures to `fixtures/`, tests to `tests/`, receipts/proofs to `data/`, and release records to `release/`.
- [x] It preserves fail-closed posture for missing policy inputs, unsupported bundles, stale policy, unresolved sensitivity, missing evidence, missing release references, public-surface leakage, and overclaiming schema/runtime success.
- [x] It distinguishes policy validation from policy decision authority, evidence closure, release approval, redaction authority, and publication approval.
- [x] It marks executable scripts, registry wiring, policy bundle homes, schema files, fixtures, tests, receipt emission, release integration, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to policy validators are searched and classified.
- [ ] Policy bundle homes, accepted bundle ids, versions, and digest rules are verified.
- [ ] Canonical schema and contract homes for PolicyInputBundle, PolicyDecision, SensitivityLabel, obligations, reason codes, and redaction/generalization outputs are verified.
- [ ] Fixture files are added only as synthetic/minimized public-safe payloads with documented expected outcomes.
- [ ] Tests prove positive and negative policy cases pass/fail for the intended reason.
- [ ] CI invokes the relevant policy validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with policy validator parent README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
