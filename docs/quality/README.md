<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-quality-readme
title: docs/quality/ — Quality Guidance and Validation Index
type: README
version: v1.0
status: draft; repository-grounded; BOUNDARY_COMPACT; documentation-only; non-authoritative
owner: NEEDS VERIFICATION — no independent quality steward or separation-of-duties assignment was verified for this lane
created: 2026-08-16
updated: 2026-08-16
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
policy_label: repository-facing; public-safe; quality-guidance; non-publisher
owning_root: docs/
responsibility: orient maintainers and reviewers to human-readable quality expectations, quality evidence, validation entry points, claim limits, and adjacent authority surfaces without becoming executable proof, policy, release, or publication authority
truth_posture: cite-or-abstain
canonical_relationship: same-path replacement of an existing placeholder; no sibling authority, new root, move, rename, or canonical direct-child reclassification
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 46a6fb9d8abad66c1d7df98717d4e6ea4a057660
  prior_blob: e25f1814e51579d5f55c0f1fe0135ddb28a47f4a
  prior_content: one-character placeholder
  direct_child_files: 2
  open_pull_requests_at_preflight: 0
notes:
  - "The created date records this first substantive boundary README; the placeholder file's original creation date was not verified."
  - "Accepted ADR-0029 adopts the exact current Directory Rules v2 bytes; this same-path documentation change uses the existing docs/ authority boundary."
  - "The parent docs README records quality as an existing child lane but does not make every observed child a new canonical direct-child category."
  - "This document changes no contract, schema, policy, validator, test, workflow, runtime, receipt, proof, release, deployment, promotion, publication, or repository setting."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/quality/` — Quality Guidance and Validation Index

> **One-line purpose.** `docs/quality/` explains KFM quality expectations, evidence boundaries, validation entry points, and review responsibilities; executable proof remains with the tests, validators, workflows, artifacts, and governed records that own it.

> [!IMPORTANT]
> **Quality documentation is not quality proof.** A page, checklist, test, validator, badge, workflow, receipt, pull request, or merged commit proves only its declared assertion at a known revision. None of those objects alone establishes source truth, `EvidenceBundle` closure, policy approval, review completion, release, deployment, promotion, publication, or production parity.

> [!NOTE]
> This is a same-path replacement of the prior one-character placeholder. It documents an existing lane under [`docs/`](../README.md); it does not create a new root, a parallel authority, or a new canonical direct-child class.

**Quick navigation:** [Purpose](#purpose-and-authority) · [Status](#status-and-evidence-boundary) · [Posture](#quality-operating-posture) · [Belongs](#what-belongs-here) · [Does not belong](#what-does-not-belong-here) · [Authority map](#responsibility-and-authority-map) · [Direct children](#direct-child-map) · [Evidence](#quality-evidence-and-result-grammar) · [Validation](#validation-and-repository-checks) · [Review](#review-triggers-and-maintenance) · [Related surfaces](#related-surfaces) · [Rollback](#correction-rollback-and-last-evidence-review)

---

## Purpose and authority

`docs/quality/` is a human-readable quality-guidance lane inside KFM's canonical [`docs/`](../README.md) responsibility root. It exists to help maintainers, reviewers, domain stewards, application owners, validator authors, and release stewards understand:

- which quality properties a change claims to preserve or improve;
- which repository surfaces can provide evidence for those claims;
- which checks are required, applicable, observational, pending, or out of scope;
- what a passing check does and does not prove;
- how quality concerns connect to evidence, policy, security, performance, accessibility, reliability, correction, and rollback; and
- where executable behavior and authority actually live.

Accepted [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact current Directory Rules v2 bytes at [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md). Those rules make `docs/` the authority root for maintained human-readable explanation and require owned boundaries to state purpose, prohibited content, inputs, outputs, exposure, mutation, validation, and review triggers.

The parent [`docs/README.md`](../README.md) records `quality/` as an existing child lane whose presence is implementation evidence, not automatic authority to create a new canonical documentation category. This README therefore uses the compact boundary profile for the lane as it exists. Any future structural reclassification remains a separate Directory Rules or ADR decision.

### Negative authority

This lane does **not**:

- define semantic object meaning;
- define machine-valid object shape;
- decide allow, deny, restrict, redact, quarantine, or abstain outcomes;
- implement validators, tests, workflows, application behavior, or runtime instrumentation;
- store canonical evidence, receipts, proofs, release records, or published payloads;
- approve a quality exception, release, deployment, promotion, or publication; or
- convert repository state into a claim about production behavior.

[Back to top](#top)

---

## Status and evidence boundary

This revision was prepared against `main@46a6fb9d8abad66c1d7df98717d4e6ea4a057660`.

| Surface | CONFIRMED observation | Bounded conclusion |
|---|---|---|
| Target | `docs/quality/README.md` contained only `y` at blob `e25f1814e51579d5f55c0f1fe0135ddb28a47f4a` | A substantive same-path boundary README is required |
| Direct lane inventory | The directory contained this README and [`maplibre-perf-governance.md`](./maplibre-perf-governance.md) | The direct-child navigation surface is small and exactly known at the inspected base |
| Placement | `docs/` is the human-readable documentation root; ADR-0029 adopts Directory Rules v2 | `PLACE` applies to this same-path documentation replacement |
| Parent classification | The parent docs index treats `quality/` as current implementation evidence without automatically canonizing every observed child lane | This README documents the current lane but does not amend the docs taxonomy |
| Repository validation surface | The root [`Makefile`](../../Makefile) exposes registry-driven validation, repository-topology, workflow-security, release-prerequisite, and MapLibre quality targets | Commands may be cited as current entry points; results must be tied to an exact run and revision |
| Hosted validation | [`validator-suite.yml`](../../.github/workflows/validator-suite.yml) runs on pull requests with read-only repository permissions | Its conclusion is a bounded CI signal, not release or publication authority |
| Open overlap | No open pull request was returned during preflight | No active PR owned the target path at preflight |
| Runtime, production, release, deployment, publication | Not established by this documentation review | `UNKNOWN` unless proven by their owning surfaces at an exact revision |

### State separation

Do not collapse these independent states:

| State | Example |
|---|---|
| Documentation presence | A quality page exists |
| Documentation currency | Its commands and links match current repository bytes |
| Check implementation | A validator, test, or workflow exists |
| Check execution | A named check ran against a known revision |
| Check result | `PASS`, `FAIL`, `PENDING`, `NOT_RUN`, `NOT_APPLICABLE`, or `UNKNOWN` |
| Evidence adequacy | The result supports the exact claim being made |
| Review state | Qualified review is complete for a defined scope |
| Release state | A governed release decision exists |
| Publication state | A public-safe product is exposed through governed delivery |
| Production parity | The released behavior matches the deployed environment |

A change may be well documented while unimplemented, implemented while unverified, verified for a narrow fixture while not release-ready, or released while not yet published.

[Back to top](#top)

---

## Quality operating posture

KFM quality is not a single score. It is the inspectable relationship among a claim, its scope, its evidence, its checks, its limitations, and its correction path.

| Quality dimension | Minimum question | Primary evidence owner |
|---|---|---|
| Semantic correctness | Does behavior preserve the accepted meaning and invariants? | [`contracts/`](../../contracts/README.md) plus implementation and tests |
| Machine conformance | Does the object satisfy the current machine shape and cross-field rules? | [`schemas/`](../../schemas/README.md), validators, fixtures, and tests |
| Evidence integrity | Can consequential claims resolve through `EvidenceRef` to the required `EvidenceBundle`? | Governed evidence contracts, stores, resolvers, and tests |
| Policy and safety | Are rights, sensitivity, access, source role, and public-path constraints enforced fail-closed? | [`policy/`](../../policy/README.md), reviewers, negative tests, and runtime boundaries |
| Determinism and replay | Can the same governed inputs reproduce the same identity and result where practical? | Implementation, fixtures, receipts, replay checks, and generated manifests |
| Reliability | Are failures finite, observable, diagnosable, and free of unsafe fallback? | Applications, packages, runtime, tests, validators, workflows, and runbooks |
| Performance | Are declared budgets measured under a named profile without hiding trust or accessibility state? | Owning app/runtime plus performance fixtures, validators, and evidence |
| Accessibility and usability | Can users understand content, negative states, scope, time, and evidence without relying on color or hidden context? | UI implementation, accessibility tests, review, and user-facing docs |
| Security and privacy | Are secrets, sensitive data, harmful precision, and untrusted execution bounded? | Security guidance, policy, implementation, tests, workflows, and review |
| Compatibility | Are consumers, identifiers, aliases, migrations, and generated outputs kept coherent? | Contracts, schemas, implementation, migration records, and tests |
| Correction and rollback | Can incorrect or unsafe state be corrected, withdrawn, superseded, and rolled back visibly? | [`release/`](../../release/README.md), accountability objects, consumers, and drills |

> [!CAUTION]
> Optimize quality in dependency order. Provenance, policy, validation, source integrity, reversibility, and public safety outrank cosmetic polish. Performance work must not remove evidence visibility, deny states, accessibility, or correction context merely to improve a metric.

### Quality claim contract

A material quality claim should identify:

1. the exact revision, artifact, environment, and scope;
2. the property being checked and the authority that defines it;
3. the command, workflow, fixture, or observation used;
4. the expected finite outcome and stable failure reason;
5. the actual result;
6. known omissions, inherited failures, and untested consumers;
7. whether network, time, randomness, credentials, or external services were involved;
8. the reviewer or owner role still required; and
9. the correction or rollback path if the claim is wrong.

[Back to top](#top)

---

## What belongs here

Appropriate content includes:

- quality doctrine and review guidance that spans more than one executable surface;
- bounded quality budgets whose measurement and authority remain explicit;
- explanations of validation classes, result grammar, claim limits, and evidence requirements;
- quality-focused architecture notes that link to the contracts, schemas, policy, implementation, fixtures, tests, validators, workflows, receipts, proofs, and releases they depend on;
- maintainership guidance for deterministic checks, negative paths, failure attribution, correction, and rollback;
- quality debt, drift, and verification backlogs when their status and owning authority are clear; and
- human-readable interpretation of quality signals without turning those signals into sovereign truth.

A quality document should be reviewable without inventing a command, owner, status, threshold, route, workflow, release, or implementation claim.

[Back to top](#top)

---

## What does not belong here

Do not place these artifact families under `docs/quality/`:

- executable tests or reusable test fixtures;
- validator, scanner, benchmark, profiler, or instrumentation code;
- GitHub Actions or other CI orchestration;
- semantic contracts, machine schemas, or policy rules;
- application, package, runtime, connector, pipeline, or infrastructure implementation;
- canonical evidence, source registry records, receipts, proofs, manifests, release decisions, rollback cards, or published payloads;
- generated reports, coverage output, screenshots, trace dumps, browser recordings, or benchmark artifacts without a separately governed generated-output home;
- secrets, private incident details, restricted data, harmful precision, or credentials; or
- a second copy of guidance already owned by security, standards, runbooks, release, tests, or validators.

When documentation discovers a defect in another responsibility root, link the defect to its owner or open scoped follow-up work. Do not silently move executable or authority-bearing material into `docs/quality/`.

[Back to top](#top)

---

## Responsibility and authority map

| Concern | Owning surface | Role of `docs/quality/` |
|---|---|---|
| Human-readable quality guidance | This lane under [`docs/`](../README.md) | Explain, index, and bound claims |
| Placement and documentation inheritance | Accepted Directory Rules and the parent docs contract | Apply; do not amend implicitly |
| Semantic meaning | [`contracts/`](../../contracts/README.md) | Cite; do not redefine |
| Machine shape | [`schemas/`](../../schemas/README.md) | Cite; do not duplicate |
| Allow, deny, hold, restrict, redact, or abstain | [`policy/`](../../policy/README.md) plus governed review | Explain expected quality implications |
| Executable conformance | [`tests/`](../../tests/README.md) | Route readers to bounded evidence |
| Reusable validation logic | [`tools/validators/`](../../tools/validators/README.md) | Reference current entry points and claim limits |
| CI orchestration and check names | [`.github/workflows/`](../../.github/workflows/) | Link to current workflow definitions; do not redefine required-check semantics |
| Repository-wide command routing | Root [`Makefile`](../../Makefile) and declared project configuration | Cite commands verified at the inspected revision |
| Source identity and evidence | Governed source/evidence authorities | Require resolution; do not create support |
| Receipts, proofs, and lifecycle accountability | Governed `data/` accountability families | Reference immutable records; do not author them here |
| Release, correction, withdrawal, rollback | [`release/`](../../release/README.md) | Explain prerequisites and hand off decisions |
| Runtime metrics and user-facing behavior | Owning `apps/`, `packages/`, `runtime/`, and `infra/` surfaces | State expected quality and require observed evidence |
| Security and exposure guidance | [`docs/security/`](../security/README.md) and owning enforcement surfaces | Cross-link; do not dilute fail-closed posture |
| Standards profiles | [`docs/standards/`](../standards/README.md) | Cite applicable standards; do not claim conformance without evidence |

[Back to top](#top)

---

## Direct-child map

Directory Rules require a boundary README to describe only the directory it governs and its direct children.

```text
docs/quality/
├── README.md
└── maplibre-perf-governance.md
```

| Direct child | Responsibility | Claim boundary |
|---|---|---|
| [`README.md`](./README.md) | Lane purpose, authority boundary, navigation, evidence grammar, validation routing, and review triggers | Documentation only; no executable, policy, release, or publication authority |
| [`maplibre-perf-governance.md`](./maplibre-perf-governance.md) | Human-readable MapLibre performance budgets, trust-preserving measurement guidance, and quality-gate context | Budget prose and named checks must be reverified against current implementation, Makefile targets, validators, workflows, and artifacts before operational reliance |

No direct child directory existed at the inspected base. A proposed benchmark, report, asset, or archive directory is not current merely because a future document mentions one.

[Back to top](#top)

---

## Quality evidence and result grammar

### Validation classes

| Class | Meaning | Completion effect |
|---|---|---|
| `REQUIRED_CHANGED_AREA` | Repository-native checks for changed behavior and direct dependencies | Expected before delivery; required before ready-for-review when applicable |
| `REQUIRED_SAFETY` | Secret, rights, sensitivity, policy, destructive-change, or unsafe-execution checks | Must pass before the related change leaves the workspace |
| `REQUIRED_DELIVERY` | Branch, commit, bytes, diff, and pull-request identity checks | Must pass for any claimed remote delivery |
| `HOSTED_CI` | Required or informative server-side checks | May be pending on a draft PR; required checks must pass before ready-for-review |
| `OBSERVATIONAL` | External links, optional integrations, unrelated existing status, or non-blocking measurements | May remain pending, unknown, not run, or not applicable when disclosed |

### Result states

Use these states rather than collapsing every condition into pass/fail:

| State | Meaning |
|---|---|
| `PASS` | The declared check passed for the named scope and revision |
| `FAIL` | The declared criterion failed and must be attributed |
| `PENDING` | The check is expected but has not completed |
| `NOT_RUN` | The check was not executed; the reason must be stated |
| `NOT_APPLICABLE` | The check does not apply to the changed scope |
| `UNKNOWN` | Available evidence cannot establish the state |

Qualify failures as introduced, repaired, inherited, unrelated, or unobserved. Never weaken a required check after seeing it fail, and never report a readiness marker or zero-exit placeholder as quality evidence.

[Back to top](#top)

---

## Validation and repository checks

Choose the smallest repository-native check set that supports the changed claim. Inspect command bodies before execution and keep repository tests no-network by default unless an explicitly bounded integration profile says otherwise.

### Documentation-only change in this lane

```bash
printf '%s\n' docs/quality/README.md > /tmp/kfm-quality-changed-paths.txt
CHANGED_PATH_FILE=/tmp/kfm-quality-changed-paths.txt make validator-changed-area
make repository-topology
```

These commands validate the current registry-selected changed area and the repository-topology ratchet. They do not establish link health, semantic truth, policy approval, release readiness, or publication.

### Validator registry or workflow references changed

```bash
make validator-registry-check
make workflow-security
```

Run these when documentation changes depend on validator registration or workflow-security claims. A passing result proves only the bounded registry or workflow-security rules encoded at that revision.

### MapLibre performance guidance changed

```bash
make maplibre-govern
```

Run `make maplibre-proof` only when the governed scope includes the performance proof pack and its generated release-adjacent artifacts. Do not create or refresh proof artifacts merely to make documentation appear current.

### Broader trust-spine confidence

```bash
make validator-focused
```

Use the focused profile when the change materially affects cross-cutting quality doctrine or trust-bearing references. Full-profile validation is required only when repository policy, impact, or acceptance criteria make it material.

### Hosted pull-request checks

The current [`validator-suite`](../../.github/workflows/validator-suite.yml) workflow runs on pull requests with read-only repository permissions. Its logs and conclusion are CI evidence for the checks it names. They are not a `ValidationReport`, receipt, proof, policy decision, release record, or published artifact.

> [!WARNING]
> Do not copy command names from older documentation without checking the current Makefile, validator registry, workflow, and target implementation. A stale command is a documentation defect, not an invitation to create a compatibility alias without review.

[Back to top](#top)

---

## Review triggers and maintenance

Review this README and its direct child when any of these changes occur:

- the parent `docs/` boundary or adopted Directory Rules change;
- `quality/` is proposed for canonical reclassification, migration, consolidation, or retirement;
- a direct child is added, renamed, generated, moved, superseded, or deleted;
- quality result states, validation classes, check names, or command entry points change;
- a documented budget, threshold, environment, fixture, workflow, or validator changes;
- a quality claim gains or loses an implementation, evidence, policy, release, or public-surface dependency;
- a new security, rights, sensitivity, accessibility, reliability, performance, or correction obligation becomes material;
- an inbound link, stable heading, or related authority path changes; or
- hosted CI reveals that a documented command or boundary is stale.

### Maintenance rules

- Pin implementation claims to an exact revision or clearly mark them `NEEDS VERIFICATION`.
- Preserve stable headings when practical; repair authorized inbound links when headings change.
- Keep examples synthetic, deterministic, rights-safe, and no-network unless their integration classification is explicit.
- Record pre-existing failures separately from failures introduced by the documentation change.
- Update the owning implementation, test, validator, workflow, contract, schema, policy, or release surface when the documentation would otherwise become false.
- Do not use spare documentation scope for unrelated cleanup.
- Prefer a transparent correction over silent wording that hides a quality gap.

[Back to top](#top)

---

## Related surfaces

| Surface | Why it matters |
|---|---|
| [`docs/README.md`](../README.md) | Parent documentation authority, child-lane classification, and inherited README contract |
| [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) | Adopted placement, boundary, dependency, generated-output, and README rules |
| [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption authority for the exact Directory Rules v2 bytes |
| [`control_plane/root_registry.yaml`](../../control_plane/root_registry.yaml) | Machine projection of root responsibilities; it does not classify every docs child lane |
| [`tests/README.md`](../../tests/README.md) | Canonical executable-conformance boundary and bounded “passing does not prove” posture |
| [`tools/validators/README.md`](../../tools/validators/README.md) | Validator responsibilities, finite outcomes, and non-authority limits |
| [`validator-suite.yml`](../../.github/workflows/validator-suite.yml) | Current aggregate pull-request validator workflow and read-only trust boundary |
| [`Makefile`](../../Makefile) | Current repository-owned command routing and readiness-marker warnings |
| [`docs/security/README.md`](../security/README.md) | Security, exposure, sensitive-data, deny-test, and incident-guidance boundary |
| [`docs/standards/README.md`](../standards/README.md) | Human-readable standards profiles and conformance context |
| [`release/README.md`](../../release/README.md) | Release, promotion, correction, withdrawal, and rollback decision boundary |
| [`maplibre-perf-governance.md`](./maplibre-perf-governance.md) | Current direct quality-governance document for MapLibre performance |

[Back to top](#top)

---

## Correction, rollback, and last evidence review

**Last evidence review:** 2026-08-16 against `main@46a6fb9d8abad66c1d7df98717d4e6ea4a057660`.

Before merge, rollback is to close or abandon the unmerged pull request and retain the baseline branch. After merge, use a transparent revert or forward-fix pull request against the actual merged commit; never rewrite shared history.

A documentation rollback does not undo a validator result, release, deployment, publication, cache entry, or consumer reliance. When incorrect quality guidance affected another system, correct the owning contract, schema, policy, implementation, fixture, test, validator, workflow, receipt, proof, release, public artifact, or runbook as required, and preserve the relevant correction and supersession lineage.

Open items remain:

- `NEEDS VERIFICATION`: accountable quality stewardship and independent review assignment;
- `NEEDS VERIFICATION`: whether `docs/quality/` should remain an existing non-canonical child lane or receive a future adopted classification;
- `NEEDS VERIFICATION`: complete inbound-link and hosted-render validation for this lane;
- `UNKNOWN`: current required-check/ruleset coupling for quality-related workflows; and
- `UNKNOWN`: production quality, release readiness, deployment state, publication state, and public parity.

[Back to top](#top)
