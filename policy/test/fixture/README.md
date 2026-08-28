<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy-test-fixture-readme
title: policy/test/fixture/ — Singular Policy-Test Fixture Placeholder Hold
type: readme
version: v1.0.0
status: draft; routing-and-hold; placeholder-only; no-fixture-payload; no-consumer; non-release; non-publication
owner: NEEDS VERIFICATION — fixture, policy, test, and independent review ownership are not established
created: 2026-08-28
updated: 2026-08-28
current_path: policy/test/fixture/README.md
owning_root: policy/test/
policy_label: public; policy; fixture-routing; placeholder-hold; non-release; non-publication
responsibility: Explain the empty singular fixture child and prevent it from becoming a parallel reusable-fixture, policy-decision, or sensitive-data authority.
base_commit: 010de13f1604264b15376ae50dd8b16d8c9c86d6
prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
truth_posture: CONFIRMED one-byte README plus .gitkeep before this revision and no fixture payload, manifest, schema, validator, test, workflow, consumer, result, or release binding / CONFIRMED root fixtures owns reusable test inputs and policy/test remains a held singular compatibility lane / HOLD retention, migration, aliasing, or retirement / UNKNOWN external consumers and accepted stewardship
[/KFM_META_BLOCK_V2] -->

# Singular policy-test fixture placeholder hold

> **Current boundary:** `policy/test/fixture/` is empty placeholder drift. It is not a fixture registry, canonical test-input family, policy evaluator input store, source corpus, decision log, release record, or public asset.

## Current contents

```text
policy/test/fixture/
├── .gitkeep
└── README.md
```

At `main@010de13f1604264b15376ae50dd8b16d8c9c86d6`, the README was one byte and `.gitkeep` was the only other tracked file. No JSON, YAML, Rego input, expected result, snapshot, golden file, manifest, generator, validator, test, workflow, receipt, proof, or consumer is implemented here.

## Placement and authority

Reusable synthetic, valid, invalid, deny, abstain, and golden inputs belong under root [`fixtures/`](../../../fixtures/README.md), routed by their primary assertion and owning family. Executable conformance belongs under root [`tests/`](../../../tests/README.md), normally [`tests/policy/`](../../../tests/policy/README.md) for policy and trust-boundary assertions.

The parent [`policy/test/`](../) lane and plural [`policy/tests/`](../../tests/) lane are unresolved placeholders. Neither can authorize this child by proximity. Accepted Directory Rules prohibit parallel writable authority and make fixtures subordinate to contracts, schemas, policy, tests, evidence, review, release, correction, and rollback.

## Permitted changes

While held, this directory may contain only:

- this evidence and routing boundary;
- `.gitkeep` while the directory remains intentionally tracked;
- verified consumer or reference inventories;
- an accepted path-decision or migration reference; and
- reviewed tombstone guidance after migration or retirement is authorized.

Do not add:

- reusable or one-off fixture payloads;
- real people, DNA/genomic, private land, protected cultural, exact sensitive-location, infrastructure, credential, or restricted-source data;
- expected policy outcomes presented as authoritative decisions;
- executable tests, rules, validators, runners, or workflow configuration;
- generated reports, receipts, proofs, release objects, or published carriers; or
- files copied from Drive, Notion, AI output, dashboards, maps, or external sources without canonical admission.

## Contributor routing

| Proposed artifact | Correct starting point |
|---|---|
| Policy contract/schema valid and invalid cases | Accepted contract fixture family under root `fixtures/` plus root tests |
| Bounded Rego release-gate inputs | [`fixtures/policy/release_gate_v1/`](../../../fixtures/policy/release_gate_v1/) |
| PolicyDecision shape cases | [`fixtures/contracts/v1/policy/policy_decision/`](../../../fixtures/contracts/v1/policy/policy_decision/) |
| Domain-sensitive policy cases | Accepted synthetic domain fixture lane with domain and sensitivity review |
| Executable policy boundary assertions | [`tests/policy/`](../../../tests/policy/README.md) |

Do not create a new fixture family until its contract or policy authority, identity, version, expected polarity, consumer, validator/test, workflow, sensitivity, correction, and retention rules are reviewable.

## Validation

From the repository root:

```bash
git ls-tree -r --name-only HEAD -- policy/test/fixture

find policy/test/fixture -type f \
  ! -name 'README.md' \
  ! -name '.gitkeep' \
  -print
```

For the current placeholder posture, the `find` command must print nothing. The broad [`policy-test`](../../../.github/workflows/policy-test.yml) workflow does not scan this singular path, so its result cannot substitute for this inventory.

Any future payload requires deterministic positive, negative, boundary, and regression cases; pinned toolchain provenance; no-network execution where practical; exact fixture identities and digests; and a consumer that exercises the actual bytes. Passing proves only those declared assertions at the checked revision.

## Lifecycle and safety

Fixture bytes are not sovereign truth. They do not become RAW, WORK/QUARANTINE, PROCESSED, CATALOG/TRIPLET, or PUBLISHED records even when they model those shapes. A matching expected result does not create a policy decision, EvidenceBundle, review approval, release authorization, deployment, promotion, or publication.

Public clients must use governed interfaces or released public-safe artifacts, never repository fixtures, policy source, internal stores, or workflow output as live data.

## Migration and rollback

Moving, aliasing, or retiring this placeholder requires an accepted outcome, canonical target, verified writers and consumers, reference closure, single-write behavior, exit criteria, and rollback. Do not delete `.gitkeep` or this README merely because the directory contains no fixture payload; path identity and stale references may still matter.

This revision changes documentation only. Before merge, close the draft pull request and abandon its branch. After merge, use a focused corrective pull request. Do not restore the one-byte README or add payloads to make the directory appear implemented.

## Open questions

| ID | Question | Status |
|---|---|---|
| PTEST-FX-001 | Does any repository or external consumer require this singular fixture path? | **UNKNOWN** |
| PTEST-FX-002 | Should the path migrate to a canonical root fixture family or retire after reference closure? | **HOLD / NEEDS DIRECTORY REVIEW** |
| PTEST-FX-003 | Should a containment workflow guard this singular path before convergence? | **PROPOSED / NOT IMPLEMENTED** |
| PTEST-FX-004 | Who owns fixture safety and independent review? | **NEEDS VERIFICATION** |

## Related surfaces

- [Parent singular-lane hold](../README.md)
- [Plural policy-tests hold](../../tests/README.md)
- [Policy-local fixtures hold](../../fixtures/README.md)
- [Canonical fixture root](../../../fixtures/README.md)
- [Canonical policy tests](../../../tests/policy/README.md)
- [Broad policy readiness workflow](../../../.github/workflows/policy-test.yml)

## Changelog

| Version | Date | Change |
|---|---|---|
| v1.0.0 | 2026-08-28 | Replaces the one-byte placeholder with an evidence-grounded fixture routing and retirement hold; no fixture payload or operational behavior is added. |
