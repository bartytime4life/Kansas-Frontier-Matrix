<a id="top"></a>

# policy :: tests

> **One-line purpose.** `policy/tests/` documents a held, policy-local test placeholder and routes executable conformance work to its admitted home; it is not an independent test authority, policy evaluator, fixture registry, release gate, or publication surface.

**Quick navigation:** [Purpose](#purpose) · [Status](#status) · [Placement](#placement-and-authority) · [Directory map](#current-direct-child-map) · [Belongs](#what-belongs-here) · [Routing](#test-and-fixture-routing) · [Validation](#validation) · [Admission](#admission-and-graduation-gate) · [Review](#ownership-and-review) · [Rollback](#correction-and-rollback) · [Open work](#open-verification-register)

> [!IMPORTANT]
> **Current safe conclusion:** this directory is a documentation-and-placeholder boundary only. At the evidence snapshot, its tracked descendants are this README plus two empty lanes retained by `.gitkeep`; no executable policy test, runner configuration, fixture, result, or accepted local test convention is present here.

> [!CAUTION]
> Do not add `.py`, `.sh`, `.rego`, test fixtures, generated reports, or authoritative policy outcomes here merely because the path is named `tests`. Accepted Directory Rules make root [`tests/`](../../tests/README.md) the canonical home for executable conformance and root [`fixtures/`](../../fixtures/README.md) the canonical home for reusable test inputs. The current [`policy-test`](../../.github/workflows/policy-test.yml) readiness workflow also fails if executable test or evaluator payloads appear under `policy/tests/` without deliberate graduation.

---

## Purpose

This README provides a compact, evidence-grounded boundary for `policy/tests/` while the repository resolves whether the path should be retired, migrated, or admitted as a narrowly governed compatibility or colocation lane.

It answers four practical questions:

1. What is actually present here now?
2. Where should new policy-related tests and fixtures go?
3. What review is required before this path can acquire executable content?
4. What does a passing test prove—and what does it never authorize?

The directory inherits its posture from [`policy/`](../README.md). Policy source decides admissibility; tests exercise bounded behavior. Neither a file path nor a passing test creates evidence, approves a release, clears rights or sensitivity, authenticates human review, or publishes KFM material.

**Local scope ID:** `path:policy/tests/` — repository-path identity only; no independent object-family or authority ID is accepted.

[Back to top](#top)

---

## Status

| Field | Current posture |
|---|---|
| README profile | `BOUNDARY_COMPACT` under Directory Rules §16.3 |
| Placement | Existing child of canonical `policy/`; same-path documentation update |
| Implementation maturity | **CONFIRMED placeholder-only** |
| Authority | **None independently**; inherits the policy root and defers executable-test authority to root `tests/` |
| Decision posture | **HOLD / NEEDS DIRECTORY REVIEW** |
| Owner signal | `@bartytime4life` is the confirmed CODEOWNERS review route for `/policy/`; stewardship assignment and independent approval remain **NEEDS VERIFICATION** |
| Exposure | Public repository documentation and empty markers only; all committed content must remain public-safe |
| Mutation | Versioned repository change through review |
| Retention | No independent retention entitlement; preserve until a reviewed migration, retirement, or bounded admission decision is recorded |
| Runtime effect | **None** |
| Release or publication effect | **None** |

### Evidence labels used here

| Label | Meaning |
|---|---|
| **CONFIRMED** | Verified against current repository files or an accepted decision at the pinned snapshot |
| **PROPOSED** | A possible future design or disposition; not current implementation |
| **NEEDS VERIFICATION** | Checkable, but not established strongly enough to treat as fact |
| **HOLD** | Do not expand the lane until the named placement or authority question is resolved |

### Current implementation evidence

| Surface | Observed state | Safe interpretation |
|---|---|---|
| `policy/tests/README.md` | 43-byte greenfield stub before this revision | The path existed, but the stub established no test contract or implementation. |
| `policy/tests/domains/fauna/.gitkeep` | Empty marker | Path presence only; no fauna policy test exists here. |
| `policy/tests/flora/.gitkeep` | Empty marker | Path presence only; no flora policy test exists here. |
| Executable extensions under `policy/tests/` | None observed | No local runner, suite, evaluator, or executable convention is implemented. |
| Open pull requests overlapping this path | None observed before authoring at the pinned snapshot | No active PR survivor or consolidation target was identified; this is not proof that all unmerged branches are conflict-free. |

Directory Rules `DIR-ROOT-005` and `DIR-README-002` are controlling guardrails: a README and `.gitkeep` do not establish implementation or maturity.

[Back to top](#top)

---

## Placement and authority

Accepted [`ADR-0029`](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) makes [`docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md) the canonical human-readable Directory Rules authority. Its machine projection in [`control_plane/root_registry.yaml`](../../control_plane/root_registry.yaml) separates the relevant responsibilities:

| Responsibility | Canonical home | Consequence for `policy/tests/` |
|---|---|---|
| Normative allow, deny, hold, restrict, and abstain rules | [`policy/`](../README.md) | This lane cannot become a second policy root or store decision instances. |
| Executable conformance, boundary, negative, integration, and end-to-end evidence | [`tests/`](../../tests/README.md) | New general policy tests route to [`tests/policy/`](../../tests/policy/README.md). |
| Reusable synthetic, valid, invalid, and golden inputs and expected outputs | [`fixtures/`](../../fixtures/README.md) | New reusable policy fixtures route under `fixtures/policy/`, not here. |
| Repository-wide validators and test operators | [`tools/`](../../tools/README.md) | Shared test tooling does not belong in this lane. |
| Workflow orchestration | [`.github/workflows/`](../../.github/workflows/README.md) | Workflow YAML and check configuration remain platform integration, not local test content. |
| Release, correction, withdrawal, and rollback decisions | [`release/`](../../release/README.md) | A test result may support review but cannot approve or publish. |

Directory Rules §9.3 also keeps meaning, machine shape, and admissibility separate: contracts define meaning, schemas define valid shape, and policy defines what is allowed. Tests exercise those authorities without replacing them.

### Parallel-lane drift

The repository currently contains all three of these patterns:

| Path | Current evidence | Posture |
|---|---|---|
| `tests/policy/` | Executable Python policy and trust-boundary suites plus a substantial boundary README | **Canonical executable test lane** under root `tests/` |
| `policy/rego/release_gate_v1_test.rego` | One bounded native Rego test beside its reviewed rule and a dedicated checksum-pinned OPA workflow | **Confirmed exception-shaped implementation; not a general convention** |
| `policy/test/fixture/` | `.gitkeep` and a blank README | **Placeholder drift / NEEDS DIRECTORY REVIEW** |
| `policy/tests/` | This boundary README and empty markers | **Placeholder drift / HOLD** |

The coexistence of `test/`, `tests/`, root `tests/`, and a colocated Rego test must not be normalized by documentation alone. Any convergence must preserve references, review the native-runner constraint, and avoid two writable homes for the same responsibility.

[Back to top](#top)

---

## Current direct-child map

Verified against `main@0358516e7deaefaf3cbc8a2d7752ff174e1937e2`:

```text
policy/tests/
├── README.md              # boundary contract; no executable authority
├── domains/               # placeholder container; no admitted test payload
└── flora/                 # placeholder lane; no admitted test payload
```

Per Directory Rules `DIR-README-003`, this map shows direct children only. The deeper marker at `domains/fauna/.gitkeep` does not make `fauna/` implemented, and `flora/.gitkeep` does not make `flora/` implemented.

> [!NOTE]
> The asymmetric paths `domains/fauna/` and `flora/` are recorded as observed state, not endorsed taxonomy. Do not add more domain folders by copying either pattern while the placement decision remains open.

[Back to top](#top)

---

## What belongs here

While the lane is on **HOLD**, only narrowly bounded content belongs here:

- this README and corrections to its evidence-grounded boundary;
- public-safe navigation or compatibility notices needed to prevent misplacement;
- existing empty markers until a reviewed convergence decision disposes of them;
- migration pointers, if a future accepted path decision requires them and names an owner, canonical target, and exit condition.

Content belongs here because it preserves or explains this boundary—not because it concerns policy or tests.

### What is prohibited

| Do not place here | Route or reason |
|---|---|
| General executable policy tests | [`tests/policy/`](../../tests/policy/README.md) |
| New colocated Rego tests by analogy | Require a reviewed native-runner exception; the current release-gate test is not blanket authority |
| Policy modules or bundles | The owning policy family under [`policy/`](../README.md) |
| Reusable valid, invalid, deny, abstain, or golden fixtures | [`fixtures/`](../../fixtures/README.md), normally a bounded `fixtures/policy/` family |
| Test-local reusable helper libraries | The appropriate `tests/`, `packages/`, or `tools/` lane by responsibility |
| Schemas, contracts, or duplicated outcome vocabularies | [`schemas/`](../../schemas/README.md), [`contracts/`](../../contracts/README.md), or the accepted policy family |
| Decision instances, receipts, proofs, approvals, manifests, or releases | Their governed data, proof, receipt, or [`release/`](../../release/README.md) family |
| Workflow YAML or required-check configuration | [`.github/workflows/`](../../.github/workflows/README.md) and repository settings |
| Generated JUnit, coverage, logs, caches, or downloaded tools | Ephemeral CI or governed artifact storage; never this source lane |
| Secrets, real sensitive records, exact sensitive locations, or restricted source payloads | Prohibited from public test content; use reviewed synthetic or generalized fixtures |

[Back to top](#top)

---

## Inputs and outputs

### Current inputs

This placeholder has no runtime or evaluator inputs. The README is maintained from:

- the exact repository tree and target blob;
- the parent [`policy/` contract](../README.md);
- accepted Directory Rules and ADR-0029;
- the root registry and CODEOWNERS routing;
- executable evidence in `tests/policy/`, `policy/rego/`, and the associated workflows.

### Current outputs

The only current output is human-readable placement guidance. It emits no test result, `PolicyDecision`, receipt, proof, review record, release decision, artifact, deployment, or publication.

If executable content is ever admitted, each result must name the system under test, command and version, fixture identity, expected polarity, checked revision, and authority limit. Generated reports remain non-authoritative unless a separate governed process promotes them into an accepted record family.

[Back to top](#top)

---

## Test and fixture routing

Use the primary assertion—not topical proximity—to choose a path.

| Question being proved | Route | Current executable evidence |
|---|---|---|
| Does a repository boundary prevent connectors or pipelines from publishing, preserve control-plane metadata, or protect a governed API seam? | [`tests/policy/`](../../tests/policy/README.md) | [`policy-boundary-guards`](../../.github/workflows/policy-boundary-guards.yml) runs `make boundary-guards-ci` over 18 bounded structural/static/API tests. |
| Does the Pass 12 release-gate rule allow or deny explicit native inputs with deterministic reasons? | [`policy/rego/release_gate_v1_test.rego`](../rego/release_gate_v1_test.rego) | [`pass12-release-policy-v1`](../../.github/workflows/pass12-release-policy-v1.yml) formats and tests the bounded Rego pair with checksum-pinned OPA 1.19.0 and verifies fixture polarity. |
| Does a policy contract or schema accept and reject deterministic instances? | Root `tests/` plus [`fixtures/`](../../fixtures/README.md) under the owning family | Follow the contract/schema fixture harness and validator lane; do not duplicate fixtures here. |
| Does a policy validator preserve shape and semantic invariants? | `tests/validators/` paired with `tools/validators/policy/` | Use the validator-specific test and workflow already associated with that profile. |
| Does a public or release path enforce policy end to end? | The appropriate root integration/E2E lane | Local rule tests are necessary but not sufficient; include denial, correction, rollback, and public-safe diagnostics where material. |

### What passing evidence means

A passing test supports only its declared assertion, inputs, command, environment, and revision. It does not prove:

- the source claim is true or evidence-complete;
- rights, consent, sensitivity, or reviewer identity are valid;
- a policy bundle is active outside the tested entrypoint;
- branch protection requires the check;
- a lifecycle transition, release, deployment, or publication is authorized;
- production configuration or consumers match the test harness.

[Back to top](#top)

---

## Validation

### Boundary inventory

Use repository-native inspection before changing this lane:

```bash
git ls-tree -r --name-only HEAD -- policy/tests policy/test tests/policy policy/rego

find policy/tests -type f \
  \( -name '*.py' -o -name '*.sh' -o -name '*.rego' \) \
  -print
```

For the current placeholder posture, the second command must print nothing. The [`policy-test`](../../.github/workflows/policy-test.yml) readiness workflow enforces the same executable-extension hold across `policy/tests/` and `policy/fixtures/`.

### Confirmed bounded execution surfaces

```bash
# Canonical structural policy-boundary suite.
make boundary-guards-ci

# Bounded native Rego lane; requires the reviewed OPA version.
opa fmt --fail policy/rego/release_gate_v1.rego \
  policy/rego/release_gate_v1_test.rego
opa test policy/rego/release_gate_v1.rego \
  policy/rego/release_gate_v1_test.rego
```

The dedicated hosted Rego workflow downloads checksum-pinned OPA 1.19.0. A locally available `opa` binary must be provenance- and version-checked before its result is compared with hosted evidence.

### README acceptance checks

For a documentation-only revision, verify at minimum:

- exactly one H1;
- no broken repository-relative links or anchors;
- a current, direct-child-only directory map;
- no trailing whitespace, tabs used for prose alignment, or missing final newline;
- no claim that placeholders are executable or that workflow presence means a required check;
- exact one-file diff and unchanged test, fixture, workflow, policy, and release behavior.

> [!WARNING]
> The broad `policy-test` workflow intentionally records readiness holds. Its green outcome does not establish a repository-wide policy evaluator, bundle selector, runtime consumer, decision receipt, release approval, or publication authority.

[Back to top](#top)

---

## Admission and graduation gate

Executable content must not enter `policy/tests/` until a reviewed decision answers all of the following:

1. **Responsibility:** Why can the test not live in canonical `tests/policy/` or beside a rule under a narrowly accepted native-runner exception?
2. **Canonical target:** Is this path canonical, compatibility-only, or scheduled for retirement—and what prevents parallel writes?
3. **Scope:** Which policy package, entrypoint, and object family does the test exercise?
4. **Inputs:** Which synthetic fixtures, versions, digests, and positive/negative polarities are required?
5. **Command:** What deterministic, repository-native command collects and runs the test non-vacuously?
6. **Environment:** Which runner, dependency pins, network posture, filesystem effects, and time/randomness controls apply?
7. **Outputs:** Which diagnostics or reports are emitted, where are they retained, and why are they non-authoritative?
8. **Review:** Who owns the rule, test, fixtures, CI, sensitive-domain review, and independent approval?
9. **Integration:** Which workflow invokes the command, and is required-check status confirmed or still unknown?
10. **Migration and rollback:** How are old references preserved, duplicate paths frozen, and the change reverted safely?

Admission requires updates to the parent policy README, canonical test documentation, relevant fixture family, validation workflow, and path-decision record when those surfaces are affected. Adding a README or `.gitkeep` does not satisfy the gate.

### Minimum executable test contract

If a future decision admits a test here, each case must include:

- a stable name and bounded system-under-test reference;
- at least one meaningful positive case and the applicable deny, restrict, hold, abstain, invalid, stale, correction, or rollback cases;
- deterministic, public-safe inputs with no live-source dependency by default;
- explicit expected outcomes and stable reason/obligation assertions where applicable;
- a non-vacuity check proving the intended test was collected and executed;
- failure diagnostics that do not leak sensitive material;
- a statement of what passing does not prove.

[Back to top](#top)

---

## Exposure, mutation, and retention

| Dimension | Rule for this lane |
|---|---|
| Public exposure | Treat every committed byte, diff, log excerpt, and fixture reference as public. |
| Sensitivity | Use synthetic, redacted, or generalized examples only; never commit credentials, living-person data, DNA/genomic content, private-land joins, exact sensitive locations, or restricted payloads. |
| Mutation | Reviewed, versioned edits only. Do not generate or overwrite source content during a test run. |
| Storage | Source documentation and empty markers only at present; no caches, downloaded binaries, JUnit, coverage, screenshots, or test output. |
| Retention | Preserve history until a reviewed migration or retirement closes references; placeholder presence alone is not a retention reason. |
| Publication | A commit, pull request, check, merge, or test result is not KFM publication. |

[Back to top](#top)

---

## Ownership and review

Current [CODEOWNERS](../../.github/CODEOWNERS) routes `/policy/` and `/tests/` review requests to `@bartytime4life`. That routing is **not** proof of review, stewardship assignment, separation of duties, branch protection, or release approval.

Review this README and any future disposition with:

- the policy-family owner for admissibility meaning;
- the test or QA owner for executable evidence and runner behavior;
- the fixture and validator owner when shared inputs or tools change;
- the workflow owner when triggers, permissions, dependencies, artifacts, or check names change;
- security, rights, sensitivity, and domain reviewers when the tested boundary could expose protected material;
- release stewardship when the test is claimed as a promotion, correction, withdrawal, or rollback prerequisite.

Follow [`CONTRIBUTING.md`](../../CONTRIBUTING.md) and the repository pull-request template. Draft review remains the safe terminal state for governance-significant or AI-authored changes unless a maintainer explicitly authorizes progression.

[Back to top](#top)

---

## Related surfaces

| Surface | Relationship |
|---|---|
| [`policy/`](../README.md) | Inherited admissibility authority and parent boundary |
| [`tests/`](../../tests/README.md) | Canonical executable conformance root |
| [`tests/policy/`](../../tests/policy/README.md) | Canonical general policy and trust-boundary test lane |
| [`fixtures/`](../../fixtures/README.md) | Canonical reusable test-input root |
| [`policy/rego/`](../rego/) | Current bounded policy source plus one colocated native test |
| [`policy-test`](../../.github/workflows/policy-test.yml) | Static readiness and executable-payload hold |
| [`policy-boundary-guards`](../../.github/workflows/policy-boundary-guards.yml) | Bounded structural policy and trust-membrane suite |
| [`pass12-release-policy-v1`](../../.github/workflows/pass12-release-policy-v1.yml) | Bounded native Rego validation and fixture-polarity workflow |
| [Directory Rules](../../docs/doctrine/directory-rules.md) | Canonical placement and README-profile authority |
| [`ADR-0029`](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted adoption decision |

[Back to top](#top)

---

## Correction and rollback

This README changes documentation only. It does not move or delete placeholders, add tests or fixtures, alter a policy rule, change a workflow, select a bundle, approve a release, or publish material.

- **Before merge:** close the draft pull request and delete its feature branch if the boundary is rejected or superseded.
- **After merge:** revert the documentation commit, then rerun the same Markdown, link, anchor, and diff checks.
- **If placement changes later:** use a separately reviewed migration that freezes duplicate writers, records the canonical target, updates references atomically where practical, preserves history, verifies zero unintended consumers, and defines rollback before any deletion.
- **If a claim is found inaccurate:** prefer a transparent forward correction with a new evidence snapshot; do not silently rewrite executable or release history.

[Back to top](#top)

---

## Open verification register

| ID | Question | Current status | Closure evidence |
|---|---|---:|---|
| PTEST-001 | Should `policy/tests/` be retired, migrated, or admitted as a narrowly bounded compatibility/colocation lane? | **HOLD / NEEDS DIRECTORY REVIEW** | Accepted path decision naming responsibility, owner, target, writers, exit conditions, migration, and rollback |
| PTEST-002 | How should `policy/test/fixture/`, `policy/tests/`, root `tests/policy/`, and the colocated Rego test converge? | **NEEDS DECISION** | Zero-parallel-authority plan plus verified reference and consumer inventory |
| PTEST-003 | Is the native Rego colocation pattern a one-profile exception or an accepted repository convention? | **NEEDS VERIFICATION** | Accepted runner/placement contract and corresponding test-root documentation |
| PTEST-004 | Are `domains/fauna/` and `flora/` intentional distinct taxonomies or abandoned scaffolds? | **UNKNOWN** | Owner-confirmed domain-lane decision and migration/retirement disposition |
| PTEST-005 | Which policy-related workflows are required by branch protection or rulesets? | **UNKNOWN** | Current repository-setting evidence at an observed timestamp |
| PTEST-006 | Who supplies independent policy-test and sensitive-domain review beyond CODEOWNERS routing? | **NEEDS VERIFICATION** | Accepted stewardship assignments and enforced approval controls |

[Back to top](#top)

---

## Last evidence review

| Evidence | Snapshot |
|---|---|
| Repository base | `main@0358516e7deaefaf3cbc8a2d7752ff174e1937e2` |
| Prior target blob | `576646f0ae2d952dc30539feb709168abd326081` |
| Prior target content | `# policy :: tests` plus `Greenfield bundle stub.` |
| `policy/tests/` tree | `515fd948900ce460e9652a92866b2f010be30b58` |
| Directory Rules blob | `fd49a0b83e55cef52c1124281f093e263526898d` |
| Root-registry blob | `024f668b5f0a9239bafa4f8b09e2afd86300ff8c` |
| CODEOWNERS blob | `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61` |
| Review date | 2026-08-12 |

Re-review when any child path, executable extension, fixture, runner, workflow, CODEOWNERS route, repository control, accepted ADR, parent boundary, or canonical test-root contract changes—or when a migration, correction, security event, or rollback affects this lane.

### Changelog

| Edition | Date | Change |
|---|---|---|
| Greenfield stub | Before 2026-08-12 | Declared the path name and placeholder status only. |
| Boundary contract | 2026-08-12 | Expands the stub in place with current inventory, canonical routing, explicit hold, validation, admission gates, review burden, rollback, and open verification items; changes no executable behavior. |

<p align="right"><a href="#top">Back to top</a></p>
