# People/DNA/Land genealogy fixtures

`fixtures/domains/people-dna-land/genealogy/`

Status: draft / fixture parent index / genealogy synthetic examples.

This directory is the parent lane for small synthetic genealogy fixtures in the People / Genealogy / DNA / Land domain. Use it to organize positive-path and negative-path toy examples for genealogy relationship assertions, life events, family groups, source citations, identity-resolution cases, consent posture, evidence refs, policy refs, release refs, correction posture, rollback posture, drawer contexts, Focus Mode responses, decision envelopes, and expected outputs.

These files are examples only. They are not source records, lifecycle data, GEDCOM files, family trees, vital records, DNA data, land records, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, policy decisions, consent records, review approvals, release state, public API material, public map material, public tiles, genealogy truth, source authority, policy authority, release authority, AI authority, or published artifacts.

## Genealogy fixture posture

Genealogy doctrine treats kinship and life-event material as assertion-first, evidence-bound, and privacy-aware. A fixture may imitate a relationship, event, family group, source-citation chain, identity-resolution issue, or public-safe summary, but it must remain synthetic and must not become canonical genealogy truth.

People / DNA / Land is a deny-first domain. Living-person outputs, DNA-derived outputs, raw kit/vendor identifiers, raw GEDCOM identifiers, and private person-to-parcel joins are denied or restricted by default. Positive fixtures must stay public-safe and evidence-referenced; negative fixtures must make the blocked condition explicit and fail closed.

This fixture parent can support future validation and governed-API checks, but examples here do not prove validator implementation, route behavior, policy enforcement, schema enforcement, consent enforcement, EvidenceBundle storage, release integration, UI rendering, or CI coverage by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Child lane inventory

The following child lanes have populated README coverage. This table is a navigation index, not proof that payload files, validators, tests, governed API routes, UI checks, policy bundles, release manifests, source-registry records, proof stores, or CI coverage exist.

| Child lane | Purpose | Expected posture |
|---|---|---|
| `positive/` | Synthetic public-safe historical genealogy examples with evidence, citation, rights, sensitivity, release, correction, and rollback posture visible. | `ANSWER`, validation pass, review-ready, evidence-resolved, citation-ready, source-role-preserved, release-ready, correction-visible, or rollback-visible. |
| `negative/` | Synthetic fail-closed genealogy examples for missing evidence, missing consent, privacy exposure, source-role conflicts, identity conflicts, raw-source exposure, land-link exposure, missing release, or missing rollback support. | `ABSTAIN`, `DENY`, `ERROR`, validation failure, review-required, blocked render, correction-required, rollback-required, or release-readiness failure. |

## Relationship between fixture lanes

| Lane | Use |
|---|---|
| `positive/` | Positive-path public-safe toy examples for historical, evidence-referenced genealogy claims. |
| `negative/` | Fail-closed toy examples for unsafe, unsupported, unresolved, or unreviewed genealogy cases. |
| Future `golden/` or expected-output lane | Stable expected outputs for positive and negative inputs, if added. |
| Parent People/DNA/Land fixture lane | Broader domain fixture family; not inspected during this update. |

## Relationship to People/DNA/Land governance

| Lane or document | Relationship |
|---|---|
| `../../../docs/domains/people-dna-land/sublanes/genealogy.md` | Genealogy doctrine and boundary; this fixture lane supplies examples only. |
| `../../../docs/domains/people-dna-land/API_CONTRACTS.md` | Governed surface and finite outcome posture; fixtures do not define API behavior. |
| `../../../docs/domains/people-dna-land/IDENTITY_MODEL.md` | Identity model and publication constraints; fixtures do not create canonical identities. |
| `../../../docs/domains/people-dna-land/LAND_OWNERSHIP.md` | Land ownership doctrine; fixtures do not create title or parcel truth. |
| `../../../contracts/domains/people-dna-land/` | Contract home for domain object meaning; fixtures do not define contracts. |
| `../../../schemas/contracts/v1/domains/people-dna-land/` | Schema home if present; fixtures do not define schemas. |
| `../../../policy/domains/people-dna-land/` | Policy home; fixtures do not decide access or release. |
| `../../../data/registry/sources/people-dna-land/` | Source registry home if present; fixtures do not create source authority. |
| `../../../data/proofs/people-dna-land/` | Proof home if present; fixtures do not create proof authority. |
| `../../../release/candidates/people-dna-land/` and `../../../release/manifests/people-dna-land/` | Release homes if present; fixtures do not publish. |

## Accepted material

This parent lane and its children may contain:

- small synthetic `*.input.json`, `*.positive.json`, `*.negative.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy historical relationship, life-event, family-group, source-citation, identity-resolution, consent, evidence-ref, policy-ref, release-ref, correction, rollback, drawer, Focus Mode, or decision-envelope examples;
- toy positive cases for evidence-backed historical relationship assertions, cited life events, public-safe ancestor summaries, source-role-preserved tree overlays, bounded map overlay pointers, correction-visible outputs, and rollback-ready outputs;
- toy negative cases for missing evidence, unresolved identity, contradictory assertion, unsupported source role, unknown rights, unresolved sensitivity, absent consent, living-person exposure, DNA-derived inference exposure, private person-to-parcel join exposure, raw GEDCOM exposure, missing release, or missing rollback target;
- contrast examples showing why one synthetic historical claim can pass while a related living-person, DNA-derived, raw-source, or land-link case must fail closed;
- paired expected outputs when behavior becomes stable.

## Exclusions

Do not use this lane for real GEDCOM files, real family trees, real vital records, real living-person records, real DNA data, real kit/vendor identifiers, real person-to-parcel joins, real land records, real source exports, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, consent records, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy names, toy IDs, toy dates, toy places, toy relationship refs, toy source refs, toy evidence refs, toy consent refs if needed, toy policy refs, toy release refs, toy rollback refs, toy hashes, and toy timestamps.
- Prefer generic placeholders such as `PersonA`, `PersonB`, `AncestorExample`, `SyntheticFamily1`, `ToyPlaceRef`, and `ToyParcelRef`; do not use real people, real family trees, real parcel identifiers, real coordinates, or real DNA identifiers.
- Make the fixture posture explicit: positive, negative, evidence-backed, evidence-missing, identity-resolved, identity-conflicted, source-role-preserved, source-role-conflicted, rights-visible, rights-unknown, sensitivity-reviewed, sensitivity-unresolved, release-ready, release-missing, correction-visible, correction-missing, rollback-ready, rollback-missing, or expected output.
- Make expected outcome explicit when known: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, validation pass, validation failure, review-ready, review-required, evidence-resolved, citation-ready, blocked render, correction-required, rollback-required, release-ready, release-readiness failure, or expected output.
- Pair each stable input with an expected output when practical.
- Keep schema validity, semantic validity, identity resolution, evidence resolution, citation validation, consent posture, rights posture, sensitivity posture, source-role validity, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, correction posture, rollback posture, and expected-output state separate.
- Do not treat fixture success or failure as identity truth, relationship truth, title truth, consent proof, EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected fixture families

| Scenario family | Preferred child lane | Expected posture |
|---|---|---|
| Evidence-backed toy historical relationship assertion | `positive/` | Validation pass, review-ready, or bounded `ANSWER`. |
| Cited toy life event for a historical person | `positive/` | Validation pass, citation-ready, or review-ready. |
| Public-safe ancestor summary with evidence refs | `positive/` | `ANSWER` or review-ready. |
| Source-role-preserved tree overlay hypothesis | `positive/` | Review-ready or validation pass, while remaining modeled/candidate until reviewed. |
| Relationship assertion lacks evidence refs | `negative/` | `ABSTAIN` or validation failure. |
| Living-person field requested without scoped consent | `negative/` | `DENY`. |
| DNA-derived inference requested for public output | `negative/` | `DENY` or review-required. |
| Raw GEDCOM identifier exposed in a public surface | `negative/` | `DENY` or validation failure. |
| Private person-to-parcel join lacks release and sensitivity review | `negative/` | `DENY` or release-readiness failure. |
| Stable expected output is ready to compare | Future `golden/` or documented pair | Deterministic expected output. |

## Maintenance notes

- Update this README when new child lanes, payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each stable fixture to the exact check and consumer that uses it.
- If expected behavior stabilizes, update the paired input, expected output, consumer notes, child README, and this parent index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real person data, DNA data, land records, source exports, precise sensitive geography, or release material, move it out of this lane, quarantine it through the governed lifecycle or registry process, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Child README inventory: PARTIALLY VERIFIED against populated `positive/README.md` and `negative/README.md` fetched during this update.
- Fixture payload inventory: no payload files verified under this parent during this update.
- Positive fixture alignment: PARTIALLY VERIFIED against `positive/README.md`.
- Negative fixture alignment: PARTIALLY VERIFIED against `negative/README.md`.
- Genealogy doctrine alignment: PARTIALLY VERIFIED against `docs/domains/people-dna-land/sublanes/genealogy.md` from recent preceding updates.
- API trust-membrane alignment: PARTIALLY VERIFIED against `docs/domains/people-dna-land/API_CONTRACTS.md` from recent preceding updates.
- Identity model alignment: PARTIALLY VERIFIED against `docs/domains/people-dna-land/IDENTITY_MODEL.md` from recent preceding updates.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md` from recent preceding updates.
- Parent People/DNA/Land fixture alignment: NEEDS VERIFICATION.
- Consumer alignment: NEEDS VERIFICATION against validators, genealogy checks, identity-resolution checks, consent checks, source-role checks, evidence-bundle checks, citation-validation checks, rights checks, sensitivity checks, land-link checks, decision-envelope checks, drawer checks, Focus Mode checks, release-readiness checks, correction checks, rollback checks, schema checks, policy checks, renderer checks, and CI implementation.
- Tests and validators: NOT RUN.
