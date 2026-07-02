# Hazards invalid fixtures

`fixtures/domains/hazards/invalid/`

Status: draft / invalid fixture index / negative-path Hazards examples.

This directory is the parent lane for small synthetic negative-path Hazards fixtures. Invalid fixtures are designed to exercise fail-closed behavior for Hazards claim resolution, drawer projection, Focus Mode, source-role preservation, evidence resolution, trust-membrane access, freshness state, policy state, release posture, correction posture, rollback posture, and public-safe UI behavior.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hazards truth, AI authority, or published artifacts.

## Invalid fixture posture

Use this lane for synthetic inputs that should not produce a normal public `ANSWER`. Expected outcomes may include `ABSTAIN`, `DENY`, `ERROR`, review-required, validation-failure, blocked-render, stale-state, missing-evidence, or other finite fail-closed states.

Invalid fixtures should make the defect explicit. They should also keep the expected failure separate from implementation proof: a fixture can describe the desired negative case before validators, UI checks, route behavior, schema enforcement, release integration, or CI coverage exist.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic invalid examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says RAW, WORK, and QUARANTINE data do not belong in `fixtures/`, sensitive exact geometry does not belong here, and fixture corpora must not be treated as canonical truth. The parent Hazards fixture README is still a greenfield stub during this update.

## Current child lane inventory

The following child lanes have populated README coverage. This table is a navigation index, not proof that payload files, validators, tests, governed API routes, UI checks, policy bundles, release manifests, or CI coverage exist.

| Child lane | Invalid case | Expected posture |
|---|---|---|
| `drawer_missing_disclaimer/` | Drawer-like payload missing required public-facing label/disclaimer state. | `DENY`, `ERROR`, review-required, or validation failure. |
| `expired_warning_as_current/` | Expired `WarningContext` or `AdvisoryContext` presented as current. | `DENY`, `ABSTAIN`, `ERROR`, review-required, or validation failure. |
| `focus_mode_as_alert/` | Focus Mode request used as current-action or alert-like authority. | `DENY`, `ABSTAIN`, `ERROR`, review-required, or validation failure. |
| `modeled_labeled_observed/` | Modeled, derived, aggregate-like, or reconstructed context labeled as observed evidence. | `DENY`, `ABSTAIN`, `ERROR`, review-required, or validation failure. |
| `regulatory_labeled_observed/` | Regulatory or designation-style context labeled as observed event evidence. | `DENY`, `ABSTAIN`, `ERROR`, review-required, or validation failure. |
| `temporal_role_swap/` | Source role changes incorrectly across event, issue, retrieval, review, correction, or release time. | `DENY`, `ABSTAIN`, `ERROR`, review-required, or validation failure. |
| `ui_reads_raw_directly/` | UI, drawer, Focus, map, export, or helper reads lifecycle/internal material directly. | `DENY`, `ABSTAIN`, `ERROR`, review-required, or validation failure. |
| `unresolved_evidence_ref/` | Claim, drawer, Focus response, layer, release candidate, or export references unresolved evidence. | `ABSTAIN`, `DENY`, `ERROR`, review-required, or validation failure. |

## Relationship to sibling fixture lanes

| Sibling lane | Relationship |
|---|---|
| `../feature_resolver/` | Positive or bounded resolver examples; invalid fixtures define resolver failure paths. |
| `../drawer/` | Positive or bounded drawer examples; invalid fixtures define blocked drawer states. |
| `../focus/` | Positive or bounded Focus Mode examples; invalid fixtures define blocked Focus states. |
| `../identity/` | Identity examples; invalid fixtures define source-role, temporal-scope, and evidence-consistency failures. |
| `../golden/` | Expected failure outputs should be paired there when stable. |
| `../README.md` | Parent Hazards fixture lane; still a greenfield stub during this update. |

## Related references

- `drawer_missing_disclaimer/README.md`
- `expired_warning_as_current/README.md`
- `focus_mode_as_alert/README.md`
- `modeled_labeled_observed/README.md`
- `regulatory_labeled_observed/README.md`
- `temporal_role_swap/README.md`
- `ui_reads_raw_directly/README.md`
- `unresolved_evidence_ref/README.md`
- `../feature_resolver/README.md`
- `../drawer/README.md`
- `../focus/README.md`
- `../identity/README.md`
- `../golden/README.md`
- `../../README.md`
- `../../../../docs/architecture/governed-api.md`
- `../../../../docs/architecture/hazards-trust-membrane.md`
- `../../../../docs/domains/hazards/API_CONTRACTS.md`
- `../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md`
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

This lane and its children may contain:

- small synthetic `*.input.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy resolver, drawer, Focus Mode, identity, evidence, policy, release, correction, rollback, source-role, freshness, and trust-membrane negative-path examples;
- toy `ABSTAIN`, `DENY`, `ERROR`, review-required, validation-failure, blocked-render, stale-state, missing-evidence, or expected-output examples;
- contrast examples showing the difference between an invalid input and a valid governed envelope;
- paired expected outputs in `../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Make the defect explicit in the file name, payload, expected output, and consumer notes.
- Make expected outcome explicit: `ABSTAIN`, `DENY`, `ERROR`, review-required, validation failure, blocked render, stale-state, missing-evidence, or expected output.
- Pair each invalid input with an expected failure output when practical.
- Keep schema validity, semantic validity, evidence resolution, citation validation, policy filtering, source-role validity, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, resolver context, UI behavior, correction posture, and rollback posture separate.
- Do not treat fixture failure as EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Maintenance notes

- Update this README when new invalid child lanes, invalid payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each invalid fixture to the exact check and consumer that uses it.
- If expected invalid behavior changes, update the paired input, expected output, consumer notes, child README, and this index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: replaced one-character placeholder content.
- Child README inventory: PARTIALLY VERIFIED against populated invalid child READMEs fetched during this update.
- Fixture payload inventory: no payload files verified under this parent during this update.
- Hazards drawer invalid alignment: PARTIALLY VERIFIED against `drawer_missing_disclaimer/README.md`.
- Hazards freshness invalid alignment: PARTIALLY VERIFIED against `expired_warning_as_current/README.md`.
- Hazards Focus invalid alignment: PARTIALLY VERIFIED against `focus_mode_as_alert/README.md`.
- Hazards source-role invalid alignment: PARTIALLY VERIFIED against `modeled_labeled_observed/README.md` and `regulatory_labeled_observed/README.md`.
- Hazards temporal-role invalid alignment: PARTIALLY VERIFIED against `temporal_role_swap/README.md`.
- Hazards trust-membrane invalid alignment: PARTIALLY VERIFIED against `ui_reads_raw_directly/README.md`.
- Hazards evidence-resolution invalid alignment: PARTIALLY VERIFIED against `unresolved_evidence_ref/README.md`.
- Parent Hazards fixture README: present but still a greenfield stub during this update.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, invalid-fixture checks, governed-API tests, feature-resolver checks, drawer checks, Focus Mode checks, identity checks, evidence-resolution checks, citation-validation checks, source-role checks, freshness checks, UI tests, release-readiness checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.
