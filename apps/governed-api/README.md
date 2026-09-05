<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://app/governed-api/readme
title: Governed API App README
type: app-readme
version: v0.3
status: draft; repository-grounded; bounded-scaffold
owners: OWNER_TBD — Apps steward · API steward · Policy steward · Evidence steward · Release steward · Runtime steward · Docs steward
created: 2026-06-16
updated: 2026-09-05
policy_label: public
owning_root: apps/
current_path: apps/governed-api/README.md
responsibility: explain the current app entrypoint, routes, envelope shape, local operation, validation limits, and governed graduation boundary
truth_posture: CONFIRMED source and test inventory; PROPOSED broader capabilities; UNKNOWN deployment and operational closure
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: de25f099381cf0cad87884fe5bb35b17d4c1fa04
  initial_inspection_commit: cbd6d82bad962a58ab62cfb776ee31696b575107
  prior_readme_blob: 4f21150852f133ba919b11f4f8792185fa870dae
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  main_module_blob: 4eb335c7c0b27f62c7419c478542e8fe40e1ff38
  route_registry_blob: 3418168d0b267160d6ad6dd87f289e880ef4a024
  envelope_builder_blob: 371e60d9f96c78e31c8a1e6109d19dee5da4213b
  response_schema_blob: 8b86e7db8b18b65a56a4e639dfc54e1b2db93155
  api_workflow_blob: 84ba16a3c36a1d58b2f6f1059a31ed6354063357
related:
  - ../README.md
  - ../explorer-web/README.md
  - ../../CONTRIBUTING.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md
  - ../../contracts/runtime/runtime_response_envelope.md
  - ../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../.github/workflows/api-test.yml
tags: [kfm, apps, governed-api, wsgi, runtime-response-envelope, finite-outcomes, evidence, policy, release]
notes:
  - "Same-path documentation update; no runtime, schema, policy, dependency, or release change."
  - "Current handlers emit RuntimeResponseEnvelope-shaped ABSTAIN or ERROR scaffolds, not operational evidence or policy decisions."
  - "ADR-0029 is accepted; ADR-0004 remains draft/proposed. Historical ADR implementation snapshots do not override current source."
  - "Execution results belong to exact-head PR/check records; this README does not claim continuously passing CI."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed API App

`apps/governed-api/` contains KFM's **bounded Python WSGI scaffold** for the governed API. It runs locally and registers three GET routes. Each returns `ABSTAIN / NOT_IMPLEMENTED`; unknown routes and unsupported methods return safe `ERROR` envelopes. It is **not yet a production evidence, policy, or release service**.

[Local quick start](#111-local-quick-start) · [Actual routes](#7-route-family-map) · [Envelope](#9-runtime-outcome-contract) · [Tests and CI](#12-validation-expectations) · [Open gates](#15-open-verification-items)

| Status axis | Evidence at the pinned base |
|---|---|
| Source inventory — **CONFIRMED** | WSGI entrypoint, route registry, envelope builders, six app tests, and command-bearing API workflow exist. |
| Capability maturity | **Bounded scaffold**: `ABSTAIN` and routing `ERROR` paths; no registered `ANSWER` or policy `DENY` implementation. |
| Architecture authority | Accepted ADR-0029 governs placement. ADR-0004's trust-membrane decision remains **draft/proposed**, not accepted by this README. |
| Operational closure | **UNKNOWN / NEEDS VERIFICATION**: live client integration, deployment, operational isolation, evidence/policy/release integration, observability, and rollback rehearsal. |
| Stewardship | `OWNER_TBD` is retained; named app stewardship and independent review are not inferred from a repository owner. |

> [!IMPORTANT]
> HTTP `200 OK` is not an answered claim. Inspect `outcome` and `reason_code`. The scaffold's empty evidence list, fixed hash, and synthetic state strings are not proof of evidence, policy approval, freshness, or release.

## Quick jump

[1. Purpose](#1-purpose) · [2. Repo fit](#2-repo-fit) · [3. Authority boundary](#3-authority-boundary) · [4. Default posture](#4-default-posture) · [5. Inputs](#5-inputs) · [6. Exclusions](#6-exclusions) · [7. Route family map](#7-route-family-map) · [8. Diagram](#8-diagram) · [9. Runtime outcome contract](#9-runtime-outcome-contract) · [10. API obligations](#10-api-obligations) · [11. Inspection path](#11-inspection-path) · [12. Validation expectations](#12-validation-expectations) · [13. Safe change pattern](#13-safe-change-pattern) · [14. Definition of done](#14-definition-of-done) · [15. Open verification items](#15-open-verification-items)

## 1. Purpose

The intended responsibility is the dynamic trust boundary between ordinary clients and KFM evidence, policy, and released public-safe projections. Explorer Web, an Evidence Drawer, Focus Mode, stories, comparisons, exports, and role-gated review retrieval are potential consumers; their existence does not prove integration with this process.

The current app proves a smaller boundary: importable route handlers, finite negative responses, JSON serialization, and local WSGI dispatch. It does not acquire sources, resolve `EvidenceRef -> EvidenceBundle`, evaluate policy, authorize callers, invoke Qwen/Ollama, or approve publication. Future capabilities must preserve those responsibility boundaries rather than return invented success from the scaffold.

## 2. Repo fit

This existing path remains under `apps/`, the deployable-application root. [Directory Rules §10.1, `DIR-EXEC-001`](../../docs/doctrine/directory-rules.md), adopted by [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md), separates app composition from reusable packages, source acquisition, and pipeline transformations. No new root, route home, or authority is introduced.

| Verified surface | Role |
|---|---|
| [Parent app guide](../README.md) | Application ownership and cross-app orientation. |
| [App manifest](pyproject.toml) | `kfm-governed-api` version `0.0.0`; explicitly a placeholder, not a complete packaging/run configuration. |
| [WSGI entrypoint](src/governed_api/main.py) | `app(environ, start_response)`, JSON responses, and loopback development server. |
| [Route registry](src/governed_api/routes/registry.py) | Executable registration of `/bootstrap`, `/layers`, and `/evidence`. |
| [Envelope builders](src/governed_api/stub.py) | Scaffold-only `ABSTAIN` and routing `ERROR` values. |
| [App tests](tests/) | Route/envelope assertions and bounded import/store-literal guards. |
| [Root Makefile](../../Makefile) | Local server and focused API validation targets. |
| [API workflow](../../.github/workflows/api-test.yml) | Two Python 3.11 jobs for the smoke suite and focused ABSTAIN contract test. |

The importable route modules live under **`src/governed_api/routes/`**. The separate `routes/`, `src/routes/`, and `src/ai/` trees contain documentation and, in some lanes, placeholders at this snapshot. They do not register additional endpoints or provide a model adapter. A README or directory name is not routing evidence.

## 3. Authority boundary

The API is an enforcement and projection responsibility, not the authority for source truth, semantic contracts, machine schemas, policy authorship, evidence authorship, review approval, release decisions, or canonical storage.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
                                                     governed transition ^

Intended client access: governed API or separately governed released artifacts
Never ordinary client access: raw/work/quarantine/canonical/internal/model stores
```

Promotion requires its own evidence, rights, sensitivity, validation, integrity, policy, review, correction, and rollback closure. A response, commit, PR, merge, passing test, or rendered map does not perform that transition. Maps, tiles, graphs, summaries, scenes, and AI remain downstream carriers rather than truth authorities.

[ADR-0004](../../docs/adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md) remains design lineage with a draft/proposed decision. Its older DecisionEnvelope-shaped implementation description is historical: the current builder and tests use the `RuntimeResponseEnvelope` field set described below. This source reconciliation neither accepts the ADR nor claims full trust-membrane enforcement.

## 4. Default posture

Keep this scaffold fail-closed. Missing evidence, policy, rights, sensitivity, review, or release support must not be concealed by a successful HTTP status, synthetic content, or generated language.

In the **current implementation**, abstention means the route is not implemented; it is not an evidence-quality assessment. The 404/405 paths return `ERROR`, not a policy `DENY`. The server does not perform request-schema validation, caller authorization, policy evaluation, evidence resolution, or response-schema validation on each request. These remain graduation work.

For sensitive exact locations, archaeology, rare species, infrastructure, living-person/DNA information, private land, or unclear cultural/sovereignty authority, preserve denial, quarantine, redaction, generalization, or staged access until the governing controls permit exposure. Adding a route or UI layer must not bypass those controls.

## 5. Inputs

| Current input | Actual use and limit |
|---|---|
| WSGI `PATH_INFO` | Exact lookup in `ROUTES`; absent value defaults to an empty path. |
| WSGI `REQUEST_METHOD` | Defaults to `GET` if absent; any non-GET method on a registered path is rejected. |
| `GOVERNED_API_ISSUED_AT` | Optional timestamp override for reproducible fixtures; otherwise current UTC time is used. The override is not validated by the builder. |
| Query string, request body, caller identity, selected feature/time | Not consumed by the current handlers. Supplying parameters does not activate lookup, filtering, authentication, or temporal support. |

Future inputs such as bounded layer/feature identifiers, spatial and temporal scope, evidence references, or caller context require explicit contracts, parsing, policy checks, and negative tests. Client-supplied release or policy claims cannot become authority.

## 6. Exclusions

| Responsibility excluded from this app | Owning responsibility |
|---|---|
| Reusable evidence, temporal, hashing, or policy-support logic | `packages/` |
| Source-specific acquisition and admission | `connectors/` |
| Lifecycle transformations and declarative run graphs | `pipelines/` and `pipeline_specs/` |
| Semantic meaning, machine shape, admissibility rules | `contracts/`, `schemas/`, and singular `policy/`, respectively |
| Lifecycle artifacts, identities, receipts, and proofs | Their governed lanes under `data/` |
| Release, correction, withdrawal, and rollback decisions | `release/` |
| Provider wiring and deployment/network exposure | `runtime/` and `infra/`, respectively |
| Browser rendering or stewardship UI | The appropriate client application, not this WSGI server |

These are responsibility boundaries, not a claim that every supporting capability is implemented. Do not create a parallel schema, contract, policy, registry, proof, or release home here.

## 7. Route family map

The [registry](src/governed_api/routes/registry.py) and [dispatcher](src/governed_api/main.py) define the following exact behavior:

| Request | HTTP response | Envelope outcome / reason | Current meaning |
|---|---|---|---|
| `GET /bootstrap` | `200 OK` | `ABSTAIN / NOT_IMPLEMENTED` | No runtime configuration or feature flags are supplied. |
| `GET /layers` | `200 OK` | `ABSTAIN / NOT_IMPLEMENTED` | No layer catalog, geometry, tiles, or manifests are supplied. |
| `GET /evidence` | `200 OK` | `ABSTAIN / NOT_IMPLEMENTED` | No EvidenceBundle or Evidence Drawer lookup occurs. |
| Non-GET on any registered path | `405 Method Not Allowed` | `ERROR / SAFE_RUNTIME_ERROR` | `id=stub:error:method-not-allowed`. |
| Any unregistered path | `404 Not Found` | `ERROR / SAFE_RUNTIME_ERROR` | `id=stub:error:route-not-found`. |

Paths are exact: `/layers/`, `/evidence/example`, and `/runtime/bootstrap` are not registered. `HEAD` and `OPTIONS` do not have special support. The checked-in method test explicitly covers `POST`, `PUT`, and `DELETE`; the dispatch condition rejects every non-GET method on a registered path.

Focus, story, compare, export, review, correction, diagnostics, and temporal-query route families remain **PROPOSED**, not endpoints promised by this README. Do not infer routes from the documentation-only domain trees or from another branch's implementation.

## 8. Diagram

```text
Current bounded implementation

WSGI request -> exact route + method dispatch
                |-- registered GET -> stub builder -> 200 + ABSTAIN
                |-- registered non-GET ------------> 405 + ERROR
                `-- unknown path ------------------> 404 + ERROR

No evidence, policy, release, storage, or model backend is connected here.
```

The intended governed extension is `bounded request -> evidence resolution -> policy/rights/sensitivity/review/release checks -> validated finite response -> client`. That sequence is an integration obligation, not a description of a connected production service.

## 9. Runtime outcome contract

The [RuntimeResponseEnvelope semantic contract](../../contracts/runtime/runtime_response_envelope.md) and its [paired machine schema](../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json) remain proposed/schema-paired artifacts consumed by bounded implementation and tests. Keep them distinct from an internal `DecisionEnvelope` or a `PolicyDecision`.

| Outcome | Intended meaning | Registered app behavior today |
|---|---|---|
| `ANSWER` | Evidence-supported, permitted response with disclosed precision and limitations. | Not emitted. |
| `ABSTAIN` | Insufficient support or unsupported scope; no fabricated answer. | Emitted only as `NOT_IMPLEMENTED`. |
| `DENY` | Policy, rights, sensitivity, role, or release decision prevents response. | Not emitted; no policy evaluation is implemented. |
| `ERROR` | Reliable completion is prevented by a runtime/validation fault. | Safe envelopes for unknown-route and unsupported-method handling only. |

The ten unconditional fields are `id`, `spec_hash`, `version`, `issued_at`, `outcome`, `reason_code`, `evidence_refs`, `policy_state`, `freshness`, and `correction_state`. The schema closes additional properties. For `ANSWER`, it additionally requires `precision_actually_used` and at least one top-level evidence reference; non-ANSWER outcomes must omit the precision field.

With the timestamp override in the local example, `GET /layers` returns this scaffold payload:

```json
{
  "id": "stub:layers",
  "spec_hash": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "version": "v1-stub",
  "issued_at": "2026-09-05T00:00:00+00:00",
  "outcome": "ABSTAIN",
  "reason_code": "NOT_IMPLEMENTED",
  "evidence_refs": [],
  "policy_state": "baseline",
  "freshness": "current",
  "correction_state": "none"
}
```

> [!CAUTION]
> The 64-`a` hash is a fixed placeholder, not a computed integrity or provenance digest. `baseline`, `current`, and `none` are hard-coded scaffold labels, not evaluated policy, source freshness, or correction history. The timestamp describes envelope issuance, not observation time or data validity. Reproducibility requires a fixed timestamp override.

The routing errors contain no reflected request path or `detail` field. This bounded behavior is not a general exception-redaction middleware guarantee. Do not add unsupported citation, release, audit, or payload fields to a closed envelope without a coordinated contract/schema/consumer change.

## 10. API obligations

Before an endpoint graduates beyond the stub, it must establish bounded request parsing, trusted caller context where required, evidence/citation closure, policy pre/post-checks, rights and sensitivity handling, review and release state, correction/rollback support, validated response shape, and audit-safe error handling.

Public clients must not select internal filesystem paths or directly call model providers. A governed static-delivery path may serve already released public-safe artifacts; it must not become an alternate policy or release authority. Qwen/Ollama integration, when admitted, stays server-side and evidence-subordinate, with finite answer/abstain/deny/error results.

Temporal support must distinguish envelope issuance from observation, validity, retrieval, and release time as required by the governing contracts. No time slider, map animation, chart, or workspace state can supply evidence or release authority missing from this API.

## 11. Inspection path

### 11.1 Local quick start

Use a full repository checkout and Python **3.11 or newer**, as declared by the [root Python manifest](../../pyproject.toml). From the repository root:

```bash
make governed-api-dev
```

The [Makefile](../../Makefile) invokes the module directly with its source path. `make api-run` is an alias. The equivalent command is:

```bash
PYTHONPATH=apps/governed-api/src python -m governed_api.main
```

The development server binds to **`127.0.0.1:8000`**. Stop it with `Ctrl-C`. For deterministic example output, stop the first server and start:

```bash
GOVERNED_API_ISSUED_AT='2026-09-05T00:00:00+00:00' make governed-api-dev
```

From a second terminal, inspect both HTTP and envelope state:

```bash
curl -i http://127.0.0.1:8000/layers
curl -i -X POST http://127.0.0.1:8000/layers
curl -i http://127.0.0.1:8000/not-a-route
```

Expect respectively `200 / ABSTAIN`, `405 / ERROR`, and `404 / ERROR`, not real layer data. The server uses the standard-library WSGI implementation. The app-local placeholder `pyproject.toml` is not the basis for a standalone package installation or production server command.

Keep the development listener on loopback. This example does not configure public hosting, TLS, firewall rules, a reverse proxy, process supervision, production authorization, or a live Explorer/Sites connection.

### 11.2 Inspect the actual surface

```bash
git ls-files apps/governed-api
sed -n '1,180p' apps/governed-api/src/governed_api/main.py
sed -n '1,120p' apps/governed-api/src/governed_api/routes/registry.py
sed -n '1,180p' apps/governed-api/src/governed_api/stub.py
```

Re-pin current main and relevant source blobs before refreshing this snapshot. Read the current code and tests rather than inheriting maturity claims from historical branches, PDFs, ADR snapshots, or coordination notes.

## 12. Validation expectations

For repository testing, follow [CONTRIBUTING](../../CONTRIBUTING.md) from the repository root. In a dedicated environment:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -e ".[test]"
make governed-api-smoke
make governed-api-verify
python -m pytest apps/governed-api/tests/test_abstain_routes.py -q --strict-config --strict-markers
make deny-test
git diff --check
```

Dependency installation may contact package indexes; these API tests do not require live source systems, model services, or public deployments. These are verified command definitions, not a claim that every command or hosted job has passed on every revision.

| Check | What it covers | Evidence limit |
|---|---|---|
| [ABSTAIN route test](tests/test_abstain_routes.py) | All registered GET routes, deterministic ten-field payloads, fixed timestamp, empty evidence, and no DecisionEnvelope/precision fields. | One test loops over the route set; not evidence-backed answers. |
| [Boundary tests](tests/test_boundary_guards.py) | 404/405 safe shapes, three-route inventory, renderer/model import prefixes, and forbidden store-path literals. | Five tests; static string guards are not sandboxing, authorization, or proof against all dynamic access. |
| [Schema subset helper](tests/schema_assert.py) | Types, required keys, and closed additional properties. | Does not implement full JSON Schema: `$ref`, formats, patterns, enums, and conditionals are not generally evaluated by this helper. Some values are asserted explicitly by the route tests. |
| `make governed-api-verify` | App test suite plus tracked-file `git grep` for forbidden renderer/model import lines. | Requires a real Git checkout; not an egress firewall or provider-isolation proof. |
| `make deny-test` | The five boundary tests with strict pytest options. | The target name does not mean the app emits policy `DENY`. |
| [API workflow](../../.github/workflows/api-test.yml) | `governed-api-tests` runs the smoke suite; `envelope-shape-tests` runs the focused ABSTAIN test on Python 3.11 after repository CI dependency installation. | Workflow wiring is not a successful run, a required merge gate, or release permission. |

The workflow handles pull requests, pushes to main, and manual dispatch with read-only contents permission. It emits logs/check summaries, not release artifacts. Record hosted run IDs, exact tested SHA, actual conclusions, and any base/head failure comparison in the PR. Never call inherited, skipped, pending, or unrun checks passing.

## 13. Safe change pattern

Keep each change dependency-closed and reversible: pin base/target bytes, check overlapping work, inspect the registered routes and governing contracts, add focused positive/negative cases for changed behavior, then validate the actual changed area. Do not use missing production readiness as a reason to block safe documentation or fixture authoring.

A new evidence-bearing or public route requires the appropriate contract/schema/policy/consumer changes and tests; a README must not create those promises by itself. Preserve finite outcomes, source roles, spatial/temporal scope, rights/sensitivity controls, evidence references, citation obligations, correction state, and rollback lineage wherever material.

Update affected app/client guidance when behavior changes. This revision changes only this README: route code, contracts, schemas, policy, workflows, dependencies, parent navigation, and historical records remain unchanged. Existing numbered section anchors and `doc_id` are preserved.

## 14. Definition of done

For **this documentation slice**, completion means a source-pinned current inventory, accurate route/envelope examples and commands, resolving navigation, explicit test limits, and a reviewable diff with actual validation evidence. It does not mean the API is production-ready.

Before **runtime graduation**, the following remain required:

- [ ] Assigned stewardship, independent review appropriate to risk, and resolved decision authority.
- [ ] Bounded request validation and trusted authentication/authorization where required.
- [ ] EvidenceBundle resolution, citation closure, policy/rights/sensitivity decisions, and release checks.
- [ ] Contract-compliant responses with meaningful non-placeholder identity, precision, freshness, and correction semantics.
- [ ] Positive and negative integration tests, safe exception handling, and verified client behavior.
- [ ] Operational isolation, auditability, release/correction/rollback support, and a separately authorized deployment/release decision.

## 15. Open verification items

| Remaining work | First boundary affected |
|---|---|
| Replace synthetic envelope labels through governed implementation, not wording changes | Any claim-bearing response. |
| Add complete schema validation and request/error handling without widening closed contracts casually | New request/response behavior. |
| Integrate evidence, policy, rights, sensitivity, and release/correction/rollback services | `ANSWER`, policy `DENY`, or real released-artifact delivery. |
| Prove client transport, evidence selection, temporal behavior, and finite-state rendering | Live Explorer, Sites, chart, report, or Focus integration. |
| Verify authentication, resource limits, operational isolation, logging, and safe errors | Public or role-gated exposure. |
| Obtain exact-head CI and qualified review for each change | Integration of that change; not retroactive runtime proof. |
| Verify deployment and rollback rehearsal separately | Public operation, release, promotion, and publication. |

### Appendix A — preservation and rollback

The prior v0.2 README's trust-membrane purpose, lifecycle, finite outcomes, responsibility split, and sensitive/public-access exclusions are retained. Blanket unknown-route/test statements are replaced with the inspected scaffold. Proposed route families remain explicitly proposed, and no historical record is rewritten into proof of current behavior.

Rollback for this documentation-only revision is to restore the prior README blob `4f21150852f133ba919b11f4f8792185fa870dae` through a reviewed revert. No data migration, source activation, schema change, policy rollback, or deployment rollback is needed. Restoration also restores the old documentation limitations; it is not a recommended runtime change.

## Status summary

**CONFIRMED:** a small local WSGI scaffold with three abstaining GET routes, safe routing errors, proposed schema-paired envelopes, and focused test/CI wiring. **Not established:** a complete governed production API. Continue through bounded, tested, independently reviewed slices without collapsing implementation, evidence, policy, approval, release, and publication.

[Back to top](#top)
