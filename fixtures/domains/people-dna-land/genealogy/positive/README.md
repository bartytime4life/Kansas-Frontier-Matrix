# People/DNA/Land genealogy positive fixtures

`fixtures/domains/people-dna-land/genealogy/positive/`

Status: draft / positive fixture lane / genealogy public-safe examples.

This directory is for small synthetic positive-path genealogy fixtures in the People / Genealogy / DNA / Land domain. Use it for toy cases that can demonstrate bounded, evidence-backed, public-safe historical genealogy behavior without exposing real people, raw genealogy source material, DNA-derived inference, private land links, or unreviewed identity claims.

These files are examples only. They are not source records, lifecycle data, GEDCOM files, family trees, vital records, DNA data, land records, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, policy decisions, consent records, review approvals, release state, public API material, public map material, public tiles, genealogy truth, source authority, policy authority, release authority, AI authority, or published artifacts.

## Positive fixture posture

Genealogy doctrine treats kinship and life-event material as assertion-first, evidence-bound, and privacy-aware. A positive fixture may show a toy historical relationship, life event, family group, or source-citation flow only when the example remains synthetic, evidence-referenced, rights-visible, sensitivity-visible, release-aware, correction-aware, rollback-aware, and public-safe.

People / DNA / Land remains a deny-first domain even in positive fixtures. A positive example is not permission to publish living-person fields, DNA-derived relationship inference, raw kit/vendor identifiers, private person-to-parcel joins, raw GEDCOM identifiers, or unreviewed model-generated lineage text. Those cases belong in `../negative/` or another fail-closed lane.

This lane can support future validation and governed-API checks, but examples here do not prove validator implementation, route behavior, policy enforcement, schema enforcement, consent enforcement, EvidenceBundle storage, release integration, UI rendering, or CI coverage by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Relationship to People/DNA/Land governance

| Lane or document | Relationship |
|---|---|
| `../negative/README.md` | Sibling fail-closed lane for blocked genealogy cases and contrast examples. |
| `../../../../docs/domains/people-dna-land/sublanes/genealogy.md` | Genealogy doctrine and boundary; this fixture lane supplies examples only. |
| `../../../../docs/domains/people-dna-land/API_CONTRACTS.md` | Governed surface and finite outcome posture; fixtures do not define API behavior. |
| `../../../../docs/domains/people-dna-land/IDENTITY_MODEL.md` | Identity model and publication constraints; fixtures do not create canonical identities. |
| `../../../../docs/domains/people-dna-land/LAND_OWNERSHIP.md` | Land ownership doctrine; fixtures do not create title or parcel truth. |
| `../../../../contracts/domains/people-dna-land/` | Contract home for domain object meaning; fixtures do not define contracts. |
| `../../../../schemas/contracts/v1/domains/people-dna-land/` | Schema home if present; fixtures do not define schemas. |
| `../../../../policy/domains/people-dna-land/` | Policy home; fixtures do not decide access or release. |
| `../../../../data/registry/sources/people-dna-land/` | Source registry home if present; fixtures do not create source authority. |
| `../../../../data/proofs/people-dna-land/` | Proof home if present; fixtures do not create proof authority. |
| `../../../../release/candidates/people-dna-land/` and `../../../../release/manifests/people-dna-land/` | Release homes if present; fixtures do not publish. |

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.positive.json`, `*.valid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy historical relationship, life-event, family-group, source-citation, identity-resolution, evidence-ref, policy-ref, release-ref, correction, rollback, drawer, Focus Mode, or decision-envelope examples;
- toy cases for evidence-backed historical relationship assertions, cited birth/death/marriage-like events, synthetic source-citation chains, source-role-preserved tree overlays, public-safe ancestor summaries, bounded map overlay pointers, correction-visible claim display, and rollback-ready fixture outputs;
- toy expected outputs such as `ANSWER`, validation pass, review-ready, evidence-resolved, citation-ready, rights-visible, sensitivity-visible, source-role-preserved, correction-visible, rollback-visible, or release-ready;
- contrast examples that show why a public-safe historical claim can pass while a living-person, DNA-derived, or private land-link case must fail closed.

## Exclusions

Do not use this lane for real GEDCOM files, real family trees, real vital records, real living-person records, real DNA data, real kit/vendor identifiers, real person-to-parcel joins, real land records, real source exports, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, consent records, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy names, toy IDs, toy dates, toy places, toy relationship refs, toy source refs, toy evidence refs, toy consent refs if needed, toy policy refs, toy release refs, toy rollback refs, toy hashes, and toy timestamps.
- Prefer generic placeholders such as `PersonA`, `PersonB`, `AncestorExample`, `SyntheticFamily1`, and `ToyPlaceRef`; do not use real people, real family trees, real parcel identifiers, real coordinates, or real DNA identifiers.
- Make the positive condition explicit: evidence-backed historical claim, source-role-preserved assertion, rights-visible source citation, sensitivity-reviewed output, release-ready envelope, correction-visible display, rollback-ready output, or public-safe bounded summary.
- Make expected outcome explicit: `ANSWER`, validation pass, review-ready, evidence-resolved, citation-ready, source-role-preserved, release-ready, correction-visible, rollback-visible, or expected output.
- Pair each stable positive input with an expected output when practical.
- Keep schema validity, semantic validity, identity resolution, evidence resolution, citation validation, consent posture where relevant, rights posture, sensitivity posture, source-role validity, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, correction posture, rollback posture, and expected-output state separate.
- Do not treat fixture success as identity truth, relationship truth, title truth, consent proof, EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected positive fixture families

| Scenario family | Expected posture | Notes |
|---|---|---|
| Evidence-backed toy historical parent-child assertion | Validation pass or review-ready | Relationship remains an assertion with evidence refs. |
| Cited toy life event for a historical person | Validation pass or citation-ready | Source role, time, and citation remain visible. |
| Public-safe ancestor summary | `ANSWER` or review-ready | Summary must be bounded and evidence-referenced. |
| Source-role-preserved tree overlay hypothesis | Review-ready or validation pass | Hypothesis remains modeled/candidate until reviewed. |
| Synthetic family group with no living-person fields | Validation pass | Uses toy identities only. |
| Public-safe overlay pointer | `ANSWER` or release-ready | Pointer does not expose raw source IDs. |
| Correction-visible genealogy claim | Review-ready | Correction path remains attached. |
| Rollback-ready genealogy fixture output | Review-ready | Rollback target remains attached. |
| Positive case contrasted with sibling negative fixture | Expected output pair | Pair should show why one passes and the other fails closed. |

## Maintenance notes

- Update this README when payload files, child lanes, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each stable fixture to the exact check and consumer that uses it.
- If expected positive behavior stabilizes, update the paired input, expected output, consumer notes, sibling negative/contrast notes, and this README together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real person data, DNA data, land records, source exports, precise sensitive geography, or release material, move it out of this lane, quarantine it through the governed lifecycle or registry process, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Sibling negative fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/people-dna-land/genealogy/negative/README.md`.
- Genealogy doctrine alignment: PARTIALLY VERIFIED against `docs/domains/people-dna-land/sublanes/genealogy.md`.
- API trust-membrane alignment: PARTIALLY VERIFIED against `docs/domains/people-dna-land/API_CONTRACTS.md`.
- Identity model alignment: PARTIALLY VERIFIED against `docs/domains/people-dna-land/IDENTITY_MODEL.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, genealogy checks, identity-resolution checks, consent checks, source-role checks, evidence-bundle checks, citation-validation checks, rights checks, sensitivity checks, land-link checks, decision-envelope checks, drawer checks, Focus Mode checks, release-readiness checks, correction checks, rollback checks, schema checks, policy checks, renderer checks, and CI implementation.
- Tests and validators: NOT RUN.
