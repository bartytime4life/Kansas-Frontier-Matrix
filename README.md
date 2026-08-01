<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/root-readme
title: Kansas Frontier Matrix — Repository Entry Point
type: repository-readme
version: v2.0.0
status: repository-grounded draft
owners: ["@bartytime4life"]
created: 2026-05-11
updated: 2026-08-01
policy_label: public
current_path: README.md
owning_root: repository-root
responsibility: repository-wide identity, orientation, contribution, and validation entry point
truth_posture: cite-or-abstain; implementation claims require pinned repository evidence
related:
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/ai-build-operating-contract.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/truth-posture.md
  - CONTRIBUTING.md
  - SECURITY.md
  - .github/README.md
notes:
  - "Restores the root README as the repository identity and orientation surface required by the adopted Directory Rules."
  - "The superseded Markdown-agent prompt remains recoverable in Git history; this change does not adopt, publish, or create a second prompt authority."
  - "Current-state claims are bounded to repository evidence inspected at the listed evidence checkpoint."
[/KFM_META_BLOCK_V2] -->

<p align="center">
  <img src="docs/brand/logo/The-Kansas-Frontier-Matrix-Seal-transparent-cropped.png" alt="Kansas Frontier Matrix seal" width="240" />
</p>

# Kansas Frontier Matrix

> A governed, evidence-first, map-first, time-aware spatial knowledge system for Kansas and the surrounding frontier.

Kansas Frontier Matrix (KFM) is organized so that a file's location identifies its responsibility, authority, lifecycle, and review boundary. The repository combines human doctrine, machine contracts and schemas, policy, synthetic fixtures, validators, applications, pipelines, governed data lanes, and release-supporting records without treating any one surface as sovereign truth.

> [!IMPORTANT]
> A document, map, test, receipt, commit, pull request, merge, or GitHub release does not by itself establish factual truth, policy approval, KFM release, promotion, or publication.

**Quick navigation:** [Purpose](#purpose) · [Authority and status](#authority-and-status) · [Core invariants](#core-invariants) · [Start here](#start-here) · [Repository map](#repository-map) · [Validation](#build-and-validation) · [Contributing](#contributing-and-review) · [Governance](#governing-decisions-and-guidance)

## Purpose

This README is the repository-wide identity and orientation entry point. It explains:

- what KFM is and is not;
- the trust boundaries that apply across the repository;
- how responsibility roots divide authority;
- which current commands provide bounded validation evidence;
- where contributors should begin.

It does not replace the doctrine, contracts, schemas, policy, tests, receipts, proofs, release records, or root-specific READMEs it links to.

## Authority and status

| Field | Current repository evidence |
|---|---|
| Root class | Repository root governed by the [root-file law](docs/doctrine/directory-rules.md#81-root-file-law) |
| README profile | `ROOT_FULL` under the [README contract](docs/doctrine/directory-rules.md#162-root_full-fields) |
| Placement authority | [ADR-0029](docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](docs/doctrine/directory-rules.md) |
| Review route | [CODEOWNERS](.github/CODEOWNERS) routes the root file to `@bartytime4life`; routing is not approval evidence |
| Package metadata | [pyproject.toml](pyproject.toml) uses this file as the Python distribution README |
| Conformance | Existing responsibility roots are classified below; known compatibility, deprecated, and conditional roots remain visible |
| Implementation posture | Mixed and evidence-bounded; file presence and configured commands do not prove deployment, release, or publication |
| Public posture | This is public-facing repository documentation, not a public data interface or release record |

## Core invariants

KFM changes must preserve these boundaries unless a current adopted decision explicitly changes them:

1. **Lifecycle is governed.** The shorthand remains `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED`. Promotion is a governed state transition, not a file move.
2. **Claims resolve evidence.** An `EvidenceRef` must resolve to an `EvidenceBundle` before a consequential claim is presented as authoritative; otherwise the surface abstains, denies, or reports an error.
3. **Public access crosses a trust membrane.** Ordinary clients use governed APIs and released public-safe artifacts, not RAW, WORK, QUARANTINE, candidate, canonical-internal, or model-runtime stores.
4. **Interpretive surfaces remain subordinate.** AI, maps, tiles, graphs, indexes, dashboards, scenes, screenshots, summaries, badges, and tests do not become truth authorities.
5. **Automation does not publish.** Watchers and drift detectors may propose work and emit bounded records; they do not promote or publish.
6. **Object families stay distinct.** Receipts, proofs, registries, catalogs, manifests, reviews, decisions, corrections, rollback records, and published carriers have separate responsibilities.
7. **Sensitive material fails closed.** Unknown rights, living-person or genomic data, rare-species locations, archaeology, infrastructure, land/title data, harmful precision, and cultural or sovereignty concerns require quarantine, redaction, generalization, staged access, delay, abstention, or denial.
8. **Corrections remain traceable.** Identity, replay, supersession, correction lineage, and rollback are preserved where the consequence requires them.

Read the full doctrine before changing a trust-bearing boundary: [Lifecycle Law](docs/doctrine/lifecycle-law.md), [Trust Membrane](docs/doctrine/trust-membrane.md), [Truth Posture](docs/doctrine/truth-posture.md), and [AI Build Operating Contract](docs/doctrine/ai-build-operating-contract.md).

## Start here

| Goal | First source |
|---|---|
| Understand placement and responsibility roots | [Directory Rules](docs/doctrine/directory-rules.md) and [ADR-0029](docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) |
| Prepare a repository change | [CONTRIBUTING.md](CONTRIBUTING.md) and [.github/README.md](.github/README.md) |
| Browse human documentation | [docs/README.md](docs/README.md), [doctrine](docs/doctrine/README.md), [architecture](docs/architecture/README.md), and [ADRs](docs/adr/README.md) |
| Work on the governed API | [apps/governed-api/README.md](apps/governed-api/README.md) |
| Work on the Explorer Web app | [apps/explorer-web/README.md](apps/explorer-web/README.md) |
| Add or validate a contract | [contracts/README.md](contracts/README.md), [schemas/README.md](schemas/README.md), and [tools/validators/README.md](tools/validators/README.md) |
| Report a vulnerability or unsafe exposure | [SECURITY.md](SECURITY.md) |

## Current implementation surface

The following are narrow statements about bytes and configured entry points in the current repository. They do not assert that every path is complete or deployed.

| Surface | Confirmed repository state | Evidence boundary |
|---|---|---|
| Python distribution | [pyproject.toml](pyproject.toml) defines a Python 3.11+ `kfm` scaffold and packages [src/kfm](src/kfm/) | The manifest explicitly says the namespace is a scaffold, not a public API or release authority |
| Governed API | [apps/governed-api](apps/governed-api/) contains an application README, source, and tests | Presence is not deployment or public-release evidence |
| Explorer Web | [apps/explorer-web](apps/explorer-web/) contains a Vite/TypeScript application, tests, and its own README | Presence is not hosted-service evidence |
| Schema and contract baseline | `make validate` invokes the aggregate validators plus schema and contract tests | Passing proves only the configured check scope |
| Boundary checks | The [Makefile](Makefile) exposes governed-API, policy-boundary, deny, UI-build, and MapLibre validation targets | Each target must be run and reported separately |
| JavaScript workspace | [package.json](package.json) coordinates the private workspace and pins `pnpm@11.17.0` with Node 22.13.x | Root `lint`, `test`, and `build` scripts are intentional `WORKFLOW_HOLD` failures |
| GitHub automation | [.github/workflows](.github/workflows/) contains repository workflows documented in [.github/README.md](.github/README.md) | A workflow file or badge is not proof of a successful run |

## Repository map

This direct-child map was verified at the evidence checkpoint listed in [Last evidence review](#last-evidence-review). Child READMEs own deeper detail.

~~~text
Kansas-Frontier-Matrix/
├── .github/               # platform automation, templates, and review routing
├── apps/                  # deployable applications
├── artifacts/             # compatibility output lanes; no trust-bearing authority
├── catalog/               # deprecated containment root; frozen to new writes
├── configs/               # non-secret configuration profiles and templates
├── connectors/            # source acquisition and admission edges
├── contracts/             # semantic and interface meaning
├── control_plane/         # machine governance projections and indexes
├── data/                  # governed lifecycle and accountability instances
├── docs/                  # human doctrine, decisions, architecture, and guidance
├── examples/              # runnable public-safe demonstrations
├── fixtures/              # reusable synthetic, valid, invalid, and golden inputs
├── infra/                 # deployment and exposure infrastructure
├── migrations/            # versioned migrations and rollback definitions
├── packages/              # reusable non-deployable implementation
├── pipeline_specs/        # declarative pipeline definitions
├── pipelines/             # executable lifecycle transformations
├── policy/                # normative allow, deny, hold, restrict, and abstain rules
├── release/               # release, correction, withdrawal, and rollback decisions
├── runtime/               # bounded runtime composition and local adapters
├── schemas/               # machine-checkable shapes
├── scripts/               # thin non-authoritative operator wrappers
├── src/                   # conditional root distribution facade; decision held
├── tests/                 # executable conformance evidence
└── tools/                 # validators, generators, builders, and operators
~~~

The 22 canonical or platform roots are defined by [Directory Rules §7](docs/doctrine/directory-rules.md#7-canonical-root-registry). The same rules classify:

- `artifacts/` as a compatibility and generated-output transition;
- `catalog/` as a deprecated containment root frozen to new writes;
- `src/` as conditional and unresolved while the minimal Python facade remains in place.

Do not create a new root, revive a deprecated root, or turn a compatibility path into a writable authority without an adopted decision and migration plan.

### Root entry points

| Entry point | Responsibility |
|---|---|
| [README.md](README.md) | Repository identity and orientation |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution, validation, review, and generated-work requirements |
| [SECURITY.md](SECURITY.md) | Vulnerability reporting and sensitive-disclosure boundary |
| [CHANGELOG.md](CHANGELOG.md) | Repository change history; not release or publication proof by itself |
| [LICENSE](LICENSE) | Repository license text; package-specific rights still require verification |
| [Makefile](Makefile) | Repository-native orchestration and readiness markers |
| [pyproject.toml](pyproject.toml) | Python scaffold, dependencies, packaging, and test configuration |
| [package.json](package.json) | Private JavaScript workspace coordination |

## What belongs at the root

| Belongs | Prohibited |
|---|---|
| Repository identity, governance, build, packaging, security, and ecosystem entry points | Domain documents, datasets, schemas, policy modules, release objects, or one-off scripts |
| Platform integration under `.github/` | KFM truth, policy, or release authority embedded in platform configuration |
| Coordinating manifests and reviewed tool configuration | Secrets, private endpoints, signed URLs, credentials, or production data |
| One current project README | Parallel project READMEs or prompt artifacts occupying the root identity surface |

Domain material belongs in lanes inside the responsibility roots. A topic does not become a new top-level directory merely because it is important.

## Inputs, outputs, and permitted writers

| Boundary | Repository-root contract |
|---|---|
| Inputs | Reviewed source changes, doctrine and ADR decisions, contracts, schemas, policy, synthetic fixtures, application code, manifests, and configuration in their owning roots |
| Outputs | Versioned repository state, validation evidence, candidate artifacts, and reviewable changes; release and publication require their separate governed transitions |
| Permitted writers | Contributors working through scoped feature branches and repository automation limited to its declared output lanes |
| Writer constraint | A writer may modify only the canonical source and required synchronized outputs for its accepted slice |
| Review constraint | CODEOWNERS routes review; it does not prove review, approval, separation of duties, or merge eligibility |

## Public exposure and sensitivity

The root README and linked human documentation are orientation surfaces. They must not expose credentials, private services, production payloads, restricted sources, living-person or genomic records, harmful-precision locations, or security-sensitive details.

Browser and ordinary UI traffic belongs behind the [governed API boundary](docs/architecture/governed-api.md). Sensitive or uncertain material follows the fail-closed posture in [SECURITY.md](SECURITY.md) and [sensitivity doctrine](docs/doctrine/sensitivity.md).

## Mutability, retention, generation, and storage

- Root entry points are tracked Git source and change through reviewable commits.
- Generated or mirrored files are changed through their declared canonical source and generator, not hand-edited.
- AI-authored or substantively AI-modified artifacts require a receipt under [data/receipts/generated](data/receipts/generated/) with human review pending until an authorized reviewer acts.
- Build products use declared output lanes and do not become receipts, proofs, releases, or publications because they exist under `artifacts/`.
- Git history preserves prior root README bytes and enables focused reversion. The misplaced v5 prompt is not copied to a second writable path by this correction.
- Retention, release, correction, withdrawal, and publication are owned by their specific contracts and records; this README cannot perform those transitions.

## Build and validation

The documented Python baseline is:

~~~bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -e ".[test]"
make validate
git diff --check
~~~

`make validate` runs the aggregate schema validators and the configured schema/contract tests. Use narrower targets when the change affects a specific boundary:

| Target | Bounded purpose |
|---|---|
| `make governed-api-smoke` | Governed API test suite |
| `make governed-api-verify` | Governed API tests plus renderer/model import-boundary check |
| `make boundary-guards` | Policy, API, connector, and pipeline boundary tests |
| `make deny-test` | Public-route, store, and runtime-import guards |
| `make ui-build` | Explorer Web production build |
| `make maplibre-govern` | MapLibre performance-governance validation |

> [!WARNING]
> The Makefile targets `policy`, `fixtures`, `proof-slice`, `catalog`, `release-dry-run`, and `publish-check` are readiness markers that print `TODO`. Their zero exit status is not validation evidence. Root JavaScript `lint`, `test`, and `build` scripts intentionally fail with `WORKFLOW_HOLD`.

Validation must match the changed area. A green check proves its declared scope, not system correctness, rights clearance, security, release fitness, or publication.

## Contributing and review

Before editing:

1. Read [CONTRIBUTING.md](CONTRIBUTING.md), [Directory Rules](docs/doctrine/directory-rules.md), and the path-scoped README for every affected boundary.
2. Freeze one observable goal, its direct dependency set, validation plan, and rollback boundary.
3. Use a feature branch; preserve unrelated work and avoid force-push.
4. Add tests, fixtures, contracts, schemas, policy, generated outputs, and documentation when they are direct dependencies of the behavior.
5. Include the required generated-work receipt and keep its human-review state accurate.
6. Open a draft pull request unless the current request and required checks support a ready-for-review state.

Security-sensitive findings follow [SECURITY.md](SECURITY.md), not public issue or pull-request discussion.

## Compatibility, migration, and rollback

This same-path replacement preserves `kfm://doc/root-readme` while restoring the file's governed repository-entry-point role. It does not move roots, change runtime behavior, adopt a prompt, or claim a release.

- **Before merge:** abandon or close the draft pull request and retain or delete the feature branch only with appropriate authority.
- **After merge:** use a focused revert or forward-fix pull request against the actual merged commit; do not rewrite shared history.
- **Structural follow-up:** compatibility, deprecated, and conditional roots remain governed by Directory Rules and their own migration evidence. This README does not authorize their retirement.

## Governing decisions and guidance

| Source | Role |
|---|---|
| [Directory Rules](docs/doctrine/directory-rules.md) | Canonical human-readable placement and responsibility authority |
| [ADR-0029](docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted adoption decision and migration boundary |
| [AI Build Operating Contract](docs/doctrine/ai-build-operating-contract.md) | AI-authored change and receipt discipline |
| [Lifecycle Law](docs/doctrine/lifecycle-law.md) | Lifecycle and promotion boundary |
| [Trust Membrane](docs/doctrine/trust-membrane.md) | Public and internal trust boundary |
| [Truth Posture](docs/doctrine/truth-posture.md) | Evidence labels and cite-or-abstain behavior |
| [Authority Ladder](docs/doctrine/authority-ladder.md) | Claim-specific authority resolution |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Repository contribution and review workflow |

## Last evidence review

| Field | Value |
|---|---|
| Date | 2026-08-01 |
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Base commit | `86985a48b15a3ad3a26fbfdcbfc7a09ad1779bd0` |
| Review method | Complete prior root README read; direct-child inventory; governing Directory Rules and ADR review; current manifests, Makefile, CODEOWNERS, contribution, security, app, validator, and workflow entry-point inspection |
| Confirmed scope | Root identity, current direct children, linked file presence, configured commands, and stated governance boundaries |
| Not proved | Full repository correctness, every workflow result, deployment, runtime operation, external services, release, promotion, publication, or administrator settings |

Re-review this README when root topology, authority, package metadata, owner routing, public exposure, validation entry points, or the governing Directory Rules change.
