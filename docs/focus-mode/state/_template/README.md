<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/focus-mode/state/template-boundary
title: State Focus Mode Template Boundary
type: readme; boundary-compact; authoring-template-lane
version: v0.1.0
status: draft; repository-grounded; current-path; non-authoritative; non-release; non-publication
owners:
  - "@bartytime4life — verified CODEOWNERS review route; not specialist stewardship, independent review, release approval, or publication authority"
created: 2026-08-22
updated: 2026-08-22
policy_label: public; documentation; focus-mode; state-template; fail-closed
owning_root: docs/
responsibility: >-
  Explain this state Focus Mode template directory, constrain use of the sibling
  scaffold, and expose the authority, validation, migration, and rollback
  boundaries that apply before a copy can advance beyond human planning.
current_path: docs/focus-mode/state/_template/README.md
base_commit: c3f85604a8792e6147e2006256019926880cb3ef
prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
canonical_relationship: >-
  Same-path PLACE inside the tracked singular Focus compatibility lane. Final
  state identity, destination, state-tree split, alias, and migration remain
  HOLD because ADR-0028 is proposed and consumer-safe migration is unproved.
truth_posture: >-
  CONFIRMED blank prior target, two-child tree, sibling template, accepted
  Directory Rules v2, proposed ADR-0028, current state index, semantic payload
  contract, county-only index validator, validator-registry omission, and four
  runtime outcomes / PROPOSED this authoring boundary / CONFLICTED template,
  validator, schema, and path claims / UNKNOWN evidence, policy, review, release,
  correction, rollback, deployment, and public parity.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: c3f85604a8792e6147e2006256019926880cb3ef
  target_prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  sibling_template_blob: e7d2f2542ddcfee416c4d3fd709e972ff193d446
  adr_0028_blob: d14ea2b4ad57294ab52da643c954a7f83d5e24e9
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  focus_index_validator_blob: 89391d75680e859dddf3696b9b782369f364c73e
  validator_registry_blob: 86aeadabe7104114c3f1efe60a8708ec11563bb1
inspection_boundary: >-
  Current GitHub reads covered this directory, sibling and parent docs, the state
  index, ADRs, Directory Rules, Focus contract/schema-family docs, validator,
  registry, CODEOWNERS, open PRs, and branches. No live source, resolver, policy
  engine, payload, API, map, release, correction cascade, or rollback drill ran.
related:
  - ../README.md
  - ../STATE_INDEX.md
  - ./state-build-plan.md
  - ../../../doctrine/directory-rules.md
  - "../../../adr/ADR-0028 — State-scale Focus Mode scope.md"
  - ../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../../contracts/focus_mode/focus_mode_payload.md
  - ../../../../schemas/contracts/v1/focus/README.md
  - ../../../../tools/validators/validate_focus_mode_index.py
  - ../../../../tools/validators/validator_registry.json
  - ../../../../.github/CODEOWNERS
tags: [kfm, focus-mode, state, template, boundary-compact, validation, migration, rollback]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# State Focus Mode Template Boundary

> **Purpose.** This directory contains reusable human authoring guidance for a proposed state-scale Focus composition. It does not register a state scope, define machine shape, admit evidence, decide policy, release data, or publish a Kansas-wide product.

> [!IMPORTANT]
> A copied or completed plan remains documentation until scope identity, evidence, rights, sensitivity, machine shape, policy, validation, accountable review, release, correction, and rollback obligations close through their owning responsibility roots.

> [!CAUTION]
> ADR-0028 remains **proposed**. It does not register `kansas-state`, authorize a destination lane, accept the mixed state tree, or permit structural migration.

> [!WARNING]
> The current Focus index validator is county-focused: it permits `county`, `region`, and `corridor`, expects a different plural-tree grammar, and is absent from the validator registry. The sibling template's state-extension language is planning lineage, not current validator support.

**Navigation:** [Status](#status-and-placement) · [Map](#current-map) · [Authority](#authority-and-non-effects) · [Authoring](#authoring-contract) · [Validation](#validation) · [Lifecycle](#exposure-mutation-and-retention) · [Rollback](#migration-correction-and-rollback) · [Open work](#open-verification-backlog) · [References](#related-surfaces)

---

## Status and placement

This page replaces a one-byte blank placeholder at the same tracked path.

| Surface | Current evidence | Bounded result |
|---|---|---|
| Local tree | `README.md` and `state-build-plan.md` are tracked. | This README owns only the local boundary and direct-child map. |
| Sibling | [`state-build-plan.md`](./state-build-plan.md) is a proposed scaffold with placeholders and ADR-0028 dependency. | Planning only; not a lane, parser contract, payload, or release. |
| State index | [`../STATE_INDEX.md`](../STATE_INDEX.md) records one proposed identity and zero verified state lanes. | Planning lineage only. |
| Directory authority | [ADR-0029](../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) accepts [Directory Rules v2](../../../doctrine/directory-rules.md). | `docs/` owns this `BOUNDARY_COMPACT` README; same-path repair is `PLACE`. |
| State decision | [ADR-0028](../../../adr/ADR-0028%20%E2%80%94%20State-scale%20Focus%20Mode%20scope.md) is proposed. | Scope, path, split, and migration remain `HOLD`. |
| Payload/schema | [`FocusModePayload`](../../../../contracts/focus_mode/focus_mode_payload.md) is proposed semantic meaning; [`schemas/contracts/v1/focus/`](../../../../schemas/contracts/v1/focus/README.md) is mixed scaffold/compatibility. | No closed state-scale machine shape. |
| Validation | [`validate_focus_mode_index.py`](../../../../tools/validators/validate_focus_mode_index.py) is county-focused and omitted by [`validator_registry.json`](../../../../tools/validators/validator_registry.json). | No current state-aware admission path. |
| Review | [CODEOWNERS](../../../../.github/CODEOWNERS) routes review to `@bartytime4life`. | Routing is not specialist review, policy approval, release, or publication authority. |

| Action | Outcome |
|---|---|
| Replace the blank README in place | `PLACE` |
| Treat this tree as final canon | `DENY` |
| Create a second writable template home | `DENY` |
| Move or split the state tree now | `HOLD` |

[Back to top](#top)

---

## Current map

```text
docs/focus-mode/state/_template/
├── README.md              # this boundary and authoring guide
└── state-build-plan.md     # proposed state-scale planning scaffold
```

The parent state README's inherited deeper-tree map omits this previously blank child README. Directory shape is unchanged here, so that omission remains separate follow-up drift rather than widening this one-file slice.

[Back to top](#top)

---

## Authority and non-effects

This README may explain template use, repository conflicts, validation needs, and reversible maintenance. It cannot:

- accept ADR-0028, register `kansas-state`, choose a destination, or authorize migration;
- define contracts, schemas, policy, evidence, runtime, or release objects;
- change the client outcomes `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`;
- create source admission, EvidenceBundle closure, policy approval, review, promotion, release, correction, rollback, deployment, or publication state.

A Markdown file, passing check, commit, pull request, merge, or badge is not evidence authority, policy permission, release approval, deployment, or KFM publication.

### Belongs here

- this local boundary README;
- a reusable state-plan Markdown scaffold with visible placeholders;
- instructions that keep document metadata separate from plan assertions;
- template-local cautions and migration notes.

### Prohibited here

Contracts, schemas, policy, fixtures, validators, tests, application code, source/evidence/receipt/proof/catalog instances, release/correction/rollback objects, published payloads, and real sensitive examples belong in their owning responsibility roots—not this public template directory.

[Back to top](#top)

---

## Authoring contract

A future approved copy of [`state-build-plan.md`](./state-build-plan.md) must:

1. update the top KFM Meta Block for document identity, review route, dates, and status;
2. update the section-13 plan-data block separately for proposed scope, domain coverage, sensitivity, evidence, validation, and release references;
3. replace prompts with evidence-bounded content or explicit `UNKNOWN`, `NEEDS VERIFICATION`, or `HOLD` entries;
4. preserve source-role and scale distinctions—county Focus outputs must not become statewide evidence roots;
5. keep sensitive examples synthetic;
6. never invent owners, accepted paths, admitted sources, evidence counts, policy decisions, gate results, release IDs, rollback IDs, or CI/runtime claims.

| Candidate milestone | Proves | Does not prove |
|---|---|---|
| Template copied | Authoring started. | Scope acceptance or canonical path. |
| Placeholders resolved | Human review is possible. | Evidence or policy closure. |
| Markdown passes | Source structure is well formed. | Truth or release readiness. |
| Validator passes | Its bounded grammar matched. | Payload, policy, or publication. |
| Schema-valid payload | Machine shape matched. | Evidence, review, or release. |

[Back to top](#top)

---

## Validation

For this README, validate UTF-8/LF/final newline, one H1, one `top` anchor, balanced fences and tables, same-document fragments, repository-relative links, no tabs/trailing whitespace/conflict markers, exact direct-child map, remote bytes, and exact changed paths. Hosted exact-head checks and human review are reported separately after draft PR creation.

Future state-template convergence also needs negative fixtures proving that:

- unresolved placeholders, duplicate plan-data blocks, unregistered state scope, lane mismatch, and unknown vocabulary fail;
- direct internal-store paths fail;
- unresolved `EvidenceRef` cannot become `ANSWER`;
- missing policy and sensitive precision fail closed;
- county Focus payloads cannot silently become statewide evidence roots;
- `released` without release, correction, and rollback references fails;
- templates and validators cannot write lifecycle or publication state.

[Back to top](#top)

---

## Exposure, mutation, and retention

| Axis | Rule |
|---|---|
| Parent | [`docs/focus-mode/state/`](../README.md), a mixed compatibility lane. |
| Scope ID | None accepted; `kansas-state` is proposed only. |
| Exposure | Public documentation; no secret, restricted, or precise sensitive content. |
| Inputs/outputs | Current doctrine/evidence in; human authoring guidance and candidate Markdown out. |
| Mutation | Versioned branch edits; no direct default-branch write or second writable mirror. |
| Retention | Durable while this compatibility path remains a writer or verified consumer. |
| Publication | None; repository merge is not KFM publication. |
| Correction | Transparent forward correction or revert with prior-blob lineage. |

**Safe sequence:** pin current repository state; classify the task; check collisions; resolve placement; branch from an exact base; copy only to an approved target; fill metadata without inventing closure; add dependencies only in owning roots; run proportional checks; verify remote bytes/diff; open a draft PR; stop before merge, ADR acceptance, source activation, release, deployment, promotion, or publication.

[Back to top](#top)

---

## Migration, correction, and rollback

Structural change remains `HOLD` until an accepted decision supplies state-scope and authority owners, final paths, full link/consumer inventory, identity mapping, one canonical writer, bounded compatibility, parser/schema/test parity, migration and rollback evidence, and zero-writer/zero-consumer proof before retirement or deletion.

Before merge, close the draft PR and abandon the branch. After a separately authorized merge, restore prior blob `8b137891791fe96927ad78e64b0aad7bded08bdc` through a transparent revert or bounded forward correction. Do not rewrite shared history.

This documentation rollback changes no public data, API, map, AI, release, deployment, correction, or publication state.

[Back to top](#top)

---

## Open verification backlog

| Priority | Item | Closure evidence |
|---|---|---|
| P0 | Decide ADR-0028 disposition and separate geographic from system/trust state. | Accepted decision, owners, migration manifest, consumer inventory, rollback. |
| P0 | Select and register final state template/lane identity. | Scope registry and accepted path/alias decision. |
| P1 | Reconcile template grammar with a state-aware validator. | One grammar, valid/invalid fixtures, tests, migration note. |
| P1 | Close FocusModePayload schema ownership without parallel `focus/`, `focus_mode/`, UI, or runtime authority. | Accepted schema home, crosswalk, validator, fixtures, compatibility plan. |
| P1 | Register validators only after contracts converge. | Registry entry, path globs, focused and changed-area tests. |
| P1 | Name accountable Focus, evidence, policy, sensitivity, validation, app, release, and correction stewards. | Verified assignments; CODEOWNERS alone is insufficient. |
| P2 | Correct parent state README map drift and prove one synthetic state plan with correction/rollback. | Separate docs repair plus no-network validation and drill evidence. |

[Back to top](#top)

---

## Related surfaces

- [State documentation boundary](../README.md)
- [State planning index](../STATE_INDEX.md)
- [State build-plan template](./state-build-plan.md)
- [Accepted Directory Rules v2](../../../doctrine/directory-rules.md)
- [ADR-0028 — proposed state scope](../../../adr/ADR-0028%20%E2%80%94%20State-scale%20Focus%20Mode%20scope.md)
- [ADR-0029 — accepted Directory Rules adoption](../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [`FocusModePayload` semantic contract](../../../../contracts/focus_mode/focus_mode_payload.md)
- [Focus schema-family index](../../../../schemas/contracts/v1/focus/README.md)
- [County-focused Focus index validator](../../../../tools/validators/validate_focus_mode_index.py)
- [Validator registry](../../../../tools/validators/validator_registry.json)
- [CODEOWNERS review route](../../../../.github/CODEOWNERS)

### Change history

| Version | Date | Change | Authority effect |
|---|---|---|---|
| `v0.1.0` | 2026-08-22 | Replaced a one-byte blank placeholder with a repository-grounded BOUNDARY_COMPACT README. | Documentation only; no state scope, migration, runtime, release, deployment, or publication effect. |

---

**Current disposition:** same-path `PLACE` · state scope `PROPOSED` · structural migration `HOLD` · runtime/release/publication effect `none`.

[Back to top](#top)
