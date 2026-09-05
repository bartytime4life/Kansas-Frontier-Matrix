<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture/directory-implementation-profiles
title: Directory Implementation Profiles
type: architecture-profile
version: v0.1.0
status: proposed
owners: ["@bartytime4life"]
created: 2026-09-05
updated: 2026-09-05
policy_label: public
owning_root: docs/
responsibility: Candidate implementation profiles accompanying an unadopted Directory Rules amendment; not a second doctrine or requirements registry.
related:
  - ../adr/ADR-0039-directory-build-and-verification-profiles.md
  - ../doctrine/directory-rules.md
  - ./directory-current-state-20260905.md
[/KFM_META_BLOCK_V2] -->

# Directory implementation profiles

**Layer B / PROPOSED / NO CUTOVER.** [ADR-0039](../adr/ADR-0039-directory-build-and-verification-profiles.md) carries this profile. Existing adopted Directory Rules and accepted ADRs remain controlling. The named owner is the verified CODEOWNERS review route, not evidence of independent stewardship or approval.

Placement basis: adopted Directory Rules §9.1 gives `docs/` human-facing architecture responsibility; §§10, 14–16 define the existing implementation, dependency, generation, and documentation boundaries. This file explains candidate conventions inside that accepted owner. It creates no root, policy, schema, lifecycle store, deployment profile, or active enforcement mechanism.

## 1. Placement decision in practice

Classify the artifact before choosing a folder: one authority owner, lifecycle where applicable, execution role, scope, exposure, mutability, retention, writers, and consumers. Reference related authorities rather than copying them into a new owner. Use existing `PLACE`, `SPLIT`, `MIGRATE`, `MIRROR`, `HOLD`, and `DENY` outcomes.

| Artifact responsibility | Existing owning root | Boundary |
| --- | --- | --- |
| Deployable composition, framework routing, local feature state/views/controllers, app authentication and worker entrypoints | `apps/` | App-local is legitimate; no imports into a different app's private implementation. |
| Genuinely shared, independently testable implementation | `packages/` | Public interfaces and dependency direction; extraction is justified by behavior/reuse, not tree appearance. |
| Source acquisition and source-specific adaptation | `connectors/` | Candidate capture and receipts, not canonical truth, feature UI, or publication. |
| Transformation implementation and declarative run specification | `pipelines/`, `pipeline_specs/` respectively | Separate executable transformation from declared run identity; neither grants approval. |
| Meaning, machine shape, admissibility | `contracts/`, `schemas/`, `policy/` respectively | Bind generated transport types to their sources; no parallel semantic writers. |
| Provider composition and deployment/exposure | `runtime/`, `infra/` respectively | Browser code receives no secrets or internal-store access; host adapters remain downstream of governed interfaces. |
| Operator validators/generators and thin invocations | `tools/`, `scripts/` respectively | Production app code must not acquire its implementation by importing repository tools. |
| Shared conformance and reusable public-safe test inputs | `tests/`, `fixtures/` | Preserve permitted colocation; do not centralize all tests or create competing fixture authorities. |
| Lifecycle/accountability instances and release decisions | `data/`, `release/` | Classify actual family, sensitivity and retention; filenames and build copies do not promote data. |

Framework-required hidden files, server composition, browser shell, local worker and build plugin may legitimately coexist inside an application. Provider-specific configuration alone does not justify a new root. A folder called `packages` nested in an app does not inherit root `packages/` authority.

## 2. Application and package dependency contract

Each supported entrypoint should carry the following compact contract in its existing boundary documentation. Do not create another machine registry merely to collect it.

| Field | Required evidence |
| --- | --- |
| Edited source | Exact app/package path and revision, framework entrypoints, route and worker wiring. |
| Interface dependencies | Public exports, source aliases, transitive source imports, generated bindings and required assets. |
| Installer inputs | Actual installer/version constraints, manifest, workspace membership, consumed lockfile and build-script policy. |
| Assembly | Source input root or explicit assembly command; input manifest, generator identity and exclusions. |
| Builder | The context actually received by the builder, not a developer's larger checkout. |
| Verification | Real build/typecheck command, target tests and selectors, CI entrypoint and observed result. |
| Correction | Coupled source/alias/installer/artifact changes and a coherent rollback unit. |

An app-only source export cannot drop sibling packages referenced by TypeScript or bundler aliases. Either preserve the permitted dependency layout or test an explicit assembly procedure. Installing npm dependencies does not itself supply repository source aliases. A presence guard is useful but does not validate transitive imports, package resolution, workers, styles, or runtime behavior.

Preserve the accepted package-owned MapLibre acquisition seam, including worker/CSS/plugin/protocol delivery. Do not create another renderer package or use CDN/global acquisition as an export workaround. Keep the neutral runtime port distinct from the concrete renderer adapter: importing the former does not prove acquisition or rendering of the latter.

Preserve each lockfile with a verified installer consumer. A root pnpm workspace and app-specific npm entrypoint may both be legitimate. Dependency cleanup must preserve the existing allow/deny build-script policy; blanket approval, ignored audit failures and unrelated upgrades are outside a placement repair.

## 3. Local and cross-system test ownership

| Test class | Placement and discovery | What a passing result can establish |
| --- | --- | --- |
| Unit/algorithm | App/package-local where permitted; real local selector | Owned logic and negative cases, not full app integration. |
| Component/DOM | App/package-local, with explicitly test-only host and fixtures | Interaction/state within that host; not GPU or deployed operation. |
| Contract/schema/policy | Existing repository-wide owner and registered fixtures | Meaning/shape/admissibility assertions actually checked; never approval merely from schema validity. |
| Cross-system integration | Existing shared test owner; explicit runtime adapters and no-network posture | The tested boundaries, with mocks distinguished from actual providers. |
| Browser/end-to-end | Actual application path where claimed, with declared browser/environment | Keyboard/focus, worker/CSS delivery, rendering or user journey only to the extent observed. |
| Visual/performance/long-session | Capability-specific repeatable conditions and measured budgets | Recorded conditions and durations, not an untested production SLO or GPU/device matrix. |

Before moving a test, prove its old and new selectors collect the intended nonzero cases; preserve its target imports and CI reachability. A deliberately relevant mutation should demonstrate a new guard where proportionate. Exact expected diagnostics and state effects distinguish an expected negative from an unrelated error. Do not count arbitrary nonzero exits, skipped checks, intentional root placeholders or empty discovery as passes.

Existing aggregate check names remain stable unless separately reviewed. Selective validation should follow actual dependency changes, not one new workflow per folder. Report missing coverage as backlog and an unavailable dependency/tool/network as an environment limitation.

## 4. Fixture, generated-content and bundle boundaries

| Class | Ownership and inclusion | Retention and exposure |
| --- | --- | --- |
| Shared public-safe test fixture | Existing fixture owner; declared consumers and selectors | Test-only by default; inclusion in a public build requires an explicit reviewed purpose. |
| Private or restricted test input | Controlled test owner and access | Least privilege, redacted diagnostics/exports, explicit retention; never ordinary public-bundle content. |
| Runtime demonstration | App-owned presentation input or a separately governed fixture interface | Persistent synthetic/fixture disclosure; no live-source, approval or release claim. |
| Released data carrier | Governed released artifact/API | Identity, rights, sensitivity, validation, provenance, integrity, receipts/proofs, policy, review, correction and rollback closure. |
| Generated code/assets | Owning implementation or declared generated subtree | Source pointer, generator/version, content digest, edit policy and regeneration command. |
| QA/build output | Existing `artifacts/` permitted lane or external CI artifact | Disposable/rebuildable unless a specific audit obligation says otherwise; not a durable release record. |
| Receipt/proof/catalog/release record | Existing family owner, not generic build output | Preserve durable or audit-bound history and correction links; never move by filename alone. |

Keep large geospatial payloads, imagery, terrain, tiles, weights, installations, caches and disposable output out of ordinary Git unless a reviewed exception applies. Retain logical IDs, metadata, digests, recipes and locators; a pointer does not authorize admission. Before removal, establish writers, known consumers, exposure, retention and recovery. Unknown consumer closure is not permission to delete.

Default applications must not conceal a failed live path by substituting synthetic content while retaining live-data language. Trace every broad copy/glob into the actual builder input. Runtime demonstrations, test-only data, internal stores and released products require separate inclusion decisions.

## 5. Capability-to-verification records

Reuse existing requirement/capability IDs and feature/function projections. A projection's word `ACTIVE`, `VERIFIED_SLICE` or `SITE PROOF` is not an executed result. Trace stable public boundaries rather than all private functions:

`existing ID -> user outcome -> app surface -> owner -> function/type/command/API -> contract/schema/policy -> fixtures/tests -> CI -> acceptance -> evidence/status -> correction/rollback`.

Accepted requirement, proposal, example and recovered research idea are separate categories. Record implementation, integration, validation, deployment and release independently. A branch may contain a tested fixture while the actual app adapter is dormant and no public deployment has been inspected.

## 6. Negative acceptance matrix

These are candidate acceptance criteria, not claims of current coverage.

| Situation | Required bounded behavior | Relevant evidence |
| --- | --- | --- |
| Denied/restricted or stale evidence | No protected detail or unsupported current claim | Contract/policy cases plus the actual display/export/log boundary. |
| Malformed local import | Safe rejection and correct preview clearing; no unintended upload | Parser negatives and real browser network/storage observation. |
| Unsupported time or interrupted frame | Explicit unsupported/error state; stale frame/evidence cannot win | Temporal contract cases, cancellation/replay and app composition tests. |
| Missing sibling package/renderer capability | Explicit diagnostic; no global/CDN renderer or misleading synthetic substitution | Source-context negative, real build and capability-specific browser tests. |
| Focus/Qwen unavailable or unsupported | Finite contract outcome and cite-or-abstain; no direct browser-provider path | Governed transport tests, provider-adapter boundary and UI outcome tests. |
| Workspace/report replay | Preserve input/evidence/version/time identity and privacy | Save/restore/export round-trip, correction and redaction cases. |
| Keyboard/mobile/accessibility | Operable focus, controls, panels and escape paths | Actual browser interactions plus manual assistive/device work where needed. |
| Worker/CSS, visual/performance and long sessions | Measure the actual delivery and runtime path | Browser/GPU evidence for rendering; explicit device, duration and resource limits. |

Observation, model and synthetic status remain distinct. Valid, observed, retrieval and release time must not be silently substituted. A visual animation is not a new observation, and a measurement is not automatically source truth.

## 7. Hosting and operation

Keep Linux development, a proposed self-hosting profile, repository build contexts, and the existing hosted Site as separately evidenced surfaces. A server-rendered composition, provider-specific plugin and browser entrypoint can have legitimate different homes within one app. This profile does not migrate hosting, change the Site, select a canonical app, or authorize Vercel deployment.

Public clients use governed APIs or released artifacts, never RAW/WORK/QUARANTINE/internal stores. Runtime model providers remain behind governed interfaces. Exposure and administration are deny-by-default, least-privilege and auditable. Preserve the existing Explorer identity, slug, URL and rollback history.

## 8. Migration and rollback checklist

A proposed move/merge/deletion/alias records current and target paths, owning root, rule/ADR basis, immutable artifact identity, writers, known consumers, exposure, retention, affected tests, decision required and rollback. Separate mechanical relocation from behavior changes. Preserve fragments and aliases until legitimate retirement closes; never hide unresolved ownership in a giant archive.

Code rollback restores compatible interfaces, aliases, installer inputs and tests together. It does not rewrite historical receipts, restore revoked access, restore damaged conflict markers, or imply data/deployment rollback. Active authority cutover and any held migration remain distinct decisions under DIR-AUTH-004.
