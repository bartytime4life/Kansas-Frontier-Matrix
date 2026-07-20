<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-normalize-fauna-readme
title: Fauna Shared-Normalization Adapter README
type: readme
version: v0.2
status: draft
owners:
  - <pipeline-owner>
  - <normalization-steward>
  - <fauna-domain-steward>
  - <geoprivacy-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-07-20
policy_label: public-with-fauna-normalization-geoprivacy-and-receipt-gates
path: pipelines/normalize/fauna/README.md
related:
  - docs/architecture/directory-rules.md
  - docs/doctrine/directory-rules.md
  - docs/registers/DRIFT_REGISTER.md
  - pipelines/README.md
  - pipelines/normalize/README.md
  - pipelines/domains/fauna/README.md
  - docs/domains/fauna/ARCHITECTURE.md
  - pipeline_specs/fauna/README.md
  - contracts/domains/fauna/README.md
  - schemas/contracts/v1/domains/fauna/README.md
  - policy/domains/fauna/README.md
  - policy/sensitivity/fauna/README.md
  - tests/domains/fauna/README.md
  - fixtures/domains/fauna/README.md
  - data/raw/fauna/README.md
  - data/work/fauna/README.md
  - data/quarantine/fauna/README.md
  - data/processed/fauna/README.md
  - data/receipts/pipeline/README.md
  - data/receipts/fauna/README.md
  - data/proofs/evidence_bundle/README.md
  - data/proofs/fauna/README.md
  - .github/workflows/domain-fauna.yml
tags: [kfm, pipelines, normalize, fauna, adapter, occurrence, monitoring, geoprivacy, receipt, evidence, policy, governance]
notes:
  - "v0.2 is grounded in bartytime4life/Kansas-Frontier-Matrix main@0b9307b94c67920e3451e1d40b80d287e7364ee7."
  - "The target README exists, but no executable sibling, adapter-specific test lane, fixture lane, active normalize spec, parser, or runtime consumer was verified for this path."
  - "The current path is PROPOSED / CONFLICTED as a long-term executable home: shared normalization belongs in pipelines/normalize/, while domain-owned Fauna behavior belongs in pipelines/domains/fauna/."
  - "This documentation-only revision does not move the path, activate a source or spec, create executable behavior, approve a geoprivacy transform, or authorize release."
  - "Fauna normalization must preserve source roles, knowledge character, original fields, restricted/public separation, sensitivity state, EvidenceRef candidates, and auditable transform context."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Shared-Normalization Adapter Boundary

> Documentation boundary for possible Fauna adapters around genuinely shared normalization helpers. This lane does not own Fauna domain normalization, taxonomic truth, source admission, schemas, policy, geoprivacy approval, EvidenceBundles, lifecycle promotion, catalog truth, release decisions, or publication.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![placement](https://img.shields.io/badge/placement-CONFLICTED-orange)
![implementation](https://img.shields.io/badge/implementation-NEEDS%20VERIFICATION-orange)
![sensitivity](https://img.shields.io/badge/fauna%20sensitivity-fail%20closed-d62728)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)

**Document status:** Draft documentation revision  
**Path:** `pipelines/normalize/fauna/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic, the **how**  
**Sublane posture:** `PROPOSED / CONFLICTED`; retain as a documented adapter boundary until placement is resolved  
**Implementation posture:** `NEEDS VERIFICATION`; this README does not prove an adapter, parser, consumer, test, fixture, receipt emitter, or active specification exists  
**Public posture:** no direct publication; unresolved rights, sensitivity, geoprivacy, evidence, review, or release state fails closed

> [!IMPORTANT]
> `pipelines/normalize/` is documented as shared cross-domain normalization. The parent README says behavior that belongs to only one domain belongs in that domain's pipeline lane. Directory Rules likewise place domain pipeline code under `pipelines/domains/<domain>/`. Do not add primary Fauna normalization here until an accepted placement decision distinguishes a genuinely shared adapter from domain-owned behavior.

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Fauna normalize anti-collapse rules](#3-fauna-normalize-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Adapter scope](#6-adapter-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal adapter receipt fragment](#11-minimal-adapter-receipt-fragment)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)
- [16. Evidence ledger](#16-evidence-ledger)
- [17. No-loss crosswalk](#17-no-loss-crosswalk)
- [18. Changelog](#18-changelog)

---

## 1. Purpose

`pipelines/normalize/fauna/` documents the boundary for Fauna-specific wrappers around normalization capabilities that are genuinely shared across KFM domains.

If this lane is retained, it may adapt shared behavior for:

- original-field and immutable source-reference preservation;
- explicit source-role and source-vintage carriage;
- unit, temporal, CRS, geometry, and uncertainty transform context;
- occurrence-versus-monitoring knowledge-character preservation;
- taxon crosswalk **candidate** preparation without accepting taxonomy;
- restricted/public representation separation;
- geoprivacy input preparation without approving a transform or release;
- deterministic receipt-fragment preparation for an owning Fauna caller;
- finite quarantine or hold reasons when required context is unresolved.

The owning Fauna domain pipeline remains [`pipelines/domains/fauna/`](../../domains/fauna/README.md). This lane must return control to that owner and must not become a second Fauna pipeline authority.

### Audience

This README is for pipeline maintainers, Fauna stewards, normalization-library owners, schema and contract reviewers, sensitivity/geoprivacy reviewers, test maintainers, evidence reviewers, and release reviewers deciding whether a proposed adapter belongs here.

[Back to top](#top)

---

## 2. Placement and authority

### Directory Rules basis

Directory Rules map executable pipeline logic to `pipelines/`, declarative intent to `pipeline_specs/`, and domain pipeline logic to `pipelines/domains/<domain>/`. The existing target therefore has the correct **responsibility root**, but its Fauna segment under the shared normalize lane conflicts with the documented domain-placement pattern.

| Question | Evidence-bounded answer | Status |
|---|---|---|
| Does this file exist at the requested path? | Yes; the exact target bytes were fetched at the evidence commit. | CONFIRMED |
| Is `pipelines/` the correct root for executable normalization logic? | Yes. | CONFIRMED doctrine and parent-root contract |
| Is `pipelines/normalize/` a shared normalization lane? | The parent README defines it that way. | CONFIRMED documentation |
| Is this Fauna child the accepted primary normalize home? | No accepted ADR or migration note establishing that role was verified. | UNKNOWN / NEEDS VERIFICATION |
| Where is current Fauna pipeline ownership documented? | `pipelines/domains/fauna/README.md`. | CONFIRMED documentation |
| May this lane publish or decide policy/geoprivacy? | No. Those responsibilities remain outside this directory. | CONFIRMED governance boundary |

> [!WARNING]
> The repository contains multiple Directory Rules artifacts with overlapping authority claims. [`docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md), [`docs/architecture/DIRECTORY_RULES.md`](../../../docs/architecture/DIRECTORY_RULES.md), and [`docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) remain an authority/supersession concern. Their shared placement law supports `pipelines/` for executable logic and `pipelines/domains/fauna/` for domain ownership, but the controlling Directory Rules edition still needs governance resolution.

This revision preserves the existing path and does not create, move, rename, or delete another authority surface.

[Back to top](#top)

---

## 3. Fauna normalize anti-collapse rules

The following substitutions are prohibited:

```text
adapter output -> Fauna truth
normalization success -> validation pass
source access -> source authority
taxon crosswalk candidate -> accepted taxonomic identity
monitoring event -> occurrence observation
range, model, or habitat context -> occurrence evidence
OccurrenceRestricted -> OccurrencePublic
geometry transform -> public-safe representation
geoprivacy input -> geoprivacy approval
receipt fragment -> approved receipt
receipt -> EvidenceBundle
EvidenceRef candidate -> resolved evidence
schema-valid object -> policy-allowed object
green workflow -> release readiness
generated summary -> evidence
```

Required distinctions include:

- access source, origin source, publisher, aggregator, and evidence role;
- raw/original values, normalized values, transform method, and transform result;
- taxonomic candidate, accepted taxonomy, occurrence evidence, monitoring event, range, model, aggregate, and contextual join;
- restricted occurrence and public-safe derivative;
- transform metadata, RedactionReceipt, review record, policy decision, EvidenceBundle, release decision, and public artifact;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, and PUBLISHED state.

[Back to top](#top)

---

## 4. What belongs here

Until placement is resolved, additions should be limited to documentation or narrowly scoped adapter material that meets **all** of these conditions:

1. It delegates domain meaning and lifecycle ownership to the Fauna domain pipeline.
2. It wraps a normalization capability already shared across multiple domains.
3. It preserves original fields, source refs, source roles, knowledge character, sensitivity state, and transform context.
4. It has no source-fetch, policy, validation-approval, catalog, release, or publication side effects.
5. Its placement rationale and rollback path are explicit in the pull request.
6. Its accepted tests and fixtures are identified without inventing a parallel test or fixture authority.

Examples of potentially admissible responsibilities, subject to those conditions:

- a Fauna field-binding layer for an accepted shared unit/time/geometry helper;
- a caller adapter that converts accepted Fauna contract fields to and from a shared normalizer without changing their meaning;
- a quarantine-reason mapper for lossless shared-transform failures;
- a receipt-fragment mapper that targets an accepted receipt schema and leaves final emission to the owning caller.

[Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Verified or governing responsibility home |
|---|---|
| Primary Fauna pipeline or domain-only normalizer | [`pipelines/domains/fauna/`](../../domains/fauna/README.md); an exact child normalize path remains NEEDS VERIFICATION |
| Declarative Fauna profiles | [`pipeline_specs/fauna/`](../../../pipeline_specs/fauna/README.md); no active normalize profile was verified |
| Source clients or live fetching | `connectors/<source_id>/` after source admission and rights review |
| Source descriptors or activation records | Governed source-registry/activation homes; Fauna registry topology remains conflicted |
| Fauna object meaning | [`contracts/domains/fauna/`](../../../contracts/domains/fauna/README.md) |
| Fauna machine shape | [`schemas/contracts/v1/domains/fauna/`](../../../schemas/contracts/v1/domains/fauna/README.md); schema authority remains subject to proposed ADR-0001 |
| Domain policy or sensitivity decisions | [`policy/domains/fauna/`](../../../policy/domains/fauna/README.md) and [`policy/sensitivity/fauna/`](../../../policy/sensitivity/fauna/README.md) |
| Test fixtures | [`fixtures/domains/fauna/`](../../../fixtures/domains/fauna/README.md) or another accepted fixture lane |
| Executable tests | [`tests/domains/fauna/`](../../../tests/domains/fauna/README.md) or another accepted test lane |
| RAW, WORK, QUARANTINE, or PROCESSED records | The corresponding verified Fauna lifecycle lanes under `data/` |
| Fauna process receipts | [`data/receipts/fauna/`](../../../data/receipts/fauna/README.md); exact subtype layout remains unresolved |
| Generic pipeline-run receipts | [`data/receipts/pipeline/`](../../../data/receipts/pipeline/README.md) |
| EvidenceBundle or Fauna proof objects | [`data/proofs/evidence_bundle/`](../../../data/proofs/evidence_bundle/README.md) and [`data/proofs/fauna/`](../../../data/proofs/fauna/README.md) |
| Release decisions, corrections, or rollback cards | `release/` authority surfaces |
| Public API, UI, map, tile, export, or AI-serving code | Governed application/package surfaces; never this adapter lane |
| Sensitive real-world coordinates or reconstructable examples | Restricted governed stores only, with least privilege and review |

[Back to top](#top)

---

## 6. Adapter scope

The table below is a **PROPOSED contract for any future implementation**, not evidence that one exists.

| Concern | Adapter responsibility | Fail-closed result |
|---|---|---|
| Caller | Require an accepted Fauna pipeline or proof harness scope. | `HOLD` or `ERROR` when ownership is unresolved. |
| Original fields | Preserve raw labels, values, payload refs, and hashes. | `FAIL`/QUARANTINE on lossy transformation. |
| Source role | Carry provided roles; never invent authority. | `HOLD` on ambiguity; no best-effort upgrade. |
| Knowledge character | Keep observation, monitoring, range, model, aggregate, and context distinct. | `FAIL` on collapse. |
| Taxonomy | Prepare a crosswalk candidate with authority/version/ambiguity context. | `HOLD`; never auto-accept taxonomy. |
| Time and space | Preserve distinct time kinds, CRS, precision, uncertainty, and transform method. | `HOLD` or QUARANTINE when context is incomplete. |
| Restricted/public split | Keep restricted records separate from public-safe derivatives. | `DENY` public routing by default. |
| Geoprivacy | Prepare inputs and method refs only. | `HOLD` pending policy, transform, receipt, and review. |
| Evidence | Carry EvidenceRef candidates without fabricating resolution. | `ABSTAIN` downstream when evidence cannot resolve. |
| Receipts | Prepare deterministic fragments against an accepted schema. | `ERROR` or `HOLD` if schema/emitter/hashes are unresolved. |
| Handoff | Return candidate fragments and blockers to the owning caller. | No validation, catalog, release, or publication side effects. |

[Back to top](#top)

---

## 7. Lifecycle contract

Every future adapter must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal bounded flow:

1. The owning caller supplies stable refs to an approved fixture, RAW capture, WORK candidate, or explicitly authorized QUARANTINE remediation input.
2. The adapter performs only the accepted shared transformation and preserves original fields, roles, identity context, time/space context, sensitivity state, evidence refs, and method metadata.
3. The adapter returns a WORK fragment, QUARANTINE reason, and/or receipt candidate to the caller.
4. The Fauna domain lane owns validation and any later governed transition.
5. Evidence, policy, review, catalog/triplet, release, correction, and rollback remain separate closures.

A file move, successful transform, receipt, passing check, commit, pull request, or merge is not promotion or publication.

[Back to top](#top)

---

## 8. Required gates

Any future executable adapter must close or explicitly fail on:

1. **Placement gate** — the file belongs in this lane rather than the domain lane.
2. **Caller gate** — an accepted owner and bounded execution scope are present.
3. **Input-state gate** — lifecycle state and immutable input refs are allowed.
4. **Source gate** — stable source identity, origin/access roles, rights, and activation state resolve.
5. **Original-field gate** — source material remains recoverable and hash-linked.
6. **Knowledge-character gate** — observation, monitoring, range, model, aggregate, and context do not collapse.
7. **Taxonomy gate** — authority, version, crosswalk, and ambiguity state remain explicit.
8. **Temporal/spatial gate** — relevant time kinds, CRS, uncertainty, precision, and method are explicit.
9. **Sensitivity/geoprivacy gate** — exact or reconstructable detail fails closed; public-safe status is not inferred.
10. **Contract/schema gate** — accepted meaning and machine shape resolve without creating local authority.
11. **Evidence gate** — EvidenceRefs remain unresolved until an EvidenceBundle resolver closes them.
12. **Policy/review gate** — missing decisions remain missing and block higher-risk exposure.
13. **Receipt gate** — accepted receipt family, deterministic identity, inputs, transforms, hashes, outputs, and outcome are available.
14. **No-side-effect gates** — no direct validation approval, catalog/triplet write, release decision, public API/UI write, deployment, or publication.

[Back to top](#top)

---

## 9. Directory contract

### Current verified boundary

The target README was fetched directly at the evidence commit:

```text
pipelines/normalize/fauna/README.md
```

This file read does **not** establish an exhaustive sibling inventory. No executable adapter, adapter contract, active spec, adapter-specific fixture lane, adapter-specific test lane, parser, consumer, or receipt emitter was verified for this path during the revision.

### Expansion rule

Do not use the v0.1 candidate tree as proof that proposed files exist or belong here. Before adding an executable file:

1. resolve the shared-versus-domain placement question;
2. inspect accepted ADRs and the drift register;
3. identify the owning contract, schema, policy, spec, test, fixture, receipt, and caller;
4. prove no parallel authority is created;
5. use a focused branch and document rollback;
6. update this README from future-state language to exact implementation evidence.

Generated outputs must never be written beside adapter code.

[Back to top](#top)

---

## 10. Inputs and outputs

| Class | Governing home or boundary | Adapter posture |
|---|---|---|
| Fauna fixtures | [`fixtures/domains/fauna/`](../../../fixtures/domains/fauna/README.md) or another accepted fixture lane | Synthetic, generalized, redacted, public-safe, deterministic, and no-network by default. |
| Declarative intent | [`pipeline_specs/fauna/`](../../../pipeline_specs/fauna/README.md) | Current `refresh.yaml` is documented there as a placeholder, not an active normalize spec. |
| RAW input | [`data/raw/fauna/`](../../../data/raw/fauna/README.md) | Read only through stable caller-provided refs; never fetch live here. |
| WORK input/output | [`data/work/fauna/`](../../../data/work/fauna/README.md) | Candidate-only and non-public. |
| QUARANTINE reason/input | [`data/quarantine/fauna/`](../../../data/quarantine/fauna/README.md) | Remediation requires explicit scope; unresolved material stays held. |
| PROCESSED state | [`data/processed/fauna/`](../../../data/processed/fauna/README.md) | Not written or approved by this adapter. |
| Fauna receipt | [`data/receipts/fauna/`](../../../data/receipts/fauna/README.md) | Domain process memory; exact adapter subtype remains NEEDS VERIFICATION. |
| Pipeline receipt | [`data/receipts/pipeline/`](../../../data/receipts/pipeline/README.md) | Generic run/process memory; not proof or release. |
| Evidence/proof | [`data/proofs/evidence_bundle/`](../../../data/proofs/evidence_bundle/README.md), [`data/proofs/fauna/`](../../../data/proofs/fauna/README.md) | Referenced only; not fabricated or approved here. |
| Release handoff | `release/candidates/fauna/` | Owned by release workflow; candidate is not release. |

[Back to top](#top)

---

## 11. Minimal adapter receipt fragment

No accepted Fauna adapter-receipt schema was verified. The following YAML is **illustrative, non-canonical, inactive, and not valid production input**. It shows information that an eventual accepted receipt family should preserve without asserting field names or paths as repository contracts.

```yaml
# ILLUSTRATIVE ONLY — no accepted schema or emitter was verified.
receipt_family_candidate: fauna_shared_normalize_adapter
outcome: HOLD
caller:
  pipeline_ref: <accepted-fauna-pipeline-ref>
  adapter_ref: <versioned-adapter-ref>
inputs:
  lifecycle_refs: []
  source_descriptor_refs: []
  payload_hashes: []
  source_roles: []
transforms:
  method_refs: []
  original_fields_preserved: false
  knowledge_character_preserved: false
  taxonomy_candidate_only: true
  restricted_public_split_preserved: false
  geoprivacy_approval_claimed: false
checks:
  rights_resolved: false
  sensitivity_state_preserved: false
  evidence_refs_carried_forward: false
  policy_state_preserved: false
outputs:
  work_candidate_refs: []
  quarantine_reason_refs: []
failure:
  reason_code: ACCEPTED_VOCABULARY_UNRESOLVED
rollback:
  target_ref: <required-before-activation>
```

Receipt presence records process memory. It does not prove evidence closure, policy approval, geoprivacy safety, review approval, release, or publication.

[Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

### Current evidence

- [`tests/domains/fauna/README.md`](../../../tests/domains/fauna/README.md) is a documented scaffold boundary.
- [`fixtures/domains/fauna/README.md`](../../../fixtures/domains/fauna/README.md) documents public-safe fixture lanes.
- Adapter-specific `tests/pipelines/normalize/fauna/README.md` and `fixtures/normalize/fauna/README.md` were not found by direct path reads at the evidence commit.
- [`domain-fauna.yml`](../../../.github/workflows/domain-fauna.yml) is an explicit readiness/hold workflow. It does not run an accepted Fauna validation, proof, or release-dry-run producer.
- No repository-native command for this adapter was verified; therefore this README does not publish a runnable command.

### Minimum future test matrix

| Case | Required observation |
|---|---|
| Deterministic valid fixture | Same accepted inputs and versions produce the same bounded fragment and hashes. |
| Invalid/lossy transform | Fails or quarantines; original values remain recoverable. |
| Missing caller | `HOLD`/`ERROR`; no ownerless execution. |
| Missing/ambiguous source role | Holds; no authority inference. |
| Taxonomic ambiguity | Remains a candidate; no accepted identity claim. |
| Knowledge-character mismatch | Fails when range/model/context/monitoring would become occurrence evidence. |
| Restricted-to-public route | `DENY`; no exact or reconstructable exposure. |
| Missing geoprivacy review | Holds; transform input is not approval. |
| Missing EvidenceBundle | Downstream claim path abstains. |
| Missing receipt schema/emitter | Holds or errors; no invented local receipt authority. |
| Network access in default tests | Fails; default fixtures are no-network. |
| Side-effect attempt | Fails on catalog, triplet, release, published-data, public API/UI, deploy, or publication write. |

A passing adapter suite would prove only the exercised adapter contract. It would not prove source authority, taxonomic truth, complete Fauna pipeline behavior, production safety, EvidenceBundle closure, geoprivacy approval, policy approval, release readiness, or publication.

[Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

If implemented, this lane may emit candidate fragments, blockers, and receipt context to its owning caller. It must not promote or publish.

```text
accepted caller scope
  -> shared helper plus Fauna adapter
  -> WORK candidate or QUARANTINE reason plus receipt context
  -> Fauna-domain validation
  -> evidence, rights, sensitivity, geoprivacy, policy, and review closure
  -> processed/catalog/triplet handoff
  -> independent release decision and rollback target
  -> public-safe artifact
```

Correction and rollback requirements:

- preserve failed-run and supersession lineage;
- never overwrite original inputs or hide failed transforms;
- invalidate downstream derivatives when source, taxonomy, transform, evidence, sensitivity, policy, review, or release state changes materially;
- keep correction notices, rollback cards, release manifests, receipts, and proofs as separate object families;
- before merge, rollback this documentation change by closing the draft pull request or reverting the scoped commit after merge;
- never rewrite shared history as rollback.

[Back to top](#top)

---

## 14. Definition of done

### This README revision

This documentation revision is complete when:

- the exact existing path and responsibility root are stated;
- the shared-versus-domain placement conflict is visible rather than normalized away;
- current repository evidence is separated from proposed future behavior;
- nonexistent or unverified filenames are not presented as a directory plan;
- verified Fauna spec, contract, schema, policy, lifecycle, receipt, proof, test, fixture, and workflow boundaries are linked accurately;
- source-role, taxonomy, knowledge-character, sensitivity, geoprivacy, evidence, lifecycle, release, correction, and rollback controls are preserved;
- links, anchors, Markdown structure, line endings, and the final newline pass review;
- the remote branch and draft pull request contain only this README change.

### Future executable adapter

An executable adapter is not done until placement, ownership, accepted contracts/schemas/specs, deterministic identity, parser/consumer binding, public-safe fixtures, no-network positive and negative tests, source/rights/sensitivity gates, receipt emission, EvidenceRef handling, policy/review handoff, CI wiring, correction, deactivation, and rollback all close.

[Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-NORM-FAUNA-001` | Should this path remain a thin adapter boundary, migrate under `pipelines/domains/fauna/`, or be retired after callers use shared helpers directly? | NEEDS VERIFICATION / ADR or migration decision |
| `PIPE-NORM-FAUNA-002` | Which Directory Rules artifact controls placement and supersedes the duplicate copies? | CONFLICTED / NEEDS VERIFICATION |
| `PIPE-NORM-FAUNA-003` | Does any executable sibling or runtime consumer currently use this path? | UNKNOWN |
| `PIPE-NORM-FAUNA-004` | Which accepted schema and emitter own Fauna adapter or normalization receipts? | NEEDS VERIFICATION |
| `PIPE-NORM-FAUNA-005` | Which accepted test and fixture lanes own adapter-specific cases? | NEEDS VERIFICATION |
| `PIPE-NORM-FAUNA-006` | Which shared normalization helpers are actually implemented and stable enough to adapt? | UNKNOWN |
| `PIPE-NORM-FAUNA-007` | How will the documented Fauna source-registry topology conflict be resolved? | NEEDS VERIFICATION / ADR |
| `PIPE-NORM-FAUNA-008` | Which taxonomy authority, crosswalk vocabulary, knowledge-character vocabulary, sensitivity vocabulary, and geoprivacy transform profiles are accepted? | NEEDS VERIFICATION |
| `PIPE-NORM-FAUNA-009` | Which maintainers own this path and which independent reviews are required? | OWNER_TBD / NEEDS VERIFICATION |
| `PIPE-NORM-FAUNA-010` | Which CI job will run substantive adapter tests after implementation, without converting a readiness hold into proof? | UNKNOWN |

[Back to top](#top)

---

## 16. Evidence ledger

Evidence snapshot: `bartytime4life/Kansas-Frontier-Matrix` at `main@0b9307b94c67920e3451e1d40b80d287e7364ee7`, inspected through authenticated GitHub file reads on 2026-07-20.

| Evidence | Observation used here | Limit |
|---|---|---|
| This README, parent normalize README, and pipelines root README | Existing path; `pipelines/` owns executable logic; `pipelines/normalize/` describes shared helpers. | Documentation does not prove executable implementation. |
| Directory Rules copies and drift register | Executable logic belongs under `pipelines/`; domain logic follows a responsibility-root domain lane; authority copies conflict. | No accepted ADR resolving the duplicate Directory Rules authority was verified. |
| `pipelines/domains/fauna/README.md` | Documents the primary Fauna executable boundary and fail-closed gates. | Concrete pipeline behavior remains unverified. |
| `pipeline_specs/fauna/README.md` | Declarative Fauna boundary; current refresh profile is documented as a placeholder. | No active normalize spec, parser, consumer, or activation record was verified. |
| Fauna contract/schema/policy READMEs | Separate meaning, machine shape, and admissibility homes exist. | Schema ADR is proposed; policy lanes include scaffold content. |
| Fauna RAW/WORK/QUARANTINE/PROCESSED READMEs | Lifecycle boundaries exist and deny public-path shortcuts. | README presence does not prove stored data, promotion, or runtime behavior. |
| `data/receipts/pipeline/README.md` and `data/receipts/fauna/README.md` | Generic pipeline and Fauna receipt parents exist. | Exact adapter subtype and schema remain unresolved. |
| `data/proofs/evidence_bundle/README.md` and `data/proofs/fauna/README.md` | EvidenceBundle and Fauna proof boundaries exist. | No proof inventory or resolver execution was established. |
| Fauna test/fixture READMEs | Domain test and public-safe fixture documentation exists. | Adapter-specific executable tests and fixtures were not verified. |
| `.github/workflows/domain-fauna.yml` | Read-only, hosted-runner readiness workflow with explicit holds. | A green held run would not prove substantive validation, evidence, release, or publication. |
| `.github/CODEOWNERS` | `/pipelines/` currently routes to `@bartytime4life`. | Independent review and branch-protection enforcement remain NEEDS VERIFICATION. |

### Current-session evidence limit

This README does not claim exhaustive directory inventory, branch-protection state, accepted owners, active sources/specs, successful adapter tests, runtime deployment, production data, current external rights, geoprivacy approval, EvidenceBundle closure, release state, or publication.

[Back to top](#top)

---

## 17. No-loss crosswalk

| v0.1 concern | v0.2 treatment |
|---|---|
| Adapter-only, not primary Fauna authority | Preserved and strengthened with the placement conflict. |
| Source-role and original-field preservation | Preserved. |
| Occurrence, monitoring, range, and taxonomy anti-collapse | Preserved and expanded to explicit knowledge character. |
| Restricted/public and geoprivacy boundaries | Preserved with reconstruction-risk and review language. |
| EvidenceRef/EvidenceBundle separation | Preserved. |
| Receipt, policy, review, lifecycle, release, correction, and rollback separation | Preserved and grounded in verified parent READMEs. |
| Candidate directory and test trees | Replaced because proposed filenames and homes were not verified. |
| Minimal receipt example | Retained only as an explicitly non-canonical field-group illustration. |
| Open questions | Preserved and updated from current repository evidence. |

No strong v0.1 trust, sensitivity, provenance, or non-publication control was intentionally removed.

[Back to top](#top)

---

## 18. Changelog

### v0.2 — 2026-07-20

- Grounded the README in the pinned remote repository state.
- Marked the shared-versus-domain placement conflict explicitly.
- Removed the unverified candidate implementation and test trees.
- Replaced the nonexistent `pipeline_specs/normalize/fauna.yaml` reference with the verified Fauna spec boundary.
- Corrected receipt references to verified generic-pipeline and Fauna receipt parents without inventing a subtype.
- Added repository-grounded test, fixture, workflow, authority, evidence, and no-loss boundaries.
- Preserved fail-closed sensitivity, geoprivacy, source-role, evidence, release, correction, and rollback controls.

### v0.1 — 2026-06-13

- Established the initial Fauna shared-normalization adapter boundary and future-state governance controls.

---

## Maintainer note

Do not solve the placement conflict by silently growing this directory. First prove that the proposed code adapts a capability shared across domains and does not own Fauna meaning or lifecycle behavior. If it is domain-only, place it with the accepted Fauna domain pipeline. In either case, keep exact/reconstructable fauna locations fail-closed, preserve source and knowledge character, require deterministic receipts and no-network tests, and leave evidence, policy, review, release, correction, and publication to their governing authorities.

[Back to top](#top)
