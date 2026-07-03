# Runtime and synthetic fixtures

`fixtures/`

Status: draft / fixture root index / runtime, synthetic, public-safe, positive, negative, expected-output, and release-governance examples.

This directory contains runtime and synthetic fixture corpora used by renderer smoke tests, performance-governance checks, governed API dry-runs, Evidence Drawer examples, Focus Mode examples, documentation examples, release-governance dry-runs, correction checks, rollback checks, and expected-output comparisons.

These files are examples only. They are not source records, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, policy decisions, review approvals, release manifests, public API material, public map material, public tiles, canonical truth, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, or published artifacts.

## Fixture root posture

`fixtures/` is for operational rendering inputs, runtime smoke examples, benchmark-style fixture corpora, synthetic governed-object examples, fail-closed examples, positive-path examples, and deterministic expected outputs.

Fixtures are not validators, contracts, schemas, policies, releases, proofs, receipts, source descriptors, lifecycle data, public surfaces, or truth authority. A fixture may demonstrate intended behavior before validators, routes, renderer checks, policy bundles, schemas, release gates, or CI coverage exist. Fixture success or failure is not implementation proof by itself.

Use the smallest useful fixture lane that preserves ownership, sensitivity, reviewability, and reversibility. Prefer a domain-specific lane under `fixtures/domains/` when the object family or policy context is clear.

## Placement basis

This root belongs under `fixtures/` because it contains runtime/checking inputs and synthetic examples. It is separate from:

| Path | Purpose |
|---|---|
| `fixtures/` | Runtime benchmark inputs, synthetic examples, positive/fail-closed examples, and expected-output examples. |
| `tests/fixtures/` | Deterministic test-only fixtures that are not runtime/benchmark corpora. |
| `artifacts/` | Generated CI/build outputs. Do not treat generated artifacts as fixture authority. |
| `data/` | Governed lifecycle lanes. Real data belongs there, not here. |

Root rules remain:

- Do not place RAW, WORK, or QUARANTINE data here.
- Do not place sensitive exact geometry here.
- Do not treat fixture corpora as canonical truth.
- Prefer small, public-safe, reproducible datasets.
- Use external storage or Git LFS for large corpora only by explicit repo decision.
- Every stable corpus should eventually have a source note, rights note, and generation receipt or generation note.

## Current top-level lane inventory

The following lanes have populated README coverage or are governed by this root. This table is a navigation index, not proof that payload files, validators, tests, governed API routes, renderer checks, UI checks, policy bundles, release manifests, proof stores, source-registry records, or CI coverage exist.

| Lane | Purpose | Expected posture |
|---|---|---|
| `slim/` | Small runtime fixture lane for renderer smoke inputs, governed API dry-runs, map runtime examples, Evidence Drawer examples, Focus Mode examples, documentation examples, and lightweight performance checks. | Synthetic, compact, public-safe, renderer-safe, drawer-safe, Focus-safe, or bounded output. |
| `heavy/` | Heavy runtime stress lane for larger public-safe runtime corpora when `slim/` is not enough. | Synthetic stress input; explicit storage decision needed for large corpora. |
| `valid/` | Top-level positive-path fixture index for broad valid examples not yet routed to a domain-specific owner. | Validation pass, review-ready, renderer-safe, evidence-resolved, citation-ready, release-ready, correction-visible, rollback-ready, or expected output. |
| `invalid/` | Top-level fail-closed fixture index for broad invalid examples not yet routed to a domain-specific owner. | `ABSTAIN`, `DENY`, `ERROR`, validation failure, policy failure, review-required, blocked render, release-readiness failure, or expected failure output. |
| `golden/` | Top-level expected-output fixture index for stable synthetic outputs paired with sibling input fixtures. | Deterministic expected output, not release or proof. |
| `public_safe/` | Parent lane for public-safe documentation/runtime examples. | Public-safe, generalized, bounded, or finite governed output. |
| `public_safe/settlement/` | Public-safe synthetic settlement-side examples. | Generalized settlement examples only; not municipal, census, historic-site, land, infrastructure, or release authority. |
| `synthetic/` | Parent lane for synthetic compatibility examples before ownership is clear. | Synthetic, public-safe, not authoritative, and routed to domain lanes when stable. |
| `synthetic/people-dna-land/` | Synthetic People/DNA/Land compatibility lane before stable examples move to `fixtures/domains/people-dna-land/`. | Deny-first, toy-only, public-safe, fail-closed where needed. |
| `release/` | Parent lane for synthetic release-governance examples. | Synthetic release-governance dry-runs only; not release state. |
| `release/promotion_decision/` | Synthetic PromotionDecision fixture family. | `APPROVE`, `DENY`, `ABSTAIN`, valid, invalid, expected output, or bounded summary posture. |
| `release/promotion_decision/valid/` | Positive-path synthetic PromotionDecision examples. | Validation pass, policy pass, release-readiness pass, or bounded expected output. |
| `release/promotion_decision/invalid/` | Fail-closed synthetic PromotionDecision examples. | Validation failure, policy failure, review-required, `DENY`, `ABSTAIN`, or expected failure output. |
| `infrastructure-generalized/` | Top-level generalized-infrastructure runtime fixture lane. | Public-safe, generalized, synthetic infrastructure context only. |
| `hydrology/` | Top-level Hydrology runtime fixture lane. | Synthetic runtime/staging examples that defer domain-owned Hydrology cases to `fixtures/domains/hydrology/`. |
| `ecology/` | Cross-domain ecology fixture root. | Public-safe synthetic ecology examples; domain lanes preferred when ownership is clear. |
| `fauna/` | Fauna compatibility/staging fixture root. | Public-safe synthetic Fauna examples; domain-owned Fauna lanes preferred when ownership is clear. |
| `generated_receipt/` | Generated-receipt fixture root. | Receipt-shape and receipt-validation examples only; not actual receipt storage. |
| `domains/` | Domain-owned fixture roots. | Preferred home when object-family ownership, policy context, or sensitivity context is clear. |

## Relationship to authority roots

| Responsibility | Correct home | Fixture boundary |
|---|---|---|
| Semantic meaning | `contracts/` | Fixtures may imitate shapes but do not define meaning. |
| Machine shape | `schemas/` | Fixtures may exercise schemas but do not define schemas. |
| Policy/admissibility | `policy/` | Fixtures may exercise policy checks but do not decide policy. |
| Lifecycle data | `data/` | Fixtures are not RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data. |
| Source registry | `data/registry/sources/` | Fixtures are not SourceDescriptors or source authority. |
| Proofs and receipts | Accepted proof/receipt roots | Fixtures are not actual proofs or receipts. |
| Release decisions and artifacts | `release/` and release contracts/policies | Fixtures do not publish, promote, withdraw, correct, or roll back real releases. |
| Public clients | Governed API/UI/map roots | Fixtures are not public API, public map, public tile, or public AI surfaces. |
| Generated build output | `artifacts/` | Artifacts are not fixture authority. |
| Test-only fixtures | `tests/fixtures/` | Use for deterministic tests that are not runtime/benchmark corpora. |

## Use guidance

| Use case | Preferred lane |
|---|---|
| Small runtime smoke input | `slim/` |
| Heavy renderer or benchmark stress input | `heavy/`, with storage decision if large |
| Broad positive-path example | `valid/` until routed to a domain/object lane |
| Broad fail-closed example | `invalid/` until routed to a domain/object lane |
| Stable expected output | `golden/` or domain-specific `golden/` lane |
| Public-safe documentation/runtime example | `public_safe/` or a child lane |
| Synthetic compatibility example | `synthetic/` or a child lane |
| Release-governance dry-run | `release/` or a release child lane |
| Domain-owned object fixture | `domains/<domain>/...` |
| Real lifecycle data, proof, release, source, or publication material | Not fixtures; route to the governed responsibility root |

## Accepted material

This root and its child lanes may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.positive.json`, `*.invalid.json`, `*.negative.json`, `*.expected.json`, `*.golden.json`, `*.geojson`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- PMTiles, MLT, MapLibre, Cesium, vector-tile, GeoJSON, JSON, JSONL, SVG, YAML, and Markdown examples when synthetic or public-safe;
- toy governed-object shapes, runtime envelopes, drawer payloads, Focus Mode contexts, source-role states, evidence refs, policy refs, release refs, correction refs, rollback refs, and expected outputs;
- positive-path, fail-closed, and expected-output examples that remain synthetic, deterministic, public-safe, and reviewable;
- README files documenting fixture intent, boundaries, consumer checks, and verification state.

## Exclusions

Do not use this root for RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data; real source exports; live upstream payloads; sensitive exact geometry; credentials; lifecycle data; SourceDescriptors; actual EvidenceBundles; actual RunReceipts; proof packs; release manifests; generated CI artifacts; implementation code; public API material; public map material; public tiles; direct model runtime output; source authority; evidence authority; policy authority; proof authority; release authority; AI authority; or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Prefer `slim/` before `heavy/`.
- Prefer domain-specific fixture lanes when ownership is clear.
- Make fixture posture explicit: synthetic, public-safe, valid, invalid, positive, negative, golden, expected output, evidence-resolved, evidence-missing, source-role-preserved, source-role-conflicted, rights-visible, rights-unknown, sensitivity-reviewed, sensitivity-unresolved, release-ready, release-blocked, correction-visible, rollback-ready, or blocked render.
- Make expected outcome explicit when known: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, validation pass, validation failure, policy pass, policy failure, review-ready, review-required, renderer-safe, drawer-safe, Focus-safe, blocked render, correction-required, rollback-required, release-ready, release-readiness failure, or deterministic expected output.
- Keep schema validity, semantic validity, evidence resolution, citation validation, rights posture, sensitivity posture, source-role validity, policy filtering, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, UI behavior, correction posture, rollback posture, replay posture, and expected-output state separate.
- Pair stable inputs with expected outputs when practical.
- Do not treat fixture success or failure as truth, source admission, EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, tile authority, or published output.

## Maintenance notes

- Update this README when top-level lanes, child lanes, payload files, validators, tests, helper scripts, generation recipes, expected-output names, storage decisions, or consumer contracts are added.
- Link each stable fixture to the exact validator, renderer check, governed-API dry-run, Evidence Drawer check, Focus Mode check, source-role check, evidence-resolution check, citation-validation check, policy check, release-readiness check, correction check, rollback check, benchmark harness, or documentation example that consumes it.
- Move stable domain-owned examples into the owning `fixtures/domains/` lane once ownership is clear.
- If expected behavior stabilizes, update the paired input, expected output, consumer notes, child README, and this root README together.
- Keep payloads small enough for normal code review unless an explicit large-corpus storage decision exists.
- If a fixture accidentally includes real source material, lifecycle data, proof material, release material, generated CI output, sensitive exact geometry, private material, or restricted material, move it out of this root, quarantine it through the governed lifecycle or responsibility root, and record the correction path.

## Verification status

- Target README: replaced shorter runtime fixture note with expanded parent index.
- Top-level README inventory: PARTIALLY VERIFIED from recently populated child README files and targeted fetches; no exhaustive tree listing was performed during this update.
- Fixture payload inventory: no payload files verified under `fixtures/` during this update.
- Root fixture alignment: PARTIALLY VERIFIED against the previous `fixtures/README.md` boundary and Directory Rules responsibility-root doctrine.
- Child-lane alignment: PARTIALLY VERIFIED against recently populated `slim/`, `heavy/`, `valid/`, `invalid/`, `golden/`, `public_safe/`, `synthetic/`, `release/`, `infrastructure-generalized/`, `hydrology/`, and related child READMEs.
- Directory Rules alignment: PARTIALLY VERIFIED against `docs/doctrine/directory-rules.md`; `fixtures/` remains a responsibility root for runtime/checking examples and not a lifecycle, schema, policy, proof, release, or publication root.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, performance-governance checks, benchmark harnesses, governed-API tests, Evidence Drawer tests, Focus Mode tests, replay checks, source-role checks, evidence-resolution checks, citation-validation checks, rights checks, sensitivity checks, policy checks, release-readiness checks, correction checks, rollback checks, schema checks, storage decisions, and CI implementation.
- Tests and validators: NOT RUN.
