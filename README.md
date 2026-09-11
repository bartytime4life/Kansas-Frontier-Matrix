<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/root-readme
title: Kansas Frontier Matrix — Project Home
type: repository-readme
version: v3.0.1
status: repository-grounded draft
owners: ["@bartytime4life"]
created: 2026-05-11
updated: 2026-09-11
policy_label: public
current_path: README.md
owning_root: repository-root
responsibility: repository-wide identity, orientation, contribution, and validation entry point
truth_posture: cite-or-abstain; implementation claims require pinned repository evidence
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 664e46697d4d237870f5a482904bb9acd8f11b20
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
  - "Preserves the visitor-first orientation, root README identity, headings, and governing boundaries. v3.0.1 reconciles current implementation, setup, and delivery guidance."
  - "Current implementation claims are bounded to the exact GitHub snapshot recorded above."
  - "The public Explorer address is linked as a project entry point; hosted availability and version state remain separately verifiable runtime claims."
[/KFM_META_BLOCK_V2] -->

<p align="center">
  <img src="docs/brand/logo/The-Kansas-Frontier-Matrix-Seal-transparent-cropped.png" alt="Kansas Frontier Matrix seal" width="220" />
</p>

# Kansas Frontier Matrix

<p align="center">
  <strong>Make place, time, and evidence easier to explore.</strong><br />
  A governed, map-first spatial knowledge system for Kansas and the surrounding frontier.
</p>

<p align="center">
  <a href="https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site"><img src="https://img.shields.io/badge/Explore-KFM%20Explorer-2f6f4e?style=for-the-badge" alt="Explore the KFM Explorer" /></a>
  <a href="#why-kfm"><img src="https://img.shields.io/badge/Design-evidence--first-5b4abf?style=for-the-badge" alt="Evidence-first design" /></a>
  <a href="#the-kfm-experience"><img src="https://img.shields.io/badge/Interface-map--first-1769aa?style=for-the-badge" alt="Map-first interface" /></a>
  <a href="#current-posture"><img src="https://img.shields.io/badge/Posture-repository--grounded-b7791f?style=for-the-badge" alt="Repository-grounded posture" /></a>
</p>

<p align="center">
  <a href="https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site">Open the Explorer</a> ·
  <a href="apps/kansas-frontier-matrix-explorer/README.md">Read the site guide</a> ·
  <a href="CONTRIBUTING.md">Contribute</a> ·
  <a href="SECURITY.md">Report a security concern</a>
</p>

> [!NOTE]
> KFM is an active build. The repository contains real applications, contracts, schemas, policy, validators, fixtures, tests, and workflows. Explorer Web now includes a package-owned MapLibre composition using synthetic/generalized geometry. Production renderer graduation, source admission, live governed transport, release, deployment, and publication remain separate gates, not consequences of a working canvas.

**New here?** Start with [Why KFM](#why-kfm), [Explore](#start-here), [The KFM experience](#the-kfm-experience), or [Current posture](#current-posture). Contributors can jump to [Run locally](#run-locally), [Validation](#validation), and [Contributing](#contributing).

## Why KFM

Most maps answer **where**. KFM is being built to help answer **where, when, what supports the claim, what changed, and what can responsibly be shown**.

The project brings geography, history, natural systems, people, infrastructure, time, and source lineage into one inspectable experience. A map is the doorway—not the authority. A fluent explanation is useful only when it remains downstream of evidence, policy, and review.

| What makes KFM interesting | What that means for a user |
|---|---|
| **Explore connected systems** | Move from a place to layers, time, context, and related evidence instead of browsing isolated pins. |
| **Inspect the claim** | See the source role, evidence reference, time context, correction state, and limits behind a consequential result. |
| **Make uncertainty visible** | Missing, stale, restricted, conflicted, or unsupported information can become an honest abstention—not a confident guess. |
| **Protect what should not be exposed** | Rights, cultural sensitivity, living-person data, rare species, archaeology, infrastructure, and harmful precision are handled conservatively. |
| **Keep the trail recoverable** | Identity, provenance, review, release, correction, and rollback remain part of the system’s design. |

KFM’s public value is not a larger pile of layers. It is a more trustworthy path from **question → place and time → evidence → bounded action**.

## Start here

| If you want to… | Start with… |
|---|---|
| **See the project’s public-facing Explorer** | [KFM Explorer](https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site) — the repository records this OpenAI Sites/Vinext project, slug, and public address. Hosted availability and version state require current runtime verification. |
| **Understand the current site application** | [`apps/kansas-frontier-matrix-explorer/`](apps/kansas-frontier-matrix-explorer/) — the single-route Vinext site, synthetic/generalized catalog surface, renderer-neutral shell, fail-closed evidence behavior, and public-safe export boundary. |
| **Study the browser workbench** | [`apps/explorer-web/`](apps/explorer-web/) — a Vite/TypeScript local composition with a bounded Living Atlas MapLibre canvas, Map, Knowledge, Features, Trust, Focus, Story, Evidence Drawer, and validation slices. Its inline geography is synthetic/generalized, not factual Kansas source data. |
| **Learn the project’s rules** | [`docs/doctrine/`](docs/doctrine/), [`docs/architecture/`](docs/architecture/), and [`docs/adr/`](docs/adr/). |
| **Make a change safely** | [`CONTRIBUTING.md`](CONTRIBUTING.md), [`Directory Rules`](docs/doctrine/directory-rules.md), and the README nearest the path you will touch. |
| **Understand evidence and public boundaries** | [`Trust Membrane`](docs/doctrine/trust-membrane.md), [`Truth Posture`](docs/doctrine/truth-posture.md), [`Lifecycle Law`](docs/doctrine/lifecycle-law.md), and [`SECURITY.md`](SECURITY.md). |
| **Find the machine side** | [`contracts/`](contracts/), [`schemas/`](schemas/), [`policy/`](policy/), [`data/`](data/), [`pipelines/`](pipelines/), [`runtime/`](runtime/), and [`tools/`](tools/). |

## The KFM experience

The north-star interaction path is:

**Map → area of interest → layers → time → inspect → evidence → report → share**

This is a product direction, not a claim that every stage is integrated today. Each link in the chain must preserve the distinction between a user interaction, a derived carrier, a supported claim, and a governed action.

```mermaid
flowchart LR
    place["Place"] --> context["Layers + time"]
    context --> inspect["Inspect"]
    inspect --> evidence["Evidence + limits"]
    evidence --> action["Report / share"]
```

The Explorer is intended to make that chain feel natural:

- begin with a place, region, layer, story, or question;
- narrow the spatial and temporal context before making a claim;
- open the evidence and provenance context instead of treating pixels as proof;
- compare or report only what remains within the applicable rights, sensitivity, release, and correction boundaries;
- share a safe, inspectable result—or clearly say why the system cannot.

## Exploration themes

KFM organizes work across connected themes rather than treating each domain as a separate application.

| Living landscapes | History and human stories | Built world and change |
|---|---|---|
| Geology, soil, hydrology, habitat, flora, fauna, atmosphere, and agriculture | Archaeology, settlements, people, genealogy, DNA, and land—subject to stronger privacy, cultural, consent, and stewardship controls | Hazards, roads, rail, trade, infrastructure, and the changing relationship between people and place |

These are exploration and implementation lanes, not a promise that each theme has live, complete, or publishable data. Rights, source terms, stewardship, cultural authority, sensitive geometry, and currentness remain claim-specific.

> [!WARNING]
> Exact archaeological, burial, sacred, rare-species, infrastructure, private-land, living-person, DNA/genomic, and other harmful-precision details are not assumed to be public-safe. KFM defaults to quarantine, redaction, generalization, staged access, delay, abstention, or denial when the required authority is unclear.

## Current posture

The table below is the honest maturity snapshot for the repository at `main@664e46697d4d237870f5a482904bb9acd8f11b20`.

| Surface | Current repository evidence | Boundary |
|---|---|---|
| **Repository foundation** | Responsibility roots for apps, contracts, schemas, policy, data, pipelines, runtime, docs, tests, tools, and release are present. | A path’s presence does not make it truth, policy, release, or publication authority. |
| **KFM Explorer site app** | `apps/kansas-frontier-matrix-explorer/` contains a Vinext application, a renderer-neutral `NullMapRuntime` composition, synthetic/generalized catalog metadata, fail-closed evidence behavior, public-safe export guidance, and Sites identity metadata. | This proves tracked implementation slices. It does not prove a live renderer, live data, hosted health, release, or publication. |
| **Explorer Web workbench** | The [app README](apps/explorer-web/README.md) and [Living Atlas composition](apps/explorer-web/src/site/mount-living-atlas.ts) record the package-owned MapLibre canvas, inline synthetic/generalized geometry, public navigation/context, shared trust surface, synthetic Focus, Evidence Drawer, Story/map-selection slices, temporal controls, and draft-only report/story capture. | A mounted renderer is not an admitted factual layer. Live governed transport, EvidenceBundle closure, the production-shell decision, and real-data graduation remain separate gates. |
| **MapLibre path** | The [package manifest](packages/maplibre/package.json) pins `maplibre-gl@6.7.0` and exports the renderer-neutral facade, adapter, and Vite adapter. Explorer Web imports the package-owned Vite adapter; the Sites-derived app remains a distinct consumer. | Dependency presence and bounded composition do not establish source/protocol admission, broader browser/CSP/accessibility/performance readiness, distribution, release, or deployment. Older `6.6.0` README snapshots are historical; the pinned manifest controls the current dependency claim. |
| **Evidence and trust path** | Contracts, finite outcomes, defensive adapters, fail-closed fixtures, negative cases, and policy-boundary tests are present in bounded slices. | End-to-end EvidenceBundle resolution, source admission, live transport, and public release are not established by this README. |
| **AI path** | KFM treats AI as interpretive and downstream of evidence, policy, review, release, correction, and rollback. | Browser code must not become a model provider, internal-store reader, evidence authority, or publication path. A model response is never evidence by itself. |
| **Hosting** | The repository records the OpenAI Sites/Vinext project identity and preserves the existing Explorer slug and public address. | Hosted version history, availability, authentication, CSP/CORS, observability, and production operation require current runtime evidence. |

### Repository, saved Site, and published state

Keep three observations separate: **repository implementation**, **saved Site version**, and **production/released state**. Do not copy capabilities, test totals, or deployment claims from one surface to another.

- [PR #4464](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4464) merged on 2026-09-11 at the pinned main commit. It improves full Layer Catalog scroll/visibility affordances and labels requested visibility separately from time compatibility. It does not prove renderer delivery, enlarge the eight-fixture Library projection, or deploy the Site.
- The [Drive Site backfill checkpoint](https://docs.google.com/document/d/1uROL1Hkgr15oe2nH-9B2MUXdmzt2KSBo6ay1jt5dh4s/edit) records saved Site v24 and additional external-context capabilities. That coordination record is not byte-equivalence with this checkout, a production observation, source admission, or release authority. The [Site guide](apps/kansas-frontier-matrix-explorer/README.md#repository-and-saved-site-reconciliation) records the handoff boundary.
- [Issue #4024](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024) remains open at this review. No open PRs were returned by the live listing; that observation does not close the delivery-control incident or prove independent approval.

For a real-data layer, preserve exact source/asset identity, rights, spatial coverage, observation or model-valid time, units, uncertainty, EvidenceBundle resolution, and correction/rollback lineage. For animation, available frames and gaps must remain explicit; a layer toggle or a timestamp selector does not prove historical coverage or authorize interpolation. See the [temporal feature boundary](apps/explorer-web/src/features/temporal/README.md).

### How to read KFM status

- **CONFIRMED** — verified from the named repository bytes, tests, or exact snapshot.
- **PROPOSED** — a design or decision that is not yet adopted or fully implemented.
- **NEEDS VERIFICATION** — checkable, but not established by the evidence in scope.
- **HOLD** — intentionally blocked until a named dependency, authority, safety, rights, sensitivity, or review condition is met.

Implementation maturity and authority are separate axes. An implemented validator can enforce only a proposed profile; an accepted decision can still be only partially implemented.

## How KFM protects meaning

KFM keeps the system’s trust path explicit:

1. **Source and lineage** identify where material came from, what role it has, and what remains unresolved.
2. **Evidence** binds a consequential claim to an `EvidenceRef` and an `EvidenceBundle` or to an already governed public-safe artifact.
3. **Policy** evaluates rights, sensitivity, access, precision, time, consent, cultural or stewardship limits, and release conditions.
4. **Review and release** remain governed transitions. A receipt, test, badge, commit, pull request, merge, or generated explanation cannot silently perform them.
5. **Public carriers**—maps, tiles, graphs, indexes, scenes, reports, dashboards, and AI language—display bounded results while preserving citations, uncertainty, correction, and rollback context.

The core lifecycle remains:

**RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLETS → PUBLISHED**

Promotion is a governed state transition, not a file move. Public clients use governed APIs and released public-safe artifacts; they do not read internal lifecycle stores, candidate material, private records, or model-runtime stores directly.

## Repository map

This is the verified direct-child snapshot of the repository at the evidence commit above. Child READMEs own deeper detail.

```text
Kansas-Frontier-Matrix/
├── .editorconfig
├── .env.example
├── .github/
├── .gitignore
├── .pre-commit-config.yaml
├── AUTHORS.md
├── CHANGELOG.md
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── Makefile
├── README.md
├── SECURITY.md
├── apps/
├── artifacts/
├── catalog/
├── configs/
├── connectors/
├── contracts/
├── control_plane/
├── data/
├── docs/
├── examples/
├── fixtures/
├── infra/
├── migrations/
├── package.json
├── packages/
├── pipeline_specs/
├── pipelines/
├── pnpm-lock.yaml
├── pnpm-workspace.yaml
├── policy/
├── pyproject.toml
├── release/
├── runtime/
├── schemas/
├── scripts/
├── tests/
└── tools/
```

### Where common work belongs

| Responsibility | Home |
|---|---|
| Browser and deployable applications | [`apps/`](apps/) |
| Semantic meaning and interfaces | [`contracts/`](contracts/) |
| Machine-checkable shapes | [`schemas/`](schemas/) |
| Rights, sensitivity, access, and release policy | [`policy/`](policy/) |
| Lifecycle records, evidence, receipts, and proofs | [`data/`](data/) |
| Executable transformations and specifications | [`pipelines/`](pipelines/) and [`pipeline_specs/`](pipeline_specs/) |
| Runtime composition and bounded adapters | [`runtime/`](runtime/) and [`packages/`](packages/) |
| Human doctrine, decisions, architecture, and runbooks | [`docs/`](docs/) |
| Tests, validators, fixtures, and operator tools | [`tests/`](tests/), [`fixtures/`](fixtures/), and [`tools/`](tools/) |
| Release, correction, withdrawal, and rollback decisions | [`release/`](release/) |

Directory placement is part of the trust model. Read the adopted [Directory Rules decision](docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) and the current [Directory Rules](docs/doctrine/directory-rules.md) before creating a path, reviving a deprecated root, or introducing a parallel authority.

## Run locally

The repository pins Node `>=22.13 <23` and `pnpm@11.17.0` for its private JavaScript workspace. Use the lane that matches what you are inspecting.

### Explorer Web workbench

```bash
corepack enable
pnpm install --frozen-lockfile
pnpm --filter explorer-web build
pnpm --filter explorer-web test
pnpm --filter explorer-web dev
```

The workbench’s local composition and fixture-first tests are useful for inspecting trust-visible UI, bounded Focus and Story behavior, map-selection handoffs, accessibility paths, and negative states. They do not establish a deployed product or live data path.

### KFM Explorer Sites application

The Sites application targets Node `>=22.13.0` and Linux helpers such as `flock`, `curl`, and GNU `timeout` for its bounded install/build scripts. The following commands are for deliberate local diagnosis, not repeated install/build steps during the normal Sites checkpoint lifecycle.

```bash
cd apps/kansas-frontier-matrix-explorer
npm run install:ci
npm run build
npm test
npm run dev
```

The project’s Sites identity, replacement, version, and rollback boundaries are documented in [`apps/kansas-frontier-matrix-explorer/README.md`](apps/kansas-frontier-matrix-explorer/README.md) and [`apps/kansas-frontier-matrix-explorer/docs/openai-sites-in-place-replacement.md`](apps/kansas-frontier-matrix-explorer/docs/openai-sites-in-place-replacement.md). A repository checkout does not deploy or restore a Site version.

### Python and repository validators

The Python project declares Python `>=3.11`. At this pin, [`pyproject.toml`](pyproject.toml) still points Hatch at `src/kfm`, while the root tree has no `src/` directory. Do not present `pip install -e ".[test]"` as a verified setup path. Repairing that distribution/placement mismatch needs its own reviewed slice; this documentation does not create a new root or a Python package.

For dependency-only validator setup from the inspected manifest, without building the missing root distribution:

```bash
python3 -m venv .venv
. .venv/bin/activate
python - <<'PYSETUP'
from pathlib import Path
import subprocess
import sys
import tomllib

project = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))["project"]
requirements = project["dependencies"] + project["optional-dependencies"]["test"]
subprocess.run([sys.executable, "-m", "pip", "install", *requirements], check=True)
PYSETUP
make validate
git diff --check
```

This installs the manifest's declared development dependencies, not KFM itself. It is not a locked Python environment, packaging repair, or a promise that aggregate validation passes. The setup command was inspected but not executed in this documentation review. `make validate` remains the repository-native aggregate validator entry point; use the narrowest relevant target and report exact results and inherited failures.

## Validation

Validation is evidence about a declared scope, not a universal correctness or release claim.

| Change | Proportionate evidence |
|---|---|
| README or documentation only | One H1, stable headings, relative links, balanced code fences/HTML, accurate status language, final newline, and `git diff --check`. |
| Contract, schema, policy, or validator | Focused positive and negative fixtures, the owning validator/tests, and review of downstream consumers. |
| Explorer UI or browser behavior | Targeted unit/browser tests, keyboard and focus paths, prior-render clearing, no-leak checks, and exact tested SHA. |
| Map-facing behavior | Renderer-import boundary, synthetic selection, governed resolver injection, no direct internal-store access, and compatibility evidence. |
| Release or publication-adjacent work | Evidence, rights, sensitivity, integrity, review, release, correction, and rollback records; a green test is not enough. |

Useful repository targets include:

```bash
make validate
make boundary-guards
make deny-test
make governed-api-smoke
make governed-api-verify
make ui-build
make maplibre-govern
make maplibre-proof
```

Some Make targets are readiness markers that intentionally print `TODO`, and the root JavaScript `lint`, `test`, and `build` scripts intentionally report `WORKFLOW_HOLD`. A zero exit status from a marker is not validation evidence; a workflow pass proves only its declared job for its exact revision and inputs.

## Contributing

The best contribution is a small, inspectable improvement that leaves the next step easier and safer.

1. Read [`CONTRIBUTING.md`](CONTRIBUTING.md), the applicable path-scoped README, and the [Directory Rules](docs/doctrine/directory-rules.md).
2. Define one observable goal, its owning responsibility root, affected contracts or interfaces, validation, and rollback.
3. Search for overlapping work and use a feature branch based on the current `main`.
4. Preserve evidence, rights, sensitivity, time, correction, and release boundaries in code and documentation.
5. Add focused tests, fixtures, receipts, or docs when they are direct dependencies of the change.
6. Use a draft pull request only through an eligible delivery path under [`CONTRIBUTING.md`](CONTRIBUTING.md). Where [issue #4024](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024) quarantines that path, preserve the branch and exact head with performed/skipped checks and rollback notes; do not create a same-path successor PR or infer ready/merge authority. Branch authoring is not itself blocked.

Good first contribution shapes include:

- improve an existing validator or negative fixture;
- make a trust-visible UI state more accessible;
- document one verified path without promoting its maturity;
- close a small contract-to-test gap;
- reconcile a stale link, anchor, or status claim;
- add a public-safe, deterministic example with its provenance and limitations.

Please use [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) for community expectations and [`SECURITY.md`](SECURITY.md) for private security reporting. Do not put credentials, restricted geometry, living-person or genomic data, private review material, or sensitive exploit detail into public issues or pull requests.

## Governing principles

KFM preserves these principles across maps, APIs, pipelines, reports, and AI-assisted workflows:

1. **Evidence outranks fluency.** If required support cannot be resolved, narrow, abstain, deny, hold, or report an error.
2. **A carrier is not an authority.** Maps, tiles, graphs, indexes, scenes, summaries, tests, badges, and generated language can carry a result; they do not become truth by displaying it.
3. **Public access crosses a trust membrane.** Ordinary clients consume governed interfaces and released public-safe artifacts, not internal stores.
4. **Sensitive material fails closed.** Unclear rights, sovereignty, cultural authority, privacy, consent, or harmful precision are reasons to restrict exposure—not to guess.
5. **Automation proposes; governance decides.** Watchers, builders, receipts, checks, and pull requests support review but do not perform approval, promotion, release, deployment, or publication by implication.
6. **Corrections remain visible.** Identity, supersession, correction, withdrawal, provenance, and rollback stay traceable when consequences require them.

Read the [Trust Membrane](docs/doctrine/trust-membrane.md), [Truth Posture](docs/doctrine/truth-posture.md), [Lifecycle Law](docs/doctrine/lifecycle-law.md), [AI Build Operating Contract](docs/doctrine/ai-build-operating-contract.md), and [accepted ADR-0029](docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) before changing a trust-bearing boundary.

## Current edges and non-goals

This README does not:

- admit a new renderer dependency or equate the implemented synthetic MapLibre canvas with real-data or production readiness;
- create a live API, model-provider, Qwen/Ollama, or internal-store browser path;
- activate a source or promote a lifecycle record;
- release a dataset, publish a report, deploy a site, or change hosting/settings;
- establish rights, cultural authority, stewardship, consent, review approval, or public-use permission;
- replace a contract, schema, policy, evidence bundle, receipt, proof, release record, or rollback card.

The most important open edges are the exact packaging mismatch noted above, hosted Explorer runtime/version verification, the integrated Explorer route and transport contract, Sites consumer capability reconciliation, real-layer admission, end-to-end evidence closure, complete accessibility and operational evidence, and governed release/publication proof.

## Project references

| Reference | Purpose |
|---|---|
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution, branch, pull-request, evidence, validation, and rollback discipline |
| [`SECURITY.md`](SECURITY.md) | Vulnerability reporting and sensitive-disclosure boundary |
| [`docs/`](docs/) | Human-readable doctrine, architecture, decisions, standards, source guidance, and runbooks |
| [`apps/kansas-frontier-matrix-explorer/`](apps/kansas-frontier-matrix-explorer/) | Public-facing Sites application source and hosting boundary |
| [`apps/explorer-web/`](apps/explorer-web/) | Fixture-first Explorer Web workbench with the package-owned Living Atlas MapLibre composition |
| [`apps/governed-api/`](apps/governed-api/) | Governed API implementation boundary |
| [`packages/maplibre/`](packages/maplibre/) | MapLibre-facing package and adapter seam |
| [`contracts/`](contracts/) and [`schemas/`](schemas/) | Meaning and machine-checkable shape |
| [`policy/`](policy/) and [`release/`](release/) | Admissibility and release/correction/rollback boundaries |
| [`CITATION.cff`](CITATION.cff) | Citation metadata for the repository |
| [`CHANGELOG.md`](CHANGELOG.md) | Tracked change history; not release or publication proof by itself |

## Last evidence review

| Field | Value |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Evidence snapshot | `main@664e46697d4d237870f5a482904bb9acd8f11b20` |
| Open pull requests at review time | `0` |
| Reviewed for this refresh | Root tree and README; root and MapLibre manifests; Python manifest; Explorer app documentation and Living Atlas import surface; PR #4464 metadata; open-PR listing; #4024; contribution/directory/AI-authoring guidance; Drive backfill and Notion Living Atlas coordination |
| Change class | Same-path documentation reconciliation; no application, dependency, schema, workflow, settings, or source-adapter change |
| No mutation implied | No source activation, settings change, release, deployment, promotion, publication, or lifecycle transition |
| Not proved | Fresh application build/unit/browser/hosted-CI results, full repository correctness, all workflow behavior, hosted runtime health, authentication, live data, rights clearance, human approval, release readiness, or public operation |

Re-review this README when repository topology, Explorer identity or host, authority boundaries, package metadata, validation entry points, or the adopted Directory Rules change.
