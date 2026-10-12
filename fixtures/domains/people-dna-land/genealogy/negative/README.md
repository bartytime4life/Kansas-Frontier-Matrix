# People/DNA/Land genealogy negative fixtures

`fixtures/domains/people-dna-land/genealogy/negative/`

Status: draft / negative fixture lane / genealogy fail-closed examples.

This directory is for small synthetic negative-path genealogy fixtures in the People / Genealogy / DNA / Land domain. Use it for toy cases that should not produce a public genealogy claim, person identity, relationship assertion, land-link assertion, map overlay, Focus Mode answer, drawer projection, or API `ANSWER` because evidence, consent, rights, sensitivity, identity resolution, source role, release state, correction posture, or rollback posture is missing or unsafe.

These files are examples only. They are not source records, lifecycle data, GEDCOM files, family trees, vital records, DNA data, land records, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, policy decisions, consent records, review approvals, release state, public API material, public map material, public tiles, genealogy truth, source authority, policy authority, release authority, AI authority, or published artifacts.

## Negative fixture posture

Genealogy doctrine treats kinship and life-event material as assertion-first, evidence-bound, and privacy-aware. A relationship, event, or identity claim is not a sovereign fact just because a tree, file, memory, or model output says it. It needs evidence support, rights posture, sensitivity review, and governed release before it can appear in any public surface.

People / DNA / Land is a deny-first domain. Living-person outputs, DNA-derived outputs, raw kit/vendor identifiers, and private person-to-parcel joins are denied or restricted by default. A negative fixture should therefore make the blocked condition explicit and expect `ABSTAIN`, `DENY`, `ERROR`, validation failure, review-required, blocked render, release-readiness failure, correction-required, or rollback-required output.

This lane can support future validation and governed-API checks, but examples here do not prove validator implementation, route behavior, policy enforcement, schema enforcement, consent enforcement, EvidenceBundle storage, release integration, UI rendering, or CI coverage by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Relationship to People/DNA/Land governance

| Lane or document | Relationship |
|---|---|
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

- small synthetic `*.input.json`, `*.negative.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy relationship, life-event, family-group, source-citation, consent, identity-resolution, land-link, evidence-ref, policy-ref, release-ref, correction, rollback, drawer, Focus Mode, or decision-envelope examples;
- toy cases for missing evidence, unresolved source role, unsupported citation, unknown rights, unresolved sensitivity, absent consent, living-person exposure, DNA-derived inference exposure, private person-to-parcel join exposure, unresolved identity conflict, contradictory relationship assertions, candidate-tree misuse, GEDCOM-as-public-surface misuse, missing release state, or missing rollback target;
- toy expected outputs such as `ABSTAIN`, `DENY`, `ERROR`, validation failure, review-required, blocked render, correction-required, rollback-required, or release-readiness failure;
- contrast examples that show the difference between a public-safe historical claim and a blocked claim.

## Exclusions

Do not use this lane for real GEDCOM files, real family trees, real vital records, real living-person records, real DNA data, real kit/vendor identifiers, real person-to-parcel joins, real land records, real source exports, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, consent records, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy names, toy IDs, toy dates, toy places, toy relationship refs, toy source refs, toy evidence refs, toy consent refs, toy policy refs, toy release refs, toy rollback refs, toy hashes, and toy timestamps.
- Prefer generic placeholders such as `PersonA`, `PersonB`, `AncestorExample`, `SyntheticFamily1`, and `ToyParcelRef`; do not use real people, real family trees, real parcel identifiers, real coordinates, or real DNA identifiers.
- Make the blocked condition explicit: missing evidence, unresolved identity, contradictory assertion, unsupported source role, unknown rights, unresolved sensitivity, absent consent, living-person field, DNA-derived inference, private person-land join, candidate-tree claim, GEDCOM exposure, missing release, missing correction path, or missing rollback target.
- Make expected outcome explicit: `ABSTAIN`, `DENY`, `ERROR`, validation failure, review-required, blocked render, correction-required, rollback-required, or release-readiness failure.
- Pair each stable negative input with an expected output when practical.
- Keep schema validity, semantic validity, identity resolution, evidence resolution, citation validation, consent posture, rights posture, sensitivity posture, source-role validity, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, correction posture, rollback posture, and expected-output state separate.
- Do not treat fixture failure as identity truth, relationship truth, title truth, consent proof, EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected negative fixture families

| Scenario family | Expected posture | Notes |
|---|---|---|
| Relationship assertion lacks evidence refs | `ABSTAIN` or validation failure | Genealogy claims are assertion-first and evidence-bound. |
| Tree overlay treated as observed fact | `ABSTAIN` or validation failure | Hypothesis material must not become observed truth. |
| Living-person field requested without scoped consent | `DENY` | Deny-first posture is correct behavior. |
| DNA-derived relationship inference requested for public output | `DENY` or review-required | DNA-derived outputs are restricted by default. |
| GEDCOM identifier exposed in a public surface | `DENY` or validation failure | GEDCOM is raw/source material, not public output. |
| Person-to-parcel join lacks release and sensitivity review | `DENY` or release-readiness failure | Land links require policy and release gates. |
| Conflicting identity assertions are unresolved | `ABSTAIN` or review-required | Identity resolution must remain evidence-bound. |
| Missing correction or rollback path | Review-required or release-readiness failure | Published claims need correction and rollback support. |
| Model-generated lineage text lacks evidence refs | `ABSTAIN` or validation failure | AI cannot substitute for evidence. |

## Maintenance notes

- Update this README when payload files, child lanes, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each stable fixture to the exact check and consumer that uses it.
- If expected negative behavior stabilizes, update the paired input, expected output, consumer notes, and this README together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real person data, DNA data, land records, source exports, precise sensitive geography, or release material, move it out of this lane, quarantine it through the governed lifecycle or registry process, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Genealogy doctrine alignment: PARTIALLY VERIFIED against `docs/domains/people-dna-land/sublanes/genealogy.md`.
- API trust-membrane alignment: PARTIALLY VERIFIED against `docs/domains/people-dna-land/API_CONTRACTS.md`.
- Identity model alignment: PARTIALLY VERIFIED against `docs/domains/people-dna-land/IDENTITY_MODEL.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, genealogy checks, identity-resolution checks, consent checks, source-role checks, evidence-bundle checks, citation-validation checks, rights checks, sensitivity checks, land-link checks, decision-envelope checks, drawer checks, Focus Mode checks, release-readiness checks, correction checks, rollback checks, schema checks, policy checks, renderer checks, and CI implementation.
- Tests and validators: NOT RUN.
