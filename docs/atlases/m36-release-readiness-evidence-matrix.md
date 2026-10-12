<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/m36-release-readiness-evidence-matrix
title: M36 Synthetic Atlas Release-Readiness Evidence Matrix
type: evidence-index
version: v0.2
status: proposed; bounded; synthetic-only; partial; hold; non-authoritative; non-release; non-publication
owner: "@bartytime4life via CODEOWNERS; independent atlas, release, evidence, security, accessibility, operations, and stewardship review NEEDS VERIFICATION"
created: 2026-09-14
updated: 2026-09-15
policy_label: repository-public; documentation; synthetic; cite-or-abstain; release-readiness; no-network; no-authority
owning_root: docs/
responsibility: "Index current repository evidence and M01-M35 coordination records for one synthetic atlas candidate, classify explicit readiness gaps, and define a reversible review packet without duplicating milestone evidence or creating release, deployment, promotion, publication, source-admission, or policy authority."
truth_posture: "CONFIRMED execution-start pin, issue states, Directory Rules placement, materialized synthetic carrier bytes, manifest and reference digest closure, carrier metadata validation, and non-authorization regression / PARTIAL fixture-only identity, geometry, time, reference, policy-context, validation, catalog, correction-field, and rollback-reference coverage / ABSENT governed API, Explorer rendering, accessibility acceptance, observability, stewardship, correction and rollback execution, and monitoring / UNKNOWN hosted exact-head results, production parity, external consumers, release authority, deployment state, and publication state"
evidence_repository: bartytime4life/Kansas-Frontier-Matrix
evidence_base_ref: main
evidence_base_commit: fbd08c2c9f361ea7b2e255923a27e4a549469d42
evidence_inspected_at: 2026-09-15
evidence_open_pull_requests: 0
evidence_issue: 3396
evidence_candidate_fixture_sha256: 23d166d23be3872ce9e754413e08de53dcea117de070a73146e8799f88cecf12
evidence_promotion_packet_sha256: aa941c1d36e36052123a36e7a1da6c319f770904b6d31cd315b5a6b090f27f9d
evidence_release_manifest_sha256: 5138edd2e8f44a4576956790d66fde442a1c86e7c3a4c196c3e7e7b6751f3f39
evidence_synthetic_carrier_sha256: 8ad3948994680b0e6a85a3eb4c82f69466d0c5c2baf4c15fb4e14e43c1acb26d
evidence_directory_rules_sha256: 44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e
evidence_merged_non_authorization_regression: 27202a0595ecdc6afd6f98b3aedaa236243e07b3
inspection_boundary: "Current-session reads covered issue 3396, M01-M35 issue state and labels, issues 4415 and 4418, the zero-open-PR queue, current main, accepted ADR-0029, the atlas and release README contracts, the selected synthetic fixture family, its focused tests, and a tracked-working-tree SHA-256 scan. No live source, governed API, browser, hosted Site, deployment, release store, signing service, production telemetry, external consumer, or publication endpoint was exercised."
related:
  - ./README.md
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../doctrine/directory-rules.md
  - ../../release/README.md
  - ../../contracts/release/operational_trust_rollup.md
  - ../../fixtures/release/promotion_verification_execution/valid/pass.json
  - ../../tests/release/test_synthetic_release_closure.py
  - ../../tests/validators/test_validate_operational_trust_rollup.py
tags: [kfm, m36, atlas, release-readiness, evidence-matrix, synthetic, hold, non-authoritative]
notes:
  - "This document references milestone coordination records; it does not copy their closure evidence."
  - "Closed milestone issue state is not release, deployment, promotion, publication, or current-main conformance evidence."
  - "The selected candidate is a documentation-only coordination label over an existing synthetic fixture subject, not a new lifecycle object."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# M36 Synthetic Atlas Release-Readiness Evidence Matrix

This is the first bounded matrix for [issue #3396](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3396).
It indexes current repository evidence for one synthetic atlas candidate and
records every unresolved prerequisite requested by M36. It deliberately does
not assemble a release candidate, repeat M01-M35 evidence, or make a release
decision.

> [!IMPORTANT]
> **Overall classification: `PARTIAL`; readiness decision: `HOLD`.** The
> repository has useful fixture-only release prerequisites, but it does not
> contain the candidate-specific data, API, UI, operational, review, correction,
> rollback, or monitoring closure needed for a later release decision.

> [!CAUTION]
> `READY`, `PASS`, `APPROVED`, or `RELEASED` inside a synthetic fixture describes
> only that fixture's test case. It is not evidence of source admission, human
> approval, lifecycle promotion, release, deployment, or publication.

## Execution-start pin and overlap

| Observation | Current evidence | Classification | Limitation |
|---|---|---|---|
| Implementation baseline | `main@fbd08c2c9f361ea7b2e255923a27e4a549469d42` | `IMPLEMENTED` | Pins repository bytes only; it is not an approved release base. |
| Open pull requests | Zero at execution start | `IMPLEMENTED` | A zero-length queue does not prove branch, issue, or external-work closure. |
| M36 coordination | [#3396](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3396) open with `priority: p1`, `needs-review`, `evidence`, `governance`, and `status: proposed` | `PARTIAL` | The issue is coordination evidence, not implementation or approval. |
| Production-readiness child | [#4415](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4415) open | `PARTIAL` | Dry-run decision work remains non-production and non-authorizing. |
| Deployment-reliability child | [#4418](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4418) open | `PARTIAL` | Repository handoff work cannot deploy or restore the existing Site. |
| Readiness-boundary regression | [PR #4532](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4532) merged at `27202a0595ecdc6afd6f98b3aedaa236243e07b3` | `IMPLEMENTED` | Proves bounded output and non-authorization assertions only. |
| Exact issue-number branch probe | No branch containing `3396` was returned at execution start | `PARTIAL` | Name search is not a proof that no semantically overlapping branch exists. |

The latest merged change at the pin is PR #4589, the first M36 evidence-matrix
slice. This revision extends that same bounded fixture and matrix family.

## Selected synthetic atlas candidate

The matrix selects one documentation-only candidate label:
`atlas-candidate:synthetic-kansas-proof-v1`. It points to the existing fixture
subject `overlay:synthetic-kansas-promotion-proof`; it does not mint a schema
identity, release identity, catalog identity, or lifecycle record.

| Candidate element | Exact current anchor | Classification | What remains unproved |
|---|---|---|---|
| Evaluation input | [`valid/pass.json`](../../fixtures/release/promotion_verification_execution/valid/pass.json), SHA-256 `23d166d2...cf12` | `IMPLEMENTED` | Fixture validity does not establish a real atlas candidate. |
| Promotion packet | [`promotion_packet.json`](../../fixtures/release/promotion_verification_execution/artifacts/promotion_packet.json), SHA-256 `aa941c1d...7f9d` | `IMPLEMENTED` | Its policy, review, catalog, correction, and rollback fields are synthetic declarations. |
| Release-manifest-shaped fixture | [`release_manifest.json`](../../fixtures/release/promotion_verification_execution/artifacts/release_manifest.json), SHA-256 `5138edd2...3f39` | `IMPLEMENTED` | It is not an append-only release decision under `release/`. |
| Synthetic carrier | [`synthetic_atlas_carrier.geojson`](../../fixtures/release/promotion_verification_execution/artifacts/synthetic_atlas_carrier.geojson), SHA-256 `8ad39489...b26d` | `IMPLEMENTED` | Deterministic fixture-only generalized geometry; it is not observed, surveyed, source-admitted, or production data. |
| Catalog/provenance references | [STAC](../../fixtures/release/promotion_verification_execution/references/stac.json), [DCAT](../../fixtures/release/promotion_verification_execution/references/dcat.json), and [PROV](../../fixtures/release/promotion_verification_execution/references/prov.json) stubs | `PARTIAL` | Identity-binding stubs are not atlas catalog records, distributions, or served endpoints. |
| Evidence reference | [`evidence.json`](../../fixtures/release/promotion_verification_execution/references/evidence.json) | `PARTIAL` | A reference stub is not an EvidenceBundle, citation closure, or source authentication. |
| Rollback reference | [`rollback.json`](../../fixtures/release/promotion_verification_execution/references/rollback.json) | `PARTIAL` | No executable rollback, invalidation, restoration, operator, or readback is established. |
| Non-authorizing regression | [`test_synthetic_release_closure.py`](../../tests/release/test_synthetic_release_closure.py) and [`test_validate_operational_trust_rollup.py`](../../tests/validators/test_validate_operational_trust_rollup.py) | `IMPLEMENTED` | Test success cannot create authority or production parity. |

This revision closes the prior `ABSENT` byte-carrier gap: the execution plan now
requires the carrier binding, checks the actual bytes against the embedded and
standalone manifest, and fails closed when carrier, subject, geometry, time, or
fixture-governance metadata diverge.

## M01-M35 evidence reference ledger

Each row points to the milestone's own coordination and closure record. This
matrix uses those records as references and does not copy their evidence,
receipts, validation counts, or historical SHA claims.

At the execution snapshot, M11, M16, and M23 are closed; the other milestone
issues are open. All 35 retain `needs-review` and `status: proposed`. Every row
therefore remains `PARTIAL` for M36: issue state alone does not prove current-main
closure or authorize a release effect.

| Milestone evidence owner | M36 dependency indexed here | Matrix classification |
|---|---|---|
| [M01 #3365](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3365) | Authority, Directory Rules, and program baseline | `PARTIAL` |
| [M02 #3368](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3368) | Contracts, schemas, policy, and compatibility | `PARTIAL` |
| [M03 #3370](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3370) | Deterministic identity and temporal authority | `PARTIAL` |
| [M04 #3367](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3367) | Evidence resolution and governed response | `PARTIAL` |
| [M05 #3369](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3369) | Source admission, rights, and sensitive data | `PARTIAL` |
| [M06 #3366](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3366) | Validation, security, and supply-chain gates | `PARTIAL` |
| [M07 #3371](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3371) | Catalog, provenance, release, and rollback closure | `PARTIAL` |
| [M08 #3372](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3372) | Public-safe hydrology and ecology proof slices | `PARTIAL` |
| [M09 #3374](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3374) | Interoperable data and delivery artifacts | `PARTIAL` |
| [M10 #3375](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3375) | MapLibre, PMTiles, and Evidence Drawer | `PARTIAL` |
| [M11 #3373](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3373) | Governed API, Focus Mode, and AI | `PARTIAL` |
| [M12 #3378](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3378) | Cross-domain atlas and operational readiness | `PARTIAL` |
| [M13 #3379](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3379) | Repository control, review integrity, and conformance | `PARTIAL` |
| [M14 #3376](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3376) | Security classification and critical-asset exposure | `PARTIAL` |
| [M15 #3380](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3380) | Incident response, key lifecycle, and recovery | `PARTIAL` |
| [M16 #3377](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3377) | Quality baselines, non-vacuous tests, and CI reliability | `PARTIAL` |
| [M17 #3382](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3382) | Dependencies, containers, SBOM, and supply chain | `PARTIAL` |
| [M18 #3383](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3383) | Temporal compatibility and correction lineage | `PARTIAL` |
| [M19 #3381](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3381) | Evidence resolver, citation integrity, and consumer closure | `PARTIAL` |
| [M20 #3384](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3384) | Source rights, health, watchers, and change detection | `PARTIAL` |
| [M21 #3385](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3385) | Transportation, infrastructure, and public-safe geometry | `PARTIAL` |
| [M22 #3390](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3390) | Drought, water, soil, and agriculture observations | `PARTIAL` |
| [M23 #3387](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3387) | Runtime admission, accessibility, and performance | `PARTIAL` |
| [M24 #3386](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3386) | GeoParquet, PMTiles, and COG interoperability | `PARTIAL` |
| [M25 #3388](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3388) | Decision ledger, ownership, and portfolio closure | `PARTIAL` |
| [M26 #3389](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3389) | Trust membrane, sensitivity, and public path | `PARTIAL` |
| [M27 #3392](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3392) | Evidence authentication, citation, and consumer closure | `PARTIAL` |
| [M28 #3393](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3393) | Source-admission operations, rights, and freshness | `PARTIAL` |
| [M29 #3394](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3394) | Temporal replay, correction, and migration | `PARTIAL` |
| [M30 #3391](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3391) | Domain convergence and cross-lane joins | `PARTIAL` |
| [M31 #3395](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3395) | Catalog graph, provenance, and release-candidate closure | `PARTIAL` |
| [M32 #3400](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3400) | Governed API and serving readiness | `PARTIAL` |
| [M33 #3397](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3397) | Explorer Web, accessibility, and interaction continuity | `PARTIAL` |
| [M34 #3398](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3398) | Observability, incident, correction, and recovery | `PARTIAL` |
| [M35 #3399](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3399) | Reproducible builds, SBOM, attestation, and integrity | `PARTIAL` |

## Candidate readiness gap matrix

The required-evidence column names the smallest candidate-specific proof that a
later slice must reference. It does not prescribe or authorize implementation.

| Readiness dimension | Current candidate-specific evidence | Outcome | Explicit gap before a later decision | Milestone references |
|---|---|---|---|---|
| Data | A materialized GeoJSON fixture binds one generalized Kansas test extent to its manifest digest, RFC 7946 schema reference, synthetic rights/sensitivity labels, time scope, quality assertions, and fixture-only lifecycle. | `PARTIAL` | Replace self-asserted fixture metadata with independently reviewed schema, data-quality, rights, sensitivity, and source-admission evidence before any real candidate exists; do not enter `data/published/` from this slice. | M03, M05, M08, M09, M21, M22, M24, M28, M30 |
| APIs | No candidate ID occurs in `apps/` or a governed route surface. | `ABSENT` | Add a no-network contract fixture proving finite outcomes, bounded query limits, EvidenceBundle envelope, safe errors, cache semantics, and denial of RAW/WORK/QUARANTINE/candidate access. | M11, M19, M32 |
| UI | The selected subject occurs only in release-fixture families, not in Explorer code. | `ABSENT` | Prove renderer-neutral selection, map display, Evidence Drawer continuity, time/uncertainty cues, restricted-state denial, state restore, cleanup, and no upload or hidden model call. | M10, M12, M23, M33 |
| Evidence | One digest-bound `EVIDENCE_BUNDLE` reference stub is present. | `PARTIAL` | Resolve a real synthetic EvidenceBundle fixture with citations, claim bindings, provenance, limitations, stale/corrected/revoked behavior, and cite-or-abstain consumer proof. | M04, M07, M19, M27, M31 |
| Policy | Fixture context says `public-safe`/`PASS`, and a fixture-only Rego rule reads those declarations. | `PARTIAL` | Bind an accepted policy profile and deterministic evaluation receipt covering rights, license, source role, sensitivity, public precision, obligations, denial, and error without letting the candidate self-assert safety. | M02, M05, M14, M26, M28 |
| Accessibility | No candidate-specific browser or accessibility result is referenced. | `ABSENT` | Record keyboard, screen-reader naming/announcements, focus continuity, non-color state, zoom/reflow, reduced-motion, target-size, and Evidence Drawer reading-order results at an exact build. | M23, M33 |
| Quality | Focused fixture tests cover carrier-byte, manifest, subject, geometry, temporal, governance, reference, identity, and non-authorization binding. | `PARTIAL` | Add real-candidate data, render, API, UI, deterministic-replay, performance-budget, and long-session results; record all skipped and not-run checks explicitly. | M06, M09, M16, M23, M24, M35 |
| Security | Fixture denies network/lifecycle writes and carries an offline fake-Cosign plan. | `PARTIAL` | Prove dependency and secret scans, SBOM, provenance/attestation verification, CSP/worker boundaries, unsafe-path and information-disclosure negatives, critical-asset/sensitivity denial, and current advisory disposition. | M06, M13, M14, M15, M17, M26, M35 |
| Observability | No candidate-specific logs, metrics, traces, SLOs, alert routing, retention, or production readback exists. | `ABSENT` | Define safe telemetry fields, redaction, trace-to-evidence binding, availability/freshness/integrity SLOs, deterministic incident triggers, owner routing, retention, and a no-production rehearsal. | M20, M34 |
| Correction | The fixture exposes `supersedes_prior: false` and `notice_ref: null`. | `PARTIAL` | Add a corrected synthetic case that preserves prior bytes and identity, emits a correction reference, enumerates derivatives and consumers, invalidates stale views, and proves replay without publication. | M03, M18, M27, M29, M34 |
| Rollback | One rollback reference stub and target spec hash are present. | `PARTIAL` | Bind a valid RollbackCard fixture to materialized prior/current carrier bytes; rehearse target verification, alias/cache invalidation plan, restore plan, failure attribution, receipt, and readback without mutation. | M07, M15, M18, M29, M34 |
| Stewardship | Fixture identities and approval are synthetic; no independent candidate steward is authenticated. | `ABSENT` | Name and authenticate data, evidence, policy/sensitivity, accessibility, security, operations, release, and monitoring responsibilities; prove separation of author, reviewer, and operator and record an owner decision. | M01, M13, M25, M26 |
| Monitoring | No candidate-specific post-release plan or active watcher is referenced. | `ABSENT` | Define public-safe availability, freshness, source/right/terms drift, evidence revocation, security, accessibility, performance, correction, rollback, and user-impact checks with cadence, thresholds, owners, and stop/escalation rules. | M20, M25, M34 |

No row is `SUPERSEDED`, `CONFLICTED`, or `DEPRECATED` at this snapshot. Those
classifications remain available if later evidence establishes replacement,
incompatible authority, or an accepted retirement state. Anything outside the
inspection boundary is `NOT_INSPECTED`, not passed.

## Focused validation and hosted-check expectations

The candidate's no-network assertions and new carrier closure are replayed
without changing release behavior:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 \
  python -m pytest -q \
  tests/release/test_promotion_verification_execution.py \
  tests/release/test_synthetic_release_closure.py \
  tests/validators/test_validate_operational_trust_rollup.py
```

The documentation slice must also pass the existing changed-file metadata,
local-link, document-graph, and stale-scan validators. The matrix-specific audit
must confirm exactly one reference for every M01-M35 coordination issue, all 13
readiness dimensions, the exact base pin, `PARTIAL`/`ABSENT` classifications,
and the non-effects below.

Expected hosted checks for the Markdown change are `docs-meta-block`,
`link-check`, `docs-document-graph`, `docs-stale-scan`, and `docs-build` according
to their path filters. A held or skipped documentation build remains `SKIPPED`
or `NOT_RUN`; it must not be reported as pass. Release, browser, API, security,
accessibility, deployment, and production checks are not expected to run from
this documentation-only diff. If they do not run, they remain `NOT_RUN`.

Introduced failures are failures whose changed-path diagnostics bind this
matrix or its index edit. Unrelated existing failures are inherited and must be
reported separately; neither class may be waived or relabeled as pass.

## Correction, rollback, and forward fix

- If a referenced issue, path, digest, or state changes, create a new reviewed
  matrix revision pinned to a new base. Do not rewrite historical milestone
  evidence or backdate the snapshot.
- If a referenced record is corrected or superseded, preserve the old link and
  add the correction/supersession relationship before changing a classification.
- Before merge, close the draft and delete its branch to roll back. After an
  authorized merge, revert the single documentation commit through normal
  review. No data, release, alias, cache, Site, deployment, or publication
  rollback is involved.
- Prefer a forward fix for an incorrect current-state claim or broken link when
  preserving the review history is more valuable than reverting the whole matrix.

## Review and completion boundary

This slice is complete only when the matrix and atlas-lane index are reviewed at
one exact head, the focused fixture tests and changed-document checks are
reported with explicit pass/fail/skipped/not-run states, introduced and inherited
failures are separated, and independent review remains explicit.

Closing this documentation slice would not close M36. M36 remains open until its
inventory and overlap map, dependency/path/validation/rollback contract, and
every unresolved readiness item satisfy the issue's own completion boundary.

## Non-effects

This matrix does not accept an ADR or policy; authenticate a reviewer; admit or
activate a source; fetch live payloads; materialize, catalog, sign, release, or
publish an atlas; expose an API route; change the Explorer; promote lifecycle
data; mutate a release record, alias, cache, Site, deployment, ruleset, branch
protection, or repository setting; activate monitoring; or authorize release,
deployment, promotion, or publication. A milestone, issue, pull request, merge,
fixture, receipt, proof, matrix, or passing check cannot authorize those effects.

[Back to top](#top)
