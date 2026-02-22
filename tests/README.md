<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/96cf4ebe-f113-4d54-b0c8-2ae15a28d129
title: tests/README.md
type: standard
version: v1
status: draft
owners: TBD
created: 2026-02-22
updated: 2026-02-22
policy_label: public
related:
  - kfm://doc/definitive-design-governance-guide-vnext
tags: [kfm, tests, ci, promotion-gates, governance, fail-closed]
notes:
  - Defines KFM test categories, fixtures, and CI merge gates.
  - Treat this file as the contract for what “green CI” means.
[/KFM_META_BLOCK_V2] -->

# tests — KFM test suite

Executable contracts for the trust membrane, promotion gates, and evidence-first UX.

![Status](https://img.shields.io/badge/status-draft-yellow)
![Gates](https://img.shields.io/badge/gates-fail--closed-critical)
![Policy](https://img.shields.io/badge/policy-default--deny-critical)
![Evidence](https://img.shields.io/badge/ux-evidence--first-blue)

---

## Navigation

- [Quick start](#quick-start)
- [What we test](#what-we-test)
- [CI gates](#ci-gates)
- [Quality metrics](#quality-metrics)
- [Promotion contract gates](#promotion-contract-gates)
- [Release definition of done](#release-definition-of-done)
- [Recommended layout](#recommended-layout)
- [Writing good tests](#writing-good-tests)
- [Fixtures and test data](#fixtures-and-test-data)
- [Golden queries for Focus Mode](#golden-queries-for-focus-mode)
- [Troubleshooting](#troubleshooting)

---

## Quick start

> NOTE  
> This repository’s exact test runner commands are **not confirmed in repo**.  
> Until a single runner is standardized, use the discovery steps below.

1. **Find the component runner**
   - Node or TypeScript packages: look for `package.json` scripts (example: `test`, `lint`, `typecheck`).
   - Python packages: look for `pyproject.toml` or `requirements.txt` and a `pytest` configuration.
   - Policy: look for an OPA policy bundle and fixtures (often `policy/**/*.rego`, `tests/policy/**`).

2. **Run the merge gates for what you changed**
   - If you changed **catalogs**: run schema + link checks.
   - If you changed **policy**: run policy tests.
   - If you changed **domain logic**: run unit tests.
   - If you changed **API contracts**: run contract tests.
   - If you changed **UI evidence drawer or Story Mode**: run E2E and accessibility smoke checks.

3. **Aim for a single “green bar” command**
   - Target state: a single command (for example `make test-gates` or `./tools/kfm test-gates`) that runs the merge-blocking gate set.

---

## What we test

KFM is only trustworthy if governance invariants are encoded as tests and those tests **fail closed**.

### Test categories

Minimum categories and what they protect:

| Category | Protects | Examples | Merge blocking |
|---|---|---|---|
| Unit | Core correctness and determinism | `spec_hash` canonicalization, controlled vocab validation | Yes |
| Schema | Catalog integrity | DCAT, STAC, PROV profile validation | Yes when catalogs change |
| Policy | Governance outcomes | OPA fixture-driven allow/deny and obligation outputs | Yes |
| Contract | Interface stability | OpenAPI diffs, DTO validation, resolver responses | Yes |
| Integration | Cross-component behavior | evidence resolver resolves sample EvidenceRefs | Yes |
| E2E UI | User-visible trust surface | layer toggle → evidence drawer shows attribution; Story citations resolve; Focus citations resolve | Yes for UI trust changes |

> TIP  
> If a change can affect what the public sees, what gets promoted, or what Focus Mode can cite, it needs a test.

### How tests relate to the trust membrane

We test the boundary, not just the code inside it:

- Frontend and external clients must never access DB or object storage directly.
- Core services must not bypass repositories to reach storage directly.
- All access must go through governed APIs that apply policy decisions, redactions, and logging.

In practice, this means adding tests that:
- deny direct storage paths in build outputs,
- assert API layers enforce policy,
- ensure evidence resolver checks policy before returning evidence bundles.

### Policy parity between CI and runtime

Policy is a shared contract:

- CI and runtime must evaluate policy the same way, using the same fixtures and expected outcomes.
- The evidence resolver and API layer must enforce policy before serving data or evidence.
- The UI may display policy badges and notices, but must not make policy decisions.

---

## CI gates

CI merge gates are **status checks** that block merges when they fail.

### Minimum merge gates

These are the minimum merge gates expected for KFM:

- Lint and typecheck for frontend and backend
- Schema validation for changed catalog artifacts
- Story Node template validation
- Policy tests
- `spec_hash` stability tests
- Citation verification and linting for EvidenceRefs and media rights
- Dependency vulnerability scanning and optional SBOM generation
- Accessibility smoke checks for UI trust-surface changes

CI citation checks should include:

- syntax check for EvidenceRefs
- resolver check in a test environment
- policy check for intended policy label
- rights check for any included media

If citation checks fail, Story Nodes must not merge.

> WARNING  
> A gate that can be bypassed is not a gate. If it matters for governance, it must be merge blocking.

---

## Quality metrics

Track governance and reliability metrics. Use metrics to detect drift and risk, not to create perverse incentives.

- Percent of promoted artifacts with explicit license metadata
- Percent of Story Nodes with fully resolvable citations
- Evidence resolver latency, P95
- Tile serving latency for public layers, P95
- Reindex time from processed artifacts
- Count of quarantined datasets by reason code
- Count of policy denials by reason code

---

## Promotion contract gates

Promotion gates apply when moving a dataset version through the truth path.

### Gate mapping

| Gate | What must be true | What to test |
|---|---|---|
| Gate A | Identity and versioning are stable | `spec_hash` stability; dataset and version IDs are deterministic |
| Gate B | Licensing and rights are explicit | license fields present; rights holder captured; “unclear” fails closed |
| Gate C | Sensitivity classification exists | policy label present; redaction or generalization plan recorded |
| Gate D | Triplet validates and cross-links resolve | DCAT, STAC, PROV validate and referential integrity passes |
| Gate E | Run receipt and checksums exist | receipts present; inputs and outputs enumerated with digests |
| Gate F | Policy and contract checks pass | OPA tests pass; evidence resolver resolves at least one ref; API schemas validate |
| Gate G | Production posture checks | SBOM and build provenance; perf smoke checks; accessibility checks |

> NOTE  
> Promotion gates are not “paperwork.” They are enforced contracts.

---

## Release definition of done

A release is done when:

- All gates pass in CI
- Promotion manifests exist for new dataset versions
- Evidence resolver contract tests pass for public and restricted scenarios
- Focus Mode evaluation harness passes golden queries
- UI regression tests pass and accessibility checks show no major regressions
- Release notes include policy and data changes
- Audit ledger retention and monitoring are configured

---

## Recommended layout

This directory structure is a **recommended** default to keep tests discoverable.

```text
tests/
├─ README.md
├─ fixtures/
│  ├─ catalog/              # minimal DCAT, STAC, PROV fixtures
│  ├─ policy/               # allow and deny fixtures for OPA tests
│  ├─ story/                # Story Node fixture examples
│  └─ evidence/             # EvidenceRef fixtures and expected bundles
├─ unit/                    # pure domain tests
├─ schema/                  # validators + regression fixtures
├─ policy/                  # OPA tests and helper scripts
├─ contract/                # OpenAPI and DTO contract tests
├─ integration/             # evidence resolver + API integration
├─ e2e/                     # UI journeys for trust surfaces
└─ golden/
   └─ focus-mode/           # golden query fixtures for Focus Mode
```

---

## Writing good tests

### Non-negotiables

- **Deterministic:** same inputs → same outputs, same spec → same hash.
- **No network:** tests must not depend on external services unless explicitly marked and isolated.
- **Fail closed:** missing license, missing policy label, missing citations → tests should fail, not warn.
- **Time-aware:** freeze time where needed; do not rely on wall-clock time in assertions.
- **Explain failures:** test output should tell a contributor what to fix.

### What to add when you touch a trust surface

If you change:

- **Catalog schemas or validators** → add schema regression fixtures.
- **Policy rules** → add allow and deny fixtures and obligation assertions.
- **Evidence resolver** → add at least one EvidenceRef fixture that resolves end-to-end.
- **Story Nodes** → add link-check fixtures so citations never silently rot.
- **UI evidence drawer** → add E2E tests that verify:
  - evidence panel opens
  - dataset version, license, policy label display
  - citations resolve

---

## Fixtures and test data

### Fixture rules

- Fixtures are part of the **evidence-first** posture: keep them small, explicit, and readable.
- Do not commit restricted or partner-only source data into test fixtures.
- Prefer synthetic data that still exercises:
  - sensitivity labeling,
  - redaction pipelines,
  - citation resolution.

### Sensitive location protection

If a dataset contains precise or sensitive locations:

- tests must ensure public tiles do not leak restricted bounding boxes,
- tests must ensure public exports do not include forbidden coordinate fields.

---

## Golden queries for Focus Mode

Focus Mode is a governed workflow: it must either cite admissible evidence or abstain.

Recommended golden query harness expectations:

- Every golden query has:
  - a prompt
  - a policy context
  - an expected decision outcome
  - required citations or required abstention
- Golden query tests should fail if:
  - any citation cannot be resolved
  - policy says deny but the system returns content
  - the audit record is not reproducible

---

## Troubleshooting

### Common failure types

- **Link checker fails:** a citation or EvidenceRef is broken. Fix the reference or update the fixture.
- **Policy tests fail:** your change altered allow or deny outcomes. Update fixtures and document the change.
- **Schema validation fails:** catalog output does not match profile. Fix generator or the fixture.
- **`spec_hash` test fails:** you introduced non-determinism or canonicalization drift.
- **E2E flakes:** remove timing assumptions; wait on deterministic UI states and network mocks.

### If you are unsure which gate applies

Start from the change surface:

- Catalog change → schema + link
- Policy change → policy tests
- API change → contract + integration
- UI trust change → E2E + accessibility
- Pipeline change → promotion gate mapping

---

## Appendix

### Test gate flow

```mermaid
flowchart TD
  A[Change: code, catalogs, policy, UI] --> B[Pull request]
  B --> C[CI merge gates]
  C -->|pass| D[Merge]
  C -->|fail| X[Blocked]
  D --> E[Controlled run and receipts]
  E --> F[Promotion contract gates]
  F -->|pass| G[Published API and UI]
  F -->|fail| Y[Quarantine or rollback]
```

Back to top: [Navigation](#navigation)
