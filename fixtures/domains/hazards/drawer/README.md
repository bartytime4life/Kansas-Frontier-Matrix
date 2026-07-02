# Hazards drawer fixtures

`fixtures/domains/hazards/drawer/`

Status: draft / fixture lane / Evidence Drawer and trust-visible UI examples.

This directory is for small synthetic Hazards drawer fixture examples. These fixtures describe toy Evidence Drawer payloads, finite outcomes, source summaries, citation states, freshness states, policy states, release states, rollback/correction states, and not-for-life-safety UI postures for Hazards feature/detail interactions.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, policy decisions, review approvals, release state, public API material, public map material, public tiles, alert products, life-safety guidance, official-source authority, Hazards truth, or published artifacts.

## Drawer posture

The `EvidenceDrawerPayload` contract defines the drawer payload as a governed projection envelope. It is not EvidenceBundle closure, not a policy engine, not a release manifest, not proof storage, and not AI answer authority. The drawer renders policy-filtered state from governed API surfaces and must not read RAW, WORK, QUARANTINE, or internal proof stores directly.

Hazards UI doctrine states that Hazards layers and drawer surfaces are planning, historical, regulatory, and resilience context. They are never real-time warning authority and never life-safety instruction surfaces. Hazards drawer examples must therefore preserve the `not_for_life_safety` posture, finite outcomes, source-role state, freshness/expiry state, and official-source referral state where material.

This fixture lane can support future drawer checks, but fixture examples do not prove EvidenceBundle closure, policy enforcement, governed API route behavior, UI implementation, release integration, or accessibility coverage by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README states that `fixtures/` is for operational rendering inputs, not validator-only test data. It also states that RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Hazards fixture README is still a greenfield stub during this update, so this README keeps its own boundaries explicit.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../README.md` | Parent Hazards fixture lane; currently a greenfield stub during this update. |
| `../../golden/` | Future expected-output examples may be paired there if a Hazards golden lane is created. |
| `../../invalid/` | Future negative-path examples may be paired there if a Hazards invalid lane is created. |
| `../../../../contracts/evidence/evidence_drawer_payload.md` | Drawer payload semantics; this lane supplies examples only. |
| `../../../../contracts/domains/hazards/hazards_decision_envelope.md` | Hazards finite-outcome envelope semantics; this lane may test projected drawer states. |
| `../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md` | Hazards UI and drawer doctrine; this lane supplies examples only. |
| `../../../../docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md` | Life-safety boundary; drawer fixtures must preserve this boundary. |
| `../../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md` | Publication boundary; fixtures do not approve publication. |
| `../../../../schemas/contracts/v1/evidence/` and `../../../../schemas/contracts/v1/ui/` | Expected drawer schema homes; fixture success does not prove schema authority. |
| `../../../../schemas/contracts/v1/domains/hazards/` | Hazards domain schema home; current enforcement remains bounded by contract status. |
| `../../../../policy/domains/hazards/` | Policy home; fixtures do not decide policy. |
| `../../../../release/manifests/hazards/` | Release home; fixtures do not approve publication. |

## Related references

- `../README.md`
- `../../../README.md`
- `../../../../contracts/evidence/evidence_drawer_payload.md`
- `../../../../contracts/domains/hazards/hazards_decision_envelope.md`
- `../../../../contracts/domains/hazards/domain_layer_descriptor.md`
- `../../../../contracts/domains/hazards/domain_observation.md`
- `../../../../docs/architecture/evidence-drawer.md`
- `../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md`
- `../../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md`
- `../../../../docs/domains/hazards/API_CONTRACTS.md`
- `../../../../docs/domains/hazards/SOURCE_REGISTRY.md`
- `../../../../policy/domains/hazards/`
- `../../../../schemas/contracts/v1/evidence/`
- `../../../../schemas/contracts/v1/ui/`
- `../../../../schemas/contracts/v1/domains/hazards/`
- `../../../../data/proofs/hazards/`
- `../../../../data/registry/sources/hazards/`
- `../../../../release/manifests/hazards/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy `EvidenceDrawerPayload` examples for Hazards features, layers, popovers, exports, and Focus Mode handoffs;
- toy `HazardsDecisionEnvelope` projection examples using `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`;
- toy citation, source-summary, EvidenceRef, EvidenceBundle-ref, policy-state, sensitivity-state, review-state, release-state, stale-state, no-data, failed-verification, denied, redacted, correction, and rollback examples;
- toy not-for-life-safety labels, official-source referral states, freshness/expiry states, and source-role caveats;
- paired expected outputs in a future Hazards `golden/` lane when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, operational alert feeds, life-safety instructions, official-source authority, policy authority, release authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy IDs, toy feature refs, toy layer refs, toy evidence refs, toy citation refs, toy timestamps, toy digests, and toy hashes.
- Make drawer posture explicit: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, stale, no-data, failed-verification, denied, redacted, release-blocked, correction-visible, rollback-visible, or not-for-life-safety.
- Keep source role, evidence state, citation state, policy state, sensitivity state, review state, release state, freshness state, correction state, rollback state, accessibility state, and expected outcome explicit where material.
- Pair each input with an expected output when practical.
- Keep schema validity, semantic validity, evidence support, policy filtering, release posture, freshness posture, source-role validity, accessibility state, and trust-membrane safety separate.
- Do not treat fixture success as EvidenceBundle closure, source authority, policy approval, release state, UI implementation proof, public-map authority, alert authority, or published output.

## Expected drawer fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Synthetic released historical hazard feature with evidence refs and citation summary | `ANSWER` drawer output | Planning context only; not alerting. |
| Synthetic feature missing EvidenceBundle support | `ABSTAIN` drawer output | Cite-or-abstain remains visible. |
| Synthetic current-action request or KFM-as-alert-authority request | `DENY` drawer output | Official-source referral remains visible. |
| Synthetic warning context past expiry shown as current | `DENY` or validation failure | Expired operational context cannot appear as current warning state. |
| Unknown source role | `ABSTAIN`, `DENY`, or hold output | Source-role collapse is not allowed. |
| Drawer payload requests RAW/WORK/QUARANTINE material | `DENY` or validation failure | Drawer uses governed API projection only. |
| Missing rollback/correction posture for public-facing payload | Review-required output | Public trust state must be inspectable. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, drawer contracts, or consumer contracts are added.
- Link each fixture to the Evidence Drawer contract review, Hazards decision-envelope check, schema check, citation check, policy-filter check, source-role check, freshness check, official-source-referral check, accessibility check, governed-API test, Focus Mode test, release-readiness check, correction check, rollback check, or UI dry-run that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material or operational alert content, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: replaced one-character placeholder content.
- Parent Hazards fixture README: present but still a greenfield stub during this update.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Evidence Drawer contract alignment: PARTIALLY VERIFIED against `contracts/evidence/evidence_drawer_payload.md`.
- Hazards decision-envelope alignment: PARTIALLY VERIFIED against `contracts/domains/hazards/hazards_decision_envelope.md`.
- Hazards UI alignment: PARTIALLY VERIFIED against `docs/domains/hazards/MAP_UI_CONTRACTS.md`.
- Life-safety boundary alignment: PARTIALLY VERIFIED against `docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md` and `docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, drawer checks, governed-API tests, Focus Mode tests, release-readiness checks, schema checks, policy checks, accessibility checks, and UI implementation.
- Tests and validators: NOT RUN.
