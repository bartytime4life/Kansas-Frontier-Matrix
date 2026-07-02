# Hazards invalid UI-reads-raw-directly fixtures

`fixtures/domains/hazards/invalid/ui_reads_raw_directly/`

Status: draft / invalid fixture lane / trust-membrane violation examples.

This directory is for small synthetic negative-path Hazards fixtures where a UI, drawer, Focus Mode surface, map layer, export surface, or client-side helper attempts to read RAW, WORK, QUARANTINE, PROCESSED, unpublished catalog/triplet, proof-store, object-store, graph-store, vector-index, model-runtime, or other internal material directly instead of consuming governed API envelopes.

These examples are meant to verify that direct internal reads fail closed with `DENY`, `ABSTAIN`, `ERROR`, review-required, or validation-failure outcomes rather than producing a valid Hazards public surface.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hazards truth, or published artifacts.

## Invalid-case posture

The governed API architecture defines the API as the single public trust path for KFM. Public clients, including the map shell, Evidence Drawer, Focus Mode, story player, review console, and export surfaces, use that API and only that API. They never read RAW, WORK, QUARANTINE, canonical stores, graph stores, object stores, vector indexes, model runtimes, or unpublished candidates directly.

The same architecture states that public responses derive only from released/published material with supporting proof, policy, release, evidence, and rollback references. RAW, WORK, QUARANTINE, PROCESSED, and unpublished catalog/triplet material are not public response sources.

The Hazards trust-membrane note makes this stricter for Hazards because the lane is life-safety adjacent and fail-closed. This lane tests the failure mode where a UI surface bypasses the governed API and reaches into internal lifecycle or proof material directly.

This fixture lane can support future validation and UI checks, but examples here do not prove validator implementation, API behavior, UI behavior, policy enforcement, release integration, schema enforcement, or filesystem access controls by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic invalid examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says RAW, WORK, and QUARANTINE data do not belong in `fixtures/`, sensitive exact geometry does not belong here, and fixture corpora must not be treated as canonical truth. The parent Hazards fixture README is still a greenfield stub during this update.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../../feature_resolver/` | Resolver fixtures should model governed API envelopes, not direct internal reads. |
| `../../drawer/` | Drawer fixtures should consume governed drawer payloads, not internal lifecycle material. |
| `../../focus/` | Focus fixtures should use bounded context and evidence refs, not direct model/runtime/store access. |
| `../../golden/` | Expected failure outputs may be paired there when stable. |
| `../focus_mode_as_alert/` | Related negative case for public-use boundary collapse. |
| `../expired_warning_as_current/` | Related negative case for freshness/state collapse. |
| `../modeled_labeled_observed/` | Related negative case for source-role collapse. |
| `../regulatory_labeled_observed/` | Related negative case for source-role collapse. |
| `../` | Parent invalid lane; not verified as populated during this update. |
| `../../../../docs/architecture/governed-api.md` | Governed API and trust-membrane doctrine; this lane supplies examples only. |
| `../../../../docs/architecture/hazards-trust-membrane.md` | Hazards-specific trust-membrane doctrine; this lane supplies examples only. |
| `../../../../docs/domains/hazards/API_CONTRACTS.md` | Hazards governed API surfaces; this lane supplies examples only. |
| `../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md` | Hazards map/UI surfaces; this lane supplies examples only. |
| `../../../../policy/domains/hazards/` | Policy home; fixtures do not decide policy. |
| `../../../../release/manifests/hazards/` | Release home; fixtures do not approve publication. |

## Related references

- `../../feature_resolver/README.md`
- `../../drawer/README.md`
- `../../focus/README.md`
- `../../golden/README.md`
- `../focus_mode_as_alert/README.md`
- `../expired_warning_as_current/README.md`
- `../modeled_labeled_observed/README.md`
- `../regulatory_labeled_observed/README.md`
- `../temporal_role_swap/README.md`
- `../../../README.md`
- `../../../../docs/architecture/governed-api.md`
- `../../../../docs/architecture/hazards-trust-membrane.md`
- `../../../../docs/architecture/trust-membrane.md`
- `../../../../docs/domains/hazards/API_CONTRACTS.md`
- `../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md`
- `../../../../contracts/evidence/evidence_drawer_payload.md`
- `../../../../contracts/domains/hazards/hazards_decision_envelope.md`
- `../../../../schemas/contracts/v1/domains/hazards/`
- `../../../../schemas/contracts/v1/evidence/`
- `../../../../schemas/contracts/v1/focus/`
- `../../../../policy/domains/hazards/`
- `../../../../release/manifests/hazards/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy client requests that try to read lifecycle paths or internal stores directly;
- toy drawer, feature-resolver, Focus Mode, map-layer, export, and golden-output examples that exercise trust-membrane violations;
- toy `DENY`, `ABSTAIN`, `ERROR`, review-required, validation-failure, or blocked-render expected outputs;
- toy examples showing the difference between a valid governed API envelope and an invalid direct-read request;
- paired expected outputs in `../../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy paths, toy object refs, toy evidence refs, toy release refs, toy policy refs, toy request refs, toy timestamps, toy digests, and toy hashes.
- Make the defect explicit: direct RAW read, direct WORK read, direct QUARANTINE read, unpublished catalog read, proof-store bypass, direct object-store read, direct vector-index read, direct model-runtime read, or browser-side direct store access.
- Make expected outcome explicit: `DENY`, `ABSTAIN`, `ERROR`, review-required, validation failure, blocked render, or expected output.
- Pair each invalid input with an expected failure output when practical.
- Keep schema validity, semantic validity, evidence support, policy filtering, release posture, access posture, trust-membrane safety, drawer display, Focus Mode wording, resolver context, and UI behavior separate.
- Do not treat fixture failure as EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected invalid examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Browser map layer reads `data/raw/hazards/...` directly | `DENY` or validation failure | Public clients must use governed API envelopes. |
| Evidence Drawer reads a proof store directly | `DENY` or validation failure | Drawer receives governed projection, not proof-store internals. |
| Focus Mode calls a model/runtime directly from browser context | `DENY` or validation failure | AI surfaces go through the governed API and receipts. |
| UI reads WORK or QUARANTINE candidate as public data | `DENY` or validation failure | Candidate/internal material cannot become public by direct read. |
| Export surface reads unpublished catalog/triplet material | `DENY` or validation failure | Export follows release and policy state. |
| Client receives a valid governed envelope instead | Valid contrast output | The safe path is API-mediated and finite-outcome. |

## Maintenance notes

- Update this README when invalid payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each invalid fixture to the trust-membrane check, governed-API check, access-path check, lifecycle-boundary check, drawer check, Focus Mode check, feature-resolver check, schema check, policy-filter check, release-readiness check, correction check, rollback check, or UI dry-run that consumes it.
- If expected invalid behavior changes, update the paired input, expected output, consumer notes, and verification status together.
- Keep payloads small enough for normal code review.

## Verification status

- Target README: replaced one-character placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Governed API alignment: PARTIALLY VERIFIED against `docs/architecture/governed-api.md`.
- Hazards trust-membrane alignment: PARTIALLY VERIFIED against `docs/architecture/hazards-trust-membrane.md`.
- Hazards feature-resolver fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/feature_resolver/README.md`.
- Hazards drawer fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/drawer/README.md`.
- Hazards Focus fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/focus/README.md`.
- Hazards golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/golden/README.md`.
- Parent Hazards fixture README: present but still a greenfield stub during this update.
- Parent invalid lane alignment: NEEDS VERIFICATION.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, trust-membrane checks, governed-API checks, access-path checks, lifecycle-boundary checks, drawer checks, Focus Mode checks, feature-resolver checks, UI tests, release-readiness checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.
