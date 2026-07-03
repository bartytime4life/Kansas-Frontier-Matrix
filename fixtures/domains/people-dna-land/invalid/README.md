# People/DNA/Land invalid fixtures

`fixtures/domains/people-dna-land/invalid/`

Status: draft / invalid fixture parent index / People-DNA-Land fail-closed examples.

This directory is the broad parent lane for small synthetic People / Genealogy / DNA / Land invalid fixture examples. Use it to index and stage known fail-closed cases that should not produce a public person claim, genealogy claim, DNA-derived output, land-link assertion, map overlay, Focus Mode answer, drawer projection, release-ready output, or API `ANSWER` because evidence, consent, rights, sensitivity, identity resolution, source role, release state, correction posture, or rollback posture is missing or unsafe.

These files are examples only. They are not source records, lifecycle data, GEDCOM files, family trees, vital records, DNA data, land records, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, policy decisions, consent records, review approvals, release state, public API material, public map material, public tiles, people truth, genealogy truth, DNA truth, land truth, source authority, policy authority, release authority, AI authority, or published artifacts.

## Invalid fixture posture

Use this lane for synthetic inputs that should not produce a normal public `ANSWER`. Expected outcomes may include `ABSTAIN`, `DENY`, `ERROR`, validation failure, review-required, blocked render, release-readiness failure, correction-required, rollback-required, evidence-resolution failure, citation-validation failure, consent failure, source-role failure, rights/sensitivity failure, or trust-membrane failure.

People / DNA / Land is deny-first. Living-person outputs, DNA-derived outputs, raw kit/vendor identifiers, raw genealogy source identifiers, and private person-to-parcel joins are denied or restricted by default. Invalid fixtures should make the blocked condition explicit and keep expected failure separate from implementation proof.

A fixture can describe a desired negative case before validators, governed API routes, UI checks, schema enforcement, policy bundles, release integration, or CI coverage exist.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Current child-lane inventory

The following People/DNA/Land fixture lanes currently carry more specific invalid, negative, or fail-closed README coverage. This table is a navigation index, not proof that payload files, validators, tests, governed API routes, UI checks, policy bundles, release manifests, source-registry records, proof stores, or CI coverage exist.

| Child or sibling lane | Invalid case family | Expected posture |
|---|---|---|
| `../genealogy/negative/` | Fail-closed genealogy examples for missing evidence, missing consent, privacy exposure, source-role conflicts, identity conflicts, raw-source exposure, land-link exposure, missing release, or missing rollback support. | `ABSTAIN`, `DENY`, `ERROR`, validation failure, review-required, blocked render, correction-required, rollback-required, or release-readiness failure. |
| `../genealogy/` | Parent genealogy fixture lane with positive/negative separation. | Routes stable genealogy invalid cases to `genealogy/negative/`. |
| `../golden/` | Expected outputs for stable invalid inputs. | Deterministic expected fail-closed output, once paired with an input fixture. |

Future child lanes under this `invalid/` parent may be added when broader People/DNA/Land negative-path families are stable enough to deserve their own directory, such as identity conflicts, consent failures, source-role collapse, evidence-resolution failures, citation failures, rights/sensitivity failures, raw genealogy-source exposure, DNA-derived public-output attempts, private land-link exposure, release-readiness failures, correction gaps, rollback gaps, drawer failures, Focus Mode failures, or governed-API envelope failures.

## Relationship to sibling fixture lanes

| Sibling lane | Relationship |
|---|---|
| `../genealogy/` | Genealogy fixture family; invalid genealogy cases currently live under `genealogy/negative/`. |
| `../genealogy/negative/` | Specific negative-path genealogy lane. |
| `../genealogy/positive/` | Positive-path contrast lane for public-safe synthetic historical genealogy examples. |
| `../golden/` | Stable expected fail-closed outputs should be paired there. |
| `../README.md` | Parent People/DNA/Land fixture lane; not inspected during this update. |

## When to use this lane vs specific invalid children

| Use case | Preferred lane | Reason |
|---|---|---|
| Invalid genealogy relationship, life-event, or family-group example | `../genealogy/negative/` | The object family is already known and specific. |
| Stable expected output for an invalid input | `../golden/` | Golden files anchor deterministic expectations. |
| Broad invalid People/DNA/Land scenario not yet sorted | `./` | This parent can stage or document the family without creating premature taxonomy. |
| Real person, DNA, land, source, consent, or release material appears in a fixture | Neither | Move it out of fixtures and route through the governed lifecycle, registry, consent, policy, or quarantine path. |

## Related references

- `../genealogy/README.md`
- `../genealogy/positive/README.md`
- `../genealogy/negative/README.md`
- `../golden/README.md`
- `../README.md`
- `../../README.md`
- `../../../docs/domains/people-dna-land/README.md`
- `../../../docs/domains/people-dna-land/sublanes/genealogy.md`
- `../../../docs/domains/people-dna-land/API_CONTRACTS.md`
- `../../../docs/domains/people-dna-land/IDENTITY_MODEL.md`
- `../../../docs/domains/people-dna-land/LAND_OWNERSHIP.md`
- `../../../contracts/domains/people-dna-land/`
- `../../../schemas/contracts/v1/domains/people-dna-land/`
- `../../../policy/domains/people-dna-land/`
- `../../../policy/sensitivity/people/`
- `../../../policy/consent/people/`
- `../../../data/registry/sources/people-dna-land/`
- `../../../data/proofs/people-dna-land/`
- `../../../release/candidates/people-dna-land/`
- `../../../release/manifests/people-dna-land/`
- `../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.invalid.json`, `*.negative.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- draft invalid examples for genealogy, identity resolution, consent checks, source-role checks, evidence-resolution checks, citation-validation checks, rights/sensitivity checks, land-link checks, decision envelopes, drawer outputs, Focus Mode outputs, layer resolver outputs, release-readiness checks, correction checks, rollback checks, and trust-membrane checks;
- toy `ABSTAIN`, `DENY`, `ERROR`, validation-failure, review-required, blocked-render, evidence-missing, citation-failed, consent-missing, rights-missing, sensitivity-missing, identity-conflicted, source-role-conflicted, release-blocked, correction-required, rollback-required, or expected-output examples;
- contrast examples showing the difference between a valid public-safe historical fixture and an invalid variant;
- paired expected outputs in `../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real GEDCOM files, real family trees, real vital records, real living-person records, real DNA data, real kit/vendor identifiers, real person-to-parcel joins, real land records, real source exports, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, consent records, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Make the invalid condition explicit in the file name, payload, expected output, and consumer notes.
- Make expected outcome explicit when known: `ABSTAIN`, `DENY`, `ERROR`, validation failure, review-required, blocked render, release-readiness failure, correction-required, rollback-required, or expected output.
- Pair each stable invalid input with an expected failure output in `../golden/` when practical.
- Move stable invalid cases to a specific child lane when the defect family becomes clear.
- Keep schema validity, semantic validity, identity resolution, evidence resolution, citation validation, consent posture, rights posture, sensitivity posture, source-role validity, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, layer-manifest state, UI behavior, correction posture, rollback posture, and expected-output state separate.
- Do not treat fixture failure as identity truth, relationship truth, DNA truth, title truth, consent proof, EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected invalid fixture families

| Scenario family | Preferred lane | Expected posture |
|---|---|---|
| Relationship assertion lacks evidence refs | `../genealogy/negative/` | `ABSTAIN` or validation failure. |
| Tree overlay treated as observed fact | `../genealogy/negative/` | `ABSTAIN` or validation failure. |
| Living-person field requested without scoped consent | `../genealogy/negative/` or future consent lane | `DENY`. |
| DNA-derived inference requested for public output | Future DNA/consent invalid lane or this parent until sorted | `DENY` or review-required. |
| Raw genealogy-source identifier exposed in a public surface | `../genealogy/negative/` | `DENY` or validation failure. |
| Private person-to-parcel join lacks release and sensitivity review | `../genealogy/negative/` or future land invalid lane | `DENY` or release-readiness failure. |
| Conflicting identity assertions are unresolved | `../genealogy/negative/` or future identity invalid lane | `ABSTAIN` or review-required. |
| Missing correction or rollback path | Specific fixture family or this parent until sorted | Review-required or release-readiness failure. |
| Stable fail-closed output is ready to compare | `../golden/` | Deterministic expected output. |

## Maintenance notes

- Update this README when new invalid child lanes, invalid payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each invalid fixture to the exact check and consumer that uses it.
- If expected invalid behavior stabilizes, update the paired input, expected output, consumer notes, child README, `../golden/README.md`, and this index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real person data, DNA data, land records, source exports, precise sensitive geography, or release material, move it out of this lane, quarantine it through the governed lifecycle or registry process, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payload files verified under this parent during this update.
- Genealogy negative alignment: PARTIALLY VERIFIED against `fixtures/domains/people-dna-land/genealogy/negative/README.md`.
- Genealogy fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/people-dna-land/genealogy/README.md` from the recent preceding update.
- Golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/people-dna-land/golden/README.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md` from recent preceding updates.
- Parent People/DNA/Land fixture README: NEEDS VERIFICATION.
- Consumer alignment: NEEDS VERIFICATION against validators, invalid-fixture checks, golden-file checks, People/DNA/Land governed-API tests, genealogy checks, identity-resolution checks, consent checks, source-role checks, evidence-bundle checks, citation-validation checks, rights checks, sensitivity checks, land-link checks, decision-envelope checks, drawer checks, Focus Mode checks, release-readiness checks, correction checks, rollback checks, schema checks, policy checks, renderer checks, and UI implementation.
- Tests and validators: NOT RUN.
