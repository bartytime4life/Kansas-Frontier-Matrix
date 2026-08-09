<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-readme
title: fixtures/ — Canonical Reusable Fixture Root
type: readme; root-readme; canonical-fixtures-root; reusable-test-fixture-boundary
version: v0.2.0
status: repository-grounded draft; aligned to adopted Directory Rules v2; non-authoritative
created: NEEDS VERIFICATION
updated: 2026-08-08
supersedes: v0.1 at the same path
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
current_path: fixtures/README.md
owning_root: fixtures/
root_id: root.fixtures
readme_profile: ROOT_FULL
policy_label: public-review; synthetic-public-safe-only; no-network-default; no-authority; cite-or-abstain
truth_posture: >
  CONFIRMED the existing same-path canonical fixture root, adopted Directory Rules v2
  through ADR-0029, root.fixtures machine projection, current 27-direct-child tree,
  eight-validator full aggregate profile, generated-receipt fixture lane, no-network
  validation posture, CODEOWNERS route, and make fixtures readiness-marker behavior at
  main@668b7ece693f9f8bbec32ed508044b098f6df8fc / PROPOSED the fixture admission
  checklist and scenario vocabulary below / UNKNOWN exhaustive recursive payload and
  consumer inventory, deployed consumers, third-party sample rights, and public effects /
  NEEDS VERIFICATION accountable fixture stewardship beyond the current owner route,
  every child-lane README and consumer binding, branch-protection enforcement, host
  rendering, accessibility execution, stale-fixture service levels, and retirement drills
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 668b7ece693f9f8bbec32ed508044b098f6df8fc
  prior_blob: 4486f78146e70fba6c9109a1a79f00e16400ac80
  fixtures_tree: e787a6278847f9638347669783e2f1d4289ff45d
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  root_registry_blob: 024f668b5f0a9239bafa4f8b09e2afd86300ff8c
  validator_registry_blob: 12517f368cb1c8b850d3a7138a968cee889875ba
  makefile_blob: 4abc7f941ce25d7d14703e87e387cef6e96d1592
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  overlap_preflight: no open pull request naming fixtures/README.md; historical modernization PR 1562 is merged
related:
  - ../docs/doctrine/directory-rules.md
  - ../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../control_plane/root_registry.yaml
  - ../CONTRIBUTING.md
  - ../.github/CODEOWNERS
  - ../.github/workflows/validator-suite.yml
  - ../Makefile
  - ../tools/validate_all.py
  - ../tools/validators/validator_registry.json
  - ../tests/fixtures/README.md
  - generated_receipt/README.md
  - ../schemas/contracts/v1/receipts/generated_receipt.schema.json
  - ../tools/validators/validate_generated_receipt.py
  - ../data/receipts/generated/README.md
tags: [kfm, fixtures, root-readme, synthetic, deterministic, valid, invalid, golden, denied, abstain, hold, error, correction, rollback, no-network, public-safe]
notes:
  - "v0.2.0 is a same-path, editorial-plus-additive modernization; no fixture payload, schema, policy, validator, test, workflow, lifecycle object, release object, or public route is changed."
  - "The first twelve H2 sections implement the adopted Directory Rules v2 ROOT_FULL order."
  - "The direct-child map is verified at the pinned base; deeper inventory remains child-owned or NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `fixtures/` — Canonical Reusable Fixture Root

[![Root: canonical fixtures](https://img.shields.io/badge/root-canonical%20fixtures-1f6feb?style=flat-square)](#root-class-and-authority-owner)
[![Authority: non-authoritative](https://img.shields.io/badge/authority-non--authoritative-b42318?style=flat-square)](#what-belongs-here-and-what-is-prohibited)
[![Network: off by default](https://img.shields.io/badge/network-off%20by%20default-6f42c1?style=flat-square)](#validation-and-negative-checks)
[![Publication: denied](https://img.shields.io/badge/publication-denied-b42318?style=flat-square)](#public-exposure-and-sensitivity-posture)

> **One-line purpose.** `fixtures/` holds reusable, synthetic, deterministic, public-safe inputs and expected outputs that let KFM validators, tests, pipelines, and review tooling prove bounded behavior without turning examples into source truth, policy, proof, release, runtime, or publication authority.

> [!IMPORTANT]
> A fixture can prove that a checked implementation accepted or rejected specific bytes under a specific contract. It cannot prove that the bytes are factual, rights-cleared, complete, production-ready, released, public-safe outside the modeled case, or suitable for a live decision.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs and prohibited](#what-belongs-here) · [Inputs and outputs](#inputs) · [Exposure](#public-exposure-and-sensitivity-posture) · [Storage](#mutability-retention-generation-and-physical-storage) · [Validation](#validation) · [Review](#review-burden) · [ADRs](#adrs) · [Directory map](#direct-child-directory-map) · [Last review](#last-reviewed)

| Field | Current repository-grounded result |
|---|---|
| Canonical responsibility | Reusable `test_fixture` inputs and expected outputs |
| Root registry identity | `root.fixtures` |
| Root class | `canonical` |
| Repository exposure | `public`; payloads must therefore be synthetic and public-safe |
| Mutation / retention | `versioned` / `repository_lifetime` |
| Validation profile | `synthetic_public_safe_only` |
| Direct-child snapshot | `README.md` plus 27 directories at `main@668b7ece…` |
| Normal public-client use | **DENY** — repository fixtures are not governed runtime data |
| Release or publication effect | None |

---

## Purpose

`fixtures/` is the repository-wide home for reusable fixture families shared across validators, tests, packages, pipelines, workflows, and review surfaces. It exists to make positive and negative behavior reproducible with small, inspectable, no-network inputs.

A fixture should answer a bounded question such as:

- Does this candidate satisfy the declared schema and semantic checks?
- Does one malformed or disallowed property fail closed for the expected reason?
- Does an `ANSWER`, `ABSTAIN`, `DENY`, `HOLD`, or `ERROR` envelope preserve the required non-disclosure boundary?
- Does a content hash, deterministic identifier, correction, supersession, or rollback case reproduce?
- Does a public-safe transformation withhold or generalize the sensitive field it claims to protect?

`fixtures/` does **not** replace source intake, lifecycle data, semantic contracts, machine schemas, policy, executable tests, validators, receipts, proofs, catalogs, release decisions, or published artifacts.

[Back to top](#top)

---

<a id="authority-level"></a>

## Root class and authority owner

The accepted Directory Rules v2 classify `fixtures/` as a canonical responsibility root. The machine projection in [`control_plane/root_registry.yaml`](../control_plane/root_registry.yaml) records the current repository mapping:

| Root property | Projected value | Meaning |
|---|---|---|
| `root_id` | `root.fixtures` | Stable machine identifier for this responsibility root |
| `class` | `canonical` | This is the normal repository home for reusable test fixtures |
| Allowed artifact kind | `test_fixture` | Fixture inputs and expected outputs only |
| Prohibited artifact kinds | `data_instance`, `release_decision` | No lifecycle data or release authority |
| Exposure | `public` | Committed material must be safe for public repository exposure |
| Mutation | `versioned` | Changes are reviewed and retained through Git history |
| Retention | `repository_lifetime` | Removal requires consumer and compatibility review |
| Validation profile | `synthetic_public_safe_only` | Real, restricted, or unsafe payloads are not admitted |

> [!NOTE]
> The root registry is a machine projection of adopted governance, not an independent authority. [`ADR-0029`](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) and the adopted [`Directory Rules`](../docs/doctrine/directory-rules.md) control placement.

The current machine projection and [CODEOWNERS](../.github/CODEOWNERS) route this root to `@bartytime4life`. That route is **CONFIRMED review routing**, not proof of independent approval, domain stewardship, policy permission, release authority, or branch-protection enforcement.

[Back to top](#top)

---

<a id="status"></a>

## Adoption and conformance status

| Area | Status | Evidence or limit |
|---|---|---|
| Root existence | **CONFIRMED** | `fixtures/` exists at the pinned base |
| Placement authority | **CONFIRMED** | Directory Rules v2 adopted through ADR-0029 |
| Root projection | **CONFIRMED** | `root.fixtures` is present in the root registry |
| Same-path README role | **CONFIRMED** | Existing root README modernized in place |
| Direct-child inventory | **CONFIRMED** | 27 direct-child directories at the pinned tree |
| Reusable fixture role | **CONFIRMED** | Root registry and current validator consumers |
| All child contracts current | **NEEDS VERIFICATION** | Child README depth and freshness are mixed |
| Complete recursive payload inventory | **UNKNOWN** | No claim of every nested file or consumer |
| Every payload bound to a consumer | **NEEDS VERIFICATION** | Require child-level validator/test links |
| Dedicated fixture regeneration system | **NOT IMPLEMENTED / readiness marker only** | `make fixtures` prints TODO and exits successfully |
| Production or public runtime use | **DENY by role** | Fixtures are repository test carriers, not governed runtime data |

The current tree contains mature validator-backed families, compatibility/staging lanes, broad valid/invalid groupings, and child lanes whose deeper status is not established by their directory name alone. This README therefore documents the root contract without upgrading every child to implemented or validated status.

[Back to top](#top)

---

<a id="what-belongs-here"></a>

## What belongs here and what is prohibited

### Belongs here

Admit a file only when it is a reusable test fixture or fixture documentation and all applicable conditions below hold:

- synthetic, minimized, deterministic, reviewable, and safe to commit publicly;
- consumed or intended to be consumed by a named validator, test, pipeline dry run, package test, or review tool;
- explicit about whether it is valid, invalid, denied, abstaining, held, stale, erroneous, corrected, rolled back, or golden;
- paired with an expected result or reason code when that behavior is stable;
- bounded to one primary positive behavior or one primary defect when practical;
- no-network by default, with no hidden time, randomness, environment, credential, or service dependency;
- shaped by the applicable contract and schema without claiming contract, schema, or policy authority;
- transformed before commit when a sensitive-domain case requires generalization, redaction, withholding, or synthetic replacement;
- small enough for normal review, unless a child boundary explicitly governs a justified heavy fixture.

Typical accepted formats include small JSON, JSONL, YAML, text, Markdown, CSV, SVG, and intentionally tiny binary or geospatial samples whose rights and sensitivity are clear.

### Scenario families

| Scenario | Expected role |
|---|---|
| `valid` / positive | Proves bounded acceptance under the named validator or test |
| `invalid` / negative | Proves fail-closed rejection for a named defect |
| `DENY` | Proves policy or boundary refusal without leaking protected detail |
| `ABSTAIN` | Proves evidence-bounded non-answer behavior |
| `HOLD` / quarantine | Proves unresolved review, rights, identity, or sensitivity remains blocked |
| `ERROR` | Proves finite operational failure rather than unsafe fallback |
| stale / superseded | Proves currentness, correction, or lineage handling |
| correction / rollback | Proves reversible behavior and prior-state linkage |
| golden / expected output | Pins a deterministic result for regression review |

<a id="what-does-not-belong-here"></a>

### Prohibited here

| Prohibited material | Correct responsibility |
|---|---|
| Real source exports, production records, or canonical observations | Governed `data/` lifecycle lane |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, or PUBLISHED instances | Correct `data/<plane>/` home |
| Actual generated-work receipts | [`data/receipts/generated/`](../data/receipts/generated/README.md) |
| Actual proofs, release manifests, promotion decisions, corrections, or rollback cards | `data/proofs/` or `release/`, as governed |
| Semantic meaning or field intent | `contracts/` |
| Machine-checkable shape | `schemas/` |
| Allow, deny, restrict, hold, or abstain rules | `policy/` |
| Executable tests or validators | `tests/` or `tools/validators/` |
| Connectors, packages, pipelines, applications, or runtime code | Their implementation roots |
| Build output, coverage, screenshots, or transient QA output | `artifacts/` or CI artifact storage |
| Secrets, private endpoints, signed URLs, credentials, production logs, or personal data | **Do not commit**; follow [`SECURITY.md`](../SECURITY.md) |
| Exact rare-species, archaeology, critical-infrastructure, living-person, genomic, private-land, or similarly protected detail | **DENY** until a qualified public-safe transform and review exist |

A copied production object does not become safe because it was renamed “fixture.” Unknown rights, origin, sensitivity, or redistribution status fails closed.

[Back to top](#top)

---

<a id="inputs"></a>

## Inputs, outputs, and permitted writers

### Inputs

Fixture design may be informed by:

- semantic contracts under `contracts/`;
- machine schemas under `schemas/`;
- policy outcomes and reason-code vocabularies under `policy/`;
- validators and generators under `tools/`;
- executable consumers under `tests/`, `packages/`, `pipelines/`, `apps/`, or `runtime/`;
- reviewed public-safe source examples or synthetic domain scenarios;
- correction, rollback, and migration cases that need deterministic regression coverage.

The input relationship is one-way: a fixture illustrates or exercises an authority surface; it does not become that authority.

### Outputs

A fixture family may produce:

- deterministic input files;
- expected outputs, hashes, reason codes, snapshots, or manifests used only for testing;
- child README guidance;
- validator/test results emitted elsewhere;
- bounded CI logs and summaries.

Fixture validation output is not an `EvidenceBundle`, `PolicyDecision`, proof, release record, or publication state unless a separate governed process creates the real object in its proper home.

### Permitted writers

Normal writes use a focused branch and pull request. A writer must:

1. identify the consumer and owning fixture lane;
2. preserve valid/invalid polarity and expected-output pairing;
3. verify public safety, rights, and sensitivity before commit;
4. update the child README when local behavior or inventory changes materially;
5. run the smallest repository-native checks that prove the changed case;
6. keep unrelated fixture cleanup out of the change.

The current root registry and CODEOWNERS route name `@bartytime4life`; authenticated permissions, required review, and independent stewardship remain separate controls. Watchers, connectors, pipelines, tests, and CI may read fixtures and emit diagnostics, but they do not gain write, promotion, or publication authority by doing so.

[Back to top](#top)

---

## Public exposure and sensitivity posture

The repository and `root.fixtures` projection classify this root as public. Public repository visibility changes the admission threshold:

- every committed payload must be synthetic or otherwise demonstrably redistribution-safe;
- no fixture may reveal a secret, private endpoint, real credential, precise protected location, living-person record, genomic data, private-land linkage, or restricted source payload;
- sensitive examples must use documented generalization, redaction, withholding, hashing, substitution, or denial before the bytes enter Git;
- denial fixtures should expose stable public reason codes, not the protected value or a sensitive internal rationale;
- child lanes for archaeology, biodiversity, infrastructure, people/DNA/land, or other high-risk subjects inherit the stricter domain policy;
- external sample terms, attribution, and modification rights must be verified before reuse.

> [!CAUTION]
> Git history is durable. When unsafe material is discovered, stop normal review, follow `SECURITY.md`, assess whether history remediation is required, and record a bounded correction. Do not “fix” a leak by merely adding a later redacted copy.

Public clients and ordinary UI surfaces must not read this tree as a normal data source. Any public product must use released, governed, public-safe artifacts through the normal trust membrane.

[Back to top](#top)

---

## Mutability, retention, generation, and physical storage

| Concern | Root rule |
|---|---|
| Mutability | Versioned through Git; edit source fixtures and expected outputs together |
| Retention | Repository lifetime unless consumer, compatibility, and rollback review justify retirement |
| Physical storage | Small reviewable fixture bytes live under `fixtures/`; large/generated outputs belong elsewhere unless a child contract explicitly admits a bounded test asset |
| Golden files | Update only with an explained behavior change and reviewer-visible before/after result |
| Generated fixtures | Declare the generator, source fixture, version, command, digest, and edit policy |
| Mirrors | One-way and reproducible; hand-editing a generated mirror is denied |
| Timestamps | Use fixed ISO-8601 values unless time variation is the behavior under test |
| Randomness | Pin the seed or remove randomness |
| Hashes and IDs | Use deterministic toy values; distinguish placeholders from values a validator is expected to verify |
| Deletion | Search consumers, remove references, preserve migration/compatibility facts, and retain a rollback route |

Do not use `artifacts/` as a durable fixture home and do not use `fixtures/` as a shortcut around lifecycle, receipt, proof, or release placement. A test can model a lifecycle object here, but the model remains a fixture.

### Correction and rollback

- Before merge, abandon or close the branch/PR.
- After merge, revert the fixture and all directly coupled expected outputs or submit a bounded forward fix.
- When a changed fixture intentionally changes accepted behavior, preserve a migration note or prior-version case when downstream compatibility matters.
- Never roll back in a way that recreates two writable authorities or restores unsafe bytes.

[Back to top](#top)

---

<a id="validation"></a>

## Validation and negative checks

Validation is consumer-specific. Run the narrowest check that proves the changed fixture, then broaden only when the fixture is shared by broader profiles.

### Current repository-owned command surface

```bash
# Canonical aggregate orchestrator.
python tools/validate_all.py --profile full

# Compatibility aggregate entrypoint used by the Makefile and workflow.
make schemas

# Aggregate validators plus schema/contract tests.
make validate

# Generated-receipt fixture polarity and local artifact-integrity checks.
python tools/validators/validate_generated_receipt.py --fixtures
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_generated_receipt.py' \
  --verbose

# Documentation/diff hygiene for this README or child README changes.
git diff --check
```

The current `full` validator profile in [`validator_registry.json`](../tools/validators/validator_registry.json) contains eight fixture-backed entries:

1. `source-descriptor`
2. `evidence-ref`
3. `evidence-bundle`
4. `layer-manifest`
5. `runtime-response-envelope`
6. `decision-envelope`
7. `run-receipt`
8. `ingest-receipt`

[`validator-suite.yml`](../.github/workflows/validator-suite.yml) exercises the aggregate inventory, shared schema runner, generated-receipt integrity checks, a material-change profile, and an expected EvidenceBundle rejection. Its successful conclusion is bounded validation evidence; it does not create policy, review, proof, release, or publication authority.

> [!WARNING]
> `make fixtures` is currently a readiness marker that prints `TODO: regenerate deterministic fixtures` and exits successfully. It is **not** fixture regeneration or validation evidence.

### Required negative checks

A fixture change should test the applicable failures, including:

- malformed shape and unsupported enum;
- missing evidence or citation;
- invalid identifier, digest, path, or temporal relation;
- policy denial, sensitivity redaction, or public-path non-disclosure;
- stale, corrected, superseded, revoked, withdrawn, or rolled-back state;
- no-network and no-credential behavior;
- direct canonical-store, direct model-runtime, or watcher-to-publisher bypass;
- expected rejection reason rather than “any nonzero exit is acceptable.”

### What passing does not prove

Passing a fixture check does not prove:

- source truth, completeness, currentness, or legal admissibility;
- production behavior beyond the checked path;
- public fitness outside the modeled transformation;
- evidence closure, policy approval, human review, or source activation;
- performance, deployment, availability, or security of a live service;
- promotion, release, publication, correction propagation, or rollback execution.

Record commands that were not run as `NOT_RUN` or `SKIPPED`; do not convert absence of evidence into PASS.

[Back to top](#top)

---

<a id="review-burden"></a>

## Owner, reviewers, and escalation path

| Concern | Current route or required escalation |
|---|---|
| Root review routing | `/fixtures/ @bartytime4life` in CODEOWNERS |
| Machine-projection owner/writer/reviewer | `@bartytime4life` in `root_registry.yaml` |
| Dedicated fixture steward | **NEEDS VERIFICATION** |
| Contract or semantic change | Applicable `contracts/` owner |
| Schema shape change | Applicable `schemas/` owner and schema tests |
| Policy, rights, or sensitivity change | Applicable policy/domain reviewer; do not encode policy only in a fixture |
| Security or accidental sensitive material | Private-first route in [`SECURITY.md`](../SECURITY.md) |
| Release/correction/rollback meaning | Applicable release steward and real release objects outside this root |
| Directory placement or root-boundary change | Directory Rules plus an accepted ADR when triggered |
| Unresolved drift | [`docs/registers/DRIFT_REGISTER.md`](../docs/registers/DRIFT_REGISTER.md) |

CODEOWNERS routing is not approval. The author must not represent self-review, a generated receipt, a green workflow, or a fixture’s expected result as independent human review.

Review burden increases when a change:

- alters a golden output or accepted failure reason;
- affects multiple validators or runtime surfaces;
- changes sensitive-domain generalization or denial behavior;
- introduces a binary, heavy, or externally sourced sample;
- changes stable IDs, hashes, timestamps, correction lineage, or rollback semantics;
- removes a fixture consumed by compatibility or release checks.

[Back to top](#top)

---

<a id="adrs"></a>

## Governing ADRs, migrations, aliases, and canonical target

| Governance item | Status and effect |
|---|---|
| [`ADR-0029`](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | **Accepted**; adopts Directory Rules v2 and makes the doctrine path the sole writable Directory Rules authority |
| [`Directory Rules v2`](../docs/doctrine/directory-rules.md) | Governs this canonical root and the `ROOT_FULL` README profile |
| [`root_registry.yaml`](../control_plane/root_registry.yaml) | Machine projection only; records `root.fixtures` without creating authority |
| Schema-home ADR | Current exact status must be checked before moving or duplicating schema-shaped definitions; fixtures do not choose schema authority |
| Root alias | None verified for `fixtures/` |
| Canonical target | `fixtures/` itself |
| Active root migration | None authorized by this README |
| Compatibility relationship | `tests/fixtures/` remains a separate test-local fixture lane; it is not an alias or second reusable-fixture authority |

<a id="related-folders"></a>

### Related responsibility roots

| Need | Correct home |
|---|---|
| Cross-cutting reusable fixture | `fixtures/` |
| Fixture local to one test area | [`tests/fixtures/`](../tests/fixtures/README.md) or the verified test-local lane |
| Executable conformance | `tests/` |
| Semantic meaning | `contracts/` |
| Machine shape | `schemas/` |
| Admissibility and sensitivity | `policy/` |
| Validator/generator implementation | `tools/` |
| Lifecycle, receipts, proofs, catalogs, published carriers | Correct `data/` plane |
| Release, correction, withdrawal, rollback decisions | `release/` |
| Build and QA output | `artifacts/` or CI artifact storage |

Changing the root class, creating a parallel fixture authority, moving lifecycle data here, or collapsing `tests/fixtures/` and `fixtures/` without consumer evidence is structural work and requires a separate governed migration decision.

[Back to top](#top)

---

## Direct-child directory map

The following map is verified from tree `e787a6278847f9638347669783e2f1d4289ff45d` at the pinned base. It shows direct children only; each child README owns deeper detail.

```text
fixtures/
├── README.md                     # This ROOT_FULL authority contract.
├── archaeology-public-safe/      # Public-safe archaeology fixture lane.
├── connectors/                   # Source-connector fixture families.
├── contracts/                    # Versioned contract/object-family fixtures.
├── data/                         # Synthetic data-object shapes; not lifecycle data.
├── domains/                      # Domain-owned fixture lanes.
├── ecology/                      # Ecology compatibility/cross-domain fixtures.
├── evidence/                     # Evidence-object fixture families.
├── fauna/                        # Fauna compatibility/domain fixtures.
├── generated_receipt/            # GENERATED_RECEIPT shape and integrity fixtures.
├── golden/                       # Golden expected-output fixtures.
├── heavy/                        # Bounded large-fixture lane; local rules govern.
├── hydrology/                    # Hydrology compatibility/domain fixtures.
├── infrastructure-generalized/   # Generalized public-safe infrastructure fixtures.
├── ingest/                       # Intake and ingest fixture families.
├── invalid/                      # Cross-cutting invalid cases.
├── map/                          # Map contract and delivery fixture families.
├── maplibre/                     # MapLibre runtime and governance fixtures.
├── packages/                     # Package-owned reusable fixtures.
├── pmtiles/                      # PMTiles fixture families.
├── public_safe/                  # Cross-cutting public-safe examples.
├── release/                      # Synthetic release-governance fixtures only.
├── review/                       # Review-record fixture families.
├── runtime/                      # Runtime-envelope and adapter fixtures.
├── slim/                         # Compact fixture subsets.
├── synthetic/                    # General synthetic compatibility lane.
├── ui/                           # UI trust-state fixture families.
└── valid/                        # Cross-cutting valid cases.
```

**Inventory boundary:** direct-child names are CONFIRMED. The map does not claim that every child has a current README, complete polarity, active consumer, or equivalent maturity. Ambiguous or compatibility-shaped lanes must be resolved in their own boundary documents or through a separate migration—not silently reclassified here.

[Back to top](#top)

---

<a id="last-reviewed"></a>

## Last evidence review and review triggers

| Field | Value |
|---|---|
| Last evidence review | 2026-08-08 |
| Repository snapshot | `main@668b7ece693f9f8bbec32ed508044b098f6df8fc` |
| Target prior blob | `4486f78146e70fba6c9109a1a79f00e16400ac80` |
| Direct-child tree | `e787a6278847f9638347669783e2f1d4289ff45d` |
| Directory authority | Directory Rules v2 adopted by ADR-0029 |
| Aggregate validator source | `tools/validators/validator_registry.json` |
| Open PR overlap | No open PR naming `fixtures/README.md` found before authoring |
| Runtime/deployment observation | Not performed; not required for this documentation slice |

Re-review this README when any of the following occurs:

- `root.fixtures` class, allowed kinds, exposure, writer, retention, or validation profile changes;
- a direct child is added, retired, moved, aliased, or reclassified;
- `tests/fixtures/` or another path becomes a competing reusable-fixture authority;
- the aggregate validator registry, `make schemas`, `make validate`, or `make fixtures` semantics change;
- a fixture generator or mirror relationship is introduced;
- a sensitive-domain fixture, external sample, heavy binary, or new public-exposure risk is admitted;
- a contract/schema/policy change alters fixture polarity or expected reason codes;
- drift, security incident, correction, withdrawal, rollback, or consumer breakage occurs;
- an accepted ADR changes fixture placement or authority.

No blanket review interval is asserted here; Directory Rules v2 uses event- and risk-based review. A future root profile may establish a maximum interval.

### Open verification items

- accountable fixture steward and independent review route;
- complete recursive payload and consumer inventory;
- child README coverage, freshness, and direct contract/schema/policy/test links;
- external sample rights and attribution posture;
- root-wide stale-fixture detection and retirement drill;
- branch-protection and required-check coupling;
- host-rendered Markdown and accessibility validation;
- whether compatibility-shaped top-level lanes should converge under `domains/`, `packages/`, or object-family lanes through a separate evidence-backed migration.

[Back to top](#top)
