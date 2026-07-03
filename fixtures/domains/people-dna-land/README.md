# People/DNA/Land fixtures

`fixtures/domains/people-dna-land/`

Status: draft / fixture root index / People-DNA-Land synthetic examples.

This directory is the People / Genealogy / DNA / Land fixture root for small synthetic examples used to exercise bounded genealogy, identity, consent, source-role, evidence, citation, rights, sensitivity, land-ownership, decision-envelope, drawer, Focus Mode, release-readiness, correction, rollback, and expected-output behavior.

These files are examples only. They are not source records, lifecycle data, GEDCOM files, family trees, vital records, DNA data, land records, real deeds, real title instruments, real assessor records, real tax records, real parcel records, real legal descriptions, real person-to-parcel joins, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, policy decisions, consent records, review approvals, title opinions, release state, public API material, public map material, public tiles, people truth, genealogy truth, DNA truth, land truth, title truth, source authority, policy authority, release authority, AI authority, or published artifacts.

## Fixture root posture

People/DNA/Land fixtures are reviewable synthetic inputs and expected outputs for validators, smoke checks, documentation examples, governed-API dry-runs, drawer checks, Focus Mode checks, map/UI checks, release-readiness checks, correction checks, rollback checks, and future CI coverage.

This domain remains deny-first. Living-person outputs, DNA-derived public inference, raw kit/vendor identifiers, raw genealogy source identifiers, private person-to-parcel joins, title opinions, and unreviewed model-generated claims do not become public because a fixture exists. Positive fixtures must stay public-safe and evidence-referenced. Invalid fixtures must make the blocked condition explicit and fail closed. Golden fixtures capture stable expected outputs only.

A fixture may describe intended behavior before the corresponding validator, route, policy bundle, UI surface, release gate, or CI check exists. When implementation is not verified, the README must say so.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples, runtime/checking inputs, and expected-output examples. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, legal-opinion root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Current child-lane inventory

The following People/DNA/Land fixture lanes have populated README coverage. This table is a navigation index, not proof that payload files, validators, tests, governed API routes, UI checks, policy bundles, release manifests, source-registry records, proof stores, consent stores, or CI coverage exist.

| Child lane | Purpose | Expected posture |
|---|---|---|
| `genealogy/` | Synthetic genealogy fixture family with positive and negative child lanes. | Positive public-safe historical outputs or fail-closed genealogy outcomes. |
| `genealogy/positive/` | Public-safe synthetic historical genealogy examples with evidence, citation, rights, sensitivity, release, correction, and rollback posture visible. | `ANSWER`, validation pass, review-ready, evidence-resolved, citation-ready, source-role-preserved, release-ready, correction-visible, or rollback-visible. |
| `genealogy/negative/` | Fail-closed genealogy examples for missing evidence, missing consent, privacy exposure, source-role conflicts, identity conflicts, raw-source exposure, land-link exposure, missing release, or missing rollback support. | `ABSTAIN`, `DENY`, `ERROR`, validation failure, review-required, blocked render, correction-required, rollback-required, or release-readiness failure. |
| `land-ownership/` | Synthetic land-ownership examples for ownership assertions, intervals, instruments, assessor/tax context, parcel-version context, chain-of-title reasoning, and person-land joins. | Validation pass, review-ready, evidence-resolved, source-role-preserved, release-ready, or fail-closed where title/geometry/person-land boundaries are unsafe. |
| `valid/` | Broad positive-path staging and navigation lane. | `ANSWER`, validation pass, review-ready, evidence-resolved, citation-ready, rights-visible, sensitivity-reviewed, identity-resolved, release-ready, correction-visible, rollback-ready, or deterministic expected output. |
| `invalid/` | Broad fail-closed staging and navigation lane for known invalid families. | `ABSTAIN`, `DENY`, `ERROR`, validation failure, review-required, blocked render, release-readiness failure, correction-required, rollback-required, or trust-membrane failure. |
| `golden/` | Expected-output lane for stable synthetic People/DNA/Land inputs. | Deterministic expected positive or fail-closed output. |

## Relationship between major fixture families

| Family | Relationship |
|---|---|
| `genealogy/` | Exercises assertion-first, evidence-bound, privacy-aware genealogy behavior. |
| `land-ownership/` | Exercises evidence-not-title land ownership assertions, source-role boundaries, and title/geometry non-collapse. |
| `valid/` | Stages broad positive cases and routes stable object-family examples to narrower lanes. |
| `invalid/` | Stages broad fail-closed cases and routes stable defects to narrower lanes. |
| `golden/` | Stores stable expected outputs paired with synthetic inputs from sibling lanes. |

## Recommended use

| Use case | Preferred lane |
|---|---|
| Positive genealogy relationship, life event, family group, or ancestor-summary example | `genealogy/positive/` |
| Negative genealogy, missing-evidence, living-person, DNA-derived, raw-source, or private land-link example | `genealogy/negative/` or `invalid/` until a specific lane exists. |
| Land ownership assertion, ownership interval, deed/title instrument chain, assessor/tax context, or parcel-version context | `land-ownership/` |
| Broad positive People/DNA/Land scenario not yet sorted | `valid/` |
| Broad known fail-closed People/DNA/Land scenario not yet sorted | `invalid/` |
| Stable expected output for any synthetic input | `golden/` |
| Real person, DNA, land, source, consent, proof, title, or release material | Not fixtures; route through the governed responsibility root and lifecycle. |

## Related references

- `genealogy/README.md`
- `genealogy/positive/README.md`
- `genealogy/negative/README.md`
- `land-ownership/README.md`
- `valid/README.md`
- `invalid/README.md`
- `golden/README.md`
- `../README.md`
- `../../docs/domains/people-dna-land/README.md`
- `../../docs/domains/people-dna-land/sublanes/genealogy.md`
- `../../docs/domains/people-dna-land/sublanes/land.md`
- `../../docs/domains/people-dna-land/API_CONTRACTS.md`
- `../../docs/domains/people-dna-land/IDENTITY_MODEL.md`
- `../../docs/domains/people-dna-land/LAND_OWNERSHIP.md`
- `../../contracts/domains/people-dna-land/`
- `../../schemas/contracts/v1/domains/people-dna-land/`
- `../../policy/domains/people-dna-land/`
- `../../policy/sensitivity/people/`
- `../../policy/consent/people/`
- `../../data/registry/sources/people-dna-land/`
- `../../data/proofs/people-dna-land/`
- `../../release/candidates/people-dna-land/`
- `../../release/manifests/people-dna-land/`
- `../../docs/doctrine/directory-rules.md`

## Accepted material

This root and its child lanes may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.positive.json`, `*.invalid.json`, `*.negative.json`, `*.expected.json`, `*.golden.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy genealogy relationship assertions, life events, family groups, source-citation flows, identity-resolution states, consent states, evidence refs, policy refs, release refs, correction refs, rollback refs, drawer contexts, Focus Mode contexts, decision-envelope examples, and expected outputs;
- toy land ownership assertions, ownership intervals, deed or title instrument refs, assessor/tax context, parcel-version context, legal-description context, chain-of-title notes, person-land link examples, and expected outputs;
- positive-path, fail-closed, and expected-output examples that remain synthetic, deterministic, public-safe, and reviewable;
- contrast examples where a valid fixture is paired with an invalid or negative variant;
- README files documenting fixture intent, boundaries, consumer checks, and verification state.

## Exclusions

Do not use this root or its child lanes for real GEDCOM files, real family trees, real vital records, real living-person records, real DNA data, real kit/vendor identifiers, real person-to-parcel joins, real deeds, real title instruments, real assessor records, real tax records, real parcel records, real legal descriptions, real land records, real source exports, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, consent records, proof packs, release manifests, title opinions, legal advice, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy names, toy IDs, toy dates, toy places, toy relationship refs, toy parcel refs, toy instrument refs, toy source refs, toy evidence refs, toy consent refs if needed, toy policy refs, toy release refs, toy rollback refs, toy hashes, and toy timestamps.
- Prefer generic placeholders such as `PersonA`, `PersonB`, `AncestorExample`, `SyntheticFamily1`, `ToyPlaceRef`, `ToyParcelRef`, `ToyInstrumentRef`, and `SyntheticOwnerA`.
- Make fixture posture explicit: valid, invalid, positive, negative, golden, expected output, evidence-backed, evidence-missing, identity-resolved, identity-conflicted, consent-valid, consent-missing, source-role-preserved, source-role-conflicted, rights-visible, rights-unknown, sensitivity-reviewed, sensitivity-unresolved, release-ready, release-missing, correction-visible, correction-missing, rollback-ready, rollback-missing, or blocked render.
- Make expected outcome explicit when known: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, validation pass, validation failure, review-ready, review-required, evidence-resolved, citation-ready, blocked render, correction-required, rollback-required, release-ready, release-readiness failure, or deterministic expected output.
- Pair each stable input with an expected output in `golden/` when practical.
- Move stable broad examples into the most specific family lane once the object family and consumer are clear.
- Keep schema validity, semantic validity, identity resolution, evidence resolution, citation validation, consent posture, rights posture, sensitivity posture, source-role validity, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, layer-manifest state, UI behavior, correction posture, rollback posture, and expected-output state separate.
- Do not treat fixture success or failure as identity truth, relationship truth, DNA truth, ownership truth, title truth, boundary truth, legal advice, consent proof, EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected fixture families

| Scenario family | Preferred lane | Expected posture |
|---|---|---|
| Evidence-backed toy historical relationship assertion | `genealogy/positive/` | Validation pass, review-ready, or bounded `ANSWER`. |
| Public-safe ancestor summary with evidence refs | `genealogy/positive/` | `ANSWER` or review-ready. |
| Relationship assertion lacks evidence refs | `genealogy/negative/` | `ABSTAIN` or validation failure. |
| Living-person or DNA-derived public output attempt | `genealogy/negative/` or `invalid/` until sorted | `DENY` or review-required. |
| Evidence-backed toy historical ownership interval | `land-ownership/` | Validation pass or review-ready. |
| Assessor/tax context preserved as administrative context | `land-ownership/` | Validation pass or review-ready. |
| Assessor row treated as title truth | `land-ownership/` or `invalid/` | `DENY` or validation failure. |
| Parcel geometry treated as title boundary | `land-ownership/` or `invalid/` | `DENY` or validation failure. |
| Stable output is ready to compare | `golden/` | Deterministic expected output. |

## Maintenance notes

- Update this README when new child lanes, payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each stable fixture to the exact check and consumer that uses it.
- If expected behavior stabilizes, update the paired input, expected output, consumer notes, child README, `golden/README.md`, and this root index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real person data, DNA data, land records, source exports, precise sensitive geography, proof material, consent material, title material, or release material, move it out of this root, quarantine it through the governed lifecycle or registry process, and record the correction path.

## Verification status

- Target README: replaced greenfield stub content.
- Fixture payload inventory: no payload files verified under this root during this update.
- Child README inventory: PARTIALLY VERIFIED against populated `genealogy/`, `land-ownership/`, `valid/`, `invalid/`, and `golden/` README files fetched during this update and recent preceding updates.
- Genealogy fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/people-dna-land/genealogy/README.md`.
- Land-ownership fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/people-dna-land/land-ownership/README.md`.
- Valid fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/people-dna-land/valid/README.md`.
- Invalid fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/people-dna-land/invalid/README.md`.
- Golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/people-dna-land/golden/README.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, People/DNA/Land governed-API tests, genealogy checks, land-ownership checks, identity-resolution checks, consent checks, source-role checks, evidence-bundle checks, citation-validation checks, rights checks, sensitivity checks, land-link checks, decision-envelope checks, drawer checks, Focus Mode checks, release-readiness checks, correction checks, rollback checks, schema checks, policy checks, renderer checks, and UI implementation.
- Tests and validators: NOT RUN.
