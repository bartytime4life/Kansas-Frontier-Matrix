<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-policy-readme
title: docs/policy/ — Human Policy Guidance Containment and Routing Lane
type: directory-readme
version: v1.2
status: draft; repository-active; containment-only; noncanonical-under-directory-rules; migration-hold; non-policy-authority; non-release; non-publication
owners:
  - "@bartytime4life"
owner_status: "@bartytime4life is the confirmed CODEOWNERS fallback; independent documentation, policy, security, privacy, sensitivity, QA, domain, and migration stewardship remains NEEDS VERIFICATION."
created: 2026-08-14
updated: 2026-08-23
policy_label: repository-public
current_path: docs/policy/README.md
owning_root: docs/
responsibility: "Maintain the repository-present docs/policy containment contract, distinguish historical lineage from current state, route policy-related human guidance to its owning responsibility, and prevent explanatory or scaffold Markdown from becoming policy source, executable test, or publication authority."
truth_posture: "CONFIRMED current README and child bytes, direct-child inventory, accepted Directory Rules v2 placement law, canonical policy and test authorities, documentation workflows, CODEOWNERS fallback, and current machine-registry contents / PROPOSED per-file convergence and retirement sequencing / UNKNOWN complete external consumers, final lane disposition, and independent stewardship / NEEDS VERIFICATION accepted migration decisions, branch-protection coupling, and document-registry admission"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 38715c760f0005e97ede9281b8cbe755a827346d
  base_tree: 1a4868dc9c0343fa86f666267e4d87ce6cb5c055
  current_blob_before_update: 5c483016ea0e99cb0f782d1b807542c824b6dbae
  contract_introduced_commit: afc9eabd8902a7ae85f7c8c119817c9b6db6d449
  historical_placeholder_blob: e25f1814e51579d5f55c0f1fe0135ddb28a47f4a
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  policy_root_readme_blob: 52877f1befd3112f1aec0eb122669d3fdc2634e6
  tests_root_readme_blob: 5e497ae0f5b2f6a22d795346315b94393802e38f
  tests_policy_readme_blob: d39a16c668824048c19738bbcdd3068d08f2f557
  policy_tests_readme_blob: 4bb2b04fba4a9109501a5d42a4bf1a432569c085
  docs_policy_tests_prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  docs_policy_tests_pointer_blob: ecc70dcf7ea032e6e6e45cdb5695668d7872bb51
  tests_marker_blob: e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  living_persons_scaffold_blob: 51a7da413c94280a527ada69c7fdd74a8dd08613
  fauna_scaffold_blob: 31be13d0ce49779bc0de3d6829842ef439ba07ec
related:
  - docs/README.md
  - docs/policy/tests/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - docs/domains/people-dna-land/README.md
  - docs/domains/fauna/README.md
  - docs/security/README.md
  - docs/standards/README.md
  - policy/README.md
  - policy/tests/README.md
  - policy/domains/people-dna-land/README.md
  - policy/domains/fauna/README.md
  - tests/README.md
  - tests/policy/README.md
  - fixtures/README.md
  - contracts/policy/README.md
  - schemas/contracts/v1/policy/README.md
  - tools/validators/policy/README.md
  - control_plane/document_registry.yaml
  - .github/CODEOWNERS
  - .github/workflows/docs-meta-block.yml
  - .github/workflows/link-check.yml
  - .github/workflows/docs-document-graph.yml
  - .github/workflows/docs-stale-scan.yml
  - .github/workflows/docs-build.yml
  - .github/workflows/policy-test.yml
tags:
  - kfm
  - docs
  - policy-guidance
  - containment
  - migration-hold
  - non-authoritative
  - policy-tests
  - sensitivity
  - cite-or-abstain
notes:
  - "v1.0 replaced a one-byte README whose complete content was the character y."
  - "v1.1 refreshed current-main evidence, separated historical lineage from current state, added repository-native validation commands, and corrected rollback to the actual current contract."
  - "v1.2 reconciles the tests child after PR #3448 created a blank README, pairs that child with a containment/routing pointer, and keeps executable tests under canonical tests/."
  - "The adopted Directory Rules v2 canonical docs direct-child map does not name docs/policy/; this README therefore contains and routes the current lane rather than declaring it canonical."
  - "No executable policy rule, contract, schema, fixture, test, registry, receipt, proof, release object, runtime, or public surface is changed by this documentation reconciliation."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/policy/` — Human Policy Guidance Containment and Routing Lane

`docs/policy/` is a repository-present documentation lane containing two small proposal-only guidance scaffolds and one policy-test documentation pointer. This README makes that state inspectable, routes readers to the responsibility roots that own policy-related work, and prevents the lane from becoming a second policy, test, fixture, or publication authority.

> [!IMPORTANT]
> **This path exists, but adopted Directory Rules v2 do not list `docs/policy/` as a canonical documentation lane.** The current posture is containment and migration review. Keep existing references readable; place new substantive guidance by its primary responsibility under an adopted documentation lane.

> [!WARNING]
> **Executable policy source is singular under [`policy/`](../../policy/README.md), while executable conformance belongs under [`tests/`](../../tests/README.md).** Nothing here can allow or deny an operation, run a test, authenticate consent, clear rights, downgrade sensitivity, establish evidence, approve release, or authorize publication.

> [!CAUTION]
> The child scaffolds concern living-person/DNA geoprivacy and fauna sensitivity. The tests child is public documentation. Do not add real personal data, genomic material, exact protected locations, private-land details, consent tokens, restricted evidence, executable fixtures, or reconstruction-enabling examples to this repository-facing lane.

**Quick navigation:** [Purpose](#purpose-and-authority) · [Evidence](#current-repository-state-and-lineage) · [Inventory](#current-direct-child-map) · [Routing](#authority-routing) · [Containment](#containment-contract) · [Guidance contract](#human-policy-guidance-contract) · [Sensitive content](#rights-sensitivity-and-public-exposure) · [Migration](#convergence-and-migration-discipline) · [Validation](#validation) · [Review](#ownership-and-review) · [Rollback](#correction-and-rollback) · [Open work](#open-verification-register) · [History](#change-history)

---

## Purpose and authority

This README has a deliberately narrow responsibility:

1. describe the current lane without promoting its contents;
2. distinguish current repository evidence from historical lineage;
3. separate human explanation from policy, contract, schema, runtime, test, fixture, evidence, review, release, and publication authority;
4. route future work to its owning responsibility;
5. preserve references while per-file convergence is decided; and
6. keep verification, migration, correction, and rollback visible.

It does **not** choose a final home for either sensitive-domain scaffold, retire this lane, create a compatibility alias, amend Directory Rules, admit an executable test lane, activate policy, or authorize release.

| Field | Current contract |
|---|---|
| Path | `docs/policy/` |
| Owning root | `docs/` — human-readable explanation only |
| Current lane class | Repository-present containment lane; not a canonical direct child under adopted Directory Rules v2 |
| Placement outcome for this README | `PLACE` for same-path containment while the current lane exists |
| Placement outcome for new substantive content | `HOLD` until one primary responsibility and any canonical equivalent are verified |
| Policy-source authority | [`policy/`](../../policy/README.md) |
| Policy-object meaning | [`contracts/policy/`](../../contracts/policy/README.md) |
| Machine shape | [`schemas/contracts/v1/policy/`](../../schemas/contracts/v1/policy/README.md) |
| Executable-test authority | [`tests/`](../../tests/README.md), normally [`tests/policy/`](../../tests/policy/README.md) for policy boundaries |
| Reusable-fixture authority | [`fixtures/`](../../fixtures/README.md) |
| Public-path role | Repository-facing documentation only; never a policy-evaluation, test-execution, or data-serving path |
| Writers | Reviewed documentation changes on feature branches |
| Trust posture | Cite or abstain; fail closed where rights, sensitivity, consent, public exposure, ownership, or test authority is unresolved |

### Directory Rules basis

Accepted [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact Directory Rules v2 bytes at [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md). Those rules:

- make `docs/` the human-readable explanation root without granting machine, test, policy, evidence, release, or data authority;
- list the canonical documentation lanes and do not include `docs/policy/`;
- make executable policy source singular under `policy/`;
- make `tests/` the executable-conformance responsibility root and `fixtures/` the reusable-test-input root;
- require README contracts where authority, exposure, mutation, or lifecycle behavior changes; and
- require explicit classification, single-write discipline, verified consumers, exit criteria, and rollback for compatibility or migration.

This same-path update is a bounded containment action. It does not authorize growth of `docs/policy/` or `docs/policy/tests/` as parallel authority lanes.

[Back to top](#top)

---

## Current repository state and lineage

Evidence base: `main@38715c760f0005e97ede9281b8cbe755a827346d`, tree `1a4868dc9c0343fa86f666267e4d87ce6cb5c055`. The tests-child pointer is authored on the feature branch from that exact base at blob `ecc70dcf7ea032e6e6e45cdb5695668d7872bb51`.

| Surface | Confirmed current state | Safe interpretation |
|---|---|---|
| `docs/policy/README.md` before this revision | Substantive containment contract; blob `5c483016ea0e99cb0f782d1b807542c824b6dbae` | Current parent boundary, not policy or publication authority |
| Contract introduction | Commit `afc9eabd8902a7ae85f7c8c119817c9b6db6d449` replaced the historical placeholder on 2026-08-14 | Establishes current README lineage |
| Historical placeholder | Blob `e25f1814e51579d5f55c0f1fe0135ddb28a47f4a` contained only `y` | Historical defect evidence; not current state or a preferred rollback target |
| Direct entries | This README, one Markdown file, and two directories | Small containment surface |
| `living_persons_geoprivacy.md` | Explicit `PROPOSED scaffold`; blob `51a7da413c94280a527ada69c7fdd74a8dd08613` | Not authoritative privacy or geoprivacy guidance |
| `sensitivity/fauna.md` | Explicit `PROPOSED scaffold`; blob `31be13d0ce49779bc0de3d6829842ef439ba07ec` | Not an accepted sensitivity documentation family |
| `tests/README.md` at base | One newline; blob `8b137891791fe96927ad78e64b0aad7bded08bdc` | Path presence only; no test contract or implementation |
| `tests/README.md` on this branch | Containment and routing pointer; blob `ecc70dcf7ea032e6e6e45cdb5695668d7872bb51` | Human guidance only; no executable-test authority |
| `tests/.gitkeep` | Zero bytes; blob `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | Historical marker only |
| Canonical test root | `tests/README.md` blob `5e497ae0f5b2f6a22d795346315b94393802e38f` | Executable conformance belongs under root `tests/` |
| Canonical policy-test lane | `tests/policy/README.md` blob `d39a16c668824048c19738bbcdd3068d08f2f557` | Substantive mixed-maturity boundary suite; passing remains non-authoritative |
| Policy-local tests placeholder | `policy/tests/README.md` blob `4bb2b04fba4a9109501a5d42a4bf1a432569c085` | Separate held lane; not a substitute for root `tests/policy/` |
| Canonical policy root | `policy/README.md` blob `52877f1befd3112f1aec0eb122669d3fdc2634e6` | Policy-source work belongs under `policy/`, not here |
| Placement authority | Directory Rules blob `fd49a0b83e55cef52c1124281f093e263526898d`, adopted through ADR-0029 blob `a4de0d7a96b78da59cfc499d1025e1508afd8dd9` | Same-path containment is allowed; parallel policy/test authority is not |
| CODEOWNERS | Blob `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61`; no lane-specific rule; fallback `@bartytime4life` | Review routing only, not independent approval evidence |
| Consumer closure | GitHub search is insufficient to prove complete repository or external consumers | Moves and deletion remain `HOLD` |
| Runtime, release, publication | None | Documentation presence and CI cannot establish enforcement or public state |

**CONFIRMED:** the parent README is substantive; the one-byte value is historical lineage. The child inventory is current on this branch, and every child remains proposal, containment, or marker material rather than executable authority.

**PROPOSED:** classify and converge child documents into their owning documentation responsibilities after consumer review.

**UNKNOWN:** external consumers, old bookmarks, generated reports, and uninspected branches.

**NEEDS VERIFICATION:** accepted migration or retirement decisions, complete link closure, independent stewardship, branch-protection coupling, and document-registry admission.

[Back to top](#top)

---

## Current direct-child map

```text
docs/policy/
├── README.md                         # containment, routing, and migration boundary
├── living_persons_geoprivacy.md      # PROPOSED scaffold; no policy authority
├── sensitivity/                      # one fauna scaffold; no child README
└── tests/                            # containment pointer plus .gitkeep; no executable tests
```

| Direct child | Current evidence | Current posture |
|---|---|---|
| [`living_persons_geoprivacy.md`](living_persons_geoprivacy.md) | Names [`docs/domains/people-dna-land/sublanes/dna.md`](../domains/people-dna-land/sublanes/dna.md) as its source | `HOLD`; compare domain, security/privacy, standards, and executable-policy responsibilities |
| [`sensitivity/`](sensitivity/) | Contains `fauna.md`, sourced to [`docs/domains/fauna/IDENTITY_MODEL.md`](../domains/fauna/IDENTITY_MODEL.md) | `HOLD`; no accepted child-lane contract or final documentation home |
| [`tests/`](tests/) | Contains a routing pointer and zero-byte `.gitkeep`; no executable extension or fixture | `PLACE` for containment; `HOLD` for growth or retirement pending consumer review |

No child is promoted, accepted, activated, released, or made canonical by this inventory.

[Back to top](#top)

---

## Authority routing

Route policy-related material by **primary responsibility**, not by the word “policy.”

| Primary responsibility | Owning surface |
|---|---|
| Stable KFM operating law | [`docs/doctrine/`](../doctrine/) |
| Architecture decision | [`docs/adr/`](../adr/) |
| Policy-system architecture | [`docs/architecture/`](../architecture/) |
| Domain explanation | [`docs/domains/<domain>/`](../domains/) |
| Security, privacy, threat, or exposure guidance | [`docs/security/`](../security/) |
| External or KFM standards profile | [`docs/standards/`](../standards/) |
| Operational procedure | [`docs/runbooks/`](../runbooks/) |
| Drift or unresolved authority | [`docs/registers/`](../registers/) |
| Executable admissibility rule | [`policy/`](../../policy/) |
| Policy-object meaning | [`contracts/policy/`](../../contracts/policy/) |
| Machine-valid policy-object shape | [`schemas/contracts/v1/policy/`](../../schemas/contracts/v1/policy/) |
| Executable policy and trust-boundary tests | [`tests/policy/`](../../tests/policy/README.md) or another accepted test lane |
| Reusable fixtures | [`fixtures/`](../../fixtures/README.md), normally an accepted policy or contract family |
| Evaluator or reusable runtime | Accepted app, package, or runtime implementation |
| Validator implementation | [`tools/validators/policy/`](../../tools/validators/policy/README.md) |
| Emitted decision, receipt, proof, review, or release object | Its governed data, review, proof, or release family |

A human document may explain an accepted rule and link to its source. It must not copy the rule into an independently writable second authority. A test may exercise a rule without becoming the rule or a release decision. Preserve and route discrepancies instead of choosing whichever representation is convenient.

[Back to top](#top)

---

## Containment contract

While lane disposition is unresolved, permitted content is limited to:

- this README, the current proposal scaffolds, and the tests-child routing pointer;
- bounded correction or migration preparation;
- tombstone, alias, or migration facts after an accepted decision;
- links to the current owning documentation, policy, contract, schema, validation, test, fixture, evidence, and release surfaces; and
- current evidence and verification status.

Do **not** add executable rules, bundles, evaluator configuration, schemas, DTOs, semantic contracts, domain doctrine, security/privacy doctrine, test code, reusable fixtures, emitted decisions or receipts, release objects, real sensitive data, exact protected geometry, or a new `docs/policy/<topic>/` hierarchy.

Before adding or materially expanding a file here, reviewers must establish one owning human-document responsibility, the adopted lane that owns it, whether a canonical equivalent exists, whether a verified consumer needs the current path, whether parallel authority would result, and the required compatibility, validation, and rollback. Otherwise the outcome is `HOLD`.

[Back to top](#top)

---

## Human policy-guidance contract

A policy-related human document, wherever it belongs, should expose:

| Requirement | Minimum expectation |
|---|---|
| Identity | Stable ID, title, path, status, version, and owning documentation responsibility |
| Scope | Operation, audience, domain, geography, time, and explicit exclusions |
| Authority | Accepted doctrine/ADR, policy entrypoint, semantic contract, schema, test relationship, and release relationship |
| Evidence posture | Confirmed, proposed, unknown, stale, conflicted, and verification states |
| Inputs | Governed references for source, evidence, rights, consent, sensitivity, lifecycle, review, and release |
| Outcomes | Contract-defined finite outcomes, reasons, and obligations; no invented vocabulary |
| Fail-closed behavior | Missing or untrusted context remains denied, held, restricted, or abstained |
| Sensitivity | Public-safe examples, precision limits, reconstruction risk, and protected-reason handling |
| Validation | Fixtures, tests, evaluator/validator profile, version, digest, and current execution evidence |
| Consumers | Governed APIs, applications, release gates, operators, or test harnesses |
| Non-effects | No truth, consent inference, policy activation, test authority, promotion, release, or publication from prose |
| Correction | Supersession, deactivation, test invalidation, correction propagation, and rollback target |

Do not use this README to normalize unresolved engine-native and outward runtime vocabularies. The accepted semantic contract and evaluator binding own that translation. Do not use a test name or directory as evidence that the tested system is active.

[Back to top](#top)

---

## Rights, sensitivity, and public exposure

`docs/` may be publicly readable. Public documentation and test guidance must not expose protected payloads while explaining that a protection exists.

Apply heightened review to living-person identity or location; DNA, genomic, genealogy, kinship, consent, and revocation state; private-land or person–parcel joins; sensitive fauna locations; archaeology, cultural knowledge, sacred places, sovereignty, tribal information, infrastructure, private wells, or other harmful precision; and reasons or transforms that could reconstruct protected information.

Use synthetic or irreversibly generalized examples. Never commit consent tokens, private identifiers, credentials, signed URLs, source payloads, or exact protected locations. Do not infer consent, rights, sensitivity, or public safety from missing data. Client-side hiding is not a substitute for pre-release transformation. Route consequential disclosure questions to the owning policy and qualified reviewer; documentation and test success cannot waive the requirement.

[Back to top](#top)

---

## Convergence and migration discipline

| Current item | Candidate responsibility | Result | Evidence needed before action |
|---|---|---|---|
| `living_persons_geoprivacy.md` | People/DNA/Land explanation; security/privacy guidance; standards profile | `HOLD` | Compare current docs, consumers, standards, identity, links, and qualified review |
| `sensitivity/fauna.md` | Fauna explanation; security/geoprivacy guidance; standards profile | `HOLD` | Compare fauna docs, policy lanes, source-role boundaries, links, and public-safe review |
| `tests/README.md` | Temporary test-routing pointer | `PLACE` for same-path containment; `HOLD` for executable growth or retirement | Complete consumers, one canonical documentation target or zero-successor decision, registry/link update, and rollback |
| `tests/.gitkeep` | Historical marker only | `NEEDS VERIFICATION` | Confirm no identity, generation, or consumer dependence before deletion |
| This README | Containment while referenced paths remain | `PLACE` for containment | Revisit after child migration and zero-consumer proof |

A future move, rename, consolidation, or retirement must freeze identities and consumers; classify each file by one responsibility; verify one target; inspect repository and external references; preserve identity or record a version change; keep one writable source; update links, indexes, registry candidates, generators, and consumers; validate metadata, links, graph, freshness, topology, sensitivity, and changed area; retain correction and rollback evidence; and prove zero writers and zero consumers before retirement.

Do not bulk-move by filename or topic, and never create two writable authorities.

[Back to top](#top)

---

## Validation

Documentation checks are quality evidence only. They do not prove policy correctness, test completeness, activation, runtime enforcement, release approval, or publication.

| Check | Applies | Boundary |
|---|:---:|---|
| [`docs-meta-block`](../../.github/workflows/docs-meta-block.yml) | Yes | Validates changed metadata and emits a review-only registry delta |
| [`link-check`](../../.github/workflows/link-check.yml) | Yes | Validates changed local targets; external URLs are not requested |
| [`docs-document-graph`](../../.github/workflows/docs-document-graph.yml) | Yes | Builds a bounded documentation graph projection |
| [`docs-stale-scan`](../../.github/workflows/docs-stale-scan.yml) | Yes | Reports changed-file freshness and verification debt |
| [`docs-build`](../../.github/workflows/docs-build.yml) | Yes | Records the explicit generator/preview hold; it does not publish |
| Directory-topology validation | Yes | Detects new drift; this change admits no new canonical lane |
| Policy evaluator tests | No behavior changed | These docs change no policy source or evaluator |
| Policy boundary tests | No behavior changed | Existing suites are referenced, not modified or rerun as authority |
| Rights and sensitivity review | Yes | Confirms no protected data, executable fixture, or harmful precision is introduced |

### Repository-native commands

Run in an isolated checkout after `python tools/ci/install_python_ci.py project-test`, replacing `<base>` with the pinned base commit.

```bash
python -m unittest discover \
  --start-directory tests/validators/docs/meta-block \
  --pattern 'test_*.py' --verbose

python tools/validators/docs/meta-block/check_meta_blocks.py \
  --repo-root . --profile present \
  --registry control_plane/document_registry.yaml \
  --git-diff "<base>...HEAD" --format markdown \
  --output /tmp/docs-meta-block.md \
  --registry-delta-output /tmp/document-registry-delta.json \
  README.md docs tools/validators/docs

python -m unittest discover \
  --start-directory tests/validators/docs/link-check \
  --pattern 'test_*.py' --verbose

python tools/validators/docs/link-check/check_links.py \
  --repo-root . --git-diff "<base>...HEAD" --format text

python -m unittest discover \
  --start-directory tests/validators/docs/document-graph \
  --pattern 'test_*.py' --verbose

python tools/validators/docs/document-graph/check_document_graph.py \
  --repo-root . \
  --entrypoint README.md --entrypoint docs/README.md \
  --entrypoint tools/validators/docs/document-graph/README.md \
  --registry control_plane/document_registry.yaml \
  --git-diff "<base>...HEAD" --format markdown \
  --output /tmp/docs-document-graph.md \
  README.md docs tools/validators/docs

python -m unittest discover \
  --start-directory tests/validators/docs/stale-scan \
  --pattern 'test_*.py' --verbose

python tools/validators/docs/stale-scan/check_stale_docs.py \
  --repo-root . --as-of "$(date -u +%F)" \
  --profile advisory --review-window-days 365 \
  --placeholder-grace-days 90 \
  --git-diff "<base>...HEAD" --format markdown \
  --output /tmp/docs-stale-scan.md \
  README.md docs tools/validators/docs

make repository-topology
make validator-registry-check
```

The registry delta is review-only. These commands do not mutate the registry, accept doctrine, activate policy, create test authority, approve release, deploy, or publish.

### Changed-file acceptance checks

- Both changed files contain one H1 and a closed `KFM_META_BLOCK_V2` where required.
- Every introduced local link resolves with correct case.
- The direct-child map matches the inspected tree.
- Historical lineage is not presented as current state.
- The tests child is described as a containment pointer, not executable implementation.
- No child is promoted and no policy source, schema, contract, runtime, fixture, test, decision, receipt, proof, release, or publication state is created.
- No real sensitive data, secret, credential, protected exact location, or executable fixture appears.
- The diff remains limited to the child pointer and this directly dependent parent inventory.
- Both files end with a newline and contain no trailing whitespace.

[Back to top](#top)

---

## Ownership and review

[`CODEOWNERS`](../../.github/CODEOWNERS) has no `docs/policy/`-specific rule, so the repository-wide fallback routes review to `@bartytime4life`. CODEOWNERS is routing, not proof of policy, QA, privacy, domain, legal, security, release, or independent review.

Content-specific changes also need the applicable policy, contract, schema, runtime, domain, privacy, consent, rights, biodiversity, sensitivity, geoprivacy, security, standards, QA, release, correction, rollback, and migration reviewers. Independent assignments remain `NEEDS VERIFICATION`; do not encode placeholder roles as GitHub owners.

Review of this update should verify the exact base and prior blobs, the current child map, canonical test routing, the absence of executable content, the noncanonical docs-lane posture, public-safe wording, and exact rollback.

[Back to top](#top)

---

## Correction and rollback

A correction should identify the affected claim, current evidence, whether a child or authority route changed, links or consumers requiring propagation, and the prior blob or forward-fix target.

The base parent contract for this revision is blob `5c483016ea0e99cb0f782d1b807542c824b6dbae`; the child target preimage is blob `8b137891791fe96927ad78e64b0aad7bded08bdc`; both are pinned to `main@38715c760f0005e97ede9281b8cbe755a827346d`.

Before merge, rollback normally means closing or abandoning the draft pull request and branch. After an authorized merge, use a reviewed revert of the implementation commits or a forward-fix PR against the actual merged state; never rewrite shared history.

Restoring the child blank blob is byte-accurate but removes the containment warning. A forward fix is preferred for wording errors. The historical parent one-byte blob `e25f1814e51579d5f55c0f1fe0135ddb28a47f4a` remains lineage evidence but is not a rollback target because restoring it would recreate the broken parent placeholder.

No policy, test, fixture, contract, schema, runtime, release, deployment, or public state needs rollback because none changes here.

[Back to top](#top)

---

## Open verification register

| Item | Status | Closure evidence |
|---|---|---|
| Final class and lifetime of `docs/policy/` | `NEEDS VERIFICATION` | Accepted documentation-lane or migration decision |
| Canonical target for each sensitive-domain scaffold | `HOLD` | Per-file responsibility and canonical-equivalent review |
| Complete repository and external references | `UNKNOWN` | Recursive search plus known external-consumer inventory |
| Living-person/DNA scaffold ownership | `NEEDS VERIFICATION` | Domain, privacy, security, and standards disposition |
| Fauna scaffold ownership | `NEEDS VERIFICATION` | Fauna, geoprivacy, security, and standards disposition |
| Purpose of `docs/policy/tests/` | `CONFIRMED bounded containment and routing` | This pointer; final lifetime remains separate |
| Final lifetime of `docs/policy/tests/` | `HOLD` | Canonical target or zero-successor decision plus consumer closure |
| Independent stewardship | `NEEDS VERIFICATION` | Approved assignments and repository access |
| Machine document-registry admission | `NEEDS VERIFICATION` | Reviewed metadata-validator delta and accepted registry update |
| Compatibility window and exit criteria | `UNKNOWN` | Accepted migration plan and verified consumers |
| Branch-protection and required-check coupling | `NEEDS VERIFICATION` | Repository settings evidence; workflow presence is insufficient |
| General policy evaluator and active bundle | `UNKNOWN / HOLD` | Accepted bundle, selector, evaluator, replay, decision receipt, and consumers |
| Runtime or public-release effect | `NONE` | Separate governed implementation and release evidence |

[Back to top](#top)

---

## Related documentation

- [Policy-test documentation pointer](tests/README.md)
- [Documentation root contract](../README.md)
- [Adopted Directory Rules](../doctrine/directory-rules.md)
- [Accepted ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Drift register](../registers/DRIFT_REGISTER.md)
- [Verification backlog](../registers/VERIFICATION_BACKLOG.md)
- [People, DNA, and Land guidance](../domains/people-dna-land/README.md)
- [Fauna guidance](../domains/fauna/README.md)
- [Security documentation](../security/README.md)
- [Standards documentation](../standards/README.md)
- [Canonical policy root](../../policy/README.md)
- [Policy-local tests placeholder](../../policy/tests/README.md)
- [People, DNA, and Land policy boundary](../../policy/domains/people-dna-land/README.md)
- [Fauna policy boundary](../../policy/domains/fauna/README.md)
- [Canonical test root](../../tests/README.md)
- [Executable policy-test lane](../../tests/policy/README.md)
- [Canonical fixture root](../../fixtures/README.md)
- [Policy contracts](../../contracts/policy/README.md)
- [Policy schemas](../../schemas/contracts/v1/policy/README.md)
- [Policy validators](../../tools/validators/policy/README.md)
- [Policy readiness workflow](../../.github/workflows/policy-test.yml)
- [Machine document registry](../../control_plane/document_registry.yaml)
- [Repository orchestration surface](../../Makefile)

## Evidence review triggers

Re-review when an ADR classifies the lane, a child gains a canonical successor, a consumer requires an alias, the inventory changes, adjacent authority boundaries or CODEOWNERS change, documentation QA changes, test placement changes, sensitivity/correction requirements change, or migration reaches single-write, dual-read, zero-consumer, or retirement.

**Last evidence review:** 2026-08-23 against `main@38715c760f0005e97ede9281b8cbe755a827346d`, tree `1a4868dc9c0343fa86f666267e4d87ce6cb5c055`, parent blob `5c483016ea0e99cb0f782d1b807542c824b6dbae`, child prior blob `8b137891791fe96927ad78e64b0aad7bded08bdc`, child pointer blob `ecc70dcf7ea032e6e6e45cdb5695668d7872bb51`, Directory Rules blob `fd49a0b83e55cef52c1124281f093e263526898d`, and ADR-0029 blob `a4de0d7a96b78da59cfc499d1025e1508afd8dd9`.

## Change history

| Version | Date | Material change |
|---|---|---|
| `v1.0` | 2026-08-14 | Replaced the one-byte placeholder with a containment, routing, migration, sensitivity, validation, and rollback contract. |
| `v1.1` | 2026-08-16 | Refreshed current-main evidence, separated historical lineage from current state, added repository-native validation commands, and corrected rollback to the actual current contract. |
| `v1.2` | 2026-08-23 | Reconciled the tests child after its blank README was added, linked the new containment pointer, and routed executable policy tests to canonical `tests/` responsibilities. |

## Status

**CONFIRMED:** current same-path containment contract, direct-child inventory, adopted Directory Rules, canonical `policy/` and `tests/` authorities, child routing pointer, and current documentation workflow surfaces; no executable or runtime change.

**PROPOSED:** per-file convergence after responsibility and consumer review.

**UNKNOWN / NEEDS VERIFICATION:** final lane disposition, migration targets, complete consumers, independent stewardship, registry admission, branch-protection coupling, general policy evaluator, and any public or runtime effect.

[Back to top](#top)
