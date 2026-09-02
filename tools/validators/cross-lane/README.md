<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-cross-lane-readme
title: tools/validators/cross-lane/ — Cross-Lane Compatibility Bridge
type: readme; directory-readme; compatibility-bridge; validator-alias-guardrail; non-authoritative
version: v0.2
status: draft; repository-grounded; compatibility-only; README-only-lane; canonical-target-confirmed; direct-executable-absent-at-tested-path; dedicated-tests-absent-at-tested-path; dedicated-workflow-absent-at-tested-path; aggregate-registration-absent; inbound-references-present; naming-decision-unresolved; no-parallel-authority; migration-controlled
owners: OWNER_TBD — Validator steward · Cross-domain architecture steward · Join steward · Directory Rules steward · Docs steward · CI steward
created: 2026-07-07
updated: 2026-07-16
supersedes: v0.1 compatibility-bridge README
policy_label: "repository-facing; tools; validators; compatibility; cross-lane; cross-domain-joins; alias-guardrail; no-executable-authority; no-schema-authority; no-policy-authority; no-proof-authority; no-release-authority"
owning_root: tools/
current_path: tools/validators/cross-lane/README.md
responsibility: >
  Preserve the doctrine-facing cross-lane name as a discoverable compatibility pointer to the canonical generic cross-domain
  join validator boundary at tools/validators/cross-domain-joins/. This lane may document the redirect, verify bridge health,
  record naming drift, and carry migration or deprecation notices. It must not duplicate validator implementation, packets,
  reports, reason codes, schemas, policy, fixtures, tests, proof, receipts, release state, or public behavior.
truth_posture: >
  CONFIRMED target v0.1 and prior blob; current lane surfaced as README-only in bounded search; representative executable,
  dedicated test, and dedicated workflow paths returned not found; the canonical generic validator README v0.2 is merged on
  main and identifies cross-lane as a compatibility bridge; pair-specific routing belongs to tools/validators/joins/ and
  accepted named pair lanes; the shared five-entry validator aggregate excludes both bridge and generic join lane; inbound
  documentation references to this path are present; Directory Rules place shared validators under tools/validators/<topic>/
  and prohibit parallel authority / PROPOSED bridge-health audit outcomes, inbound-reference inventory, eventual deprecation
  manifest, and static CI check / CONFLICTED canonical spelling and bridge lifetime remain unresolved by accepted ADR /
  UNKNOWN exhaustive inbound-reference inventory, branch-protection significance, production consumers, and runtime use
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: "524ec92059a367a1f1107a6d0eb781aeadecf948"
  prior_blob: f6763f2dbb436c05e6ab40cc1bd3f79f614683e1
  canonical_target_path: tools/validators/cross-domain-joins/README.md
  canonical_target_blob: 06873dea443c02aa0b70425a981a66b5cd79f365
  canonical_target_merge_commit: 67b79f1333c6b910996a1442e859ecfe23c80ab3
  canonical_target_pr: 1351
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  cross_lane_relations_blob: 15ca8eb8c7790d2962b710097196ed9b1eea0f79
  multi_domain_placement_blob: 12ba496e89b1a2bb5e1009080e4d611c7fb369d0
  joins_validator_index_blob: c67c66136b3c16857f1957f5d72ff61f6235372d
  aggregate_runner_blob: 3375cce172631dc3675cf2e46bb7788d273ff425
  validator_suite_blob: 7651f0571ba8f879819b197155d160c08f9fe7ac
  docs_build_workflow_blob: 3841ed36c0af0a41621992aff1d932cfca9ac082
  link_check_workflow_blob: 9326c5dce2fd99c70293ac61886d289e2fc15a0c
  docs_control_plane_workflow_blob: e50351863cce87a00df03356832b8deada56b325
  codeowners_blob: 6adabefcbe58b9d281f105dbabaea451aa165619
  drift_register_blob: 97a775522dcd058299f752ac7862d0fc56c13280
  generated_receipt_schema_blob: fba21ed27ebccf1362fe397fe0c3ebd85e072685
bounded_path_checks:
  - tools/validators/cross-lane/ surfaced only README.md
  - tools/validators/cross-lane/validate_cross_lane.py returned not found
  - tests/validators/cross-lane/README.md returned not found
  - .github/workflows/cross-lane.yml returned not found
related:
  - ../README.md
  - ../_common/README.md
  - ../cross-domain-joins/README.md
  - ../joins/README.md
  - ../../../docs/architecture/cross-domain/cross-lane-relations.md
  - ../../../docs/architecture/cross-domain/multi-domain-placement.md
  - ../../../docs/architecture/cross-domain/source-role-anti-collapse.md
  - ../../../docs/architecture/cross-domain/shared-kernel.md
  - ../../../docs/architecture/cross-domain/trust-membrane.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../tests/cross_domain/README.md
  - ../../../.github/workflows/validator-suite.yml
tags: [kfm, tools, validators, cross-lane, cross-domain, compatibility, alias, migration, no-parallel-authority]
notes:
  - "Documentation-only update paired with a generated provenance receipt."
  - "No executable, schema, contract, policy, fixture, test, workflow, data, proof, release record, route, or public behavior changes."
  - "This bridge remains deliberately narrower than the canonical generic validator README."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Cross-Lane Compatibility Bridge

`tools/validators/cross-lane/`

> Preserve the KFM **cross-lane** doctrine name as a stable navigation path while directing implementation, validation semantics, and generic join mechanics to [`tools/validators/cross-domain-joins/`](../cross-domain-joins/README.md).

<p>
  <img alt="Status draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Role compatibility bridge" src="https://img.shields.io/badge/role-compatibility__bridge-blueviolet">
  <img alt="Implementation README only" src="https://img.shields.io/badge/implementation-README__only-lightgrey">
  <img alt="Canonical target confirmed" src="https://img.shields.io/badge/target-cross--domain--joins-success">
  <img alt="Authority no parallel logic" src="https://img.shields.io/badge/authority-no__parallel__logic-critical">
</p>

> [!IMPORTANT]
> This directory is **not** an independent validator family. The merged generic validator boundary is [`../cross-domain-joins/README.md`](../cross-domain-joins/README.md). Until an accepted ADR or reviewed migration changes the canonical spelling, implementation, packets, reports, reason codes, fixtures, tests, and CI must not be duplicated here.

**Quick links:** [Purpose](#purpose) · [Status](#status) · [Placement](#placement) · [Authority graph](#authority-graph) · [Bridge contract](#bridge-contract) · [Health checks](#health-checks) · [Allowed content](#allowed) · [Excluded content](#excluded) · [Four invariants](#invariants) · [Naming decision](#naming) · [Inbound references](#references) · [Outcomes](#outcomes) · [Security](#security) · [Tests and CI](#tests-ci) · [Definition of done](#done) · [Migration and rollback](#rollback) · [Open verification](#open) · [Evidence ledger](#ledger) · [Changelog](#changelog)

---

<a id="purpose"></a>

## Purpose

KFM architecture doctrine consistently uses **cross-lane relation** language for composition across independently governed domains. The repository's complete generic validator boundary currently uses the path:

```text
tools/validators/cross-domain-joins/
```

This bridge keeps the doctrine-facing term discoverable without creating a second authority.

It answers one narrow question:

> Does the `cross-lane/` path point maintainers and repository references to the current generic cross-domain join validator boundary without duplicating implementation, semantics, policy, proof, or release authority?

A healthy bridge is navigation and migration infrastructure. It is not validation of a relationship claim.

[Back to top](#top)

---

<a id="status"></a>

## Status and evidence boundary

**Snapshot:** `main@524ec92059a367a1f1107a6d0eb781aeadecf948`
**Prior target blob:** `f6763f2dbb436c05e6ab40cc1bd3f79f614683e1`
**Canonical target blob:** `06873dea443c02aa0b70425a981a66b5cd79f365`
**Canonical target merged by:** PR `#1351`, merge commit `67b79f1333c6b910996a1442e859ecfe23c80ab3`

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| This directory | **CONFIRMED README-only in bounded search** | Keep it documentation- and migration-only. |
| Direct bridge executable | **Not found at representative tested path** | Do not claim a redirect command, module, or CLI. |
| Dedicated bridge tests | **Not found at representative tested path** | No executable bridge-health coverage is claimed. |
| Dedicated bridge workflow | **Not found at representative tested path** | No required check is claimed for this spelling. |
| Generic validator boundary | **CONFIRMED merged v0.2** | `cross-domain-joins/` owns generic mechanics. |
| Pair-specific routing | **CONFIRMED README index** | `joins/` and accepted named pair lanes own stricter pair checks. |
| Shared validator aggregate | **Five hard-coded top-level validators; bridge absent** | Aggregate success does not validate this bridge or generic joins. |
| Inbound documentation references | **CONFIRMED present in bounded search** | Silent deletion or rename would break discoverability. |
| Naming ADR | **Not established in inspected evidence** | Canonical spelling and bridge lifetime remain `CONFLICTED / NEEDS VERIFICATION`. |
| Production consumers | **UNKNOWN** | Documentation references do not prove runtime imports or calls. |

Bounded search and tested paths do not establish exhaustive historical or branch-wide absence.

[Back to top](#top)

---

<a id="placement"></a>

## Directory Rules and placement basis

The owning responsibility root is `tools/` because this path concerns validator routing. Directory Rules state that a validator spanning multiple domains belongs under the lowest common validator root:

```text
tools/validators/<topic>/
```

The current bridge therefore remains inside the correct responsibility root. Its role is transitional compatibility, not a new lifecycle phase or authority family.

| Concern | Owning home |
|---|---|
| Generic cross-domain validation | `tools/validators/cross-domain-joins/` |
| Pair-specific join validation | `tools/validators/joins/` and accepted named pair lanes |
| Compatibility name and migration notice | `tools/validators/cross-lane/` |
| Cross-lane doctrine | `docs/architecture/cross-domain/cross-lane-relations.md` |
| Domain endpoint meaning | Participating domain docs and contracts |
| Join/relation/crosswalk meaning | Accepted semantic contract under `contracts/` |
| Machine shape | Accepted schema profile under `schemas/contracts/v1/` |
| Policy | `policy/` |
| Evidence and proof | `data/proofs/` |
| Receipts | `data/receipts/` |
| Tests and fixtures | `tests/` and `fixtures/` |
| Release, correction, rollback | `release/` |

This README does not resolve the repository's wider joins-versus-relations-versus-crosswalk placement conflicts.

[Back to top](#top)

---

<a id="authority-graph"></a>

## Document authority and reference graph

```text
cross-lane doctrine terminology
  -> tools/validators/cross-lane/README.md
       compatibility pointer only
  -> tools/validators/cross-domain-joins/README.md
       canonical generic validator boundary
  -> tools/validators/joins/README.md
       pair-specific routing index
  -> accepted pair-specific lane
       stricter pair rules
```

| Document or lane | Classification | Authority |
|---|---|---|
| `cross-domain-joins/README.md` | Canonical generic validator boundary | Generic ownership, role, sensitivity, evidence, identity, cardinality, time, space, lifecycle, and public-boundary checks |
| `cross-lane/README.md` | Compatibility bridge | Naming continuity, routing, migration, and duplicate-authority guardrails |
| `joins/README.md` | Companion routing index | Pair-specific child discovery and stricter checks |
| Cross-lane architecture docs | Doctrine | Intended invariants and composition rules |
| Pair-specific validator READMEs | Companion or specialized lanes | Pair-specific constraints; executable maturity varies |
| Contracts, schemas, policy, tests, proof, release | Separate responsibility roots | Their own meaning, shape, decision, proof, or release authority |

No content in this bridge supersedes the canonical generic validator README.

[Back to top](#top)

---

<a id="bridge-contract"></a>

## Compatibility bridge contract

The bridge must satisfy all of these rules:

1. **One canonical target.** The relative link to `../cross-domain-joins/README.md` resolves.
2. **Reciprocal recognition.** The canonical target identifies `cross-lane/` as a compatibility bridge.
3. **No executable authority.** This directory contains no independent validator implementation.
4. **No semantic duplication.** Generic packets, reports, reason codes, invariants, and implementation plans remain in the canonical target.
5. **No test or CI duplication.** A future bridge check may audit routing, but generic validator tests and workflows must target the canonical lane.
6. **No hidden alias behavior.** No import, symlink, wrapper, generator, or redirect is assumed unless verified.
7. **Migration visibility.** Any rename, retirement, or canonical-name swap records affected references, compatibility window, deprecation state, and rollback.
8. **Fail-safe ambiguity.** When the target or naming decision cannot be resolved, return a negative documentation-audit outcome rather than guessing.

The bridge must remain useful to readers even when no executable validator exists.

[Back to top](#top)

---

<a id="health-checks"></a>

## Proposed bridge-health checks

These are documentation and repository-integrity checks, not relationship-validation rules.

| Check | Pass condition | Blocking condition |
|---|---|---|
| Target presence | Canonical target path exists at the inspected ref | Target missing or moved without migration |
| Target role | Canonical target declares generic validator authority | Two lanes both claim full authority |
| Reciprocal link | Canonical target links back or names this bridge | Bridge relationship is one-sided or stale |
| Lane purity | This directory remains README/migration-only | Executable, schema, policy, fixture, proof, or report appears here |
| Reference safety | Inbound references remain resolvable or are migrated | Silent deletion breaks repository navigation |
| CI singularity | Generic checks target one canonical implementation | Both spellings run independent validator logic |
| Outcome consistency | Bridge audit outcomes stay separate from `XDJ_*` validation outcomes | Bridge invents a competing runtime vocabulary |
| Deprecation completeness | Replacement, dates, reference updates, and rollback are recorded | Bridge retired without compatibility plan |

A future static checker should be deterministic, no-network, and read-only.

[Back to top](#top)

---

<a id="allowed"></a>

## What belongs here

Allowed content is deliberately narrow:

- this README;
- an accepted ADR link deciding canonical spelling;
- a reviewed migration note;
- a deprecation notice with replacement and compatibility window;
- a compatibility map of old-to-new repository paths;
- a generated or hand-maintained reference inventory when its ownership and update method are explicit;
- bounded bridge-health documentation.

Any additional file requires a placement check and must not turn this path into a second validator implementation.

[Back to top](#top)

---

<a id="excluded"></a>

## What does not belong here

| Excluded content | Owning home |
|---|---|
| Generic or pair-specific validator code | `cross-domain-joins/`, `joins/`, or accepted named validator lane |
| Join packets, report schemas, outcome contracts, or reason-code registries | Accepted contract/schema/registry homes |
| Domain or relationship semantics | Domain contracts and accepted join/relation/crosswalk contracts |
| Policy or sensitivity logic | `policy/` |
| Source descriptors | `data/registry/sources/` |
| EvidenceBundles and proofs | `data/proofs/` |
| Receipts and generated reports | `data/receipts/` and accepted QA/report roots |
| Fixtures and executable tests | `fixtures/` and `tests/` |
| Lifecycle data, catalog records, or triplets | Governed `data/` phase roots |
| Release manifests, corrections, withdrawals, or rollback cards | `release/` |
| Public API, map, graph, UI, export, or AI behavior | Governed application/runtime roots |

Do not add a shim executable merely to make both names appear implemented. A shim is a migration decision and requires an accepted ownership, packaging, test, and deprecation plan.

[Back to top](#top)

---

<a id="invariants"></a>

## Four invariants remain canonical elsewhere

The bridge may summarize the doctrine only to orient readers:

| Invariant | Required preservation |
|---|---|
| Ownership | Every endpoint remains owned by its domain |
| Source role | Roles are not dropped, upgraded, averaged, or synthesized |
| Sensitivity | The effective posture is at least the most restrictive input and may be stricter because of composition risk |
| EvidenceBundle support | Consequential endpoints and the relationship assertion resolve required evidence before public use |

The complete generic contract—including endpoint-versus-relation validity, identity, cardinality, temporal/spatial compatibility, uncertainty, policy, lifecycle, report shape, outcomes, security, tests, and implementation sequencing—belongs in [`../cross-domain-joins/README.md`](../cross-domain-joins/README.md).

[Back to top](#top)

---

<a id="naming"></a>

## Canonical naming decision

Current repository posture:

```text
canonical generic validator documentation: tools/validators/cross-domain-joins/
compatibility doctrine-name pointer:       tools/validators/cross-lane/
```

| Future choice | Requirements |
|---|---|
| Keep the bridge indefinitely | Maintain reciprocal links and lane purity |
| Retire `cross-lane/` | Accepted ADR or migration note, inbound-reference inventory, reference updates, deprecation window, and rollback |
| Promote `cross-lane/` to canonical | Accepted ADR, migration of canonical implementation/docs/tests/CI, retirement of `cross-domain-joins/`, and no dual-authority period |
| Add an executable alias | Accepted implementation and packaging decision, one underlying implementation, explicit tests, no outcome drift, and deprecation plan |
| Rename both lanes | New stable topic name, full reference migration, compatibility mapping, and ADR-backed authority decision |

This README records the conflict; it does not select a future naming outcome.

[Back to top](#top)

---

<a id="references"></a>

## Inbound-reference safety

Bounded repository search surfaced references from:

- the canonical generic validator README;
- the shared `joins/` index and pair-specific join lanes;
- domain and broad validator READMEs;
- cross-domain architecture doctrine;
- generated provenance records.

Before changing or removing this path:

1. inventory all repository references at a pinned commit;
2. classify each as canonical, navigational, compatibility, generated, or stale;
3. update authorized references atomically or through an ordered migration;
4. regenerate owned generated references when applicable;
5. run link and docs checks;
6. retain a rollback map.

Search results are not an exhaustive dependency graph. Dynamic consumers, external links, historical docs, and branch-local references remain `UNKNOWN`.

[Back to top](#top)

---

<a id="outcomes"></a>

## Proposed bridge-audit outcomes

These outcomes describe bridge integrity only. They are not generic join-validation outcomes and must not use the canonical `XDJ_*` namespace.

| Outcome | Meaning |
|---|---|
| `BRIDGE_OK` | Canonical target resolves and no duplicate authority was detected |
| `BRIDGE_TARGET_MISSING` | Canonical target does not resolve at the inspected ref |
| `BRIDGE_TARGET_DIVERGED` | Target no longer recognizes this bridge or claims conflict |
| `BRIDGE_DUPLICATE_AUTHORITY` | Independent implementation or semantics exist in both lanes |
| `BRIDGE_REFERENCE_BREAK` | One or more required inbound references were not migrated |
| `BRIDGE_MIGRATION_REQUIRED` | Requested change requires an ADR or reviewed migration |
| `BRIDGE_DEPRECATED` | Bridge remains only for a declared compatibility window |
| `ABSTAIN` | Evidence is insufficient to classify bridge health safely |
| `ERROR` | The audit could not complete |

This vocabulary remains `PROPOSED` until accepted by a documentation or repository-integrity contract.

[Back to top](#top)

---

<a id="security"></a>

## Security, side effects, and workflow posture

A bridge-health check must:

- use repository-local paths and pinned refs;
- deny network access by default;
- treat filenames, links, Markdown, and generated metadata as untrusted input;
- avoid executing repository content;
- reject path traversal and symlink escape;
- bound file count, bytes, recursion, and runtime;
- avoid logging secrets, restricted paths, or sensitive payloads;
- remain read-only except for an explicitly authorized migration;
- never change policy, release, lifecycle, or public state.

Relevant inspected workflows use ordinary `pull_request` and `push` triggers on GitHub-hosted runners and contain checkout plus TODO or existing validation steps. No `pull_request_target`, self-hosted runner, secret use, deployment, release, or write-capable publication step was established in the directly inspected docs/link/control-plane/validator workflows. This is a bounded workflow preflight, not proof about every workflow in the repository.

[Back to top](#top)

---

<a id="tests-ci"></a>

## Tests, validation, and CI

No dedicated executable bridge test or workflow was established.

Future no-network checks should verify:

- the canonical target exists;
- relative links resolve;
- reciprocal bridge classification is present;
- this directory contains no unauthorized implementation files;
- the bridge does not appear in a runtime validator registry;
- generic tests and workflows target the canonical lane only;
- inbound references are enumerated before retirement;
- deprecation and migration metadata are internally consistent.

Repository workflows inspected for this documentation change:

| Workflow | Current inspected posture |
|---|---|
| `docs-build` | `pull_request`/`push`; GitHub-hosted runner; TODO echo jobs |
| `link-check` | `pull_request`/`push`; GitHub-hosted runner; TODO echo job |
| `docs-control-plane` | `pull_request`/`push`; GitHub-hosted runner; TODO echo jobs |
| `validator-suite` | Runs the five-entry schema aggregate and an EvidenceBundle fail-closed canary; does not validate this bridge |

Workflow existence or a green status does not prove bridge correctness, canonical naming acceptance, or runtime enforcement.

[Back to top](#top)

---

<a id="done"></a>

## Definition of done

The bridge is complete as a maintained compatibility surface only when:

- [ ] canonical target path and authority are confirmed;
- [ ] reciprocal links are current;
- [ ] no implementation or semantic authority is duplicated here;
- [ ] inbound references are known well enough for safe maintenance;
- [ ] owners and CODEOWNERS posture are reviewed;
- [ ] canonical spelling and bridge lifetime are either accepted or visibly unresolved;
- [ ] any static bridge-health check is no-network, deterministic, and read-only;
- [ ] generic validator tests and CI target one implementation;
- [ ] deprecation or migration records include compatibility and rollback;
- [ ] documentation matches current repository state.

Current direct executable maturity remains **not established**.

[Back to top](#top)

---

<a id="rollback"></a>

## Migration, deprecation, correction, and rollback

### Current documentation update

Before merge, rollback means closing the draft pull request and abandoning the scoped branch. After merge, create a transparent revert of the README commit and revert or supersede its generated receipt. Do not rewrite shared history.

### Future bridge retirement or canonical-name swap

A governed migration must:

1. pin the old and new canonical commits;
2. identify the accepted replacement path;
3. inventory inbound references and generated copies;
4. migrate implementation, tests, fixtures, workflows, docs, and registries as one plan;
5. prevent a dual-authority window;
6. publish a deprecation notice with replacement and deadline;
7. preserve history and compatibility evidence;
8. validate links and registry references;
9. provide a rollback target restoring the previous canonical mapping.

A Git file move alone is not an authority migration.

[Back to top](#top)

---

<a id="open"></a>

## Open verification register

1. Accepted owner and CODEOWNERS coverage for this bridge.
2. Accepted canonical spelling for the generic validator family.
3. Whether the bridge is permanent, transitional, or scheduled for retirement.
4. Whether an ADR already exists outside the inspected search surface.
5. Complete inbound-reference inventory.
6. Dynamic imports, package entrypoints, or workflow consumers using either spelling.
7. Need for a machine-readable compatibility map.
8. Need for a static bridge-health checker and its owning test lane.
9. Stable audit-outcome vocabulary.
10. Documentation generator or mirror relationships.
11. Branch-protection significance of relevant workflows.
12. Migration and rollback drill evidence.

Unresolved items remain `NEEDS VERIFICATION` or `UNKNOWN`; they are not implementation facts.

[Back to top](#top)

---

<a id="ledger"></a>

## Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---|---|---|
| Prior bridge README | CONFIRMED | Existing compatibility purpose and stable `doc_id` | Executable redirect behavior |
| Canonical generic README v0.2 | CONFIRMED merged | Generic authority, topology, conflicts, and reciprocal bridge classification | Runtime implementation |
| PR #1351 and merge commit | CONFIRMED | Canonical README update reached `main` | KFM publication or accepted naming ADR |
| Directory Rules §12 | CONFIRMED doctrine | Shared validators use `tools/validators/<topic>/` and avoid picked-domain ownership | Which topic spelling is canonical |
| Cross-lane relation doctrine | CONFIRMED doctrine | Four invariants and cross-lane terminology | Validator implementation |
| `joins/README.md` | CONFIRMED README | Pair-specific routing boundary | Pair executables or complete inventory |
| Bounded direct-lane search | CONFIRMED search result | README surfaced as direct lane content | Exhaustive historical or generated absence |
| Representative missing executable/test/workflow paths | CONFIRMED at tested paths | Direct implementation not established there | Absence under every possible path |
| Shared aggregate | CONFIRMED code | Five registered top-level validators; bridge absent | No other invocation |
| Relevant workflow files | CONFIRMED definitions | Trigger and step posture for inspected workflows | All repository workflow safety |
| Inbound-reference search | CONFIRMED search-limited | Path has meaningful documentation dependencies | Exhaustive dependency graph |
| Drift register | CONFIRMED file | Existing repository drift process and naming-drift precedent | Entry specific to this bridge |
| Generated receipt schema | CONFIRMED schema | Receipt structure and pending-review posture | Human approval or merge authorization |

[Back to top](#top)

---

<a id="changelog"></a>

## Changelog

### v0.2 — 2026-07-16

- Grounded the bridge against the merged generic validator README v0.2.
- Recorded direct README-only posture and representative missing executable, test, and workflow paths.
- Added Directory Rules placement, authority graph, bridge contract, health checks, inbound-reference safety, workflow preflight, proposed audit outcomes, definition of done, migration, rollback, verification register, and evidence ledger.
- Preserved the canonical generic validator's ownership of implementation semantics and the unresolved naming decision.
- Added generated-work provenance requirement.

### v0.1 — 2026-07-07

- Created the initial compatibility bridge for `cross-lane/` and `cross-domain-joins/`.

<p align="right"><a href="#top">Back to top</a></p>
