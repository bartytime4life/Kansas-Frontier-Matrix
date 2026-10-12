<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/people-dna-land/valid/authoring-guide
title: People, DNA and Land valid fixture authoring guide
type: fixture-guide
version: v1
status: repository-grounded documentation; no new fixture payloads
owners: ["@bartytime4life"]
created: 2026-10-08
updated: 2026-10-08
policy_label: synthetic-public-safe-only; no-network; no-authority
current_path: fixtures/domains/people-dna-land/valid/README.md
owning_root: fixtures/
responsibility: Explain the actual people-dna-land valid inventory, authoring boundaries and existing consumer routes.
truth_posture: CONFIRMED inventory and code/test pointers inspected at main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe; no new runtime acceptance claimed.
related:
  - ../../../README.md
  - ../../../../tests/domains/people-dna-land/consent/revocation/test_consent_overlay_safety.py
[/KFM_META_BLOCK_V2] -->

# People, DNA and Land: valid fixture guide

Describe the positive-input lane for a specific declared profile. Valid means the input satisfies that bounded schema and semantic contract; it does not mean the source is admitted, complete or ready for publication.

## Current inventory

This directory contains documentation only at the inspected source revision; it has no executable valid payloads. It does not provide valid fixture coverage merely because the lane or this file exists. Concrete sibling families below have their own consumers and must be evaluated separately.

The adjacent `PLACEHOLDER.md` retains exact machine-checked marker bytes. This README supplies the substantive authoring guide while preserving the workflow guard and the absence of new payload coverage.

## Domain rules to preserve

The consent-overlay profile has two positive synthetic cases: historical documentary context and restricted active consent. Negative fixtures cover missing/expired/revoked consent, identifying kit fields, raw genomic material, precise locations, weak evidence, revocation-root mismatch and public-release claims. Revocation propagation is a separate family rather than a public genealogy export.

Use fictional subjects and fixture-local consent/evidence references. Preserve historical documentary context versus restricted active-consent handling. Keep authority/publication false. No real kits, living-person records, raw genomic material, person-to-parcel joins or title assertions belong in reusable fixtures.

## Author or revise a case

1. Start from the closest concrete positive family, not a free-form object or an inventory stub.
2. Keep synthetic identity and references, declared source role, time semantics and domain limitations intact. Change only fields required by the scenario.
3. Name the actual schema and semantic consumer and add a companion negative case for the boundary being demonstrated.
4. Update the consuming test's explicit inventory or manifest when required. Record which outcome is expected; a valid candidate may intentionally produce ABSTAIN or HOLD.

## Existing evidence and consumers

- [fixtures/domains/people-dna-land/consent_overlay/valid/historical_documentary_context.json](../consent_overlay/valid/historical_documentary_context.json)
- [fixtures/domains/people-dna-land/consent_overlay/valid/restricted_active_consent.json](../consent_overlay/valid/restricted_active_consent.json)
- [fixtures/domains/people-dna-land/consent_overlay/revocation_manifest.json](../consent_overlay/revocation_manifest.json)
- [fixtures/domains/people-dna-land/consent_revocation_propagation/cases.json](../consent_revocation_propagation/cases.json)
- [Primary bounded test](../../../../tests/domains/people-dna-land/consent/revocation/test_consent_overlay_safety.py)
- [Related regression coverage](../../../../tests/domains/people-dna-land/consent/revocation/test_consent_revocation_propagation_assessment.py)
- [Concrete validator](../../../../tools/validators/domains/people-dna-land/validate_consent_overlay.py)

After installing the repository's declared test dependencies, run the relevant existing tests from the repository root:

```bash
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider tests/domains/people-dna-land/consent/revocation/test_consent_overlay_safety.py tests/domains/people-dna-land/consent/revocation/test_consent_revocation_propagation_assessment.py
```

This command exercises the linked families, not an empty directory or every domain promise. It is provided as a contributor workflow and was not run for this documentation-only edit. Inspect the test assertions before extending their scope; README names and schema-file syntax checks do not establish behavioral coverage.

## Review boundary

Use only small synthetic, public-safe examples under this public fixture root. Keep real provider captures and sensitive records in their governed data lanes. Passing a fixture proves the named implementation's response to those bytes only; admission, policy decisions, source activation, release, deployment and publication remain separate.

Placement and owner routing follow [the reusable fixture-root guide](../../../README.md) and [CODEOWNERS](../../../../.github/CODEOWNERS). The existing [domain fixture index](../README.md) supplies broader context; this guide does not move any source, contract, policy or release responsibility.

## Earlier lane guidance

The following established guidance is retained for continuity; the current inventory and consumer routes above supply the source-grounded checkpoint.

# People/DNA/Land valid fixtures

`fixtures/domains/people-dna-land/valid/`

Status: draft / valid fixture parent index / People-DNA-Land positive-path examples.

This directory is the broad parent lane for small synthetic People / Genealogy / DNA / Land valid fixture examples. Use it to index and stage positive-path cases that can demonstrate bounded, evidence-backed, public-safe behavior for genealogy, identity, consent, source-role preservation, evidence resolution, citation validation, rights posture, sensitivity posture, land ownership context, decision envelopes, drawer projections, Focus Mode responses, release-readiness checks, correction posture, rollback posture, and expected outputs.

These files are examples only. They are not source records, lifecycle data, GEDCOM files, family trees, vital records, DNA data, land records, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, policy decisions, consent records, review approvals, release state, public API material, public map material, public tiles, people truth, genealogy truth, DNA truth, land truth, title truth, source authority, policy authority, release authority, AI authority, or published artifacts.

## Valid fixture posture

Use this lane for synthetic inputs that should produce a bounded positive posture such as `ANSWER`, validation pass, review-ready, evidence-resolved, citation-ready, rights-visible, sensitivity-reviewed, source-role-preserved, identity-resolved, release-ready, correction-visible, rollback-ready, or deterministic expected output.

People / DNA / Land remains a deny-first domain even in valid fixtures. Valid examples must stay public-safe and must not publish living-person fields, DNA-derived public inference, raw kit/vendor identifiers, raw genealogy source identifiers, private person-to-parcel joins, title opinions, or unreviewed model-generated claims.

A fixture can describe a desired positive case before validators, governed API routes, UI checks, schema enforcement, policy bundles, release integration, or CI coverage exist. Fixture success is not implementation proof, policy approval, release approval, or truth authority.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, legal-opinion root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Current valid fixture families

The following People/DNA/Land fixture lanes currently carry more specific positive-path or valid README coverage. This table is a navigation index, not proof that payload files, validators, tests, governed API routes, UI checks, policy bundles, release manifests, source-registry records, proof stores, or CI coverage exist.

| Child or sibling lane | Valid case family | Expected posture |
|---|---|---|
| `../genealogy/positive/` | Public-safe historical genealogy examples with evidence, citation, rights, sensitivity, release, correction, and rollback posture visible. | `ANSWER`, validation pass, review-ready, evidence-resolved, citation-ready, source-role-preserved, release-ready, correction-visible, or rollback-visible. |
| `../genealogy/` | Parent genealogy fixture lane with positive/negative separation. | Routes stable genealogy positive cases to `genealogy/positive/`. |
| `../land-ownership/` | Land-ownership fixture family, including positive and negative synthetic land examples. | Validation pass, review-ready, evidence-resolved, source-role-preserved, release-ready, or fail-closed where title/geometry/person-land boundaries are unsafe. |
| `../golden/` | Expected outputs for stable valid inputs. | Deterministic expected positive output, once paired with an input fixture. |

Future child lanes under this `valid/` parent may be added when broader People/DNA/Land positive-path families are stable enough to deserve their own directory, such as identity resolution, consent-valid examples, source-role-valid examples, EvidenceBundle examples, RunReceipt examples, decision-envelope examples, drawer examples, Focus Mode examples, release-readiness examples, correction examples, or rollback examples.

## Relationship to sibling fixture lanes

| Sibling lane | Relationship |
|---|---|
| `../genealogy/` | Genealogy fixture family; valid genealogy cases currently live under `genealogy/positive/`. |
| `../genealogy/positive/` | Specific positive-path genealogy lane. |
| `../genealogy/negative/` | Fail-closed contrast lane for unsafe or unsupported genealogy cases. |
| `../land-ownership/` | Land fixture family; valid land cases may live there when the object family is known. |
| `../invalid/` | Whole-domain invalid fixture index and fail-closed contrast lane. |
| `../golden/` | Stable expected positive outputs should be paired there. |
| `../README.md` | Parent People/DNA/Land fixture lane; not inspected during this update. |

## When to use this lane vs specific valid children

| Use case | Preferred lane | Reason |
|---|---|---|
| Valid genealogy relationship, life-event, or family-group example | `../genealogy/positive/` | The object family is already known and specific. |
| Valid land ownership assertion, ownership interval, source-role-preserved assessor context, or parcel-version context | `../land-ownership/` | Land object families and title/geometry boundaries need specific guardrails. |
| Stable expected output for a valid input | `../golden/` | Golden files anchor deterministic expectations. |
| Broad valid People/DNA/Land scenario not yet sorted | `./` | This parent can stage or document the family without creating premature taxonomy. |
| Real person, DNA, land, source, consent, proof, or release material appears in a fixture | Neither | Move it out of fixtures and route through the governed lifecycle, registry, consent, policy, proof, release, or quarantine path. |

## Related references

- `../genealogy/README.md`
- `../genealogy/positive/README.md`
- `../genealogy/negative/README.md`
- `../land-ownership/README.md`
- `../invalid/README.md`
- `../golden/README.md`
- `../README.md`
- `../../README.md`
- `../../../docs/domains/people-dna-land/README.md`
- `../../../docs/domains/people-dna-land/sublanes/genealogy.md`
- `../../../docs/domains/people-dna-land/sublanes/land.md`
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

- small synthetic `*.input.json`, `*.valid.json`, `*.positive.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- draft valid examples for genealogy, identity resolution, consent checks, source-role checks, evidence-resolution checks, citation-validation checks, rights/sensitivity checks, land-link checks, land-ownership assertions, decision envelopes, drawer outputs, Focus Mode outputs, layer resolver outputs, release-readiness checks, correction checks, rollback checks, and trust-membrane checks;
- toy `ANSWER`, validation-pass, review-ready, evidence-resolved, citation-ready, consent-valid, rights-visible, sensitivity-reviewed, source-role-preserved, identity-resolved, release-ready, correction-visible, rollback-ready, or expected-output examples;
- contrast examples showing the difference between a valid public-safe historical fixture and an invalid variant;
- paired expected outputs in `../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real GEDCOM files, real family trees, real vital records, real living-person records, real DNA data, real kit/vendor identifiers, real person-to-parcel joins, real deeds, real title instruments, real assessor records, real tax records, real parcel records, real legal descriptions, real land records, real source exports, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, consent records, proof packs, release manifests, title opinions, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Make the valid condition explicit in the file name, payload, expected output, and consumer notes.
- Make expected outcome explicit when known: `ANSWER`, validation pass, review-ready, evidence-resolved, citation-ready, consent-valid, rights-visible, sensitivity-reviewed, source-role-preserved, identity-resolved, release-ready, correction-visible, rollback-ready, or expected output.
- Pair each stable valid input with an expected output in `../golden/` when practical.
- Move stable valid cases to a specific child lane when the object family becomes clear.
- Keep schema validity, semantic validity, identity resolution, evidence resolution, citation validation, consent posture, rights posture, sensitivity posture, source-role validity, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, layer-manifest state, UI behavior, correction posture, rollback posture, and expected-output state separate.
- Do not treat fixture success as identity truth, relationship truth, DNA truth, ownership truth, title truth, boundary truth, legal advice, consent proof, EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected valid fixture families

| Scenario family | Preferred lane | Expected posture |
|---|---|---|
| Evidence-backed toy historical relationship assertion | `../genealogy/positive/` | Validation pass, review-ready, or bounded `ANSWER`. |
| Cited toy life event for a historical person | `../genealogy/positive/` | Validation pass, citation-ready, or review-ready. |
| Public-safe ancestor summary with evidence refs | `../genealogy/positive/` | `ANSWER` or review-ready. |
| Source-role-preserved tree overlay hypothesis | `../genealogy/positive/` | Review-ready or validation pass, while remaining modeled/candidate until reviewed. |
| Evidence-backed toy historical ownership interval | `../land-ownership/` | Validation pass or review-ready. |
| Toy deed/title instrument chain with surfaced gap | `../land-ownership/` | Review-ready or bounded `ABSTAIN` for the gap. |
| Assessor/tax context preserved as administrative context | `../land-ownership/` | Validation pass or review-ready. |
| Parcel geometry preserved as spatial context only | `../land-ownership/` | Validation pass or review-ready. |
| Stable positive output is ready to compare | `../golden/` | Deterministic expected output. |

## Maintenance notes

- Update this README when new valid child lanes, valid payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each valid fixture to the exact check and consumer that uses it.
- If expected valid behavior stabilizes, update the paired input, expected output, consumer notes, child README, `../golden/README.md`, and this index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real person data, DNA data, land records, source exports, precise sensitive geography, proof material, consent material, or release material, move it out of this lane, quarantine it through the governed lifecycle or registry process, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payload files verified under this parent during this update.
- Genealogy positive alignment: PARTIALLY VERIFIED against `fixtures/domains/people-dna-land/genealogy/positive/README.md`.
- Land-ownership fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/people-dna-land/land-ownership/README.md`.
- Golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/people-dna-land/golden/README.md`.
- Invalid fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/people-dna-land/invalid/README.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md` from recent preceding updates.
- Parent People/DNA/Land fixture README: NEEDS VERIFICATION.
- Consumer alignment: NEEDS VERIFICATION against validators, valid-fixture checks, golden-file checks, People/DNA/Land governed-API tests, genealogy checks, identity-resolution checks, consent checks, source-role checks, evidence-bundle checks, citation-validation checks, rights checks, sensitivity checks, land-link checks, land-ownership checks, decision-envelope checks, drawer checks, Focus Mode checks, release-readiness checks, correction checks, rollback checks, schema checks, policy checks, renderer checks, and UI implementation.
- Tests and validators: NOT RUN.
