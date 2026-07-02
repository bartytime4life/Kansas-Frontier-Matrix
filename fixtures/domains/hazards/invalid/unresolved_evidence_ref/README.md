# Hazards invalid unresolved-evidence-ref fixtures

`fixtures/domains/hazards/invalid/unresolved_evidence_ref/`

Status: draft / invalid fixture lane / unresolved evidence reference examples.

This directory is for small synthetic negative-path Hazards fixtures where a claim, feature resolver output, drawer payload, Focus Mode response, layer descriptor, release candidate, or export payload references an `EvidenceRef` that cannot resolve to an `EvidenceBundle` or other required evidence-support object.

These examples are meant to verify that unresolved evidence fails closed with `ABSTAIN`, `DENY`, `ERROR`, review-required, or validation-failure outcomes rather than producing a valid Hazards claim, drawer, Focus response, layer, map state, export, or publication surface.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hazards truth, or published artifacts.

## Invalid-case posture

The governed API architecture states the cite-or-abstain rule: no consequential claim leaves the API without a resolvable `EvidenceRef` chain to an `EvidenceBundle`; otherwise the response is `ABSTAIN`. It also states that every public response is a finite `RuntimeResponseEnvelope` with outcome `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.

The same architecture says `ANSWER` requires resolved evidence, policy allowance, and applicable release state. `ABSTAIN` is returned when evidence is insufficient, unresolvable, stale without released alternative, or an AI surface cannot cite.

The Evidence Drawer payload contract treats the drawer as a governed projection. It may carry EvidenceBundle refs, citation lists, source summaries, policy state, release state, limitation text, and rollback/correction refs, but it renders what the governed API has resolved. It does not compute new evidence, upgrade `ABSTAIN` into `ANSWER`, or generate claims.

This fixture lane can support future validation and UI checks, but examples here do not prove validator implementation, API behavior, UI behavior, policy enforcement, release integration, schema enforcement, citation resolution, or EvidenceBundle storage by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic invalid examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says RAW, WORK, and QUARANTINE data do not belong in `fixtures/`, sensitive exact geometry does not belong here, and fixture corpora must not be treated as canonical truth. The parent Hazards fixture README is still a greenfield stub during this update.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../../feature_resolver/` | Resolver fixtures should return finite outcomes when evidence refs do not resolve. |
| `../../drawer/` | Drawer fixtures should render missing-evidence states, not claims. |
| `../../focus/` | Focus fixtures should abstain when citations or evidence cannot be validated. |
| `../../golden/` | Expected failure outputs may be paired there when stable. |
| `../ui_reads_raw_directly/` | Related trust-membrane case where a client bypasses governed evidence resolution. |
| `../focus_mode_as_alert/` | Related Focus negative case for blocked public-use requests. |
| `../modeled_labeled_observed/` | Related negative case for source-role collapse with evidence implications. |
| `../regulatory_labeled_observed/` | Related negative case for source-role collapse with evidence implications. |
| `../temporal_role_swap/` | Related negative case for identity/role/evidence inconsistency. |
| `../` | Parent invalid lane; not verified as populated during this update. |
| `../../../../docs/architecture/governed-api.md` | Cite-or-abstain and finite-outcome doctrine; this lane supplies examples only. |
| `../../../../contracts/evidence/evidence_drawer_payload.md` | Drawer projection semantics; this lane supplies examples only. |
| `../../../../data/proofs/hazards/` | Proof/EvidenceBundle home; fixtures do not populate proof storage. |
| `../../../../policy/domains/hazards/` | Policy home; fixtures do not decide policy. |
| `../../../../release/manifests/hazards/` | Release home; fixtures do not approve publication. |

## Related references

- `../../feature_resolver/README.md`
- `../../drawer/README.md`
- `../../focus/README.md`
- `../../golden/README.md`
- `../ui_reads_raw_directly/README.md`
- `../focus_mode_as_alert/README.md`
- `../modeled_labeled_observed/README.md`
- `../regulatory_labeled_observed/README.md`
- `../temporal_role_swap/README.md`
- `../expired_warning_as_current/README.md`
- `../drawer_missing_disclaimer/README.md`
- `../../../README.md`
- `../../../../docs/architecture/governed-api.md`
- `../../../../docs/architecture/hazards-trust-membrane.md`
- `../../../../docs/domains/hazards/API_CONTRACTS.md`
- `../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md`
- `../../../../contracts/evidence/evidence_drawer_payload.md`
- `../../../../contracts/domains/hazards/hazards_decision_envelope.md`
- `../../../../schemas/contracts/v1/evidence/`
- `../../../../schemas/contracts/v1/runtime/`
- `../../../../schemas/contracts/v1/focus/`
- `../../../../data/proofs/hazards/`
- `../../../../policy/domains/hazards/`
- `../../../../release/manifests/hazards/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy payloads with missing, malformed, stale, mismatched, inaccessible, redacted, denied, duplicate, or orphaned `EvidenceRef` values;
- toy drawer, feature-resolver, Focus Mode, map-layer, export, release-candidate, and golden-output examples that exercise evidence-resolution failure;
- toy `ABSTAIN`, `DENY`, `ERROR`, review-required, validation-failure, or blocked-render expected outputs;
- toy examples showing the contrast between a resolvable evidence chain and an unresolved evidence reference;
- paired expected outputs in `../../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy evidence refs, toy bundle refs, toy feature refs, toy layer refs, toy release refs, toy policy refs, toy citation refs, toy request refs, toy timestamps, toy digests, and toy hashes.
- Make the defect explicit: missing EvidenceRef, malformed EvidenceRef, EvidenceRef points nowhere, EvidenceRef points to wrong domain, EvidenceRef points to unreleased proof, EvidenceRef is redacted/denied, EvidenceRef conflicts with release state, or citation validation cannot resolve.
- Make expected outcome explicit: `ABSTAIN`, `DENY`, `ERROR`, review-required, validation failure, blocked render, or expected output.
- Pair each invalid input with an expected failure output when practical.
- Keep schema validity, semantic validity, evidence resolution, citation validation, policy filtering, release posture, trust-membrane safety, drawer display, Focus Mode wording, resolver context, and UI behavior separate.
- Do not treat fixture failure as EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected invalid examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Feature resolver returns a claim with an EvidenceRef that resolves nowhere | `ABSTAIN` or validation failure | No consequential claim without resolvable evidence. |
| Drawer payload includes evidence refs but none resolve to bundles | `ABSTAIN` or blocked render | Drawer should show missing-evidence posture, not a claim. |
| Focus Mode answer cites a missing EvidenceRef | `ABSTAIN` or validation failure | AI cannot fill the evidence gap. |
| Release candidate references unreleased or denied proof | `DENY` or review-required output | Release and policy state must agree with evidence state. |
| EvidenceRef points to the wrong domain or object family | `ERROR` or validation failure | Evidence identity must match the claim scope. |
| EvidenceRef is resolvable but citation validation fails | `ABSTAIN` or validation failure | Resolvability alone is not enough for an answer. |
| Valid contrast case with resolvable EvidenceRef and permitted release | Valid expected output | The safe path is evidence-resolved and finite-outcome. |

## Maintenance notes

- Update this README when invalid payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each invalid fixture to the evidence-resolution check, citation-validation check, governed-API check, feature-resolver check, drawer check, Focus Mode check, release-readiness check, policy-filter check, schema check, correction check, rollback check, or UI dry-run that consumes it.
- If expected invalid behavior changes, update the paired input, expected output, consumer notes, and verification status together.
- Keep payloads small enough for normal code review.

## Verification status

- Target README: replaced one-character placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Governed API cite-or-abstain alignment: PARTIALLY VERIFIED against `docs/architecture/governed-api.md`.
- Evidence Drawer projection alignment: PARTIALLY VERIFIED against `contracts/evidence/evidence_drawer_payload.md`.
- Hazards feature-resolver fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/feature_resolver/README.md`.
- Hazards drawer fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/drawer/README.md`.
- Hazards Focus fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/focus/README.md`.
- Hazards golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/golden/README.md`.
- Parent Hazards fixture README: present but still a greenfield stub during this update.
- Parent invalid lane alignment: NEEDS VERIFICATION.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, evidence-resolution checks, citation-validation checks, governed-API checks, feature-resolver checks, drawer checks, Focus Mode checks, UI tests, release-readiness checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.
