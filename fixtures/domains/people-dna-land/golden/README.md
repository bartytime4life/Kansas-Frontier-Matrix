# People/DNA/Land golden fixtures

`fixtures/domains/people-dna-land/golden/`

Status: draft / fixture lane / expected-output examples.

This directory is for small synthetic People / Genealogy / DNA / Land expected-output fixtures. Golden fixtures describe the expected result for known synthetic People/DNA/Land inputs used by bounded checks, genealogy positive and negative examples, identity-resolution examples, consent checks, source-role checks, evidence-resolution checks, citation-validation checks, rights checks, sensitivity checks, land-link checks, decision-envelope examples, drawer examples, Focus Mode examples, release-readiness checks, correction checks, rollback checks, and documentation examples.

These files are examples only. They are not source records, lifecycle data, GEDCOM files, family trees, vital records, DNA data, land records, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, policy decisions, consent records, review approvals, release state, public API material, public map material, public tiles, people truth, genealogy truth, land truth, source authority, policy authority, release authority, AI authority, or published artifacts.

## Golden fixture posture

Use this lane for stable expected outputs paired with synthetic People/DNA/Land fixture inputs. A golden fixture should make the expected finite posture explicit, such as `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, validation pass, validation failure, review-ready, review-required, evidence-resolved, evidence-missing, citation-ready, citation-failed, consent-satisfied, consent-missing, rights-visible, rights-missing, sensitivity-reviewed, sensitivity-unresolved, identity-resolved, identity-conflicted, release-ready, release-blocked, correction-visible, correction-required, rollback-ready, rollback-required, or blocked render.

A golden fixture is not proof that implementation exists. It does not prove validator behavior, governed API route behavior, UI behavior, policy enforcement, consent enforcement, schema enforcement, EvidenceBundle storage, release integration, or CI coverage by itself.

## Placement basis

This lane belongs under `fixtures/` because it contains expected-output examples for synthetic fixtures. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Relationship to input lanes

Use this lane for stable expected outputs paired with synthetic People/DNA/Land inputs from sibling fixture lanes.

| Input lane | Expected-output use | Status |
|---|---|---|
| `../genealogy/` | Expected outputs for synthetic genealogy parent, positive, and negative fixture inputs. | Present README populated. |
| `../genealogy/positive/` | Expected positive outputs for public-safe historical genealogy examples. | Present README populated. |
| `../genealogy/negative/` | Expected fail-closed outputs for unsafe, unsupported, unresolved, or unreviewed genealogy examples. | Present README populated. |

Future sibling lanes may add people identity, DNA handling, land ownership, source descriptor, consent, decision envelope, evidence bundle, run receipt, layer manifest, drawer, Focus Mode, correction, rollback, or release-readiness fixtures. Expected outputs may be stored here when they are stable, deterministic, synthetic, and documented.

## Related references

- `../genealogy/README.md`
- `../genealogy/positive/README.md`
- `../genealogy/negative/README.md`
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

- small synthetic `*.expected.json`, `*.expected.geojson`, `*.expected.jsonl`, `*.expected.yaml`, `*.expected.yml`, `*.expected.svg`, `*.golden.json`, or `*.md` expected-output examples;
- expected positive-path outputs for public-safe historical genealogy, identity, consent, source-role, evidence, citation, rights, sensitivity, correction, rollback, and release-readiness fixture inputs;
- expected fail-closed outputs for living-person, DNA-derived, raw-source, private land-link, missing-consent, missing-evidence, unresolved-identity, unknown-rights, unresolved-sensitivity, missing-release, missing-correction, or missing-rollback fixture inputs;
- expected decision-envelope, EvidenceBundle, Evidence Drawer, Focus Mode, layer resolver, export, source-role, evidence-resolution, citation-validation, consent, policy, release-readiness, correction, rollback, or documentation-example outputs;
- paired expected outputs for inputs stored in sibling fixture lanes such as `../genealogy/positive/` and `../genealogy/negative/`;
- README files explaining fixture intent and boundaries.

## Exclusions

Do not use this lane for real GEDCOM files, real family trees, real vital records, real living-person records, real DNA data, real kit/vendor identifiers, real person-to-parcel joins, real land records, real source exports, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, consent records, proof packs, release manifests, correction notices, review records, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Fixture design rules

- Keep expected outputs synthetic, compact, deterministic, and reviewable.
- Pair golden outputs with a clearly named input fixture whenever practical.
- Use naming that makes the relationship obvious, such as `<scenario>.input.json` in a sibling lane and `<scenario>.expected.json` in this lane, or an equivalent documented pair.
- Keep expected outcomes explicit, such as `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, validation pass, validation failure, review-ready, review-required, evidence-resolved, evidence-missing, citation-ready, citation-failed, consent-satisfied, consent-missing, rights-visible, rights-missing, sensitivity-reviewed, sensitivity-unresolved, identity-resolved, identity-conflicted, release-ready, release-blocked, correction-visible, correction-required, rollback-ready, rollback-required, blocked render, or another documented finite posture.
- Keep schema validity, semantic validity, identity state, evidence state, citation state, consent state, rights state, sensitivity state, source-role state, freshness state, review state, release state, correction state, rollback state, and expected-output state explicit where material.
- Do not include real source properties, direct model-runtime output, unpublished candidate content, real person data, real DNA data, real land records, or geometry that could reasonably be mistaken for real sensitive data.
- Treat `schema-valid`, `semantic-valid`, `identity-resolved`, `evidence-resolved`, `citation-safe`, `consent-valid`, `rights-cleared`, `sensitivity-reviewed`, `source-role-valid`, `policy-admissible`, `release-safe`, `trust-membrane-safe`, `drawer-safe`, `focus-safe`, and `renderer-safe` as separate checks.
- Do not treat golden fixtures as evidence, approval, release state, proof authority, source authority, schema authority, implementation proof, public-map authority, tile authority, or published output.

## Expected golden fixture examples

| Input lane | Example expected output | Notes |
|---|---|---|
| `../genealogy/positive/` | Bounded `ANSWER` for a public-safe synthetic historical relationship claim | Output remains evidence-referenced and not canonical truth. |
| `../genealogy/positive/` | Validation-pass output for a cited toy life event | Source role, time, and citation remain visible. |
| `../genealogy/negative/` | `ABSTAIN` for a relationship assertion without evidence refs | Cite-or-abstain remains visible. |
| `../genealogy/negative/` | `DENY` for living-person or DNA-derived public output | Deny-first behavior is expected. |
| `../genealogy/negative/` | Release-readiness failure for private person-to-parcel join without review | Land links require policy and release gates. |
| Future `identity/` | Identity-resolved or identity-conflicted output | Canonical identity remains outside fixtures. |
| Future `consent/` | Consent-valid or consent-missing output | Consent records are not stored in fixtures. |
| Future `land/` | Public-safe land-link summary or deny output | Fixture output cannot become title truth. |

## Maintenance notes

- Update this README when payload files, input fixture lanes, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each golden fixture to the input fixture and the test, governed-API contract, Evidence Drawer test, Focus Mode test, identity resolver, consent checker, source-role check, evidence resolver, citation validator, rights check, sensitivity check, policy check, release-readiness check, schema check, renderer check, correction check, rollback check, or documentation example that consumes it.
- Keep payloads small enough for normal code review.
- If an expected output becomes broad enough to be a release artifact, move that concern to the governed release lane instead of expanding this fixture lane.
- If a fixture accidentally includes real person data, DNA data, land records, source exports, precise sensitive geography, or release material, move it out of this lane, quarantine it through the governed lifecycle or registry process, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Genealogy fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/people-dna-land/genealogy/README.md` and child lanes.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Parent People/DNA/Land fixture README: NEEDS VERIFICATION.
- Consumer alignment: NEEDS VERIFICATION against validators, golden-file checks, People/DNA/Land governed-API tests, genealogy checks, identity-resolution checks, consent checks, source-role checks, evidence-bundle checks, citation-validation checks, rights checks, sensitivity checks, land-link checks, decision-envelope checks, drawer checks, Focus Mode checks, release-readiness checks, correction checks, rollback checks, schema checks, policy checks, renderer checks, and UI implementation.
- Tests and validators: NOT RUN.
