<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy-test-readme
title: policy/test/ — Singular Policy-Test Compatibility Hold
type: readme
version: v1.0.0
status: draft; routing-and-hold; compatibility-unaccepted; implementation-empty; evaluator-unbound; non-release; non-publication
owner: NEEDS VERIFICATION — policy and test stewardship plus independent approval controls are not established
created: 2026-08-28
updated: 2026-08-28
current_path: policy/test/README.md
owning_root: policy/
policy_label: public; policy; test-routing; compatibility-hold; non-release; non-publication
responsibility: Explain the repository-present singular policy/test lane, route executable tests and reusable fixtures to their accepted roots, and prevent placeholder drift from becoming parallel test or fixture authority.
base_commit: 010de13f1604264b15376ae50dd8b16d8c9c86d6
truth_posture: CONFIRMED tracked singular lane containing only fixture/.gitkeep and a one-byte fixture README before this revision; no executable test, fixture payload, runner, evaluator, workflow binding, result, receipt, release, or public consumer under this path / CONFIRMED accepted root tests and fixtures responsibilities plus a separately documented plural policy/tests hold / HOLD singular-versus-plural convergence, compatibility status, ownership, consumers, migration, and retirement / UNKNOWN external references, repository-setting coupling, and accepted reviewer route
[/KFM_META_BLOCK_V2] -->

# Singular policy-test compatibility hold

> **Safe current conclusion:** `policy/test/` is a repository-present placeholder path, not an admitted test or fixture authority. At `main@010de13f1604264b15376ae50dd8b16d8c9c86d6`, it contains only [`fixture/`](./fixture/) with `.gitkeep` and a one-byte README. New executable policy tests belong under root [`tests/`](../../tests/README.md), normally [`tests/policy/`](../../tests/policy/README.md); reusable synthetic inputs belong under root [`fixtures/`](../../fixtures/README.md).

> [!CAUTION]
> The broad [`policy-test`](../../.github/workflows/policy-test.yml) workflow guards executable payloads beneath `policy/tests/` and `policy/fixtures/`, but it does **not** scan this singular path. A green workflow therefore provides no direct containment evidence for `policy/test/`.

## Purpose

This README closes a documentation gap without deciding whether the singular lane should be retained, migrated, or retired. It:

1. records the exact current contents and their maturity;
2. distinguishes this path from [`policy/tests/`](../tests/), root [`tests/policy/`](../../tests/policy/), and the colocated native Rego exception;
3. routes new tests and fixtures to their accepted responsibility roots;
4. preserves the unresolved `test/` versus `tests/` naming decision; and
5. states the evidence required before any executable content, alias, migration, or deletion.

It does not create a test framework, fixture profile, policy rule, bundle, evaluator, consumer, required check, release gate, or publication surface.

## Current status

| Question | Evidence-backed answer |
|---|---|
| Placement | **HOLD / NEEDS DIRECTORY REVIEW** |
| Current payload | `fixture/.gitkeep` and a documentation boundary only |
| Executable tests | None |
| Reusable fixture payloads | None |
| Runner or evaluator | None |
| Direct workflow coverage | None; `policy-test.yml` does not inspect this singular lane |
| Canonical test home | Root [`tests/`](../../tests/README.md) |
| Canonical reusable-fixture home | Root [`fixtures/`](../../fixtures/README.md) |
| Policy authority | Root `policy/` governs rules, not test results or fixture truth |
| Release or publication effect | None |

Path presence and a README are not implementation maturity. Passing tests elsewhere do not admit this lane or establish an evaluator.

## Directory map

```text
policy/test/
├── README.md
└── fixture/
    ├── .gitkeep
    └── README.md
```

The child boundary remains documentation-only. No `.py`, `.sh`, `.rego`, JSON fixture, expected output, manifest, result, or runner configuration is tracked below this path.

## Authority and routing

| Need | Route | Current evidence limit |
|---|---|---|
| Executable policy or trust-boundary conformance | [`tests/policy/`](../../tests/policy/README.md) | Tests prove only declared assertions at a checked revision. |
| Reusable valid, invalid, deny, abstain, or golden inputs | [`fixtures/`](../../fixtures/README.md), under the owning family | Fixtures are synthetic test carriers, not source truth or decisions. |
| A native test inseparable from one reviewed Rego profile | [`policy/rego/release_gate_v1_test.rego`](../rego/release_gate_v1_test.rego) | One bounded, checksum-pinned exception-shaped lane; not a general colocation rule. |
| Policy-local placeholder documentation | [`policy/tests/`](../tests/) and this path | Both remain held; neither may become a second executable authority. |
| Workflow orchestration | [`.github/workflows/`](../../.github/workflows/README.md) | Workflow presence or success is not required-check, review, release, or publication evidence. |

Accepted Directory Rules separate normative policy source under `policy/` from executable conformance under `tests/` and reusable inputs under `fixtures/`. Because both `policy/test/` and `policy/tests/` already exist, prose must not silently choose an alias or migration result. The finite outcome remains **HOLD** until a reviewed path decision identifies one owner, canonical target, consumers, compatibility behavior, exit criteria, and rollback.

## What may be added

While the path is held, additions are limited to:

- corrections to this routing and evidence boundary;
- verified reference or consumer inventories;
- an accepted path-decision or migration record reference;
- compatibility and retirement evidence; and
- link-preserving tombstone guidance after an accepted decision.

Do not add executable code, Rego, reusable fixtures, golden outputs, snapshots, real or sensitive records, secrets, generated reports, policy decisions, receipts, proofs, release objects, deployment configuration, or public-client assets.

## Validation

From the repository root, inspect the singular and neighboring lanes with:

```bash
git ls-tree -r --name-only HEAD -- \
  policy/test policy/tests policy/fixtures tests/policy policy/rego

find policy/test -type f \
  ! -name 'README.md' \
  ! -name '.gitkeep' \
  -print
```

For the current held posture, the `find` command must print nothing. If it prints a path, stop and verify placement, ownership, consumers, fixture safety, deterministic execution, workflow coverage, and rollback before treating the payload as legitimate.

Confirmed bounded execution surfaces remain separate:

```bash
# Structural/static policy boundary evidence.
make boundary-guards-ci

# One bounded native Rego profile; use the reviewed OPA 1.19.0 binary.
opa test policy/rego/release_gate_v1.rego \
  policy/rego/release_gate_v1_test.rego
```

These commands do not exercise `policy/test/`. Their success cannot establish this path's authority, admit a fixture, activate policy, approve review, release, deploy, promote, or publish.

README-focused acceptance checks are:

- exactly one H1 and a logical heading hierarchy;
- balanced fenced code blocks and tables;
- all repository-relative links resolve with correct case;
- the current tree contains no unreported executable or fixture payload;
- the parent [`policy/README.md`](../README.md) reports the same counts and hold posture; and
- the diff changes no policy rule, test, fixture payload, workflow, evaluator, release, or publication behavior.

## Safety and evidence limits

Any future policy-test input must be synthetic, minimized, or irreversibly generalized. Living-person data, DNA/genomics, private land, protected cultural material, exact sensitive locations, credentials, or restricted source payloads must not be copied here.

A fixture can model `RAW`, `WORK/QUARANTINE`, `PROCESSED`, `CATALOG/TRIPLET`, or `PUBLISHED` shapes without acquiring that lifecycle state. A test can model admission, promotion, release, correction, or rollback without performing those transitions. Public clients must not read repository tests, fixtures, policy source, internal registries, or workflow output as live truth.

## Admission or convergence gate

Before this lane gains executable content or changes identity, a reviewed decision must establish:

1. the single responsibility and why canonical root `tests/` or `fixtures/` cannot own it;
2. `PLACE`, `MIGRATE`, `MIRROR`, `HOLD`, or `DENY` outcome under accepted placement governance;
3. all known writers, readers, imports, links, external consumers, and stale references;
4. canonical target, compatibility mode, single-write rule, and exit criteria;
5. synthetic fixture identity, sensitivity, rights, retention, and expected polarity;
6. deterministic command, pinned dependencies, no-network posture, and non-vacuous negative cases;
7. workflow invocation and current repository-setting evidence;
8. correction, replay, migration, and rollback procedure; and
9. accountable policy, test, fixture, security, domain, and independent review.

A README, `.gitkeep`, green workflow, merge, or generated receipt cannot satisfy this gate by itself.

## Correction and rollback

This revision changes documentation only. Before merge, close its draft pull request and abandon the feature branch. After merge, prefer a focused corrective pull request. Do not restore the missing parent or one-byte child documentation as a shortcut, and do not move or delete either singular or plural lane without an accepted path decision and verified reference closure.

Correcting documentation does not remove sensitive data, reverse a decision, invalidate an external consumer, roll back a release, or withdraw published material. Those actions require their owning procedures and evidence.

## Open verification register

| ID | Question | Current posture |
|---|---|---|
| PTEST-S-001 | Should `policy/test/` be retained, migrated to `policy/tests/`, or retired in favor of canonical roots? | **HOLD / NEEDS DIRECTORY REVIEW** |
| PTEST-S-002 | Which repository and external consumers still reference the singular path? | **UNKNOWN** |
| PTEST-S-003 | Why does the singular lane contain `fixture/` while reusable inputs belong under root `fixtures/`? | **PLACEHOLDER DRIFT / NEEDS DECISION** |
| PTEST-S-004 | Should the broad readiness workflow explicitly guard this path before retirement? | **PROPOSED / NOT IMPLEMENTED** |
| PTEST-S-005 | Who owns policy-test placement, fixture safety, evaluator semantics, and independent approval? | **NEEDS VERIFICATION** |

## Related surfaces

- [Policy root boundary](../README.md)
- [Plural policy-tests hold](../tests/README.md)
- [Singular fixture child hold](./fixture/README.md)
- [Canonical test root](../../tests/README.md)
- [Canonical policy test lane](../../tests/policy/README.md)
- [Canonical fixture root](../../fixtures/README.md)
- [Policy-local fixture hold](../fixtures/README.md)
- [Broad policy readiness workflow](../../.github/workflows/policy-test.yml)
- [Accepted Directory Rules decision](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)

## Changelog

| Version | Date | Change |
|---|---|---|
| v1.0.0 | 2026-08-28 | Establishes the singular lane as a documented compatibility hold, records the unguarded placeholder state, routes tests and fixtures to accepted roots, and preserves migration and retirement decisions for reviewed follow-up. |
